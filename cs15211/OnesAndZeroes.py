__source__ = 'https://leetcode.com/problems/ones-and-zeroes/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/ones-and-zeroes.py
# Time:  O(s * m * n), s is the size of the array.
# Space: O(m * n)
#
# Description: 474. Ones and Zeroes
#
# In the computer world, use restricted resource you have to
# generate maximum benefit is what we always want to pursue.
#
# For now, suppose you are a dominator of m 0s and n 1s respectively.
# On the other hand, there is an array with strings consisting of only 0s and 1s.
#
# Now your task is to find the maximum number of strings that you can form
# with given m 0s and n 1s. Each 0 and 1 can be used at most once.
#
# Note:
# The given numbers of 0s and 1s will both not exceed 100
# The size of given string array won't exceed 600.
# Example 1:
# Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
# Output: 4
#
# Explanation: This are totally 4 strings can be formed
# by the using of 5 0s and 3 1s, which are "10,"0001","1", "0"
# Example 2:
# Input: Array = {"10", "0", "1"}, m = 1, n = 1
# Output: 2
#
# Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".
#
# Google
# Hide Tags Dynamic Programming
# Hide Similar Problems (H) Non-negative Integers without Consecutive Ones
#
import unittest
# This question is very similar to a 0-1 knapsack, the transition function is
#
# dp(k, x, y) = max(dp(k-1, x-z, y-o) + 1, dp(k-1, x, y))   (z is zeroes in strs[k], o is ones in strs[k])
# dp(k, x, y) is the maximum strs we can include when we have x zeros,
# y ones and only the first k strs are considered.
#
# dp(len(strs), M, N) is the answer we are looking for
#
# I first implemented a dfs + memoization, which gets MLE, so I created a bottom up style dp.
# With bottom up, we can use something called "rolling array" to optimize space complexity from O(KMN) to O(MN)
#
# 3592ms 27.34%
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in xrange(n+1)] for _ in xrange(m+1)]
        for s in strs:
            zero_count, one_count = 0, 0
            for c in s:
                if c == '0':
                    zero_count += 1
                elif c == '1':
                    one_count += 1

            for i in reversed(xrange(zero_count, m+1)):
                for j in reversed(xrange(one_count, n+1)):
                    dp[i][j] = max(dp[i][j], dp[i-zero_count][j-one_count]+1)
        return dp[m][n]

    def findMaxForm2(self, strs, m, n):
        dp = [[0] * (n+1) for _ in range(m+1)]

        def count(s):
            return sum(1 for c in s if c == '0'), sum(1 for c in s if c == '1')

        for z, o in [count(s) for s in strs]:
            for x in range(m, -1, -1):
                for y in range(n, -1, -1):
                    if x >= z and y >= o:
                        dp[x][y] = max(1 + dp[x-z][y-o], dp[x][y])

        return dp[m][n]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/ones-and-zeroes/solution/

This problem is a typical 0-1 knapsack problem,
we need to pick several strings in provided strings
to get the maximum number of strings using limited number 0 and 1.
We can create a three dimensional array, in which dp[i][j][k] means the maximum number of strings
we can get from the first i argument strs using limited j number of '0's and k number of '1's.

For dp[i][j][k], we can get it by fetching the current string i or discarding the current string,
which would result in dp[i][j][k] = dp[i-1][j-numOfZero(strs[i])][i-numOfOnes(strs[i])] and dp[i][j][k]
= dp[i-1][j][k]; We only need to treat the larger one in it as the largest number for dp[i][j][k].

# 54ms 42.98%
class Solution {
    public int findMaxForm(String[] strs, int m, int n) {
        int[][] dp = new int[m+1][n+1];
        for (String s : strs) {
            int[] count = count(s);
            for (int i=m;i>=count[0];i--)
                for (int j=n;j>=count[1];j--)
                    dp[i][j] = Math.max(1 + dp[i-count[0]][j-count[1]], dp[i][j]);
        }
        return dp[m][n];
    }

    public int[] count(String str) {
        int[] res = new int[2];
        for (int i=0;i<str.length();i++)
            res[str.charAt(i) - '0']++;
        return res;
    }
}
'''