__source__ = 'https://leetcode.com/problems/erect-the-fence/'
# Time:  O()
# Space: O()
#
# Description: 587. Erect the Fence
#
# There are some trees, where each tree is represented by (x,y) coordinate in a two-dimensional garden.
# Your job is to fence the entire garden using the minimum length of rope as it is expensive.
# The garden is well fenced only if all the trees are enclosed.
# Your task is to help find the coordinates of trees which are exactly located on the fence perimeter.
#
# Example 1:
# Input: [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
# Output: [[1,1],[2,0],[4,2],[3,3],[2,4]]
# Explanation:
#
# Example 2:
# Input: [[1,2],[2,2],[4,2]]
# Output: [[1,2],[2,2],[4,2]]
# Explanation:
#
# Even you only have trees in a line, you need to use rope to enclose them.
# Note:
#
# All trees should be enclosed together. You cannot cut the rope to enclose trees that will separate them in more than one group.
# All input integers will range from 0 to 100.
# The garden has at least one tree.
# All coordinates are distinct.
# Input points have NO order. No order required for output.
# Hide Company Tags Google
# Hide Tags Geometry

import unittest


class Solution(object):
    pass  # your function here


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/erect-the-fence/solution/

There are couple of ways to solve Convex Hull problem. https://en.wikipedia.org/wiki/Convex_hull_algorithms
The following code implements Gift wrapping aka Jarvis march algorithm
https://en.wikipedia.org/wiki/Gift_wrapping_algorithm and also added logic to handle
case of multiple Points in a line because original Jarvis march algorithm assumes no three points are collinear.
It also uses knowledge in this problem https://leetcode.com/problems/convex-polygon .
Disscussion: https://discuss.leetcode.com/topic/70706/beyond-my-knowledge-java-solution-with-in-line-explanation

Java Graham scan with adapted sorting to deal with collinear points
The trick is that once all points are sorted by polar angle with respect to the reference point:

For collinear points in the begin positions, make sure they are sorted by distance to reference point in ascending order.
For collinear points in the end positions, make sure they are sorted by distance to reference point in descending order.
For example:
(0, 0), (2, 0), (3, 0), (3, 1), (3, 2), (2, 2), (1, 2), (0, 2), (0, 1)
These points are sorted by polar angle
The reference point (bottom left point) is (0, 0)

In the begin positions (0, 0) collinear with (2, 0), (3, 0) sorted by distance to reference point in ascending order.
In the end positions (0, 0) collinear with (0, 2), (0, 1) sorted by distance to reference point in descending order.

/**
 * Definition for a point.
 * class Point {
 *     int x;
 *     int y;
 *     Point() { x = 0; y = 0; }
 *     Point(int a, int b) { x = a; y = b; }
 * }
 */

# 12ms 99.07%
class Solution {
    public List<Point> outerTrees(Point[] points) {
        Set<Point> result = new HashSet<>();
        // Find the leftmost point

        Point first = points[0];
        int firstIndex = 0;
        for (int i = 1; i < points.length; i++) {
            if (points[i].x < first.x) { //get the smallest x
                first = points[i];
                firstIndex = i;
            }
        }
        result.add(first);

        Point cur = first;
        int curIndex = firstIndex;
         do {
            Point next = points[0];
            int nextIndex = 0;
            for (int i = 1; i < points.length; i++) {
                if (i == curIndex) continue;
                int cross = crossProductLength(cur, points[i], next);
                if (nextIndex == curIndex || cross > 0 ||
                        // Handle collinear points
                        (cross == 0 && distance(points[i], cur) > distance(next, cur))) {
                    next = points[i];
                    nextIndex = i;
                }
            }
            // Handle collinear points
            for (int i = 0; i < points.length; i++) {
                if (i == curIndex) continue;
                int cross = crossProductLength(cur, points[i], next);
                if (cross == 0) {
                    result.add(points[i]);
                }
            }

            cur = next;
            curIndex = nextIndex;

        } while (curIndex != firstIndex);

        return new ArrayList<Point>(result);
    }

    private int crossProductLength(Point A, Point B, Point C) {
        // Get the vectors' coordinates.
        int BAx = A.x - B.x;
        int BAy = A.y - B.y;
        int BCx = C.x - B.x;
        int BCy = C.y - B.y;

        // Calculate the Z coordinate of the cross product.
        return (BAx * BCy - BAy * BCx);
    }

    private int distance(Point p1, Point p2) {
        return (p1.x - p2.x) * (p1.x -p2.x) + (p1.y - p2.y) * (p1.y - p2.y);
    }

}
'''