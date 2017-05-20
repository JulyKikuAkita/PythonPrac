__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/best-time-to-buy-and-sell-stock.py
# Time:  O(n)
# Space: O(1)
#
# Say you have an array for which the ith element
# is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction
# (ie, buy one and sell one share of the stock),
# design an algorithm to find the maximum profit.
# Amazon Microsoft Bloomberg Uber Facebook
# Hide Tags Array Dynamic Programming



class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        max_profit, min_price = 0, float("inf")
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max( max_profit, price - min_price)
        return max_profit

class Solution2:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        answer = 0
        if len(prices) != 0:
            cost = prices[0]
            for i in range(1,len(prices)):
                if prices[i]< cost:
                    cost = prices[i]
                if prices[i]-cost > answer:
                    answer = prices[i]-cost
        return answer

    def maxProfit2(self, prices):
        answer = 0
        if len(prices) != 0:
            cost = prices[0]
            for i in range(1,len(prices)):
                if prices[i]> cost:
                    answer += (prices[i]-cost)
                    cost = prices[i]
                if prices[i]< cost:
                    cost = prices[i]
                print i, prices[i], cost, answer
        return answer

#OT
class Naive:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if not prices or len(prices) < 2:
            return 0
        profit = float("-inf")
        for i in xrange(len(prices) - 1):
            for j in xrange(len(prices)):
                if prices[j] - prices[i] > profit:
                    profit = prices[j] - prices[i]
        return profit

t1=Solution2()
#print t1.maxProfit([1,3,5,9])
#print t1.maxProfit([9,3,5,1])
#print t1.maxProfit([9,3,5,8])
#print t1.maxProfit([])
print
#print t1.maxProfit2([])
print t1.maxProfit2([2,1,4]) #3
#print t1.maxProfit2([1,3,5,9])
#print t1.maxProfit2([9,3,5,1])
#print t1.maxProfit2([9,3,5,8])

if __name__ == "__main__":
    print Solution().maxProfit([3, 2, 1, 4, 2, 5, 6])
    print Naive().maxProfit([3, 2, 1, 4, 2, 5, 6])

#java
js = '''
public class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length < 2) {
            return 0;
        }
        int min = prices[0];
        int result = 0;
        for (int i = 1; i < prices.length; i++) {
            result = Math.max(result, prices[i] - min);
            min = Math.min(min, prices[i]);
        }
        return result;
    }
}
'''