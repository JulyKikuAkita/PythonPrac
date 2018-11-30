__source__ = 'https://leetcode.com/problems/binary-search/'
# Time:  O(LogN)
# Space: O(1)
#
# Description: Leetcode # 704. Binary Search
#
# Given a sorted (in ascending order) integer array nums of n elements and a target value,
# write a function to search target in nums.
# If target exists, then return its index, otherwise return -1.
#
# Example 1:
#
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
#
# Example 2:
#
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
#
#
# Note:
#
# You may assume that all elements in nums are unique.
# n will be in the range [1, 10000].
# The value of each element in nums will be in the range [-9999, 9999].
#
import unittest

class Solution(object):
    pass  # your function here


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# 2ms 100%
class Solution {
    public int search(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while(left + 1 < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) return mid;
            else if (nums[mid] < target) left = mid;
            else right = mid;
        }
        return nums[left] == target ? left : nums[right] == target ? right : -1;
    }
}
'''