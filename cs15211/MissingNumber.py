__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/missing-number.py
# Time:  O(n)
# Space: O(1)
#
# Given an array containing n distinct numbers taken from
# 0, 1, 2, ..., n, find the one that is missing from the array.
#
# For example,
# Given nums = [0, 1, 3] return 2.
#
# Note:
# Your algorithm should run in linear runtime complexity.
# Could you implement it using only constant extra space complexity?
#
# Bloomberg


import operator
class Solution(object):
    def missingNumber(self, nums):
         return reduce(operator.xor, nums, \
                      reduce(operator.xor, xrange(len(nums) + 1)))


class Solution2():
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1


        for n in nums:
            i = n
            if i == len(nums) and nums[len(nums)-1] != len(nums):
                n = nums[len(nums)-1]
                nums[len(nums)-1] = len(nums)
                i = n

            while i < len(nums) and i != nums[i]:
                tmp, nums[i] = nums[i], i,
                i = tmp

        for i in xrange(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)

#java
js = '''
public class Solution {
    public int missingNumber(int[] nums) {
        if (nums == null || nums.length == 0) return -1;

        for(int d : nums){
            if(d == nums.length && nums[nums.length-1] != nums.length){
                d = nums[nums.length-1];
                nums[nums.length-1] = nums.length;
            }else if(d == nums.length) break;
            int i = d;
            while( i < nums.length && i != nums[i]){
                int tmp = nums[i];
                nums[i] = i;
                i = tmp;
            }
        }


        for(int i = 0; i < nums.length; i++){
            if(nums[i] != i) return i;
        }
        return nums.length;
    }
}
'''