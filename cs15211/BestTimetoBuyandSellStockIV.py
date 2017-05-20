__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/best-time-to-buy-and-sell-stock-iv.py
# Dynamic Programming
# Time:  O(k * n)
# Space: O(k)
# DP
#
# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most k transactions.
#
# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
#
#
'''
# http://www.programcreek.com/2014/03/leetcode-best-time-to-buy-and-sell-stock-iv-java/
This is a generalized version of Best Time to Buy and Sell Stock III. If we can solve this problem, we can also use k=2 to solve III.

The problem can be solve by using dynamic programming. The relation is:

local[i][j] = max(global[i-1][j-1] + max(diff,0), local[i-1][j]+diff)
global[i][j] = max(local[i][j], global[i-1][j])
We track two arrays - local and global. The local array tracks maximum profit of j transactions & the last transaction is on ith day.
The global array tracks the maximum profit of j transactions until ith day.


'''
class Solution:
    # @return an integer as the maximum profit
    def maxProfit(self, k, prices):
        if k >= len(prices) / 2:
            return self.maxAtMostNPairsProfit(prices)
        return self.maxAtMostKPairsProfit(prices, k)

    def maxAtMostNPairsProfit(self, prices):
        profit = 0
        for i in xrange(len(prices) - 1):
            profit += max(0, prices[i + 1] - prices[i])
        return profit

    def maxAtMostKPairsProfit(self, prices, k):
        max_buy = [float("-inf") for _ in xrange(k + 1)]
        max_sell = [ 0 for _ in xrange(k + 1)]

        for i in xrange(len(prices)):
            for j in xrange(1, min(k, i/2+1) + 1):
                max_buy[j] = max(max_buy[j], max_sell[j - 1] - prices[i])
                max_sell[j] = max(max_sell[j], max_buy[j] + prices[i])
        return max_sell[k]

class JavaSol2DDP:
    # @return an integer as the maximum profit
    def maxProfit(self, k, prices):
        m = len(prices)
        if m < 2 or k < 1:
            return 0

        max_buy = [[0 for i in xrange(k+1)]for j in xrange(m)]
        max_sell = [[0 for i in xrange(k+1)]for j in xrange(m)]

        for i in xrange(1, m):
            diff = prices[i] - prices[i-1]
            for j in xrange(1, k + 1):
                max_buy[i][j] = max( max_sell[i-1][j-1]+ max(diff, 0), max_buy[i-1][j] + diff )
                max_sell[i][j] = max(max_sell[i-1][j] , max_buy[i][j])

        return max_sell[m-1][k]


class JavaSol1DDP:
    # @return an integer as the maximum profit
    def maxProfit(self, k, prices):
        m = len(prices)
        if m < 2 or k < 1:
            return 0

        max_buy = [0 for i in xrange(k+1)]
        max_sell = [0 for i in xrange(k+1)]
        for i in xrange(m-1):
            diff = prices[i+1] - prices[i]
            for j in reversed(xrange(1, k+1)):
                max_buy[j] = max(max_sell[j-1] + max(diff, 0), max_buy[j] + diff)
                max_sell[j] = max(max_buy[j], max_sell[j])
        return max_sell[k]

#test
if __name__ == '__main__':
    prices = [1, 2, 3, 4]
    print Solution().maxProfit(2, prices)
    print JavaSol2DDP().maxProfit(2, prices)
    print JavaSol1DDP().maxProfit(2, prices)

#java
js = '''
public class Solution {
    public int maxProfit(int k, int[] prices) {
        int len = prices.length;
        if (k <= 0 || len < 2) {
            return 0;
        } else if (k >= len / 2) {
            return maxProfitNoLimit(prices);
        }
        int[] local = new int[k + 1];
        int[] global = new int[k + 1];
        for (int i = 1; i < len; i++) {
            int diff = prices[i] - prices[i - 1];
            for (int j = k ; j >= 1; j--) {
                local[j] = Math.max(global[j - 1] + Math.max(diff, 0), local[j] + diff);
                global[j] = Math.max(global[j], local[j]);
            }
        }
        return global[k];
    }

    private int maxProfitNoLimit(int[] prices) {
        int result = 0;
        for (int i = 1; i < prices.length; i++) {
            result += Math.max(prices[i] - prices[i - 1], 0);
        }
        return result;
    }
}

public class Solution {
    public int maxProfit(int k, int[] prices) {
        int n = prices.length;
        if( n < 2 || k < 1) return 0;
        else if( k >= n / 2) return noLimitProfit(prices);

       int[][] cur = new int[n][k + 1];
       int[][] glo = new int[n][k + 1];
       for (int i = 1; i < n; i++) {
           int diff = prices[i] - prices[i-1];
           for (int j = 1; j <= k ; j++){
               cur[i][j] = Math.max(glo[i-1][j-1] + Math.max(diff, 0), cur[i-1][j] + diff );
               glo[i][j] = Math.max(glo[i-1][j], cur[i][j]);
           }
       }

        return glo[n-1][k];
    }

    private int noLimitProfit(int[] prices){
        int res = 0;
        for (int i = 1; i < prices.length ;i++){
            res += Math.max(0, prices[i] - prices[i-1]);
        }

        return res;
    }
}
'''