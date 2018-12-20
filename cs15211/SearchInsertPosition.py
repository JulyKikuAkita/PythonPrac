__source__ = 'https://leetcode.com/problems/search-insert-position/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/search-insert-position.py
# Time:  O(logn)
# Space: O(1)
# Binary Search
#
# Description: Leetcode # 35. Search Insert Position
#
# Given a sorted array and a target value, return the index if the target is found.
#
# If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.
#
# Here are few examples.
# [1,3,5,6], 5 -> 2
# [1,3,5,6], 2 -> 1
# [1,3,5,6], 7 -> 4
# [1,3,5,6], 0 -> 0
#
# Related Topics
# Array Binary Search
# Similar Questions
# First Bad Version

import unittest
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        low, high = 0, len(A) - 1

        while low <= high:
            mid = (low + high) / 2
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low

class SolutionOther:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        l, r = 0, len(A)
        while l < r:
            m = (l+r)/2
            if A[m] < target:
                l = m+1
            else:
                r = m
        return l
 #test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        test = SolutionOther()
        print test.searchInsert([], 8 )
        print test.searchInsert([-100, -1], 8 )
        print test.searchInsert([1,3,5,7,9], 8 )
        print test.searchInsert([1,3,5,7,9], 7 )
        print Solution().searchInsert([1, 3, 5, 6], 5)
        print Solution().searchInsert([1, 3, 5, 6], 2)
        print Solution().searchInsert([1, 3, 5, 6], 7)
        print Solution().searchInsert([1, 3, 5, 6], 0)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
# 2ms 100%
class Solution {
    public int searchInsert(int[] nums, int target) {
        if (nums.length == 0 || nums[nums.length - 1] < target) {
            return nums.length;
        }
        int start = 0;
        int end = nums.length - 1;
        while (start < end) {
            int mid = start + (end - start) / 2;
            if (nums[mid] < target) {
                start = mid + 1;
            } else {
                end = mid;
            }
        }
        return start;
    }
}

# Binary search
# version 1: find the first position >= target
# 4ms 36.75%
class Solution {
    public int searchInsert(int[] A, int target) {
        if (A == null || A.length == 0) {
            return 0;
        }
        int start = 0, end = A.length - 1;

        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (A[mid] == target) {
                return mid;
            } else if (A[mid] < target) {
                start = mid;
            } else {
                end = mid;
            }
        }

        if (A[start] >= target) {
            return start;
        } else if (A[end] >= target) {
            return end;
        } else {
            return end + 1;
        }
    }
}

# 4ms 36.75%
class Solution {
    public int searchInsert(int[] A, int target) {
        if (A == null || A.length == 0) {
            return 0;
        }
        for (int i = 0; i < A.length; i++) {
            if (target <= A[i]) {
                return i;
            }
        }
        return A.length;
    }
}
'''
