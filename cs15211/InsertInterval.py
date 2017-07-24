__source__ = 'https://leetcode.com/problems/insert-interval/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/insert-interval.py
# Time:  O(n)
# Space: O(1)
# Sort
#
# Description: Leetcode # 57. Insert Interval
#
# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
#
# You may assume that the intervals were initially sorted according to their start times.
#
# Example 1:
# Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].
#
# Example 2:
# Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].
#
# This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
# Companies
# LinkedIn Google Facebook
# Related Topics
# Array Sort
# Similar Questions
# Merge Intervals
#
import unittest
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "[{}, {}]".format(self.start, self.end)

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        return self.merge(intervals + [newInterval])

    def merge(self, intervals):
        if not intervals:
            return intervals
        intervals.sort(key = lambda x: x.start)
        result = [intervals[0]]
        for i in xrange(1, len(intervals)):
            prev, cur = result[-1], intervals[i]
            if cur.start <= prev.end:
                prev.end = max(prev.end, cur.end)
            else:
                result.append(cur)
        return result

# http://www.cnblogs.com/zuoyuan/p/3782048.html
class SolutionOther:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals.sort(key = lambda x: x.start)
        length = len(intervals)
        res = []

        for i in range(length):
            if res == []:
                res.append(intervals[i])
            else:
                size = len(res)
                if res[size-1].start <= intervals[i].start <= res[size-1].end:
                    res[size-1].end = max(intervals[i].end, res[size-1].end)
                else:
                    res.append(intervals[i])
        return res

#test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        test = SolutionOther()
        i1 = Interval(1,3)
        i2 = Interval(6,9)
        i3 = Interval(2,5)
        a1 = [i1, i2]
        i4 = Interval(1,2) ; i5 = Interval(3,5) ; i6 = Interval(6,7) ;
        i7 = Interval(8,10) ; i8 = Interval(12,16); i9 = Interval(4,9)
        a2 = [i4, i5, i6, i7,i8]
        ans1 = test.insert(a1, i3)
        ans2 = test.insert(a2, i9)
        for item in ans2:
            print item.start, item.end

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/contains-duplicate/solution/

#70.81% 15ms
/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
public class Solution {
    public List<Interval> insert(List<Interval> intervals, Interval newInterval) {
        List<Interval> result = new ArrayList<>();
        int index = 0;
        while (index < intervals.size()) {
            Interval cur = intervals.get(index);
            if (cur.end < newInterval.start) {
                result.add(cur);
            } else if (newInterval.end < cur.start) {
                break; //newInterval might be the last one
            } else {
                newInterval.start = Math.min(newInterval.start, cur.start);
                newInterval.end = Math.max(newInterval.end, cur.end);
            }
            index++;
        }
        result.add(newInterval);
        while (index < intervals.size()) {
            result.add(intervals.get(index++));
        }
        return result;
    }
}

#99% 12ms Binary search

public class Solution {
    public List<Interval> insert(List<Interval> intervals, Interval newInterval) {
        if(intervals == null || newInterval == null) {
            return intervals;
        }

        List<Interval> rst= new ArrayList<Interval>();
        int startPos = getStartPos(intervals, newInterval.start);
        int endPos = getEndPos(intervals, newInterval.end);
        if(startPos > 0 && intervals.get(startPos-1).end >= newInterval.start) {
            --startPos;
        }
        if(endPos == intervals.size() || intervals.get(endPos).start > newInterval.end) {
            --endPos;
        }

        if(startPos <= endPos) {
            newInterval = new Interval(Math.min(intervals.get(startPos).start, newInterval.start)
            , Math.max(intervals.get(endPos).end, newInterval.end));
        }

        int cur = 0;
        while(cur < startPos) {
            rst.add(intervals.get(cur++));
        }
        rst.add(newInterval);
        cur = endPos+1;
        while(cur < intervals.size()) {
            rst.add(intervals.get(cur++));
        }

        return rst;
    }

    private int getStartPos(List<Interval> intervals, int start) {
        int l = 0;
        int r = intervals.size()-1;
        while(l <= r) {
            int m = (l+r)/2;
            int cur = intervals.get(m).start;
            if(cur == start) {
                return m;
            } else if(cur < start) {
                l = m+1;
            } else {
                r = m-1;
            }
        }
        return l;
    }

    private int getEndPos(List<Interval> intervals, int end) {
        int l = 0;
        int r = intervals.size()-1;
        while(l <= r) {
            int m = (l+r)/2;
            int cur = intervals.get(m).end;
            if(cur == end) {
                return m;
            } else if(cur < end) {
                l = m+1;
            } else {
                r = m-1;
            }
        }
        return l;
    }
}
'''