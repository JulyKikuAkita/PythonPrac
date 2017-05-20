__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/best-time-to-buy-and-sell-stock-with-cooldown.py
# Time:  O(n)
# Space: O(1)

# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as
# many transactions as you like (ie, buy one and sell one share of the
# stock multiple times) with the following restrictions:
#
# You may not engage in multiple transactions at the same time
# (ie, you must sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day.
# (ie, cooldown 1 day)
# Example:
#
# prices = [1, 2, 3, 0, 2]
# maxProfit = 3
# transactions = [buy, sell, cooldown, buy, sell]
#
#  Google
# Hide Tags Dynamic Programming
# DP
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices:
            return 0

        buy, sell, coolDown = [0] * 2, [0] * 2, [0] * 2
        buy[0] = - prices[0]
        for i in xrange(1, len(prices)):
            # Bought before or buy today.
            buy [i % 2] = max(buy[(i - 1) % 2] , coolDown[(i - 1) % 2] - prices[i])
            # Sell today
            sell[i % 2] = buy[(i - 1) % 2] + prices[i]
            # Sold before yesterday or sold yesterday.
            coolDown[i % 2] = max(coolDown[(i - 1) % 2], sell[(i - 1) % 2])
        return max(coolDown[(len(prices) - 1) % 2], sell[(len(prices) - 1) % 2])

# DP
class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices:
            return 0

        buy, sell, coolDown = [0] * len(prices), [0] * len(prices), [0] * len(prices)
        buy[0] = - prices[0]
        for i in xrange(1, len(prices)):
            # Bought before or buy today.
            buy [i] = max(buy[i - 1] , coolDown[i - 1] - prices[i])
            # Sell today
            sell[i] = buy[(i - 1)] + prices[i]
            # Sold before yesterday or sold yesterday.
            coolDown[i] = max(coolDown[(i - 1)], sell[(i - 1)])
        return max(coolDown[(len(prices) - 1)], sell[(len(prices) - 1)])

if __name__ == "__main__":
    prices = [1, 2, 3, 0, 2]
    print Solution().maxProfit(prices)
    print Solution2().maxProfit(prices)
#java
js = '''
public class Solution {
    public int maxProfit(int[] prices) {
        if ( prices == null || prices.length <= 1) return 0;
        int[] yes = new int[prices.length];
        int[] no = new int[prices.length];

        yes[0] = -prices[0];
        no[0] = 0;

        for (int i = 1; i < prices.length ; i++) {
            no[i] = Math.max(no[i-1], yes[i-1] + prices[i]);
            yes[i] = i >= 2 ? no[i-2] - prices[i] : -prices[i];
            yes[i] = Math.max(yes[i-1], yes[i]);
        }
        return no[prices.length - 1];
    }
}
'''