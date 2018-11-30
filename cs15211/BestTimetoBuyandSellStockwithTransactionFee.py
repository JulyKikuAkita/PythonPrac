__source__ = 'https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/'
# Time:  O(N)
# Space: O(1)
#
# DP:
# cash = max(cash, hold + prices[i] - fee)
# hold = max(hold, cash - prices[i])
#
# Description: Leetcode # 714. Best Time to Buy and Sell Stock with Transaction Fee
#
# Your are given an array of integers prices,
# for which the i-th element is the price of a given stock on day i;
# and a non-negative integer fee representing a transaction fee.
#
# You may complete as many transactions as you like,
# but you need to pay the transaction fee for each transaction.
# You may not buy more than 1 share of a stock at a time
# (ie. you must sell the stock share before you buy again.)
#
# Return the maximum profit you can make.
#
# Example 1:
# Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# Buying at prices[0] = 1
# Selling at prices[3] = 8
# Buying at prices[4] = 4
# Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
# Note:
#
# 0 < prices.length <= 50000.
# 0 < prices[i] < 50000.
# 0 <= fee < 50000.
#
import unittest

# DP
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        cash, hold = 0, -prices[0]
        for i in xrange(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash

# greedy?
class Solution2(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        buy = prices[0]
        res = 0
        for p in prices:
            if buy > p:
                buy = p
            else:
                tmp = p - buy - fee
                if tmp > 0:
                    res += tmp
                    buy = p - fee
        return res


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/solution/

# 6ms 100%
class Solution {
    public int maxProfit(int[] prices, int fee) {
        int sold = 0, bought = -prices[0];
        for (int i = 1; i < prices.length; i++) {
            int n = bought + prices[i] - fee;
            if (sold < n) {
                sold = n;
            } else if (bought < sold - prices[i]) {
                bought = sold - prices[i];
            }
        }
        return sold;
    }
}

class Solution {
    public int maxProfit(int[] prices, int fee) {
        int cash = 0, hold = -prices[0];
        for (int i = 1; i < prices.length; i++) {
            cash = Math.max(cash, hold + prices[i] -fee);
            hold = Math.max(hold, cash - prices[i]);
        }
        return cash;
    }
}
'''