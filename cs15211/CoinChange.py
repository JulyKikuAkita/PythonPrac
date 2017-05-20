__author__ = 'July'
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

