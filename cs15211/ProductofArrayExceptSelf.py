__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/product-of-array-except-self.py
# https://leetcode.com/problems/product-of-array-except-self/#/description
# Time:  O(n)
# Space: O(1)
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
#  Amazon LinkedIn Apple Facebook Microsoft
# Hide Tags Array
# Hide Similar Problems (H) Trapping Rain Water (M) Maximum Product Subarray (H) Paint House II

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

java = '''
The idea is simply.
The product basically is calculated using the numbers before the current number
and the numbers after the current number. Thus, we can scan the array twice.
First, we calcuate the running product of the part before the current number.
Second, we calculate the running product of the part after the current number
through scanning from the end of the array.

public class Solution {
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
'''