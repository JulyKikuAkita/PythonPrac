__source__ = 'https://leetcode.com/problems/shortest-unsorted-continuous-subarray/#/description'
# Time:  O()
# Space: O()
#
# Description:
# Given an integer array, you need to find one continuous subarray that
# if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.
#
# You need to find the shortest such subarray and output its length.
#
# Example 1:
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
# Note:
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means <=.
# Hide Company Tags LiveRamp Google
# Hide Tags Array

import unittest

# Sort the list and check if it's still the same number in the list.
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        is_same = [ a == b for a, b in zip(nums, sorted(nums)) ]
        return 0 if all(is_same) else len(nums) - is_same.index(False) - is_same[::-1].index(False)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
public class Solution {
    public int findUnsortedSubarray(int[] nums) {
        int n = nums.length, start = -1, end = -2, min = nums[n-1], max = nums[0];
        for (int i=1;i<n;i++) {
            max = Math.max(max, nums[i]);
            min = Math.min(min, nums[n - 1 -i]);
            if (nums[i] < max) end = i;
            if (nums[n -1 - i] > min) start = n - 1- i;
        }
        return end - start + 1;
    }
}
'''