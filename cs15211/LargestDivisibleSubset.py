__source__ = 'https://leetcode.com/problems/largest-divisible-subset/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/largest-divisible-subset.py
# Time:  O(n^2)
# Space: O(n)
#
# Description: Leetcode # 368. Largest Divisible Subset
#
# Given a set of distinct positive integers,
# find the largest subset such that every pair (Si, Sj) of
# elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.
#
# If there are multiple solutions, return any subset is fine.
#
# Example 1:
#
# nums: [1,2,3]
#
# Result: [1,2] (of course, [1,3] will also be ok)
# Example 2:
#
# nums: [1,2,4,8]
#
# Result: [1,2,4,8]
#
# Companies
# Google
# Related Topics
# Math Dynamic Programming
#
import unittest
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        nums.sort()
        dp = [1] * len(nums)
        prev = [-1] * len(nums)
        largest_idx = 0
        for i in xrange(len(nums)):
            for j in xrange(i):
                if nums[i] % nums[j] == 0:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            if dp[largest_idx] < dp[i]:
                largest_idx = i
        result = []
        i = largest_idx
        while i != -1:
            result.append(nums[i])
            i = prev[i]
        return result[::-1]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# 21ms 94.39%
class Solution {
    public List<Integer> largestDivisibleSubset(int[] nums) {
        List<Integer> result = new ArrayList<>();
        int[] dp = new int[nums.length];
        int max = 1;

        if (nums.length == 0) {
            return result;
        }
        dp[0] = 1;
        Arrays.sort(nums);
        for (int i = 1; i < nums.length; i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++) {
                if (nums[i] % nums[j] == 0) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                    max = Math.max(max, dp[i]);
                }
            }
        }
        int index = nums.length - 1;
        Integer prev = null;
        while (max > 0) {
            while (dp[index] < max || (prev != null && prev % nums[index] != 0)) {
                index--;
            }
            result.add(nums[index]);
            prev = nums[index];
            max--;
            index--;
        }
        Collections.reverse(result);
        return result;
    }
}

# 37ms 29.93%
class Solution {
    public List<Integer> largestDivisibleSubset(int[] nums) {
        List<Integer> res = new ArrayList();
        int n = nums.length;
        if (n == 0) return res;

        Arrays.sort(nums);
        int[] count = new int[n];
        int[] pre = new int[n];
        int max = 1, index = 0;

        for (int i = 0; i < n; i++) {
            count[i] = 1;
            pre[i] = -1;
            for (int j = i - 1; j >= 0; j--) {
                if (nums[i] % nums[j] == 0) {
                    if ( 1 + count[j] > count[i]) {
                        count[i] = 1 + count[j];
                        pre[i] = j;
                    }
                }
            }
            if (count[i] > max) {
                max = count[i];
                index = i;
            }
        }

        while (index != -1) {
            res.add(nums[index]);
            index = pre[index];
        }
        return res;
    }
}

# 16ms 100%
class Solution {
    public List<Integer> largestDivisibleSubset(int[] nums) {
        int n = nums.length, maxIdx = 0;
        List<Integer> ans = new LinkedList<>();
        if (n == 0) return ans;
        Arrays.sort(nums);
        int[] lens = new int[n], prevs = new int[n];
        Arrays.fill(prevs, -1);
        for (int i = 0; nums[i] <= nums[n-1]/2; ++i) {
            for (int j = i + 1, f = 2; nums[i] <= nums[n-1]/f; f = (nums[j] + nums[i] - 1)/nums[i]) {
                int idx = Arrays.binarySearch(nums, j, n, f*nums[i]);
                if (idx > 0 && lens[idx] <= lens[i]) {
                    prevs[idx] = i;
                    lens[idx] = lens[i] + 1;
                    if (lens[idx] > lens[maxIdx]) maxIdx = idx;
                }
                j = idx >= 0 ? idx + 1 : -(idx + 1);
                if (j >= n) break;
            }
        }
        for (int i = maxIdx; i >= 0; i = prevs[i]) ans.add(0, nums[i]);
        return ans;
    }
}
'''
