__source__ = 'https://leetcode.com/problems/remove-duplicates-from-sorted-array/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/remove-duplicates-from-sorted-array.py
# Time:  O(n)
# Space: O(1)
# Array
#
# Description: Leetcode # 26. Remove Duplicates from Sorted Array
#
# Given a sorted array, remove the duplicates in place such that
# each element appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
# For example,
# Given input array A = [1,1,2],
#
# Your function should return length = 2, and A is now [1,2].
# Companies
# Microsoft Bloomberg Facebook
# Related Topics
# Array Two Pointers
# Similar Questions
# Remove Element
#

import unittest
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        last, i = 0, 1
        while i < len(A):
            if A[last] != A[i]:
                last += 1
                A[last] = A[i]
            i += 1
        return last + 1

class SolutionOther:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0:
            return 0
        cur = 1
        for i in range(1, len(A)):
            if A[i] != A[i-1]:
                A[cur] = A[i]
                cur += 1
        return cur
#test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().removeDuplicates([1, 1, 2])

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/remove-duplicates-from-sorted-array/solution/

# 5ms 100%
class Solution {
    public int removeDuplicates(int[] nums) {
        int i = 0;
        for (int n : nums)
            if (i == 0 || n > nums[i-1])
                nums[i++] = n;
        return i;
    }
}

# 5ms 100%
class Solution {
    public int removeDuplicates(int[] nums) {
        int index = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[index]) {
                nums[++index] = nums[i];
            }
        }
        return index + 1;
    }
}

Approach #1 (Two Pointers) [Accepted]
# 10ms 37.71%
class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;
        int i = 0;
        for (int j = 1; j < nums.length; j++) {
            if (nums[j] != nums[i]) {
                i++;
                nums[i] = nums[j];
            }
        }
        return i + 1;
    }
}
'''
