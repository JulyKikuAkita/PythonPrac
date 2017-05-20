__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/rectangle-area.py
# Time:  O(1)
# Space: O(1)
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

#java
js = '''
public class Solution {
    public int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        if ( E > C || F > D) return (C-A)*(D-B) + (G-E)*(H-F);
        else
            return (C-A)*(D-B) + (G-E)*(H-F) - (Math.max(0, (Math.min(H, D)- Math.max(F,B))) * Math.max(0, (Math.min(G, C)- Math.max(E,A))));
//-1500000001
//0
//-1500000000
//1
//1500000000
//0
//1500000001
//1

    }
}
'''
