__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/factorial-trailing-zeroes.py
# http://bookshadow.com/weblog/2014/12/30/leetcode-factorial-trailing-zeroes/
# Time:  O(logn)
# Space: O(1)
# Math
#
# Given an integer n, return the number of trailing zeroes in n!.  (5 * 2) = 10
#
# Note: Your solution should be in logarithmic time complexity.
#

class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        result = 0
        while n > 0:
            result += n / 5
            n /= 5
        return result

#test
if __name__ == "__main__":
    print Solution().trailingZeroes(99)