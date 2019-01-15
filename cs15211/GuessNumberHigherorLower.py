__source__ = 'https://leetcode.com/problems/guess-number-higher-or-lower/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/guess-number-higher-or-lower.py
# Time:  O(logn)
# Space: O(1)
#
# Description: Leetcode # 374. Guess Number Higher or Lower
#
# We are playing the Guess Game. The game is as follows:
#
# I pick a number from 1 to n. You have to guess which number I picked.
#
# Every time you guess wrong, I'll tell you whether the number is higher or lower.
#
# You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):
#
# -1 : My number is lower
#  1 : My number is higher
#  0 : Congrats! You got it!
# Example:
# n = 10, I pick 6.
#
# Return 6.
#
# Companies
# Google
# Related Topics
# Binary Search
# Similar Questions
# First Bad Version Guess Number Higher or Lower II Find K Closest Elements
#

import unittest
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while start <= end:
            mid = (start + end) / 2
            cur = guess(mid)
            if cur > 0:
                start = mid + 1
            elif cur < 0:
                end = mid - 1
            else:
                return mid
        return 0

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/guess-number-higher-or-lower/solution/

/* The guess API is defined in the parent class GuessGame.
   @param num, your guess
   @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
      int guess(int num); */
# Binary search
# 0ms 100%
class Solution extends GuessGame {
    public int guessNumber(int n) {
        int start = 1;
        int end = n;
        while (start <= end) {
            int mid = start + ((end - start) >> 1);
            int cur = guess(mid);
            if (cur > 0) {
                start = mid + 1;
            } else if (cur < 0) {
                end = mid - 1;
            } else {
                return mid;
            }
        }
        return 0;
    }
}

# Ternary search
Time complexity : O(log base3 n). Ternary Search is used.
Space complexity : O(1). No extra space is used.

# 0ms 100%
class Solution extends GuessGame {
    public int guessNumber(int n) {
        int low = 1;
        int high = n;
        while (low <= high) {
            int mid1 = low + (high - low) / 3;
            int mid2 = high - (high - low) / 3;
            int res1 = guess(mid1);
            int res2 = guess(mid2);
            if (res1 == 0)
                return mid1;
            if (res2 == 0)
                return mid2;
            else if (res1 < 0)
                high = mid1 - 1;
            else if (res2 > 0)
                low = mid2 + 1;
            else {
                low = mid1 + 1;
                high = mid2 - 1;
            }
        }
        return -1;
    }
}
'''