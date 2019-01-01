__source__ = 'https://leetcode.com/problems/max-chunks-to-make-sorted/'
# Time:  O(N)
# Space: O(1)
#
# Description: Leetcode # 769. Max Chunks To Make Sorted
#
# Given an array arr that is a permutation of [0, 1, ..., arr.length - 1],
# we split the array into some number of "chunks" (partitions),
# and individually sort each chunk.
# After concatenating them, the result equals the sorted array.
#
# What is the most number of chunks we could have made?
#
# Example 1:
#
# Input: arr = [4,3,2,1,0]
# Output: 1
# Explanation:
# Splitting into two or more chunks will not return the required result.
# For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2],
# which isn't sorted.
#
# Example 2:
#
# Input: arr = [1,0,2,3,4]
# Output: 4
# Explanation:
# We can split into two chunks, such as [1, 0], [2, 3, 4].
# However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.
#
# Note:
#     arr will have length in range [1, 10].
#     arr[i] will be a permutation of [0, 1, ..., arr.length - 1].
#
import unittest

# 20ms 98.80%
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ans = ma = 0
        for i, x in enumerate(arr):
            ma = max(ma, x)
            if ma == i: ans += 1
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/max-chunks-to-make-sorted/solution/
#
Approach #1: Brute Force [Accepted]
Complexity Analysis
Time Complexity: O(N), where N is the length of arr
Space Complexity: O(1)

# 2ms 100%
class Solution {
    public int maxChunksToSorted(int[] arr) {
        int ans = 0, max = 0;
        for (int i = 0; i < arr.length; ++i) {
            max = Math.max(max, arr[i]);
            if (max == i) ans++;
        }
        return ans;
    }
}
'''
