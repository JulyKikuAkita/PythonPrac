__source__ = 'https://leetcode.com/problems/profitable-schemes/'
# Time:  O(N * P * G)
# Space: O(P * G)
#
# Description: Leetcode # 879. Profitable Schemes
#
# There are G people in a gang, and a list of various crimes they could commit.
#
# The i-th crime generates a profit[i] and requires group[i] gang members to participate.
#
# If a gang member participates in one crime, that member can't participate in another crime.
#
# Let's call a profitable scheme any subset of these crimes that generates at least P profit,
# and the total number of gang members participating in that subset of crimes is at most G.
#
# How many schemes can be chosen?  Since the answer may be very large, return it modulo 10^9 + 7.
#
# Example 1:
#
# Input: G = 5, P = 3, group = [2,2], profit = [2,3]
# Output: 2
# Explanation:
# To make a profit of at least 3, the gang could either commit crimes 0 and 1, or just crime 1.
# In total, there are 2 schemes.
# Example 2:
#
# Input: G = 10, P = 5, group = [2,3,5], profit = [6,7,8]
# Output: 7
# Explanation:
# To make a profit of at least 5, the gang could commit any crimes, as long as they commit one.
# There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and (0,1,2).
#
#
# Note:
#
# 1 <= G <= 100
# 0 <= P <= 100
# 1 <= group[i] <= 100
# 0 <= profit[i] <= 100
# 1 <= group.length = profit.length <= 100
#
import unittest
# 1140ms 45.71%
class Solution(object):
    def profitableSchemes(self, G, P, group, profit):
        """
        :type G: int
        :type P: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        cur = [[0] * (G + 1) for _ in xrange(P + 1)]
        cur[0][0] = 1

        for p0, g0 in zip(profit, group):
            # p0, g0 : the current crime profit and group size
            cur2 = [row[:] for row in cur]
            for p1 in xrange(P + 1):
                # p1 : the current profit
                # p2 : the new profit after committing this crime
                p2 = min(p1 + p0, P)
                for g1 in xrange(G - g0 + 1):
                    # g1 : the current group size
                    # g2 : the new group size after committing this crime
                    g2 = g1 + g0
                    cur2[p2][g2] += cur[p1][g1]
                    cur2[p2][g2] %= MOD
            cur = cur2

        # Sum all schemes with profit P and group size 0 <= g <= G.
        return sum(cur[-1]) % MOD

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/profitable-schemes/solution/
Failed at below test case:
100
100
[2,5,36,2,5,5,14,1,12,1,14,15,1,1,27,13,6,59,6,1,7,1,2,7,6,1,6,1,3,1,2,11,3,39,21,20,1,27,26,22,11,17,3,2,4,5,6,18,4,14,1,1,1,3,12,9,7,3,16,5,1,19,4,8,6,3,2,7,3,5,12,6,15,2,11,12,12,21,5,1,13,2,29,38,10,17,1,14,1,62,7,1,14,6,4,16,6,4,32,48]
[21,4,9,12,5,8,8,5,14,18,43,24,3,0,20,9,0,24,4,0,0,7,3,13,6,5,19,6,3,14,9,5,5,6,4,7,20,2,13,0,1,19,4,0,11,9,6,15,15,7,1,25,17,4,4,3,43,46,82,15,12,4,1,8,24,3,15,3,6,3,0,8,10,8,10,1,21,13,10,28,11,27,17,1,13,10,11,4,36,26,4,2,2,2,10,0,11,5,22,6]

# https://leetcode.com/problems/profitable-schemes/discuss/157099/Java-original-3d-to-2d-DP-solution
Approach 1: Dynamic Programming
Complexity Analysis
Time Complexity: O(N * P * G), where N is the number of crimes available to the gang.
Space Complexity: O(P * G)

dp[k][i][j] means for first k crime with i members and at least j profit,
what is total schemes can be chosen.
And we need this Math.max(0, j - p), because this is for at least j profit.
dp[k][i][j] = dp[k - 1][i][j] + dp[k - 1][i - current group][Math.max(0, j - current profit)]

# 3D DP:
# 41ms 38.53%
class Solution {
    private int mod = (int)1e9 + 7;
    public int profitableSchemes(int G, int P, int[] group, int[] profit) {
        int[][][] dp = new int[group.length + 1][G + 1][P + 1];
        dp[0][0][0] = 1;
        for (int k = 1; k <= group.length; k++) {
            int g = group[k - 1];
            int p = profit[k - 1];
            for (int i = 0; i <= G; i++) {
                for (int j = 0; j <= P; j++) {
                    dp[k][i][j] = dp[k - 1][i][j];
                    if (i >= g) {
                        dp[k][i][j] = (dp[k][i][j] + dp[k - 1][i - g][Math.max(0, j - p)])%mod;
                    }
                }
            }
        }
        int sum = 0;
        for(int i = 0; i <= G; i++){
            sum = (sum + dp[group.length][i][P]) % mod;
        }
        return sum;
    }
}

# 2D DP
# 24ms 71.78%
class Solution {
    private int mod = (int)1e9 + 7;
    public int profitableSchemes(int G, int P, int[] group, int[] profit) {
        int[][] dp = new int[G + 1][P + 1];
        dp[0][0] = 1;
        for (int k = 1; k <= group.length; k++) {
            int g = group[k - 1];
            int p = profit[k - 1];
            for (int i = G; i >= g; i--) {
                for (int j = P; j >= 0; j--) {
                    dp[i][j] = (dp[i][j] + dp[i - g][Math.max(0, j - p)]) % mod;
                }
            }
        }
        int sum = 0;
        for(int i = 0; i <= G; i++){
            sum = (sum + dp[i][P])% mod;
        }
        return sum;
    }
}

# Backtracking & Memorization
# 276ms, 1.47%
class Solution {
    static final int MOD = (int)1e9 + 7;
    public int profitableSchemes(int G, int P, int[] group, int[] profit) {
        int len = group.length;
        Integer[][][] memo = new Integer[len][G + 1][P + 1];
        return dfs(0, G, P, group, profit, memo);
    }

    private int dfs(int idx, int G, int P, int[] group, int[] profit, Integer[][][] memo) {
        if (idx == group.length) return 0;
        int actP = Math.max(P, 0);
        if (memo[idx][G][actP] != null) return memo[idx][G][actP];
        int res = 0;
        if (G >= group[idx]) {
          if (P - profit[idx] <= 0) res++;
          res += dfs(idx + 1, G - group[idx], P - profit[idx], group, profit, memo);
          res %= MOD;
        }
        res += dfs(idx + 1, G, P, group, profit, memo);
        res %= MOD;
        memo[idx][G][actP] = res;
        return res;
    }
}
'''