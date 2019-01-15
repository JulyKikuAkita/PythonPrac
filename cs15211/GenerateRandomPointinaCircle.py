# coding=utf-8
__source__ = 'https://leetcode.com/problems/generate-random-point-in-a-circle/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 478. Generate Random Point in a Circle
#
# Given the radius and x-y positions of the center of a circle,
# write a function randPoint which generates a uniform random point in the circle.
#
# Note:
#
#     input and output values are in floating-point.
#     radius and x-y position of the center of the circle is passed into the class constructor.
#     a point on the circumference of the circle is considered to be in the circle.
#     randPoint returns a size 2 array containing x-position and y-position of the random point, in that order.
#
# Example 1:
#
# Input:
# ["Solution","randPoint","randPoint","randPoint"]
# [[1,0,0],[],[],[]]
# Output: [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]
#
# Example 2:
#
# Input:
# ["Solution","randPoint","randPoint","randPoint"]
# [[10,5,-7.5],[],[],[]]
# Output: [null,[11.52438,-8.33273],[2.46992,-16.21705],[11.13430,-12.42337]]
#
# Explanation of Input Syntax:
#
# The input is two lists: the subroutines called and their arguments.
# Solution's constructor has three arguments, the radius, x-position of the center,
# and y-position of the center of the circle. randPoint has no arguments.
# Arguments are always wrapped with a list, even if there aren't any.
#
import unittest


class Solution(object):
    pass  # your function here


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/generate-random-point-in-a-circle/solution/
Approach 1: Rejection Sampling
Complexity Analysis
Time Complexity: O(1) on average. O(∞) worst case. (per randPoint call)
Space Complexity: O(1)

class Solution {
    double rad, xc, yc;
    public Solution(double radius, double x_center, double y_center) {
        rad = radius;
        xc = x_center;
        yc = y_center;
    }

    public double[] randPoint() {
        double x0 = xc - rad;
        double y0 = yc - rad;
        while (true) {
            double xg = x0 + Math.random() * rad * 2;
            double yg = y0 + Math.random() * rad * 2;
            if (Math.sqrt(Math.pow((xg - xc) , 2) + Math.pow((yg - yc), 2)) <= rad)
                return new double[]{xg, yg};
        }
    }
}

Approach 2: Inverse Transform Sampling (Math)
Complexity Analysis
Time Complexity: O(1) per randPoint call.
Space Complexity: O(1)
Footnotes
This technique of using the inverse cumulative distribution function
to sample numbers at random from the corresponding probability distribution
is called inverse transform sampling.
https://en.wikipedia.org/wiki/Inverse_transform_sampling
This solution is inspired by this answer on Stack Overflow.
https://stackoverflow.com/a/50746409

# 250ms 71.12%
class Solution {
    double rad, xc, yc;
    public Solution(double radius, double x_center, double y_center) {
        rad = radius;
        xc = x_center;
        yc = y_center;
    }

    public double[] randPoint() {
        double d = rad * Math.sqrt(Math.random());
        double theta = Math.random() * 2 * Math.PI;
        return new double[]{d * Math.cos(theta) + xc, d * Math.sin(theta) + yc};
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(radius, x_center, y_center);
 * double[] param_1 = obj.randPoint();
 */

'''