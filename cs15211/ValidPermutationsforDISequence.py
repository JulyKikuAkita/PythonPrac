__source__ = 'https://leetcode.com/problems/valid-permutations-for-di-sequence/'
# Time:  O(N^2)
# Space: O(N^2)
#
# Description: Leetcode # 903. Valid Permutations for DI Sequence
#
# We are given S, a length n string of characters from the set {'D', 'I'}.
# (These letters stand for "decreasing" and "increasing".)
#
# A valid permutation is a permutation P[0], P[1], ..., P[n] of integers {0, 1, ..., n}, such that for all i:
#
# If S[i] == 'D', then P[i] > P[i+1], and;
# If S[i] == 'I', then P[i] < P[i+1].
# How many valid permutations are there?  Since the answer may be large, return your answer modulo 10^9 + 7.
#
# Example 1:
#
# Input: "DID"
# Output: 5
# Explanation:
# The 5 valid permutations of (0, 1, 2, 3) are:
# (1, 0, 3, 2)
# (2, 0, 3, 1)
# (2, 1, 3, 0)
# (3, 0, 2, 1)
# (3, 1, 2, 0)
#
# Note:
#
# 1 <= S.length <= 200
# S consists only of characters from the set {'D', 'I'}.
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
# Thought: https://leetcode.com/problems/valid-permutations-for-di-sequence/solution/
Approach 1: Dynamic Programming
Complexity Analysis
Time Complexity: O(N^3), where N is the length of S, or O(N^2) with the optimized version.
Space Complexity: O(N^2)

# 48ms 38.85%
class Solution {
    public int numPermsDISequence(String S) {
        int MOD = 1_000_000_007;
        int N = S.length();

        // dp[i][j] : Num ways to place P_i with relative rank j
        int[][] dp = new int[N+1][N+1];
        Arrays.fill(dp[0], 1);

        for (int i = 1; i <= N; i++) {
            for (int j = 0; j <= i; j++) {
                if (S.charAt(i - 1) == 'D') {
                    for (int k = j; k < i; k++) {
                        dp[i][j] += dp[i - 1][k];
                        dp[i][j] %= MOD;
                    }
                } else {
                    for (int k = 0; k < j; k++) {
                        dp[i][j] += dp [i - 1][k];
                        dp[i][j] %= MOD;
                    }
                }
            }
        }
        int ans = 0;
        for (int x : dp[N]) {
            ans += x;
            ans %= MOD;
        }
        return ans;
    }
}


Approach 2: Divide and Conquer
Complexity Analysis
Time Complexity: O(N^2), where N is the length of S.
Space Complexity: O(N^2)

# Improved DP
we could use (for S[i-1] == 'I') the fact that dp(i, j) = dp(i, j-1) + dp(i-1, j-1).
For S[i-1] == 'D', we have the similar fact that dp(i, j) = dp(i, j+1) + dp(i-1, j).

# 9ms 68.15%
class Solution {
    public int numPermsDISequence(String S) {
        int n = S.length(), mod = (int) 1e9 + 7;
        int[][] dp = new int[n + 1][n  +1];
        for (int j = 0; j <= n; j++) dp[0][j] = 1;
        for (int i = 0; i < n; i++) {
            if (S.charAt(i) == 'I') {
                for (int j = 0, cur = 0; j < n - i; j++) {
                    dp[i + 1][j] = cur = (cur + dp[i][j]) % mod;
                }
            } else {
                for (int j = n - i - 1, cur = 0; j >= 0; j--) {
                    dp[i + 1][j] = cur = (cur + dp[i][j + 1]) % mod;
                }
            }
        }
        return dp[n][0];
    }
}


'''