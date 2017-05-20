__author__ = 'July'
'''
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].
'''

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in xrange(1, len(nums)):
            if ((i % 2) and nums[i - 1] > nums[i]) or \
                (not (i % 2) and nums[i - 1] < nums[i]):
                # Swap unordered elements.
                nums[i - 1], nums[i] = nums[i], nums[i - 1]


#Java
# http://blog.csdn.net/xudli/article/details/48749155
'''
public class Solution {
    public void wiggleSort(int[] nums) {
        if(nums == null || nums.length <2 ) return;

        for(int i = 1; i < nums.length; i++){
            if( (i % 2 == 0 && nums[i-1] < nums[i] ) || (i % 2 != 0 && nums[i-1] > nums[i])){
                int tmp = nums[i];
                nums[i] = nums[i-1];
                nums[i-1] = tmp;
            }
        }

    }
}
'''