__source__ = 'https://leetcode.com/problems/guess-number-higher-or-lower-ii/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/guess-number-higher-or-lower-ii.py
# Time:  O(n^2)
# Space: O(n^2)
#
# Description: Leetcode # 375. Guess Number Higher or Lower II
#
# We are playing the Guess Game. The game is as follows:
#
# I pick a number from 1 to n. You have to guess which number I picked.
#
# Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.
#
# However, when you guess a particular number x, and you guess wrong,
# you pay $x. You win the game when you guess the number I picked.
#
# Example:
#
# n = 10, I pick 8.
#
# First round:  You guess 5, I tell you that it's higher. You pay $5.
# Second round: You guess 7, I tell you that it's higher. You pay $7.
# Third round:  You guess 9, I tell you that it's lower. You pay $9.
#
# Game over. 8 is the number I picked.
#
# You end up paying $5 + $7 + $9 = $21.
# Given a particular n >= 1, find out how much money you need to have to guarantee a win.
#
# Hint:
#
# The best strategy to play the game is to minimize the maximum loss
# you could possibly face. Another strategy is to minimize the expected loss.
# Here, we are interested in the first scenario.
# Take a small example (n = 3). What do you end up paying in the worst case?
# Check out this article if you're still stuck.
# The purely recursive implementation of minimax would be worthless
# for even a small n. You MUST use dynamic programming.
# As a follow-up, how would you modify your code to solve the problem of
# minimizing the expected loss, instead of the worst-case loss?
#
# Companies
# Google
# Related Topics
# Dynamic Programming Minimax
# Similar Questions
# Flip Game II Guess Number Higher or Lower Can I Win Find K Closest Elements
#
import unittest
# 468ms 68.49%
class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        pay = [[0] * n for _ in xrange(n+1)]
        for i in reversed(xrange(n)):
            for j in xrange(i+1, n):
                pay[i][j] = min(k+1 + max(pay[i][k-1], pay[k+1][j]) \
                                for k in xrange(i, j+1))
        return pay[0][n-1]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/guess-number-higher-or-lower-ii/solution/

# 7ms 76.45%
class Solution {
    public int getMoneyAmount(int n) {
        int[][] table = new int[n+1][n+1];
        return DP(table, 1, n);
    }

    int DP(int[][] t, int s, int e){
        if(s >= e) return 0;
        if(t[s][e] != 0) return t[s][e];
        int res = Integer.MAX_VALUE;
        for(int x=s; x<=e; x++){
            int tmp = x + Math.max(DP(t, s, x-1), DP(t, x+1, e));
            res = Math.min(res, tmp);
        }
        t[s][e] = res;
        return res;
    }
}

# 5ms 95.53%
class Solution {
    public int getMoneyAmount(int n) {
        int[][] dp = new int[n + 1][n + 1];
        for (int len = 2; len <= n; len++) {
            for (int start = 1; start <= n - len + 1; start++) {
                int minres = Integer.MAX_VALUE;
                for (int piv = start; piv < start + len - 1; piv++) {
                    int res = piv + Math.max(dp[start][piv - 1], dp[piv + 1][start + len - 1]);
                    minres = Math.min(res, minres);
                }
                dp[start][start + len - 1] = minres;
            }
        }
        return dp[1][n];
    }
}

# DFS
# 1ms 99.49%
class Solution {
    int[][] dp;
    public int getMoneyAmount(int n) {
        dp = new int[n + 1][n + 1];
        return helper(1, n);
    }

    private int helper(int start, int end) {
        if (dp[start][end] != 0) {
            return dp[start][end];
        }
        if (start >= end) {
            return 0;
        }
        if (start >= end - 2) {
            return dp[start][end] = end - 1;
        }
        int mid = (start + end) / 2 - 1, min = Integer.MAX_VALUE;
        while (mid < end) {
            int left = helper(start, mid - 1);
            int right = helper(mid + 1, end);
            min = Math.min(min, mid + Math.max(left, right));
            if (right <= left) break;
            mid++;
        }
        return dp[start][end] = min;

    }
}
'''