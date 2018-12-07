__source__ = 'https://github.com/kamyu104/LeetCode/blob/master/Python/convex-polygon.py'
# Time:  O(n)
# Space: O(1)
#
# Description: 469. Convex Polygon
#
# Given a list of points that form a polygon when joined sequentially,
# find if this polygon is convex (Convex polygon definition).
# https://en.wikipedia.org/wiki/Simple_polygon
# Note:
#
# There are at least 3 and at most 10,000 points.
# Coordinates are in the range -10,000 to 10,000.
# You may assume the polygon formed by given points is always a simple polygon
# (Simple polygon definition). In other words, we ensure that exactly two edges intersect at each vertex,
# and that edges otherwise don't intersect each other.
# Example 1:
#
# [[0,0],[0,1],[1,1],[1,0]]
#
# Answer: True
#
# Explanation:
# Example 2:
#
# [[0,0],[0,10],[10,10],[10,0],[5,5]]
#
# Answer: False
#
# Explanation:
# Hide Company Tags Google
# Hide Tags Math

import unittest
# get the cross product of the sequential input edge a, b as tmp, then:
#
# if tmp == 0, a -> b 180 degree on the same line;
# elif tmp > 0, a -> b clockwise;
# else tmp < 0, a -> anticlockwise;
#
# tmp = (p1[0]-p0[0])(p2[1]-p0[1])-(p2[0]-p0[0])(p1[1]-p0[1])

# 76ms 26.67%
class Solution(object):
    def isConvex(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        def det(A):
            return A[0][0]*A[1][1] - A[0][1]*A[1][0]

        n, prev, curr = len(points), 0, None
        for i in xrange(len(points)):
            A = [[points[(i+j) % n][0] - points[i][0], points[(i+j) % n][1] - points[i][1]] for j in (1, 2)]
            curr = det(A)
            if curr:
                if curr * prev < 0:
                    return False
                prev = curr
        return True

    def isConvex2(self, points):
        last, tmp = 0, 0
        for i in xrange(2, len(points) + 3):
            p0, p1, p2 = points[(i - 2) % len(points)], points[(i - 1) % len(points)], points[i % len(points)]
            tmp = (p1[0]-p0[0])*(p2[1]-p0[1])-(p2[0]-p0[0])*(p1[1]-p0[1])
            if tmp:
                if last * tmp < 0:
                    return False
                last = tmp
        return True


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
https://discuss.leetcode.com/topic/70643/i-believe-this-time-it-s-far-beyond-my-ability-to-get-a-good-grade-of-the-contest
https://discuss.leetcode.com/topic/70664/c-7-line-o-n-solution-to-check-convexity-with-cross-product-of-adajcent-vectors-detailed-explanation
The algorithm itself is not hard but I have no idea there exists such a way to determine
if a polygon is convex or not. Laugh at me for my ignorance... I believe 90% of programmers
can solve this problem if they were given the formula.
Anyway, following is the Java solution with in-line explanation. Accepted, 32ms.
Reference: http://csharphelper.com/blog/2014/07/determine-whether-a-polygon-is-convex-in-c/

# 22ms 15.71%
class Solution {
    public boolean isConvex(List<List<Integer>> points) {
        // For each set of three adjacent points A, B, C, find the cross product AB *BC. If the sign of
        // all the cross products is the same, the angles are all positive or negative (depending on the
        // order in which we visit them) so the polygon is convex.
        boolean gotNegative = false;
        boolean gotPositive = false;
        int numPoints = points.size();
        int B, C;
        for (int A = 0; A < numPoints; A++) {
            // Trick to calc the last 3 points: n - 1, 0 and 1.
            B = (A + 1) % numPoints;
            C = (B + 1) % numPoints;

            int crossProduct =
                crossProductLength(
                    points.get(A).get(0), points.get(A).get(1),
                    points.get(B).get(0), points.get(B).get(1),
                    points.get(C).get(0), points.get(C).get(1));
            if (crossProduct < 0) {
                gotNegative = true;
            }
            else if (crossProduct > 0) {
                gotPositive = true;
            }
            if (gotNegative && gotPositive) return false;
        }

        // If we got this far, the polygon is convex.
        return true;
    }

    // Return the cross product AB x BC.
    // The cross product is a vector perpendicular to AB and BC having length |AB| * |BC| * Sin(theta) and
    // with direction given by the right-hand rule. For two vectors in the X-Y plane, the result is a
    // vector with X and Y components 0 so the Z component gives the vector's length and direction.
    private int crossProductLength(int Ax, int Ay, int Bx, int By, int Cx, int Cy)
    {
        // Get the vectors' coordinates.
        int BAx = Ax - Bx;
        int BAy = Ay - By;
        int BCx = Cx - Bx;
        int BCy = Cy - By;

        // Calculate the Z coordinate of the cross product.
        return (BAx * BCy - BAy * BCx);
    }
}
'''