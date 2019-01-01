__source__ = 'https://leetcode.com/problems/subarray-sum-equals-k/'
# Time:  O(N)
# Space: O(N)
#
# Description: Leetcode # 560. Subarray Sum Equals K
#
# Given an array of integers and an integer k,
# you need to find the total number of continuous subarrays whose sum equals to k.
#
# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
# Note:
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
# Hide Company Tags Google
# Hide Tags Array Map
# Hide Similar Problems (E) Two Sum (M) Continuous Subarray Sum
#
import unittest
import collections
# 64ms 24.71%
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = collections.Counter()
        count[0] = 1
        ans = su = 0
        for x in nums:
            su += x
            ans += count[su-k]
            count[su] += 1
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/subarray-sum-equals-k/solution/
# O(n)
# 17ms 98.97%
class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0;
        int sum = 0;
        Map<Integer, Integer> map = new HashMap();
        map.put(0, 1);
        for (int start = 0; start < nums.length; start++) {
            sum += nums[start];
            if (map.containsKey(sum - k)) {
                count += map.get(sum - k);
            }
            map.put(sum, map.getOrDefault(sum, 0) + 1);
        }
        return count;
    }
}

'''
