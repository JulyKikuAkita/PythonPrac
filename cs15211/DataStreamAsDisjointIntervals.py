# coding=utf-8
__source__ = 'https://leetcode.com/problems/data-stream-as-disjoint-intervals/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/data-stream-as-disjoint-intervals.py
# Time:  addNum: O(n), getIntervals: O(n), n is the number of disjoint intervals.
# Space: O(n)
#
# Description: Leetcode # 352. Data Stream as Disjoint Intervals
#
# Given a data stream input of non-negative integers a1, a2, ..., an, ...,
# summarize the numbers seen so far as a list of disjoint intervals.
#
# For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be:
#
# [1, 1]
# [1, 1], [3, 3]
# [1, 1], [3, 3], [7, 7]
# [1, 3], [7, 7]
# [1, 3], [6, 7]
#
# Follow up:
# What if there are lots of merges and the number of disjoint intervals are small compared to the data stream's size?
#
# Related Topics
# Binary Search Tree
# Similar Questions
# Summary Ranges Find Right Interval
#
import unittest
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class SummaryRanges(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__intervals = []

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        def upper_bound(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) / 2
                if nums[mid].start > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        i = upper_bound(self.__intervals, val)
        start, end = val, val
        if i != 0 and self.__intervals[i-1].end + 1 >= val:
            i -= 1
        while i != len(self.__intervals) and \
              end + 1 >= self.__intervals[i].start:
            start = min(start, self.__intervals[i].start)
            end = max(end, self.__intervals[i].end);
            del self.__intervals[i]
        self.__intervals.insert(i, Interval(start, end))

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self.__intervals

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */

# 92ms 100%
class SummaryRanges {
    List<Interval> list;

    /** Initialize your data structure here. */
    public SummaryRanges() {
        list = new ArrayList<>();
    }

    public void addNum(int val) {
        int pre = searchPre(val);
        int suc = pre == list.size() - 1 ? -1 : pre + 1;
        if (pre >= 0 && suc >= 0 && val + 1 == list.get(suc).start && list.get(pre).end + 1 == val) {
            list.get(pre).end = list.get(suc).end;
            list.remove(suc);
        } else if (suc >= 0 && val + 1 == list.get(suc).start) {
            list.get(suc).start = val;
        } else if (pre >= 0 && list.get(pre).end + 1 >= val) {
            list.get(pre).end = Math.max(list.get(pre).end, val);
        } else {
            list.add(pre + 1, new Interval(val, val));
        }
    }

    public List<Interval> getIntervals() {
        return list;
    }

    private int searchPre(int val) {
        if (list.isEmpty() || list.get(0).start > val) {
            return -1;
        }
        int start = 0;
        int end = list.size() - 1;
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (list.get(mid).start > val) {
                end = mid;
            } else {
                start = mid;
            }
        }
        return list.get(end).start > val ? start : end;
    }
}

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges obj = new SummaryRanges();
 * obj.addNum(val);
 * List<Interval> param_2 = obj.getIntervals();
 */

# 96ms 96.52%
class SummaryRanges {
    List<Interval> list;
    /** Initialize your data structure here. */
    public SummaryRanges() {
        list = new LinkedList<>();
    }

    public void addNum(int val) {
        if(list.isEmpty())
            list.add(new Interval(val,val));
        else{//二分插入
            int begin = 0;
            int end = list.size()-1;
            boolean getResult = false;//是否妥善安置了新加的元素
            while(begin<=end && !getResult){
                int mid = (begin+end)/2;
                Interval mid_interval = list.get(mid);
                if(mid_interval.end>=val && mid_interval.start<=val)//要考虑重复元素
                    break;
                if(mid_interval.start-1 == val){
                    //向前可能要再合并一个
                    if(mid>0 && list.get(mid-1).end+1 == val){
                        mid_interval.start = list.get(mid-1).start;
                        list.remove(mid-1);
                    }
                    else{
                        mid_interval.start--;
                    }
                    getResult = true;
                }
                else if(mid_interval.end+1 == val){//同理可能往后合并
                    if(mid<end && list.get(mid+1).start-1 == val){
                        mid_interval.end = list.get(mid+1).end;
                        list.remove(mid+1);
                    }
                    else{
                        mid_interval.end++;
                    }
                    getResult = true;
                }
                else if(mid_interval.start-1>val && (mid == 0 || list.get(mid-1).end+1<val)){//独立情况1
                    list.add(mid,new Interval(val,val));
                    getResult = true;
                }
                else if(mid_interval.end+1<val && (mid == end || list.get(mid+1).start-1>val)){//独立情况2
                    list.add(mid+1,new Interval(val,val));
                    getResult = true;
                }
                else{//更新begin或end
                    if(mid_interval.end+1<val)
                        begin = mid+1;
                    else if(mid_interval.start-1>val)
                        end = mid-1;
                }
            }
        }
    }

    public List<Interval> getIntervals() {
        return list;
    }
}

'''