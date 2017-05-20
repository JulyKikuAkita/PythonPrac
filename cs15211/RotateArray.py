__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/rotate-array.py
# Time:  O(n)
# Space: O(1)
# Array
#
# Rotate an array of n elements to the right by k steps.
#
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
#
# Note:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
#
'''
Assuming we are given {1,2,3,4,5,6} and order 2. The basic idea is:
1. Divide the array two parts: 1,2,3,4 and 5, 6
2. Rotate first part: 4,3,2,1,5,6
3. Rotate second part: 4,3,2,1,6,5
4. Rotate the whole array: 5,6,1,2,3,4
'''
class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        k %= len(nums)
        self.reverse(nums, 0, len(nums))
        self.reverse(nums, 0, k)
        self.reverse(nums, k, len(nums))

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end - 1] = nums[end - 1], nums[start]
            start += 1
            end -= 1

from fractions import gcd
class Solution2:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        k %= len(nums)
        num_cycle = gcd(len(nums), k)
        cycle_len = len(nums) / num_cycle
        #print k, num_cycle, cycle_len
        for i in xrange(num_cycle):
            self.apply_cycle_permutation(k , i , cycle_len, nums)

    def apply_cycle_permutation(self, k, offset, cycle_len, nums):
        tmp = nums[offset]
        for i in xrange(1, cycle_len):
            print ((offset + i * k) % len(nums)), offset, nums[(offset + i * k) % len(nums)], nums
            nums[(offset + i * k) % len(nums)], tmp = tmp , nums[(offset + i * k) % len(nums)]
        nums[offset] = tmp

# http://www.programcreek.com/2015/03/rotate-array-in-java/
# Solution 2 - Bubble Rotate
# Time:  O(n * k)
# Space: O(1)
class javaSolution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        if not nums or k < 0:
            raise ValueError("Illegal argument!")
        k = k % len(nums)
        for i in xrange(k):
            for j in reversed(xrange(len(nums))):
                nums[j], nums[j-1] = nums[j-1], nums[j]


#test
if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    nums1 = [-1]
    nums2 = [1,2,3,4,5]
    Solution2().rotate(nums2, 2)
    print nums2