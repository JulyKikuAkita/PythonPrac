__source__ = 'https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 702. Search in a Sorted Array of Unknown Size
#
# Given an integer array sorted in ascending order,
# write a function to search target in nums.
# If target exists, then return its index,
# otherwise return -1. However, the array size is unknown to you.
# You may only access the array using an ArrayReader interface,
# where ArrayReader.get(k) returns the element of the array at index k (0-indexed).
#
# You may assume all integers in the array are less than 10000,
# and if you access the array out of bounds,
# ArrayReader.get will return 2147483647.
#
# Example 1:
#
# Input: array = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:
#
# Input: array = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
#
# Note:
#
# You may assume that all elements in the array are unique.
# The value of each element in the array will be in the range [-9999, 9999].
#

import unittest

# 100% 32ms
class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        first = reader.get(0)
        if first == 2147483647:
            return -1
        elif first == target:
            return 0

        l, r = 0, 10000-first
        while r-l > 0:
            mid = (l+r)//2
            cur = reader.get(mid)
            if cur == target:
                return mid
            elif cur > target:
                 r = mid
            else:
                l = mid + 1
        return -1

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# 3ms 82.95%
class Solution {
    public int search(ArrayReader reader, int target) {
        int right = 1;
        while (reader.get(right) < target) {
            right *= 2;
        }
        int left = right / 2;
        while (left + 1 < right) {
            int mid = (right -left) / 2 + left;
            if (reader.get(mid) < target) {
                left = mid;
            } else {
                right = mid;
            }
        }
        return reader.get(left) == target? left: reader.get(right) == target? right: -1;
    }
}
'''
