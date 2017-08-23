__source__ = 'https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/best-time-to-buy-and-sell-stock-iii.py
# Time:  O(n)
# Space: O(1)
# Dynamic Programming
#
# Description: Leetcode # 123. Best Time to Buy and Sell Stock III
#
# Say you have an array for which the ith element
# is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit.
# You may complete at most two transactions.
#
# Note:
# You may not engage in multiple transactions at the same time
# (ie, you must sell the stock before you buy again).
#
# Related Topics
# Array Dynamic Programming
# Similar Questions
# Best Time to Buy and Sell Stock Best Time to Buy and Sell Stock II Best Time to Buy and Sell Stock IV
#
# Thought:
# Comparing to I and II, III limits the number of transactions to 2.
# This can be solve by "devide and conquer".
# We use left[i] to track the maximum profit for transactions before i,
# and use right[i] to track the maximum profit for transactions after i.
# You can use the following example to understand the Java solution:
#
# Prices: 1 4 5 7 6 3 2 9
# left = [0, 3, 4, 6, 6, 6, 6, 8]
# right= [8, 7, 7, 7, 7, 7, 7, 0]
#
import unittest
# Time:  O(n)
# Space: O(1)
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        hold1, hold2 = float("-inf"), float("-inf")
        release1, release2 = 0, 0
        for i in prices:
            release2 = max(release2, hold2 + i)
            hold2 = max(hold2, release1 - i)
            release1 = max(release1, hold1 + i)
            hold1 = max(hold1, -i)
            print i, release2, hold2, release1, hold1
        return release2

# Time:  O(k * n)
# Space: O(k)
class Solution_GitHub2:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        return self.maxAtMostKPairsProfit(prices, 2)

    def maxAtMostKPairsProfit(self,prices,k):
        max_buy = [float("-inf") for _ in xrange(k + 1)]
        max_sell = [0 for _ in xrange(k + 1)]

        for i in xrange(len(prices)):
            for j in xrange(1, min(k, i/2+1) + 1):
                max_buy[j] = max(max_buy[j], max_sell[j-1] - prices[i])
                max_sell[j] = max(max_sell[j], max_buy[j] + prices[i])
                print i, j, max_buy, max_sell
        return max_sell[k]

# Time:  O(n)
# Space: O(n)
class Solution_GitHub3:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        min_price, max_profit_from_left, max_profits_from_left = float("inf"), 0, []
        for price in prices:
            min_price = min(min_price, price)
            max_profit_from_left = max(max_profit_from_left, price - min_price)
            max_profits_from_left.append(max_profit_from_left)

        max_price, max_profit_from_right, max_profits_from_right = 0, 0, []
        for i in reversed(range(len(prices))):
            max_price = max(max_price, prices[i])
            max_profit_from_right = max(max_profit_from_right, max_price - prices[i])
            max_profits_from_right.insert(0, max_profit_from_right)

        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit, max_profits_from_left[i] + max_profits_from_right[i])
        return max_profit

# explanation in JAVA  http://www.programcreek.com/2014/02/leetcode-best-time-to-buy-and-sell-stock-iii-java/
class Solution2:
    # @param prices, a list of integer
    # @return an integer
    # http://chaoren.is-programmer.com/posts/43727.html
    def maxProfit(self, prices):
        length = len(prices)
        if length == 0:
            return 0

        maxProfitForward = []
        minPrice = prices[0]
        maxProfit = -1
        for currPrice in prices:
            minPrice = min(minPrice, currPrice)
            maxProfit = max(maxProfit, currPrice - minPrice)
            maxProfitForward.append(maxProfit)

        maxProfitBackward = []
        maxPrice = prices[-1]
        maxProfit = -1
        for currPrice in reversed(prices):
            maxPrice = max(maxPrice, currPrice)
            maxProfit = max(maxProfit, maxPrice - currPrice)
            maxProfitBackward.insert(0, maxProfit)

        # for 0 or 1 transaction
        maxProfit = maxProfitForward[-1]

        # >= 2 transactions
        for i in xrange(length -1):
            maxProfit = max(maxProfit, maxProfitForward[i] + maxProfitBackward[i+1])
        return maxProfit

#test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        test = Solution2()
        prices = [3,3,5,0,0,3,1,4]
        print test.maxProfit(prices)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/contains-duplicate/solution/
Thought:

#19.81% 6ms
public class Solution {
    public int maxProfit(int[] prices) {
        if ( prices == null || prices.length == 0) return 0;

        int[] left = new int[prices.length];
        left[0] = 0;
        int min = prices[0];

        for(int i = 1; i < left.length ; i++) {
            left[i] = Math.max(left[i-1], prices[i] - min);
            min = Math.min(min, prices[i]);
        }

        int[] right = new int[prices.length];
        right[prices.length-1] = 0;
        int max = prices[prices.length-1];

        for(int i = prices.length - 2; i >= 0; i--){
            right[i] = Math.max(right[i], max - prices[i]);
            max = Math.max(max, prices[i]);
        }

        int res = 0;
        for (int i = 0; i < prices.length; i++) {
            res = Math.max(res, left[i] + right[i]);
        }
        return res;
    }
}

# 52.68% 4ms
public class Solution {
    public int maxProfit(int[] prices) {
        int hold1 = Integer.MIN_VALUE, hold2 = Integer.MIN_VALUE;
        int release1 = 0, release2 = 0;
        for(int i:prices){                              // Assume we only have 0 money at first
            release2 = Math.max(release2, hold2+i);     // The maximum if we've just sold 2nd stock so far.
            hold2    = Math.max(hold2,    release1-i);  // The maximum if we've just buy  2nd stock so far.
            release1 = Math.max(release1, hold1+i);     // The maximum if we've just sold 1nd stock so far.
            hold1    = Math.max(hold1,    -i);          // The maximum if we've just buy  1st stock so far.
        }
        return release2; ///Since release1 is initiated as 0, so release2 will always higher than release1.
    }
}

# 77.21% 2ms
class Solution {
    public int maxProfit(int[] prices) {
        int buy1 = Integer.MIN_VALUE, sell1 = 0, buy2 = Integer.MIN_VALUE, sell2 = 0;
        for(int price : prices) {
            if(-price > buy1) {
                buy1 = -price;
            }
            if(buy1 + price > sell1) {
                sell1 = buy1 + price;
            }
            if(sell1 - price > buy2) {
                buy2 = sell1 - price;
            }
            if(buy2 + price > sell2) {
                sell2 = buy2 + price;
            }
        }

        return sell2;
    }
}

# 98.96% 1ms
public class Solution {
    public int maxProfit(int[] prices) {
        if(prices == null || prices.length <= 1){
            return 0;
        }
        int firstBuy = Integer.MIN_VALUE, secondBuy = Integer.MIN_VALUE;
        int firstSell = 0, secondSell = 0;
        for(int curPrice : prices){
            if(firstBuy < -curPrice){
                firstBuy = -curPrice;
            }
            if(firstSell < firstBuy + curPrice){
                firstSell = firstBuy + curPrice;
            }
            if(secondBuy < firstSell - curPrice){
                secondBuy = firstSell - curPrice;
            }
            if(secondSell < secondBuy + curPrice){
                secondSell = secondBuy + curPrice;
            }
        }

        return secondSell;
    }
}
'''