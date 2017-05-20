__author__ = 'July'
# https://leetcode.com/problems/move-zeroes/
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #bubble sort
        #mark = -1 if nums[0] != 0 else 0
        mark = -1
        for i in xrange(len(nums)):
            if mark == -1 and nums[i] == 0:
                mark = i
            elif mark != -1 and nums[i] != 0 and i > mark:
                nums[i], nums[mark] = nums[mark], nums[i]
                mark = mark + 1 if nums[(mark+1)] == 0 else i




#test
nums = [0, 1, 0, 3, 12]
nums2 = [1, 0 ,1]
if __name__ == "__main__":
    Solution().moveZeroes(nums2)
    print nums2