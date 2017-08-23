__source__ = 'https://leetcode.com/problems/single-number-iii/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/single-number-iii.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 260. Single Number III
#
# Given an array of numbers nums, in which exactly two
# elements appear only once and all the other elements
# appear exactly twice. Find the two elements that appear only once.
#
# For example:
#
# Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].
#
# Note:
# The order of the result is not important. So in the
# above example, [5, 3] is also correct.
# Your algorithm should run in linear runtime complexity.
# Could you implement it using only constant space complexity?
#
# Related Topics
# Bit Manipulation
# Similar Questions
# Single Number Single Number II
#
import operator
import unittest
class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def singleNumber(self, nums):
        x_xor_y = reduce(operator.xor, nums)
        bit = x_xor_y & -x_xor_y
        result = [0, 0]
        for i in nums:
            result[bool(i & bit)] ^= i
        return result

class Solution2:
    # @param {integer[]} nums
    # @return {integer[]}
    def singleNumber(self, nums):
        x_xor_y = 0
        for i in nums:
            x_xor_y ^= i

        bit = x_xor_y & ~(x_xor_y - 1)

        x = 0
        for i in nums:
            if i & bit:
                x ^= i
        return [x, x^x_xor_y]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().containsDuplicate([12344555,12344555])

if __name__ == '__main__':
    unittest.main()

Java = '''
Thought:
Once again, we need to use XOR to solve this problem. But this time, we need to do it in two passes:

In the first pass, we XOR all elements in the array,
and get the XOR of the two numbers we need to find. Note that since the two numbers are distinct,
so there must be a set bit (that is, the bit with value '1') in the XOR result. Find
out an arbitrary set bit (for example, the rightmost set bit).

In the second pass, we divide all numbers into two groups, one with the aforementioned bit set,
another with the aforementinoed bit unset.
Two different numbers we need to find must fall into thte two distrinct groups.
XOR numbers in each group, we can find a number in either group.

by XoRing all numbers in the first group, we can get the first number.
by XoRing all numbers in the second group, we can get the second number.

# 27.30% 2ms
public class Solution {
    public int[] singleNumber(int[] nums) {
        // Pass 1 :
        // Get the XOR of the two numbers we need to find
        int diff = 0;
        for (int num : nums) {
            diff ^= num;
        }
        // Get its last set bit
        diff &= -diff;

        // Pass 2 :
        int[] rets = {0, 0}; // this array stores the two numbers we will return
        for (int num : nums)
        {
            if ((num & diff) == 0) // the bit is not set
            {
                rets[0] ^= num;
            }
            else // the bit is set
            {
                rets[1] ^= num;
            }
        }
        return rets;
    }
}

# 27.30% 2ms
public class Solution {
    public int[] singleNumber(int[] nums) {
        int xor = 0;
        for (int num : nums) {
            xor ^= num;
        }
        int diff = xor & (-xor);
        int[] result = new int[2];
        for (int num : nums) {
            if ((num & diff) == 0) {
                result[0] ^= num;
            } else {
                result[1] ^= num;
            }
        }
        return result;
    }
}
'''
