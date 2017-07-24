__source__ = 'https://leetcode.com/problems/move-zeroes/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/move-zeroes.py
# Time:  O(n)
# Space: O(1)
#
# Description: 283. Move Zeroes
#
# Given an array nums, write a function to move all 0's
# to the end of it while maintaining the relative order
# of the non-zero elements.
#
# For example, given nums = [0, 1, 0, 3, 12], after
# calling your function, nums should be [1, 3, 12, 0, 0].
#
# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# Companies
# Bloomberg Facebook
# Related Topics
# Array Two Pointers
# Similar Questions
# Remove Element
#
import unittest

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

class Solution3(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in xrange(len(nums)):
            if nums[i]:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1

    def moveZeroes2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort(cmp=lambda a, b: 0 if b else -1)


class Solution2(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in xrange(len(nums)):
            if nums[i]:
                nums[pos] = nums[i]
                pos += 1

        for i in xrange(pos, len(nums)):
            nums[i] = 0

class TestMethods(unittest.TestCase):
    def test_Local(self):
        nums = [0, 1, 0, 3, 12]
        nums2 = [1, 0 ,1]
        Solution().moveZeroes(nums2)
        print nums2

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/move-zeroes/solution/ in c++

#64.07% 0ms
public class Solution {
    // Shift non-zero values as far forward as possible
    // Fill remaining space with zeros
    public void moveZeroes(int[] nums) {
        if (nums == null || nums.length == 0) return;

        int insertPos = 0;
        for (int num: nums) {
            if (num != 0) nums[insertPos++] = num;
        }

        while (insertPos < nums.length) {
            nums[insertPos++] = 0;
        }
    }
}

# 16.67% 1ms
public class Solution {
    public void moveZeroes(int[] nums) {
        int start = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                swap(nums, start++, i);
            }
        }
        for (int i = start; i < nums.length; i++) {
            nums[i] = 0;
        }
    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}
'''