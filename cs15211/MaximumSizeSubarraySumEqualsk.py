__source__ = 'https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/maximum-size-subarray-sum-equals-k.py
# Time:  O(n)
# Space: O(n)
#
# Description: Leetcode # 325. Maximum Size Subarray Sum Equals k
#
# Given an array nums and a target value k, find the maximum length of a subarray that sums to k.
# If there isn't one, return 0 instead.
#
# Example 1:
# Given nums = [1, -1, 5, -2, 3], k = 3,
# return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)
#
# Example 2:
# Given nums = [-2, -1, 2, 1], k = 1,
# return 2. (because the subarray [-1, 2] sums to 1 and is the longest)
#
# Follow Up:
# Can you do it in O(n) time?
#
# Companies
# Palantir Facebook
# Related Topics
# Hash Table
# Similar Questions
# Minimum Size Subarray Sum Range Sum Query - Immutable Contiguous Array
#
import unittest
# O(n)
# 40ms 72.57%
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        result, acc = 0, 0
        dic = { 0: -1} # so that when i - dict[acc-k] have correct len of subarr

        for i in xrange(len(nums)):
            acc += nums[i]
            if acc not in dict:  # need to have this for (key, val) not being update
                dict[acc] = i
            if acc - k in dict:
                result = max(result, i - dict[acc-k])
        return result

class Solution2(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums = {}
        cur_sum, max_len = 0, 0
        for i in xrange(len(nums)):
            cur_sum += nums[i]
            if cur_sum == k:
                max_len = i + 1
            elif cur_sum - k in sums:
                max_len = max(max_len, i - sums[cur_sum - k])
            if cur_sum not in sums:
                sums[cur_sum] = i  # Only keep the smallest index.
        return max_len

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
# 
# 13ms 95.45%
class Solution {
    public int maxSubArrayLen(int[] nums, int k) {
        if(nums == null || nums.length == 0) return 0;
        int len = nums.length;
        int[] sums = new int[len + 1];
        for (int i = 0; i < len; i++) {
            sums[i + 1] = sums[i] + nums[i];
        }
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 1; i < len + 1; i++) {
            map.put(sums[i], i);
        }
        int result = 0;
        for (int i = 0; i < len + 1; i++) {
            int curr = sums[i] + k;
            if (map.containsKey(curr)) {
                result = Math.max(result, map.get(curr) - i);
            }
        }
        return result;
    }
}

# 23ms 26.54%
class Solution {
    public int maxSubArrayLen(int[] nums, int k) {
        if(nums == null || nums.length == 0) return 0;
        int len = nums.length;
        int[] sums = new int[len + 1];
        sums[0] = nums[0];
        for (int i = 1; i < len; i++) {
            sums[i] = sums[i - 1] + nums[i];
        }
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, -1);
        int result = 0;
        for (int i = 0; i < len; i++) {
            int curr = sums[i] - k;
            if (map.containsKey(curr)) {
                result = Math.max(result, i - map.get(curr));
            }
            if (!map.containsKey(sums[i])) map.put(sums[i], i);
        }
        return result;
    }
}

# 29ms 13.32%
class Solution {
    public int maxSubArrayLen(int[] nums, int k) {
        if(nums.length == 0) return 0;

        int len = nums.length;
        int sums = 0;
        int res = 0;
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, -1);
        for(int i = 0; i < len; i++){
            sums += nums[i];
            if(!map.containsKey(sums)){
                map.put(sums, i);
            }
            if(map.containsKey(sums - k)){
                res = Math.max(res, i - map.get(sums - k));
            }
        }
        return res;
    }
}

# 11ms 99.90%
class Solution {
    public int maxSubArrayLen(int[] nums, int k) {
        int[] sums = new int[nums.length + 1];
        for (int i = 0; i < nums.length; i++) {
            sums[i + 1] = sums[i] + nums[i];
        }
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length + 1; i++) {
            map.put(sums[i], i);
        }
        int result = 0;
        for (int i = 0; i < nums.length; i++) {
            int target = sums[i] + k;
            Integer val = map.get(target);
            if (val != null && val > i) {
                result = Math.max(result, val - i);
            }
        }
        return result;
    }
}
'''
