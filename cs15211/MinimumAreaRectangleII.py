__source__ = 'https://leetcode.com/problems/minimum-area-rectangle-ii/'
# Time:  O(N^3)
# Space: O(N)
#
# Description: Leetcode # 963. Minimum Area Rectangle II
#
# Given a set of points in the xy-plane, determine the minimum area of any rectangle formed from these points,
# with sides not necessarily parallel to the x and y axes.
#
# If there isn't any rectangle, return 0.
#
# Example 1:
#
# Input: [[1,2],[2,1],[1,0],[0,1]]
# Output: 2.00000
# Explanation: The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1], with an area of 2.
#
# Example 2:
#
# Input: [[0,1],[2,1],[1,1],[1,0],[2,0]]
# Output: 1.00000
# Explanation: The minimum area rectangle occurs at [1,0],[1,1],[2,1],[2,0], with an area of 1.
#
# Example 3:
#
# Input: [[0,3],[1,2],[3,1],[1,3],[2,1]]
# Output: 0
# Explanation: There is no possible rectangle to form from these points.
#
# Example 4:
#
# Input: [[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
# Output: 2.00000
# Explanation: The minimum area rectangle occurs at [2,1],[2,3],[3,3],[3,1], with an area of 2.
#
# Note:
#     1 <= points.length <= 50
#     0 <= points[i][0] <= 40000
#     0 <= points[i][1] <= 40000
#     All points are distinct.
#     Answers within 10^-5 of the actual value will be accepted as correct.
#
import unittest
import itertools
import collections
# 64ms 92.73%
class Solution(object):
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        points = [complex(*z) for z in points]
        seen = collections.defaultdict(list)
        for P, Q in itertools.combinations(points, 2):
            center = (P + Q) / 2
            radius = abs(center - P)
            seen[center, radius].append(P)

        ans = float("inf")
        for (center, radius), candidates in seen.iteritems():
            for P, Q in itertools.combinations(candidates, 2):
                ans = min(ans, abs(P - Q) * abs(P - (2*center - Q)))
        return ans if ans < float("inf") else 0

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/minimum-area-rectangle-ii/solution/
#
Approach 1: Iterate Triangles
Complexity Analysis
Time Complexity: O(N^3), where N is the length of points.
Space Complexity: O(N)
# 69ms 49.65%
import java.awt.Point;
class Solution {
    public double minAreaFreeRect(int[][] points) {
        int N = points.length;

        Point[] A = new Point[N];
        Set<Point> pointSet = new HashSet();
        for (int i = 0; i < N; ++i) {
            A[i] = new Point(points[i][0], points[i][1]);
            pointSet.add(A[i]);
        }

        double ans = Double.MAX_VALUE;
        for (int i = 0; i < N; ++i) {
            Point p1 = A[i];
            for (int j = 0; j < N; ++j) if (j != i) {
                Point p2 = A[j];
                for (int k = j+1; k < N; ++k) if (k != i) {
                    Point p3 = A[k];
                    Point p4 = new Point(p2.x + p3.x - p1.x, p2.y + p3.y - p1.y);

                    if (pointSet.contains(p4)) {
                        int dot = ((p2.x - p1.x) * (p3.x - p1.x) +
                                   (p2.y - p1.y) * (p3.y - p1.y));
                        if (dot == 0) {
                            double area = p1.distance(p2) * p1.distance(p3);
                            if (area < ans)
                                ans = area;
                        }
                    }
                }
            }
        }

        return ans < Double.MAX_VALUE ? ans : 0;
    }
}

Approach 2: Iterate Centers
Complexity Analysis
Time Complexity: O(N^2LogN), where N is the length of points. 
It can be shown that the number of pairs of points with the same classification is bounded by logN - 
see this link for more: https://en.wikipedia.org/wiki/Sum_of_squares_function#Particular_cases
Space Complexity: O(N)
# 52ms 70.39%   
import java.awt.Point;
class Solution {
    public double minAreaFreeRect(int[][] points) {
        int N = points.length;
        Point[] A = new Point[N];
        for (int i = 0; i < N; ++i)
            A[i] = new Point(points[i][0], points[i][1]);

        Map<Integer, Map<Point, List<Point>>> seen = new HashMap();
        for (int i = 0; i < N; ++i)
            for (int j = i+1; j < N; ++j) {
                // center is twice actual to keep integer precision
                Point center = new Point(A[i].x + A[j].x, A[i].y + A[j].y);

                int r2 = (A[i].x - A[j].x) * (A[i].x - A[j].x);
                r2 += (A[i].y - A[j].y) * (A[i].y - A[j].y);
                if (!seen.containsKey(r2))
                    seen.put(r2, new HashMap<Point, List<Point>>());
                if (!seen.get(r2).containsKey(center))
                    seen.get(r2).put(center, new ArrayList<Point>());
                seen.get(r2).get(center).add(A[i]);
            }

        double ans = Double.MAX_VALUE;
        for (Map<Point, List<Point>> info: seen.values()) {
            for (Point center: info.keySet()) {  // center is twice actual
                List<Point> candidates = info.get(center);
                int clen = candidates.size();
                for (int i = 0; i < clen; ++i)
                    for (int j = i+1; j < clen; ++j) {
                        Point P = candidates.get(i);
                        Point Q = candidates.get(j);
                        Point Q2 = new Point(center);
                        Q2.translate(-Q.x, -Q.y);
                        double area = P.distance(Q) * P.distance(Q2);
                        if (area < ans)
                            ans = area;
                    }
            }
        }

        return ans < Double.MAX_VALUE ? ans : 0;
    }
}

# 18ms 99.29%
class Solution {
    public double minAreaFreeRect(int[][] points) {
        double min = Integer.MAX_VALUE;
        for (int i = 0; i < points.length; i++){
            for (int j = i+1; j < points.length; j++){
                for (int k = j+1; k < points.length; k++){
                    int dx1 = points[j][0] - points[i][0], dy1 = points[j][1] - points[i][1];
                    int dx2 = points[k][0] - points[i][0], dy2 = points[k][1] - points[i][1];
                    if (dx1 * dx2 + dy1 * dy2 == 0) {
                        for (int[] point : points){
                            if (point[0] == points[i][0] + dx1 + dx2 && point[1] == points[i][1] + dy1 + dy2) {
                                double area = Math.sqrt(Math.pow(dx1, 2) + Math.pow(dy1, 2)) * Math.sqrt(Math.pow(dx2, 2) + Math.pow(dy2, 2));
                                min = Math.min(min, area);
                            }
                        }
                    }
                }
            }
        }
        return min == Integer.MAX_VALUE ? 0 : min;
    }
}
'''
