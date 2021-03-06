__source__ = 'https://leetcode.com/problems/coin-change-2/description/'
# Time:  O()
# Space: O()
#
# DP
# If amount >= coin then combinations[amount] += combinations[amount - coin]
#
# Description: Leetcode # 518. Coin Change 2
#
# You are given coins of different denominations and a total amount of money.
# Write a function to compute the number of combinations that make up that amount.
# You may assume that you have infinite number of each kind of coin.
#
# Note: You can assume that
#
# 0 <= amount <= 5000
# 1 <= coin <= 5000
# the number of coins is less than 500
# the answer is guaranteed to fit into signed 32-bit integer
#
#
# Example 1:
#
# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
#
#
# Example 2:
#
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
#
#
# Example 3:
#
# Input: amount = 10, coins = [10]
# Output: 1
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
# Thought:
# DP video: https://www.youtube.com/watch?v=jaNZ83Q3QGc
#
# dp[i][j] : the number of combinations to make up amount j by using the first i types of coins
# State transition:
#
# not using the ith coin, only using the first i-1 coins to make up amount j, then we have dp[i-1][j] ways.
# using the ith coin, since we can use unlimited same coin,
# we need to know how many ways to make up amount j - coins[i-1] by using first i coins(including ith),
# which is dp[i][j-coins[i-1]]
# Initialization: dp[i][0] = 1
#
# 7ms 46.02%
class Solution {
    public int change(int amount, int[] coins) {
        int[][] dp = new int[coins.length + 1][amount + 1];
        dp[0][0] = 1;
        for (int i = 1; i <= coins.length; i++) {
            dp[i][0] = 1;
            for (int j = 1; j <= amount; j++) {
                dp[i][j] = dp[i-1][j] + (j >= coins[i - 1] ? dp[i][j - coins[i - 1]] : 0);
            }
        }
        // Print out dp for amount = 5, coins = [1,2,5]
        // 1|0|0|0|0|0|
        // 1|1|1|1|1|1|
        // 1|1|2|2|3|3|
        // 1|1|2|2|3|4|
        //
        // for (int i = 0; i < dp.length; i++) {
        //     for (int j = 0; j < dp[0].length; j++) {
        //         System.out.print(dp[i][j] + "|");
        //     }
        //     System.out.println("");
        // }
        return dp[coins.length][amount];
    }
}

#one pass dp
# Now we can see that dp[i][j] only rely on dp[i-1][j] and dp[i][j-coins[i]],
# then we can optimize the space by only using one-dimension array.
# 2ms, 100%
class Solution {
    public int change(int amount, int[] coins) {
        int[] dp = new int[amount + 1];
        dp[0] = 1;
        for (int coin : coins) {
            for (int i = coin; i <= amount; i++) {
                dp[i] += dp[i - coin];
            }
        }
        return dp[amount];
    }
}

# DP
# 4ms 84.21%
class Solution {
    public int change(int amount, int[] coins) {
        int[] dp = new int[amount + 1];
        dp[0] = 1;
        for (int i = 0; i < coins.length; i++) {
            for (int j = 0; j < amount && j + coins[i] <= amount; j++) {
                dp[j + coins[i]] += dp[j];
            }
        }
        return dp[amount];
    }
}

# Backtracking
# Note: 
# Beware of duplication count when
# When amount is 2 and the coin value is 5, it would be counted as 1 way.
# When amount is 5 and the coin value is 2, the number of ways become 2.
# The set is either case remains 1 coin of 2 and 1 coin of 5. But the first method adds it twice.
# So we create use an outer loop of coins so that a combination once used cannot be used again.
# 102ms 18.42%
class Solution {
    public int change(int amount, int[] coins) {
        if (amount == 0) return 1;
        int[][] memo = new int[amount + 1][coins.length];
        for (int[] m : memo) {
            Arrays.fill(m, -1);
        }
        return helper(amount, coins, memo, 0);
    }
    
    private int helper(int amount, int[] coins, int[][] memo, int idx) {
        if (amount < 0 || idx == coins.length) return 0;
        if (amount == 0 ) return 1;
        if (memo[amount][idx] != -1) return memo[amount][idx];
        int count = 0;
        for (int i = idx; i < coins.length; i++) {
         count += helper(amount - coins[i], coins, memo, i); 
        }
        // same without iteration
        //count = helper(amount - coins[idx], coins, memo, idx) + helper(amount, coins, memo, idx + 1);        
        memo[amount][idx] = count;
        return memo[amount][idx];
    }
}
'''
