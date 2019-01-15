__source__ = 'https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/'
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
# Thought: https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/solution/

The basic idea is that construct leftmax array and rightmax array to save the leftkmax subarray index
and rightkmax subarray index. After that, we use these prepossessed array to solve this question using O(N)
since we have saved all of max subarray index!

# 8ms 35.66%
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
# Given :[1,2,1,2,6,7,5,1], K = 2
# W[]:   3, 3, 3, 8, 13, 12, 6, 
# Left:  0, 0, 0, 3, 4,  4,  4, 
# Right: 4, 4, 4, 4, 4,  5,  6, 

# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/discuss/108239/Java-DP-Generic-Solution-for-M-subarrays
# DP for any subarray
# 16ms
class Solution {
    public int[] maxSumOfThreeSubarrays(int[] nums, int k) {
        int n = nums.length;
        int m = 3;
        int[] sums = new int[n+1];
        int[][] max = new int[n+1][m+1];
        int[][] indices = new int[n+1][m+1];
        for (int i = 1; i <= n; i++) {
            sums[i] = sums[i - 1] + nums[i - 1];
        }
        
        // The outer loop is for the number of partitions - (for this problem it is 3)
        // The inner loop tries to find the max sum and the starting index for each partition - 
        // starting from the end of the previous partition.
        // So the first partition ends at k-1, so 2nd partition starts at k and 2nd partition ends at 2*(k-1), 
        // 3rd partition starts at 3k and ends at 3(k-1) and so on.
        for (int i = 1; i <= m ; i++) {
            for (int j = i * k; j <= n; j++) {
                if (max[j - k][i - 1] + sums[j] - sums[j - k] > max[j - 1][i]) {
                    indices[j][i] = j - k;
                    max[j][i] = max[j - k][i - 1] + sums[j] - sums[j - k];
                } else {
                    indices[j][i] = indices[j - 1][i];
                    max[j][i] = max[j - 1][i];
                }
            }
        }
        int[] res = new int[m];
        res[m - 1] = indices[n][m];
        for (int i = m - 2; i >= 0; i--) {
            res[i] = indices[res[i + 1]][i + 1];
        }
        return res;
    }
}
'''
