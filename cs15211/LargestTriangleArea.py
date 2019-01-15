__source__ = 'https://leetcode.com/problems/largest-triangle-area/'
# Time:  O(N^3)
# Space: O(1)
#
# Description: Leetcode # 812. Largest Triangle Area
#
# You have a list of points in the plane. Return the area of the largest triangle that can be formed
# by any 3 of the points.
#
# Example:
# Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# Output: 2
# Explanation:
# The five points are show in the figure below. The red triangle is the largest.
#
# Notes:
#
# 3 <= points.length <= 50.
# No points will be duplicated.
# -50 <= points[i][j] <= 50.
# Answers within 10^-6 of the true value will be accepted as correct.
#
import unittest
import itertools
# 132ms 51.82%
class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def area(p, q, r):
            return .5 * abs(p[0]*q[1]+q[0]*r[1]+r[0]*p[1]
                           -p[1]*q[0]-q[1]*r[0]-r[1]*p[0])

        return max(area(*triangle)
            for triangle in itertools.combinations(points, 3))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/largest-triangle-area/solution/
#
Approach #1: Brute Force [Accepted]
Complexity Analysis
Time Complexity: O(N^3), where N is the length of points. 
We use three for-loops of length O(N), 
and our work calculating the area of a single triangle is O(1)
Space Complexity: O(1)

# We will have 3 for loops to cycle through each choice of 3 points in the array.
# After, we'll need a function to calculate the area given 3 points. Here we have some options:
# We can use the Shoelace formula directly, which tells us the area given the 3 points;
# We can use Heron's formula, which requires the 3 side lengths 
# which we can get by taking the distance of two points;
# We can use the formula area = 0.5 * a * b * sin(C) and calculate the angle C with trigonometry.

# 9ms 71.09%
class Solution {
    public double largestTriangleArea(int[][] points) {
        int N = points.length;
        double ans = 0;
        for (int i = 0; i < N; ++i)
            for (int j = i+1; j < N; ++j)
                for (int k = j+1; k < N; ++k)
                    ans = Math.max(ans, area(points[i], points[j], points[k]));
        return ans;
    }
    
    private double area(int[] P, int[] Q, int[] R) {
        return 0.5 * Math.abs(P[0]*Q[1] + Q[0]*R[1] + R[0]*P[1]
                             -P[1]*Q[0] - Q[1]*R[0] - R[1]*P[0]);
    }
}

# 5ms 100%
class Solution {
    public double largestTriangleArea(int[][] points) {
        int n = points.length;
        double max = 0;
        
        for (int i = 0; i < n; ++i) 
            for (int j = i + 1; j < n; ++j)
                for (int k = j + 1; k < n; ++k) {
                    double area = area(points, i, j, k);
                    if (area > max) {
                        max = area;
                    }
                }
        return max;
    }
    
    // triangle
    double area(int[][] points, int i, int j, int k) {
        int[] p1 = points[i];
        int[] p2 = points[j];
        int[] p3 = points[k];
        
        double area = 0;
        area += area(p1, p2);
        area += area(p2, p3);
        area += area(p3, p1);
        
        return Math.abs(area);
    }
    
    // parallelogram
    double area(int[] p1, int[] p2) {
        int w = p2[0] - p1[0];
        double h = (p1[1] + p2[1] + 200) / 2.0;
        return w * h;
    }
}
'''
