__source__ = 'https://leetcode.com/problems/merge-intervals/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/merge-intervals.py
# Time:  O(nlogn)
# Space: O(1)
# sort
#
# Description: Leetcode # 56. Merge Intervals
#
# Given a collection of intervals, merge all overlapping intervals.
#
# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].
#
# Given [[1,4],[2,3]]
# return [[1,4]]
#
# Companies
# LinkedIn Google Facebook Twitter Microsoft Bloomberg Yelp
# Related Topics
# Array Sort
# Similar Questions
# Insert Interval Meeting Rooms Meeting Rooms II Teemo Attacking Add Bold Tag in String
#
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
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        if not intervals:
            return intervals
        intervals.sort(key = lambda x :  x .start)
        result = [intervals[0]]
        for i in xrange(1, len(intervals)):
            prev, cur = result[-1], intervals[i]
            if cur.start <= prev.end:
                prev.end = max(prev.end, cur.end)
            else:
                result.append(cur)
        return result

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().merge([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15,18)])

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/merge-intervals/solution/

/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
# 73ms 10.01%
class Solution {
    public List<Interval> merge(List<Interval> intervals) {
        List<Interval> result = new ArrayList<>();
        if (intervals.isEmpty()) {
            return result;
        }
        Collections.sort(intervals, (i1, i2) -> i1.start != i2.start ? Integer.compare(i1.start, i2.start) : Integer.compare(i1.end, i2.end));
        
        int start = intervals.get(0).start;
        int end = intervals.get(0).end;
        for (int i = 1; i < intervals.size(); i++) {
            Interval cur = intervals.get(i);
            if (end < cur.start) {
                result.add(new Interval(start, end));
                start = cur.start;
                end = cur.end;
            } else {
                end = Math.max(end, cur.end);
            }
        }
        result.add(new Interval(start, end));
        return result;
    }
}

# 10ms 96.43%
class Solution {
    public List<Interval> merge(List<Interval> intervals) {
        int n = intervals.size();
        int[] starts = new int[n];
        int[] ends = new int[n];
        for (int i = 0; i < n; i++) {
            starts[i] = intervals.get(i).start;
            ends[i] = intervals.get(i).end;
        }
        Arrays.sort(starts);
        Arrays.sort(ends);
        List<Interval> res = new ArrayList<Interval>();
        int startP = 0;
        for (int endP = 0; endP < n; endP++) {
            // when we begin a new intervals
            if (endP == n - 1 || starts[endP + 1] > ends[endP]) {
                res.add(new Interval(starts[startP], ends[endP]));
                startP = endP + 1;
            }
        }
        return res;
    }
}

# Merge Sort
# 48ms 42.89%
class Solution {
    public List<Interval> merge(List<Interval> intervals) {
        if (intervals == null) {
            return null;
        }
        List<Interval> result = new ArrayList<Interval>();
        Interval curr = null;
        Interval[] array = sort(intervals);
        
        for (int i = 0; i < array.length; i++) {
            if (curr == null) {
                curr = array[i];
            } else if (curr.end >= array[i].start) {
                if (curr.end < array[i].end) {
                    curr = new Interval(curr.start, array[i].end);
                }
            } else {
                result.add(curr);
                curr = array[i];
            }
        }
        
        if (curr != null) {
            result.add(curr);
        }
        
        return result;
    }
    
    public Interval[] sort(List<Interval> intervals) {
        Interval[] result = intervals.toArray(new Interval[intervals.size()]);
        mergeSort(result);
        return result;
    }
    
    public void mergeSort(Interval[] intervals) {
        mergeSort(intervals, 0, intervals.length - 1);
    }
    
    private void mergeSort(Interval[] intervals, int start, int end) {
        if (start < end) {
            int middle = (start + end) / 2;
            mergeSort(intervals, start, middle);
            mergeSort(intervals, middle + 1, end);
            merge(intervals, start, middle, end);
        }
    }
    
    private void merge(Interval[] intervals, int start, int middle, int end) {
        Interval[] helper = new Interval[intervals.length];
        for (int i = start; i <= end; i++) {
            helper[i] = intervals[i];
        }
        
        int left = start;
        int right = middle + 1;
        int curr = start;
        
        while (left <= middle && right <= end) {
            if (helper[left].start < helper[right].start) {
                intervals[curr] = helper[left];
                left++;
            } else {
                intervals[curr] = helper[right];
                right++;
            }
            curr++;
        }
        
        while (left <= middle) {
            intervals[curr] = helper[left];
            left++;
            curr++;
        }
    }
}
'''
