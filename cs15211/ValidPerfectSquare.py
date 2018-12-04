__source__ = 'https://leetcode.com/problems/valid-perfect-square/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/valid-perfect-square.py
# Time:  O(logn)
# Space: O(1)
#
# Description: Leetcode # 367. Valid Perfect Square
#
# Given a positive integer num, write a function
# which returns True if num is a perfect square else False.
#
# Note: Do not use any built-in library function such as sqrt.
#
# Example 1:
# Input: 16
# Returns: True
# Example 2:
#
# Input: 14
# Returns: False
#
# Companies
# LinkedIn
# Related Topics
# Math Binary Search
# Similar Questions
# Sqrt(x) Sum of Square Numbers
#
import unittest
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left, right = 1, num
        while left <= right:
            mid = left + (right - left) / 2
            if mid >= num / mid:
                right = mid - 1
            else:
                left = mid + 1
        return left == num / left and num % left == 0

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# 0ms 100%
public class Solution {
    public boolean isPerfectSquare(int num) {
        if (num < 0) {
            return false;
        } else if (num == 0) {
            return true;
        }
        long left = 1;
        long right = num;
        while (left <= right) {
            long mid = left + ((right - left) >> 1);
            long sq = mid * mid;
            if (sq < num) {
                left = mid + 1;
            } else if (sq > num) {
                right = mid - 1;
            } else {
                return true;
            }
        }
        return false;
    }
}

# 0ms 100%
class Solution {
    public boolean isPerfectSquare(int num) {
        if (num < 0) return false;
        else if (num == 0) return true;
        long left = 1, right = num;
        while (left + 1 < right) {
            long mid = left + (right - left) / 2;
            long sq = mid * mid;
            if ( sq < num) {
                left = mid + 1;
            } else if (sq > num) {
                right = mid - 1;
            } else {
                return true;
            }
        }
        if (right * right == num) return true;
        else if (left * left == num) return true;
        else return false;
    }
}
'''