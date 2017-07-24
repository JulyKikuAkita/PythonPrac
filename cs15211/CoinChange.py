__source__ = 'https://leetcode.com/problems/coin-change/description/'
# Time:  O(n * k), n is the number of coins, k is the amount of money
# Space: O(k)
#
# You are given coins of different denominations and
# a total amount of money amount. Write a function to
# compute the fewest number of coins that you need to
# make up that amount. If that amount of money cannot
# be made up by any combination of the coins, return -1.
#
# Example 1:
# coins = [1, 2, 5], amount = 11
# return 3 (11 = 5 + 5 + 1)
#
# Example 2:
# coins = [2], amount = 3
# return -1.
#
# Note:
# You may assume that you have an infinite number of each kind of coin.
# Related Topics
# Dynamic Programming
#TLE
class Solution_TLE(object):
    count = float("inf")
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        cur = []
        coins.sort()
        self.coinChangeRecu(coins,amount,cur)
        return self.count if self.count != float("inf") else -1

    def coinChangeRecu(self, coins, amount, cur):

        if sum(cur) > amount:
            return

        if sum(cur) == amount:
            self.count = min(self.count, len(cur))
            return

        for coin in coins:
            cur.append(coin)
            self.coinChangeRecu(coins, amount, cur)
            cur.pop()


# DP solution. (1680ms)
class Solution2(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        INF = 0x7fffffff
        amounts = [INF] * (amount + 1)
        amounts[0] = 0

        for i in xrange(amount + 1):
            if amounts[i] != INF:
                for coin in coins:
                    if i + coin <= amount:
                        amounts[i+coin] = min(amounts[i+coin], amounts[i] + 1)
        return amounts[amount] if amounts[amount] != INF else -1

class SolutionLTE1(object):
    def __init__(self):
        self.res = []
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins or len(coins) == 0 or amount < 0:
            return -1
        if amount == 0:
            return 0
        tmp = []
        self.dfs(coins, tmp, 0, amount)
        return len(self.res) if len(self.res) > 0 else -1

    def dfs(self, coins, tmp, sum, amount):
        print sum
        if sum > amount:
            return
        if sum == amount:
            if len(tmp) < len(self.res):
                self.res = tmp
                return
            else:
                return

        for coin in coins:
            tmp.append(coin)
            self.dfs(coins, tmp, sum + coin, amount)
            tmp.pop()
# test
coins = [1, 2, 5]
amount = 100
if __name__ == '__main__':
    print SolutionLTE1().coinChange(coins,amount)
    #print Solution_TLE().coinChange(coins,amount)


#Java
# http://www.cnblogs.com/springfor/p/3886576.html
Java = '''
Thought: https://leetcode.com/problems/coin-change/solution/
#Thought: https://leetcode.com/problems/maximum-product-of-three-numbers/tabs/solution

#98.46% 5ms
public class Solution {
    public int coinChange(int[] coins, int amount) {
        if (coins.length == 0 || amount <= 0) {
            return 0;
        }
        Arrays.sort(coins);
        int min = coinChange(coins, amount, coins.length - 1, Integer.MAX_VALUE, 0);
        return min == Integer.MAX_VALUE ? -1 : min;
    }

    private int coinChange(int[] coins, int amount, int index, int minCount, int curCount) {
        if (amount == 0) {
            return Math.min(minCount, curCount);
        } else if (index < 0 || curCount + amount / coins[index] >= minCount) {
            return minCount;
        }
        for (int i = amount / coins[index]; i >= 0; i--) {
            minCount = Math.min(minCount, coinChange(coins, amount - i * coins[index], index - 1, minCount, curCount + i));
        }
        return minCount;
    }
}

Approach #2 (Dynamic programming - Top down) [Accepted]
#18.27% 45ms
public class Solution {
    public int coinChange(int[] coins, int amount) {
        if (amount < 1) return 0;
        return coinChange(coins, amount, new int[amount]);
    }

    private int coinChange(int[] coins, int rem, int[] count) {
        if (rem < 0) return -1;
        if (rem == 0) return 0;
        if (count[rem - 1] != 0) return count[rem - 1];
        int min = Integer.MAX_VALUE;
        for (int coin : coins) {
            int res = coinChange(coins, rem - coin, count);
            if (res >= 0 && res < min)
                min = 1 + res;
        }
        count[rem - 1] = (min == Integer.MAX_VALUE) ? -1 : min;
        return count[rem - 1];
    }
}

Approach #3 (Dynamic programming - Bottom up) [Accepted]
#60.67%  24 ms
public class Solution {
    public int coinChange(int[] coins, int amount) {
        int max = amount + 1;
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, max);
        dp[0] = 0;
        for (int i = 1; i <= amount; i++) {
            for (int j = 0; j < coins.length; j++) {
                if (coins[j] <= i) {
                    dp[i] = Math.min(dp[i], dp[i - coins[j]] + 1);
                }
            }
        }
        return dp[amount] > amount ? -1 : dp[amount];
    }
}

'''

