__source__ = 'https://leetcode.com/problems/coin-change/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/create-maximum-number.py
# Time:  O(n * k), n is the number of coins, k is the amount of money
# Space: O(k)
#
# Description: Leetcode # 322. Coin Change
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
# TLE
import unittest
# Time:  O(k * (m + n + k)) ~ O(k * (m + n + k^2))
# Space: O(m + n + k^2)
# DP + Greedy solution. (280ms)
class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def get_max_digits(nums, start, end, max_digits):
            max_digits[end] = max_digit(nums, end)
            for i in reversed(xrange(start, end)):
                max_digits[i] = delete_digit(max_digits[i + 1])

        def max_digit(nums, k):
            drop = len(nums) - k
            res = []
            for num in nums:
                while drop and res and res[-1] < num:
                    res.pop()
                    drop -= 1
                res.append(num)
            return res[:k]

        def delete_digit(nums):
            res = list(nums)
            for i in xrange(len(res)):
                if i == len(res) - 1 or res[i] < res[i + 1]:
                    res = res[:i] + res[i+1:]
                    break
            return res

        def merge(a, b):
            return [max(a, b).pop(0) for _ in xrange(len(a)+len(b))]

        m, n = len(nums1), len(nums2)

        max_digits1, max_digits2 = [[] for _ in xrange(k + 1)], [[] for _ in xrange(k + 1)]
        get_max_digits(nums1, max(0, k - n), min(k, m), max_digits1)
        get_max_digits(nums2, max(0, k - m), min(k, n), max_digits2)

        return max(merge(max_digits1[i], max_digits2[k-i]) \
                   for i in xrange(max(0, k - n), min(k, m) + 1))

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

# test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        coins = [1, 2, 5]
        amount = 100
        print Solution2().coinChange(coins,amount)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/coin-change/solution/

# 98.46% 5ms
class Solution {
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
# 38ms 26.58%
class Solution {
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
# 19ms 80.04%
class Solution {
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

