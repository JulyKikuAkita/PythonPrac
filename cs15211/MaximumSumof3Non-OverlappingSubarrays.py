__source__ = 'https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/description/'
# Time:  O(N)
# Space: O(N)
#
# Description: Leetcode # 689. Maximum Sum of 3 Non-Overlapping Subarrays
#
# In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.
#
# Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.
#
# Return the result as a list of indices representing the starting position of each interval (0-indexed).
# If there are multiple answers, return the lexicographically smallest one.
#
# Example:
# Input: [1,2,1,2,6,7,5,1], 2
# Output: [0, 3, 5]
# Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
# We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
# Note:
# nums.length will be between 1 and 20000.
# nums[i] will be between 1 and 65535.
# k will be between 1 and floor(nums.length / 3).
#
# Companies
# Google Facebook
# Related Topics
# Array Dynamic Programming
# Similar Questions
# Best Time to Buy and Sell Stock III
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
#Thought: https://leetcode.com/articles/maximum-sum-of-3-non-overlapping-intervals/

The basic idea is that construct leftmax array and rightmax array to save the leftkmax subarray index
and rightkmax subarray index. After that, we use these prepossessed array to solve this question using O(N)
since we have saved all of max subarray index!

# 76.74% 9ms
class Solution {
    public int[] maxSumOfThreeSubarrays(int[] nums, int k) {
        int n = nums.length;

        int[] s = new int[n + 1];
        for (int i = 0; i < n; i++) {
            s[i + 1] = s[i] + nums[i];
        }

        for (int i = 0; i <= n - k; i++) {
            s[i] = s[i + k] - s[i];
        }
        int[] result = new int[3];
        int sum = Integer.MIN_VALUE;
        int l = 0;
        int[] m = new int[n + 1];
        m[n - k] = n - k;
        for (int i = n - k - 1; i >= 0; i--) {
            if (s[i] >= s[m[i + 1]]) {
                m[i] = i;
            } else {
                m[i] = m[i + 1];
            }
        }

        for (int i = k; i <= n - k - k; i++) {
            if (s[i - k] > s[l]) {
                l = i - k;
            }
            if (s[l] + s[i] + s[m[i + k]] > sum) {
                sum = s[l] + s[i] + s[m[i + k]];
                result[0] = l;
                result[1] = i;
                result[2] = m[i + k];
            }
        }
        return result;
    }
}

#78.48% 9ms
class Solution {
    public int[] maxSumOfThreeSubarrays(int[] nums, int k) {
        //W is an array of sums of windows
        int[] W = new int[nums.length - k + 1];
        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            if ( i >= k) sum -= nums[i - k];
            if (i >= k - 1) W[i - k + 1] = sum;
        }

        int[] left = new int[W.length];
        int best = 0;
        for (int i = 0; i < W.length; i++) {
            if (W[i] > W[best]) best = i;
            left[i] = best;
        }

        int[] right = new int[W.length];
        best = W.length - 1;
        for (int i = W.length - 1; i >= 0; i--) {
            if (W[i] > W[best]) best = i;
            right[i] = best;
        }

        int[] ans = new int[]{-1, -1, -1};
        for (int j = k; j < W.length - k; j++) {
            int i = left[j - k], p = right[j + k];
            if (ans[0] == -1 || W[i] + W[j] + W[p] > W[ans[0]] + W[ans[1]] + W[ans[2]] ) {
                ans[0] = i;
                ans[1] = j;
                ans[2] = p;
            }
        }
        return ans;
    }
}
'''