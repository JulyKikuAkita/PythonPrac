__source__ = 'https://leetcode.com/problems/power-of-two/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/power-of-two.py
# Time:  O(1)
# Space: O(1)
#
# Description: Leetcode # 231. Power of Two
#
# Given an integer, write a function to determine if it is a power of two.
#
# Companies
# Google
# Related Topics
# Math Bit Manipulation
# Similar Questions
# Number of 1 Bits Power of Three Power of Four
#
import unittest
import math
class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n-1)) == 0
    def isPowerOfTwo2IF(self, n):
        return n > 0 and pow(2, int(math.log(n) / math.log(2))) == n

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

4 different ways to solve -- Iterative / Recursive / Bit operation / Math
Method 1: Iterative
check if n can be divided by 2. If yes, divide n by 2 and check it repeatedly.
# 1ms 100%
class Solution {
    public boolean isPowerOfTwo(int n) {
        if(n==0) return false;
        while(n%2==0) n/=2;
        return (n==1);
    }
}

Method 2: Recursive
Time complexity = O(log n)
# 1ms 100%
class Solution {
    public boolean isPowerOfTwo(int n) {
        return n>0 && (n==1 || (n%2==0 && isPowerOfTwo(n/2)));
    }
}


Method 3: Bit operation
Time complexity = O(1)

    If n is the power of two:

    n = 2 ^ 0 = 1 = 0b0000...00000001, and (n - 1) = 0 = 0b0000...0000.
    n = 2 ^ 1 = 2 = 0b0000...00000010, and (n - 1) = 1 = 0b0000...0001.
    n = 2 ^ 2 = 4 = 0b0000...00000100, and (n - 1) = 3 = 0b0000...0011.
    n = 2 ^ 3 = 8 = 0b0000...00001000, and (n - 1) = 7 = 0b0000...0111.
    we have n & (n-1) == 0b0000...0000 == 0

    Otherwise, n & (n-1) != 0.

    For example, n =14 = 0b0000...1110, and (n - 1) = 13 = 0b0000...1101.

# 1ms 100%
class Solution {
    public boolean isPowerOfTwo(int n) {
        return n > 0 && (n & (n - 1)) == 0;
    }
}

# 1ms 100%
class Solution {
    public boolean isPowerOfTwo(int n) {
        return n>0 && Integer.bitCount(n) == 1;
    }
}


Method 4: Math derivation

    Because the range of an integer = -2147483648 (-2^31) ~ 2147483647 (2^31-1),
    the max possible power of two = 2^30 = 1073741824.
    (1) If n is the power of two, let n = 2^k, where k is an integer.
    We have 2^30 = (2^k) * 2^(30-k), which means (2^30 % 2^k) == 0.
    (2) If n is not the power of two, let n = j*(2^k), where k is an integer and j is an odd number.
    We have (2^30 % j*(2^k)) == (2^(30-k) % j) != 0.

Time complexity = O(1)

# 1ms 100%
class Solution {
    public boolean isPowerOfTwo(int n) {
        return n>0 && (1073741824 % n == 0);
    }
}

'''