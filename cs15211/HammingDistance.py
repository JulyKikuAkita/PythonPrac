__source__ = 'https://leetcode.com/problems/hamming-distance'
# https://github.com/kamyu104/LeetCode/blob/master/Python/hamming-distance.py
# Time:  O(1)
# Space: O(1)
#
# Description: Leetcode # 461. Hamming Distance
#
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

    # 20ms 100%
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

    # 20ms 100%
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
# Thought:

# 6ms 71.06%
class Solution {
    public int hammingDistance(int x, int y) {
        return Integer.bitCount(x ^ y);
    }
}

# 6ms 71.06%
class Solution {
    public int hammingDistance(int x, int y) {
        int xor = x ^ y, count = 0;
        for (int i=0;i<32;i++) count += (xor >> i) & 1;
        return count;
    }
}

# 4ms 100%
class Solution {
    public int hammingDistance(int x, int y) {
        int number = x ^ y;
        int ans = 0;
        while (number > 0) {
            ans += number & 1;
            number = number >> 1;
        }
        return ans;
    }
}
'''