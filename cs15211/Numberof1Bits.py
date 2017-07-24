__source__ = 'https://leetcode.com/problems/number-of-1-bits/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/number-of-1-bits.py
# Time:  O(m)
# Space: O(1)
#
# Description: Leetcode # 191. Number of 1 Bits
# Write a function that takes an unsigned integer
# and returns the number of '1' bits it has (also known as the Hamming weight).
#
# For example, the 32-bit integer '11' has binary representation 00000000000000000000000000001011,
# so the function should return 3.
#
# Companies
# Microsoft Apple
# Related Topics
# Bit Manipulation
# Similar Questions
# Reverse Bits Power of Two Counting Bits Binary Watch Hamming Distance
#
import unittest
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

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().hammingWeight(4)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/number-of-1-bits/solution/
Approach #2 (Bit Manipulation Trick) [Accepted]
The key idea here is to realize that for any number n,
doing a bit-wise AND of n and n - 1 flips the least-significant 1-bit in n to 0.

# 79.87% 1ms
public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int result = 0;
        while (n != 0) {
            n &= n - 1;
            result++;
        }
        return result;
    }
}

Approach #1 (Loop and Flip) [Accepted]
# Time:  O(m) 32 bit
# Space: O(1)
# 9.34% 2ms
public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int bits = 0;
        int mask = 1;
        for (int i = 0; i < 32; i++) {
            if ((n & mask) != 0) {
                bits++;
            }
            mask <<= 1;
        }
        return bits;
    }
}

'''