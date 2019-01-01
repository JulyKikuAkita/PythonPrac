__source__ = 'https://leetcode.com/problems/set-intersection-size-at-least-two/'
# Time:  O(N^2)
# Space: O(N)
#
# Description: Leetcode # 757. Set Intersection Size At Least Two
#
# An integer interval [a, b] (for integers a < b) is a set of all consecutive integers from a to b,
# including a and b.
#
# Find the minimum size of a set S such that for every integer interval A in intervals,
# the intersection of S with A has size at least 2.
#
# Example 1:
#
# Input: intervals = [[1, 3], [1, 4], [2, 5], [3, 5]]
# Output: 3
# Explanation:
# Consider the set S = {2, 3, 4}.  For each interval, there are at least 2 elements from S in the interval.
# Also, there isn't a smaller size set that fulfills the above condition.
# Thus, we output the size of this set, which is 3.
#
# Example 2:
#
# Input: intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]
# Output: 5
# Explanation:
# An example of a minimum sized set is {1, 2, 3, 4, 5}.
#
# Note:
#
#     intervals will have length in range [1, 3000].
#     intervals[i] will have length 2, representing some integer interval.
#     intervals[i][j] will be an integer in [0, 10^8].
#
import unittest
# 1588ms 0%
class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key = lambda (s, e): (s, -e))
        todo = [2] * len(intervals)
        ans = 0
        while intervals:
            (s, e), t = intervals.pop(), todo.pop()
            for p in xrange(s, s+t):
                for i, (s0, e0) in enumerate(intervals):
                    if todo[i] and p <= e0:
                        todo[i] -= 1
                ans += 1
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/set-intersection-size-at-least-two/solution/
#
# Approach #1: Greedy [Accepted]
Complexity Analysis
Time Complexity: O(N^2), where N is the length of intervals.
Space Complexity: O(N)
# 170ms 3.15%
class Solution {
    public int intersectionSizeTwo(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[0] != b[0] ? a[0] - b[0] : b[1] - a[1]);
        int[] todo = new int[intervals.length];
        Arrays.fill(todo, 2);
        int ans = 0, t = intervals.length;
        while (--t >= 0) {
            int s = intervals[t][0];
            int e = intervals[t][1];
            int m = todo[t];
            for (int p = s; p < s + m; ++p) {
                for (int i = 0; i <= t; i++) {
                    if (todo[i] > 0 && p <= intervals[i][1]) todo[i]--;
                }
                ans++;
            }
        }
        return ans;
    }
}

# 27ms 71.65%
class Solution {
    public int intersectionSizeTwo(int[][] intervals) {
        Arrays.sort(intervals, new Comparator<int[]>() {
            public int compare(int[] a, int[] b) {
                return (a[1] != b[1] ? Integer.compare(a[1], b[1]) : Integer.compare(b[0], a[0])); 
            }
        });
        int m = 0, largest = -1, second = -1;
        for (int[] interval : intervals) {
            int a = interval[0], b = interval[1];
            
            boolean is_largest_in = (a <= largest);
            boolean is_second_in = (a <= second);
            if (is_largest_in && is_second_in) continue;
            m += (is_largest_in ? 1 : 2);
            second = (is_largest_in ? largest : b - 1);
            largest = b;
        }
        return m;
    }
}

# 20ms 81.10%
class Solution {
    public int intersectionSizeTwo(int[][] intervals) {
        Arrays.sort(intervals, new Comparator<int[]>() {
            @Override
            public int compare(int[] i1, int[] i2) {
                if (i1[1] == i2[1]) return i2[0] - i1[0];
                return i1[1] - i2[1];
            }
        });
        
        int result = 0;
        int max = -1;
        int secondMax = -1;
        for (int[] interval : intervals) {
            int start = interval[0];
            int end = interval[1];
            if (start <= secondMax) continue;
            if (start <= max) {
                result += 1;
                secondMax = max;
                max = end;
            } else {
                result += 2;
                max = end;
                secondMax = end - 1;
            }
                
        }
        return result;
    }
}
'''
