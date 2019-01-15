__source__ = 'https://leetcode.com/problems/target-sum/'
# Time:  O(l * n)
# Space: O(n)
#
# Description: Leetcode # 494. Target Sum
#
# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S.
# Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.
#
# Find out how many ways to assign symbols to make sum of integers equal to target S.
#
# Example 1:
#  Input: nums is [1, 1, 1, 1, 1], S is 3.
# Output: 5
# Explanation:
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
#
# There are 5 ways to assign symbols to make the sum of nums be target 3.
# Note:
# The length of the given array is positive and will not exceed 20.
# The sum of elements in the given array will not exceed 1000.
# Your output answer is guaranteed to be fitted in a 32-bit integer.
#  Hide Company Tags Google Facebook
# Hide Tags Depth-first Search Dynamic Programming
# Hide Similar Problems (H) Expression Add Operators
#
import unittest
# 376ms 33.28%
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return 0
        dic = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}
        for i in range(1, len(nums)):
            tdic = {}
            for d in dic:
                tdic[d + nums[i]] = tdic.get(d + nums[i], 0) + dic.get(d, 0)
                tdic[d - nums[i]] = tdic.get(d - nums[i], 0) + dic.get(d, 0)
            dic = tdic
        return dic.get(S, 0)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/target-sum/solution/

This is a pretty easy problem. Just do DFS and try both "+" and "-" at every position.
Easy version of Expression Add Operators https://leetcode.com/problems/expression-add-operators/

# 556ms 23.33%
class Solution {
    int result = 0;

    public int findTargetSumWays(int[] nums, int S) {
        if (nums == null || nums.length == 0) return result;
        helper(nums, S, 0, 0);
        return result;
    }

    public void helper(int[] nums, int target, int pos, long eval){
        if (pos == nums.length) {
            if (target == eval) result++;
            return;
        }
        helper(nums, target, pos + 1, eval + nums[pos]);
        helper(nums, target, pos + 1, eval - nums[pos]);
    }
}

# https://discuss.leetcode.com/topic/76243/java-15-ms-c-3-ms-o-ns-iterative-dp-solution-using-subset-sum-with-explanation
Java (15 ms) C++ (3 ms) O(ns) iterative DP solution using subset sum with explanation
The recursive solution is very slow, because its runtime is exponential

The original problem statement is equivalent to:
Find a subset of nums that need to be positive, and the rest of them negative, such that the sum is equal to target

Let P be the positive subset and N be the negative subset
For example:
Given nums = [1, 2, 3, 4, 5] and target = 3 then one possible solution is +1-2+3-4+5 = 3
Here positive subset is P = [1, 3, 5] and negative subset is N = [2, 4]

Then let's see how this can be converted to a subset sum problem:

                  sum(P) - sum(N) = target
sum(P) + sum(N) + sum(P) - sum(N) = target + sum(P) + sum(N)
                       2 * sum(P) = target + sum(nums)
So the original problem has been converted to a subset sum problem as follows:
Find a subset P of nums such that sum(P) = (target + sum(nums)) / 2

Note that the above formula has proved that target + sum(nums) must be even
We can use that fact to quickly identify inputs that do not have a solution (Thanks to @BrunoDeNadaiSarnaglia for the suggestion)
For detailed explanation on how to solve subset sum problem, you may refer to Partition Equal Subset Sum

Here is Java solution (15 ms)

# 6ms 99.45%
class Solution {
    public int findTargetSumWays(int[] nums, int S) {
        int sum = 0;
        for (int n : nums) {
            sum += n;
        }
        return sum < S || (S + sum) % 2 > 0 ? 0 : subsetSum(nums, (S + sum) >>>1);
    }

    public int subsetSum(int[] nums, int s) {
        int[] dp = new int[s +1];
        dp[0] = 1;
        for (int n : nums) {
            for(int i = s; i >= n; i--) {
                dp[i] += dp[i - n];
            }
        }
        return dp[s];
    }
}
'''