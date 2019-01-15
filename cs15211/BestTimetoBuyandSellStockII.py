__source__ = 'https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/best-time-to-buy-and-sell-stock-ii.py
# Greedy
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 122. Best Time to Buy and Sell Stock II
#
# Say you have an array for which the ith element is
# the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit.
# You may complete as many transactions as you like
# (ie, buy one and sell one share of the stock multiple times).
# However, you may not engage in multiple transactions at the same time
# (ie, you must sell the stock before you buy again).
#
# Companies
# Bloomberg
# Related Topics
# Array Greedy
# Similar Questions
# Best Time to Buy and Sell Stock Best Time to Buy and Sell Stock III
# Best Time to Buy and Sell Stock IV Best Time to Buy and Sell Stock with Cooldown

# Thought
# This problem can be viewed as finding all ascending sequences.
# For example, given {5, 1, 2, 3, 4}, buy at 1 & sell at 4 is
# the same as buy at 1 &sell at 2 & buy at 2& sell at 3 & buy at 3 & sell at 4.
#
# We can scan the array once, and find all pairs of elements that are in ascending order.
#
import unittest
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        profit = 0
        for i in xrange(len(prices) - 1):
            profit += max(0, prices[i + 1] - prices[i])
        return profit

class SolutionIf:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        profit = 0
        for i in xrange(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            if diff > 0:
                profit += diff
        return profit

class SolutionIf2:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        profit = 0
        for i in xrange(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
#test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        prices = [3, 2, 1, 4, 2, 5, 6]
        print Solution().maxProfit(prices)
        print SolutionIf().maxProfit(prices)
        print SolutionIf2().maxProfit(prices)

if __name__ == '__main__':
    unittest.main()

Java = '''
Thought: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/solution/

# 99.17% 1ms
class Solution {
    public int maxProfit(int[] prices) {
        int res = 0;
        for (int i = 0; i < prices.length - 1; i++) {
            if ((prices[i+1] - prices[i]) > 0) res += prices[i+1] - prices[i];
        }
        return res;
    }
}

# 99.17% 1ms
class Solution {
    public int maxProfit(int[] prices) {
        int total = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i - 1] < prices[i]) total += prices[i] - prices[i - 1];
        }
        return total;
    }
}

# 99.17% 1ms
public class Solution {
    public int maxProfit(int[] prices) {
        int result = 0;
        for (int i = 0; i < prices.length - 1; i++) {
            result += Math.max(prices[i + 1] - prices[i], 0);
        }
        return result;
    }
}
'''