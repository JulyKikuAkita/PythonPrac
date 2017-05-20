__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/best-time-to-buy-and-sell-stock-iii.py
# Time:  O(n)
# Space: O(1)
# Dynamic Programming
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
#  Array Dynamic Programming
'''
Analysis

Comparing to I and II, III limits the number of transactions to 2. This can be solve by "devide and conquer". We use left[i] to track the maximum profit for transactions before i, and use right[i] to track the maximum profit for transactions after i. You can use the following example to understand the Java solution:

Prices: 1 4 5 7 6 3 2 9
left = [0, 3, 4, 6, 6, 6, 6, 8]
right= [8, 7, 7, 7, 7, 7, 7, 0]
'''
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
test = Solution2()
prices = [3,3,5,0,0,3,1,4]
print test.maxProfit(prices)

if __name__ == '__main__':
    prices = [3,3,5,0,0,3,1,4] #ans = 6
    #print Solution().maxProfit(prices)
    #print Solution_GitHub2().maxProfit(prices)
    print Solution_GitHub3().maxProfit(prices)
#java
js = '''
public class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length < 2) {
            return 0;
        }
        int[] first = new int[prices.length];
        int min = prices[0];
        for (int i = 1; i < prices.length; i++) {
            first[i] = Math.max(first[i - 1], prices[i] - min);
            min = Math.min(min, prices[i]);
        }
        int[] second = new int[prices.length];
        int max = prices[prices.length - 1];
        for (int i = prices.length - 2; i >= 0; i--) {
            second[i] = Math.max(second[i + 1], max - prices[i]);
            max = Math.max(max, prices[i]);
        }
        int result = 0;
        for (int i = 0; i < prices.length; i++) {
            result = Math.max(result, first[i] + second[i]);
        }
        return result;
    }
}


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
'''