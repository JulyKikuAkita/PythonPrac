__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/water-and-jug-problem.py
# Time:  O(logn),  n is the max of (x, y)
# Space: O(1)

# You are given two jugs with capacities x and y litres.
# There is an infinite amount of water supply available.
# You need to determine whether it is possible to
# measure exactly z litres using these two jugs.
#
# Operations allowed:
#
# Fill any of the jugs completely.
# Empty any of the jugs.
# Pour water from one jug into another till
# the other jug is completely full or
# the first jug itself is empty.
# Example 1:
#
# Input: x = 2, y = 6, z = 4
# Output: True
# Example 2:
#
# Input: x = 2, y = 6, z = 5
# Output: False

# https://www.youtube.com/watch?v=BVtQNK_ZUJg
# Jugs Problem from the movie Die Hard 3 including problem and solution.
# The solution's not explained well in the video.
#  It's explained better here : http://www.math.tamu.edu/~dallen/holl...

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        return z == 0 or ((x + y >= z) and (z % gcd(x, y) == 0))

#java
js = '''
public class Solution {
    public boolean canMeasureWater(int x, int y, int z) {
        if (x < y) {
            return canMeasureWater(y, x, z);
        } else if (z == 0) {
            return true;
        } else if (y == 0) {
            return x == z;
        } else if (x + y < z) {
            return false;
        }
        return z % gcd(x, y) == 0;
    }

    private int gcd(int x, int y) {
        int cur;
        while ((cur = x % y) != 0) {
            x = y;
            y = cur;
        }
        return y;
    }
}
'''
