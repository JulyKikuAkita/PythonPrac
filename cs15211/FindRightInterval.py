__source__ = 'https://github.com/kamyu104/LeetCode/blob/master/Python/find-right-interval.py'
# Time:  O(nlogn)
# Space: O(n)
#
# Description:
# Given a set of intervals, for each of the interval i,
# check if there exists an interval j whose start point is bigger than or
# equal to the end point of the interval i, which can be called that j is on the "right" of i.
#
# For any interval i, you need to store the minimum interval j's index,
# which means that the interval j has the minimum start point to
# build the "right" relationship for interval i. If the interval j doesn't exist,
# store -1 for the interval i. Finally, you need output the stored value of each interval as an array.
#
# Note:
# You may assume the interval's end point is always bigger than its start point.
# You may assume none of these intervals have the same start point.
# Example 1:
# Input: [ [1,2] ]
#
# Output: [-1]
#
# Explanation: There is only one interval in the collection, so it outputs -1.
# Example 2:
# Input: [ [3,4], [2,3], [1,2] ]
#
# Output: [-1, 0, 1]
#
# Explanation: There is no satisfied "right" interval for [3,4].
# For [2,3], the interval [3,4] has minimum-"right" start point;
# For [1,2], the interval [2,3] has minimum-"right" start point.
# Example 3:
# Input: [ [1,4], [2,3], [3,4] ]
#
# Output: [-1, 2, -1]
#
# Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
# For [2,3], the interval [3,4] has minimum-"right" start point.
#  Binary Search
# Hide Similar Problems (H) Data Stream as Disjoint Intervals
#
import unittest
import bisect

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        sorted_intervals = sorted((interval.start, i) for i, interval in enumerate(intervals))
        result = []
        for interval in intervals:
            idx = bisect.bisect_left(sorted_intervals, (interval.end,))
            result.append(sorted_intervals[idx][1] if idx < len(sorted_intervals) else -1)
        return result

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
1. TreeMap: O(nlogn)
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
    public int[] findRightInterval(Interval[] intervals) {
        int[] result = new int[intervals.length];
        java.util.NavigableMap<Integer, Integer> intervalMap = new TreeMap<>();
        for (int i = 0; i < intervals.length; ++i) {
            intervalMap.put(intervals[i].start, i);
        }
        for (int i = 0; i < intervals.length; ++i) {
            Map.Entry<Integer, Integer> entry = intervalMap.ceilingEntry(intervals[i].end);
            result[i] = (entry != null) ? entry.getValue() : -1;
        }
        return result;
    }
}

Java Concise Binary Search
If we are not allowed to use TreeMap:

Sort starts
For each end, find leftmost start using binary search
To get the original index, we need a map

public class Solution {
    public int[] findRightInterval(Interval[] intervals) {
        Map<Integer, Integer> map = new HashMap<>();
        List<Integer> starts = new ArrayList<>();
        for (int i = 0; i < intervals.length; i++) {
            map.put(intervals[i].start, i);
            starts.add(intervals[i].start);
        }

        Collections.sort(starts);
        int[] res = new int[intervals.length];
        for (int i = 0; i < intervals.length; i++) {
            int end = intervals[i].end;
            int start = binarySearch(starts, end);
            if (start < end) {
                res[i] = -1;
            } else {
                res[i] = map.get(start);
            }
        }
        return res;
    }

    public int binarySearch(List<Integer> list, int x) {
        int left = 0, right = list.size() - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (list.get(mid) < x) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return list.get(left);
    }
}
'''