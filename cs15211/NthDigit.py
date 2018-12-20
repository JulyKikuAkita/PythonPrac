__source__ = 'https://leetcode.com/problems/nth-digit/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/nth-digit.py
# Time:  O(logn)
# Space: O(1)
#
# Description: Leetcode # 400. Nth Digit
#
# Find the nth digit of the infinite integer sequence
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...
#
# Note:
# n is positive and will fit within the range of a 32-bit signed integer (n < 231).
#
# Example 1:
#
# Input:
# 3
#
# Output:
# 3
# Example 2:
#
# Input:
# 11
#
# Output:
# 0
#
# Explanation:
# The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
# ... is a 0, which is part of the number 10.
#
# Companies
# Google
# Related Topics
# Math
#
import unittest
# 20ms 99.50%
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit_len = 1
        while n > digit_len * 9 * (10 ** (digit_len-1)):
            n -= digit_len  * 9 * (10 ** (digit_len-1))
            digit_len += 1

        num = 10 ** (digit_len-1) + (n-1)/digit_len

        nth_digit = num / (10 ** ((digit_len-1) - ((n-1)%digit_len)))
        nth_digit %= 10

        return nth_digit

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

Straight forward way to solve the problem in 3 steps:

find the length of the number where the nth digit is from
find the actual number where the nth digit is from
find the nth digit and return

# 3ms 87.33%
class Solution {
    public int findNthDigit(int n) {
        int len = 1;
        long count = 9;
        int start = 1;

        while ( n > len * count) {
            n -= len * count;
            len += 1;
            count *= 10;
            start *= 10;
        }

        start += ( n - 1) / len;
        String s = Integer.toString(start);
        return Character.getNumericValue(s.charAt((n - 1) % len));
    }
}

'''
