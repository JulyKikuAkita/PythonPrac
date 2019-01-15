__source__ = 'https://leetcode.com/problems/line-reflection/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/line-reflection.py
# Time:  O(n)
# Space: O(n)
#
# Description: Leetcode # 356. Line Reflection
#
# Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points.
#
# Example 1:
# Given points = [[1,1],[-1,1]], return true.
#
# Example 2:
# Given points = [[1,1],[-1,-1]], return false.
#
# Follow up:
# Could you do better than O(n2)?
#
# Companies
# Google
# Related Topics
# Hash Table Math
# Similar Questions
# Max Points on a Line Number of Boomerangs
#
import collections
import unittest
# Hash solution.
class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if not points:
            return True
        groups_by_y = collections.defaultdict(set)
        left, right = float("inf"), float("-inf")
        for p in points:
            groups_by_y[p[1]].add(p[0])
            left, right = min(left, p[0]), max(right, p[0])
        mid = left + right
        for group in groups_by_y.values():
            for x in group:
                if mid - x not in group:
                    return False
        return True

# Time:  O(nlogn)
# Space: O(n)
# Two pointers solution.
class Solution2(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if not points:
            return True
        points.sort()
        # Space: O(n)
        points[len(points)/2:] = sorted(points[len(points)/2:], \
                                        lambda x, y: y[1] - x[1] if x[0] == y[0] else \
                                                     x[0] - y[0])
        mid = points[0][0] + points[-1][0]
        left, right = 0, len(points) - 1
        while left <= right:
            if (mid != points[left][0] + points[right][0]) or \
               (points[left][0] != points[right][0] and \
                points[left][1] != points[right][1]):
                return False
            left += 1
            right -= 1
        return True

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
#
[[-16,1],[16,1],[16,1]] wrong answer: should be true but return false

1. 10ms 81.56%
class Solution {
    public boolean isReflected(int[][] points) {
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        HashSet<String> set = new HashSet<>();
        for(int[] p:points){
            max = Math.max(max,p[0]);
            min = Math.min(min,p[0]);
            String str = p[0] + "a" + p[1];
            set.add(str);
        }
        int sum = max+min;
        for(int[] p:points){
            //int[] arr = {sum-p[0],p[1]};
            String str = (sum-p[0]) + "a" + p[1];
            if( !set.contains(str))
                return false;
        }
        return true;
    }
}

2.
# 3ms 100%
class Solution { // O(NLgN) sort + check
    public boolean isReflected(int[][] points) {
        if (points == null || points.length == 0) {
            return true;
        }
        long min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;
        for (int[] p : points) {
            min = Math.min(min, p[0]);
            max = Math.max(max, p[0]);
        }
        long sum = min + max; // sum = x-coord of mirror * 2
        double mid = sum / 2.0;

        Arrays.sort(points, new Comparator<int[]>(){
            @Override
            public int compare(int[] a, int[] b) {
                if (a[0] != b[0]) {
                    return a[0] - b[0];
                } else if (a[0] <= mid) {
                    return a[1] - b[1];
                } else {
                    return b[1] - a[1];
                }
            }
        });
        int len = points.length;
        int lft = 0, rgt = len - 1;
        while (points[lft][0] < points[rgt][0]) {
            if (points[lft][1] == points[rgt][1] && points[lft][0] == sum - points[rgt][0]) {
                lft++;
                rgt--;
                while (points[lft][0] == points[lft - 1][0] && points[lft][1] == points[lft - 1][1]) {
                    lft++;
                }
                while (points[rgt][0] == points[rgt + 1][0] && points[rgt][1] == points[rgt + 1][1]) {
                    rgt--;
                }
            } else {
                return false;
            }
        }
        // there are either no remaining nodes or all remaining nodes are on the mid
        return lft > rgt || (points[lft][0] * 2L == sum && points[rgt][0] * 2L == sum);
    }
}

'''
