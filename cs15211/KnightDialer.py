__source__ = 'https://leetcode.com/problems/knight-dialer/'
# Time:  O(N)
# Space: O(1)
#
# Description: Leetcode # 935. Knight Dialer
#
# A chess knight can move as indicated in the chess diagram below:
#
# This time, we place our chess knight on any numbered key of a phone pad (indicated above),
# and the knight makes N-1 hops.  Each hop must be from one key to another numbered key.
#
# Each time it lands on a key (including the initial placement of the knight),
# it presses the number of that key, pressing N digits total.
#
# How many distinct numbers can you dial in this manner?
#
# Since the answer may be large, output the answer modulo 10^9 + 7.
#
# Example 1:
#
# Input: 1
# Output: 10
# Example 2:
#
# Input: 2
# Output: 20
# Example 3:
#
# Input: 3
# Output: 46
#
# Note:
#
# 1 <= N <= 5000
#
import unittest

# 908ms 59.71%
class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        MOD = 10**9 + 7
        moves = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],
                     [1,7,0],[2,6],[1,3],[2,4]]

        dp = [1] * 10
        for hops in xrange(N-1):
            dp2 = [0] * 10
            for node, count in enumerate(dp):
                for nei in moves[node]:
                    dp2[nei] += count
                    dp2[nei] %= MOD
            dp = dp2
        return sum(dp) % MOD

# Time: O(longN) regarding ower matrix
# https://math.stackexchange.com/questions/1890620/finding-path-lengths-by-the-power-of-adjacency-matrix-of-an-undirected-graph
# https://leetcode.com/problems/knight-dialer/discuss/189252/O(logN)
# 64ms 98.74%
import numpy as np
class Solution2(object):
    def knightDialer(self, N):
        mod = 10**9 + 7
        if N == 1: return 10
        M = np.matrix([[0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                       [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                       [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                       [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                       [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 1, 0, 1, 0, 0, 0, 0, 0]])
        res, N = 1, N - 1
        while N:
            if N % 2: res = res * M % mod
            M = M * M % mod
            N /= 2
        return int(np.sum(res)) % mod

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/knight-dialer/solution/
# Best explanation: https://leetcode.com/problems/knight-dialer/discuss/190787/How-to-solve-this-problem-explained-for-noobs!!!
Approach 1: Dynamic Programming
Complexity Analysis
Time Complexity: O(N)
Space Complexity: O(1)
DP: "the total number of unique paths to (i, j) for certain hops n
is equal to the sum of total number of unique paths to each valid position
from which (i, j) can be reached using n - 1 hops".

# 47ms 59.39%
class Solution {
    public int knightDialer(int N) {
        int MOD = 1_000_000_007;
        int[][] moves = new int[][]{
            {4,6},{6,8},{7,9},{4,8},{3,9,0},
            {},{1,7,0},{2,6},{1,3},{2,4}
        };
        int[][] dp = new int[2][10];
        Arrays.fill(dp[0], 1);
        for (int hops = 0; hops < N -1; ++hops) {
            Arrays.fill(dp[~hops & 1], 0);
            for (int node = 0; node < 10; ++node) {
                for (int nei : moves[node]) {
                    dp[~hops & 1][nei] += dp[hops & 1][node];
                    dp[~hops & 1][nei] %= MOD;
                }
            }
        }
        long ans = 0;
        for (int x : dp[~N & 1]) ans += x;
        return (int) (ans % MOD);
    }
}


# Memorization
# 5ms 99.93%
class Solution {
    private static final int MOD = 1_000_000_007;
    private static final int[][] dp = new int[5001][10];
    private static final int[][] moves = {{4, 6}, {6, 8}, {7, 9}, {4, 8}, {3, 9, 0}, {}, {1, 7, 0},{2, 6}, {1, 3}, {2, 4}};

    public int knightDialer(int N) {
        int res = 0;
        for (int i = 0; i < 10; i++) {
            res = (res + helper(N, i)) % MOD;
        }
        return res;
    }

    private int helper(int N, int digit) {
        if (N == 1) return 1;
        if (digit == 5) return 0;
        if (dp[N][digit] > 0) return dp[N][digit];
        for (int next : moves[digit]) {
            dp[N][digit] = (dp[N][digit] + helper(N -1, next)) % MOD;
        }
        return dp[N][digit];
    }
}
'''