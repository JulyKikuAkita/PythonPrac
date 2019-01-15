__source__ = 'https://leetcode.com/problems/product-of-array-except-self/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/product-of-array-except-self.py
# https://leetcode.com/problems/product-of-array-except-self/#/description
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 238. Product of Array Except Self
#
# Given an array of n integers where n > 1, nums,
# return an array output such that output[i] is equal to
# the product of all the elements of nums except nums[i].
#
# Solve it without division and in O(n).
#
# For example, given [1,2,3,4], return [24,12,8,6].
#
#
# Follow up:
# Could you solve it with constant space complexity?
# (Note: The output array does not count as extra space
# for the purpose of space complexity analysis.)
#
# Companies
# Amazon LinkedIn Apple Facebook Microsoft
# Related Topics
# Array
# Similar Questions
# Trapping Rain Water Maximum Product Subarray Paint House II
#
import unittest
class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        if not nums:
            return []

        left_product = [ 1 for _ in xrange(len(nums))]
        for i in xrange(1, len(nums)):
            left_product[i] =  left_product[i-1] * nums[i - 1]

        right_product = 1
        for i in xrange(len(nums) - 2, -1, -1):
            right_product *= nums[i + 1]
            left_product[i] = left_product[i] * right_product
        return left_product

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

The idea is simply.
The product basically is calculated using the numbers before the current number
and the numbers after the current number. Thus, we can scan the array twice.
First, we calculate the running product of the part before the current number.
Second, we calculate the running product of the part after the current number
through scanning from the end of the array.

# 2ms 39.37%
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];
        res[0] = 1;
        for (int i = 1; i < n; i++) {
            res[i] = res[i - 1] * nums[i - 1];
        }
        int right = 1;
        for (int i = n - 1; i >= 0; i--) {
            res[i] *= right;
            right *= nums[i];
        }
        return res;
    }
}

# 2ms 51.31%
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];
        for (int i = 0, tmp = 1; i < n; i++) {
            res[i] = tmp;
            tmp *= nums[i];
        }
        
        for (int i = n - 1, tmp = 1; i >= 0; i--) {
            res[i] *= tmp;
            tmp *= nums[i];
        }
        return res;
    }
}
'''
