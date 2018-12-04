__source__ = 'https://leetcode.com/problems/best-time-to-buy-and-sell-stock/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/best-time-to-buy-and-sell-stock.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 121. Best Time to Buy and Sell Stock
#
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction
# (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#
# Example 1:
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
#
# max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
# Example 2:
# Input: [7, 6, 4, 3, 1]
# Output: 0
#
# In this case, no transaction is done, i.e. max profit = 0.
#
# Companies
# Amazon Microsoft Bloomberg Uber Facebook
# Related Topics
# Array Dynamic Programming
# Similar Questions
# Maximum Subarray Best Time to Buy and Sell Stock II
# Best Time to Buy and Sell Stock III
# Best Time to Buy and Sell Stock IV
# Best Time to Buy and Sell Stock with Cooldown
#
import unittest
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

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
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

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solution/

# 99.84% 1ms
class Solution {
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

# 99.84% 1ms
class Solution {
    public int maxProfit(int prices[]) {
        int minprice = Integer.MAX_VALUE;
        int maxprofit = 0;
        for (int i = 0; i < prices.length; i++) {
            if (prices[i] < minprice)
                minprice = prices[i];
            else if (prices[i] - minprice > maxprofit)
                maxprofit = prices[i] - minprice;
        }
        return maxprofit;
    }
}

# 99.84% 1ms
class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE;
        int maxProfit = 0;
        for (int i = 0; i < prices.length; i++) {
            minPrice = Math.min(prices[i], minPrice);
            maxProfit = Math.max(maxProfit, prices[i] - minPrice);
        }
        return maxProfit;
    }
}

Kadane's Algorithm - Since no one has mentioned about this so far :) (In case if interviewer twists the input)
The logic to solve this problem is same as "max subarray problem" using Kadane's Algorithm.
Since no body has mentioned this so far, I thought it's a good thing for everybody to know.

All the straight forward solution should work, but if the interviewer twists the question slightly
by giving the difference array of prices, Ex: for {1, 7, 4, 11}, if he gives {0, 6, -3, 7},
you might end up being confused.

Here, the logic is to calculate the difference
(maxCur += prices[i] - prices[i-1]) of the original array,
and find a contiguous subarray giving maximum profit. If the difference falls below 0, reset it to zero.

# 37.56% 2ms
class Solution {
    public int maxProfit(int[] prices) {
        int maxCur = 0, maxSoFar = 0;
        for(int i = 1; i < prices.length; i++) {
            maxCur = Math.max(0, maxCur += prices[i] - prices[i-1]);
            maxSoFar = Math.max(maxCur, maxSoFar);
        }
        return maxSoFar;
    }
}
*maxCur = current maximum value
*maxSoFar = maximum value found so far


'''