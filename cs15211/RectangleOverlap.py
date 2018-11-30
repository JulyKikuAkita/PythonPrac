__source__ = 'https://leetcode.com/problems/rectangle-overlap/'
# Time:  O(1)
# Space: O(1)
#
# Description: Leetcode # 836. Rectangle Overlap
#
# A rectangle is represented as a list [x1, y1, x2, y2],
# where (x1, y1) are the coordinates of its bottom-left corner,
# and (x2, y2) are the coordinates of its top-right corner.
#
# Two rectangles overlap if the area of their intersection is positive.
# To be clear, two rectangles that only touch at the corner or edges do not overlap.
#
# Given two (axis-aligned) rectangles, return whether they overlap.
#
# Example 1:
#
# Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
# Output: true
# Example 2:
#
# Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
# Output: false
# Notes:
#
# Both rectangles rec1 and rec2 are lists of 4 integers.
# All coordinates in rectangles will be between -10^9 and 10^9.
#
import unittest

#20ms 97.85%
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        return not (rec1[2] <= rec2[0] or  # left
                    rec1[3] <= rec2[1] or  # bottom
                    rec1[0] >= rec2[2] or  # right
                    rec1[1] >= rec2[3])    # top

#28ms 14.38%
class SolutionByArea(object):
    def isRectangleOverlap(self, rec1, rec2):
        def intersect(p_left, p_right, q_left, q_right):
            return min(p_right, q_right) > max(p_left, q_left)
        return (intersect(rec1[0], rec1[2], rec2[0], rec2[2]) and # width > 0
                intersect(rec1[1], rec1[3], rec2[1], rec2[3]))    # height > 0


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
Approach #1: Check Position [Accepted]
Complexity Analysis
Time and Space Complexity: O(1)

#2ms 96.56%
class Solution {
    public boolean isRectangleOverlap(int[] rec1, int[] rec2) {
        return !(rec1[2] <= rec2[0] ||   // left
                 rec1[3] <= rec2[1] ||   // bottom
                 rec1[0] >= rec2[2] ||   // right
                 rec1[1] >= rec2[3]);    // top
    }
}


# https://leetcode.com/problems/rectangle-overlap/discuss/185809/Template%3A-Interval-Overlapping
# For overlapping questions:
#
# Interval A = [leftA, rightA]
# Interval B = [leftB, rightB]
# Overlapping region:  [max(leftA, leftB) , min(rightA, rightB)]
#
class Solution {
    public boolean isRectangleOverlap(int[] rec1, int[] rec2) {
        // Interval overlapping: Max(left1, left2) < Min(right1, right2)
        // x has overlapping && y has overlapping

        int x1 = rec1[0], y1 = rec1[1], x2 = rec1[2], y2 = rec1[3];
        int x3 = rec2[0], y3 = rec2[1], x4 = rec2[2], y4 = rec2[3];
        boolean overlapX = false;
        boolean overlapY = false;
        if(Math.max(x1, x3) < Math.min(x2, x4))
            overlapX = true;
        if(Math.max(y1, y3) < Math.min(y2, y4))
            overlapY = true;
        return overlapX && overlapY;
    }
}

Approach #2: Check Area [Accepted]
Complexity Analysis
Time and Space Complexity: O(1)

#2ms 96.56%
class Solution {
    public boolean isRectangleOverlap(int[] rec1, int[] rec2) {
        //Logic here is to compare x and y of correspoding points in both rectangle
        //If Mininum of top right corners (both x and y) lies beyond(is greater than)
        Maximum of bottom left corners(both x and y), we have at least one overlapping point
        return Math.min(rec1[2],rec2[2]) > Math.max(rec1[0],rec2[0]) && Math.min(rec1[3],rec2[3]) > Math.max(rec1[1],rec2[1]);
    }
}
'''