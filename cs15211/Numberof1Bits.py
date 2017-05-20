__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/number-of-1-bits.py
# Time:  O(m)
# Space: O(1)
#
#
# Write a function that takes an unsigned integer
# and returns the number of '1' bits it has (also known as the Hamming weight).
#
# For example, the 32-bit integer '11' has binary representation 00000000000000000000000000001011,
# so the function should return 3.
#
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.
#
class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        result = 0
        while n:
            n &= n - 1
            result += 1
        return result

# http://bookshadow.com/weblog/2015/03/10/leetcode-number-1-bits/
class Solution2:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        result = 0
        while n:
            result += n & 1;
            n >>= 1;
        return result
# Java
# http://www.programcreek.com/2014/03/leetcode-number-of-1-bits-java/

if __name__ == '__main__':
  print Solution().hammingWeight(4)