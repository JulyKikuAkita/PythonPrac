__source__ = 'https://leetcode.com/problems/hamming-distance/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/hamming-distance.py
# Time:  O(1)
# Space: O(1)

# Description: Leetcode # 461. Hamming Distance
# The Hamming distance between two integers is the number of positions
# at which the corresponding bits are different.
#
# Given two integers x and y, calculate the Hamming distance.
#
# Note:
# 0 <= x, y < 231.
#
# Example:
#
# Input: x = 1, y = 4
#
# Output: 2
#
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ^   ^
# The above arrows point to positions where the corresponding bits are different.
# Companies
# Facebook
# Related Topics
# Bit Manipulation
# Similar Questions
# Number of 1 Bits Total Hamming Distance
#
import unittest
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        distance = 0
        z = x ^ y
        while z:
            distance += 1
            z &= z - 1
        return distance

    def hammingDistanceIlee(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ans = 0
        z = x ^ y
        while z:
            ans = ans + (1 & z)
            z >>= 1
            #print z, 1&z
        return ans

    def hammingDistance2(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count('1')

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().hammingWeight(4)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/number-of-1-bits/solution/

#4.82% 17ms
public class Solution {
    public int hammingDistance(int x, int y) {
        return Integer.bitCount(x ^ y);
    }
}

#75.86% 10ms
public class Solution {
    public int hammingDistance(int x, int y) {
        int xor = x ^ y, count = 0;
        for (int i=0;i<32;i++) count += (xor >> i) & 1;
        return count;
    }
}
'''