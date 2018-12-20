__source__ = 'https://leetcode.com/problems/rectangle-area/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/rectangle-area.py
# Time:  O(1)
# Space: O(1)
#
# Description: Leetcode # 223. Rectangle Area
#
# Find the total area covered by two rectilinear rectangles in a 2D plane.
#
# Each rectangle is defined by its bottom left corner
# and top right corner as shown in the figure.
#
# Rectangle Area
# Assume that the total area is never beyond the maximum
# possible value of int.
#
# Related Topics
# Math
#
import unittest
class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        return ( D - B ) * ( C - A ) + \
               ( G - E ) * ( H - F ) - \
               max(0, (min( C, G ) - max(A, E))) * \
               max(0, (min( D, H ) - max(B, F)))

#Java
# http://www.programcreek.com/2014/06/leetcode-rectangle-area-java/
class SolutionJava:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        if (C < E or G < A):
            return (G - E) * (H - F) + (C - A) * (D - B)

        if (D < F or H < B):
            return (G - E) * (H - F) + (C - A) * (D - B)

        right = min(C, G)
        left = max(A, E)
        top = min(H, D)
        bottom = max(F, B)

        return (G - E) * (H - F) + (C - A) * (D - B) - (right - left) *(top - bottom)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: 

# 2ms 100%
class Solution {
    public int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        if(B>=H || F>=D || C<=E || G<=A) {
            return (C-A)*(D-B)+(G-E)*(H-F);
        }
        int up = Math.min(D, H);
        int down = Math.max(B, F);
        int left = Math.max(A, E);
        int right = Math.min(C, G);
        return (C-A)*(D-B)+(G-E)*(H-F) - (up-down)*(right-left);
    }
}

# 2ms 100%
class Solution {
    public int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        return (int) (computeArea(A, B, C, D) + computeArea(E, F, G, H) -
            computeArea(Math.max(A, E), Math.max(B, F), Math.min(C, G), Math.min(D, H)));
    }

    private long computeArea(long A, long B, long C, long D) {
        return Math.max(C - A, 0) * Math.max(D - B, 0);
    }
}

# 3ms 56.63%
class Solution {
    public int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int left = Math.max(A,E), right = Math.max(Math.min(C,G), left);
        int bottom = Math.max(B,F), top = Math.max(Math.min(D,H), bottom);
        return (C-A)*(D-B) - (right-left)*(top-bottom) + (G-E)*(H-F);
    }
}
'''
