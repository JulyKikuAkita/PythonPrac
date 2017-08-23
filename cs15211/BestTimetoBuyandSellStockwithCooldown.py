__source__ = 'https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/best-time-to-buy-and-sell-stock-with-cooldown.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 309. Best Time to Buy and Sell Stock with Cooldown
#
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
# Companies
# Google
# Related Topics
# Dynamic Programming
# Similar Questions
# Best Time to Buy and Sell Stock Best Time to Buy and Sell Stock II
#
import unittest
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


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        prices = [1, 2, 3, 0, 2]
        print Solution().maxProfit(prices)
        print Solution2().maxProfit(prices)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
The series of problems are typical dp.
The key for dp is to find the variables to represent the states and deduce the transition function.

Of course one may come up with a O(1) space solution directly,
but I think it is better to be generous when you think and be greedy when you implement.

The natural states for this problem is the 3 possible transactions : buy, sell, rest.
Here rest means no transaction on that day (aka cooldown).

Then the transaction sequences can end with any of these three states.

For each of them we make an array, buy[n], sell[n] and rest[n].

buy[i] means before day i what is the maxProfit for any sequence end with buy.

sell[i] means before day i what is the maxProfit for any sequence end with sell.

rest[i] means before day i what is the maxProfit for any sequence end with rest.

Then we want to deduce the transition functions for buy sell and rest. By definition we have:

buy[i]  = max(rest[i-1]-price, buy[i-1])
sell[i] = max(buy[i-1]+price, sell[i-1])
rest[i] = max(sell[i-1], buy[i-1], rest[i-1])
Where price is the price of day i. All of these are very straightforward. They simply represents :

(1) We have to `rest` before we `buy` and
(2) we have to `buy` before we `sell`
One tricky point is how do you make sure you sell before you buy,
since from the equations it seems that [buy, rest, buy] is entirely possible.

Well, the answer lies within the fact that buy[i] <= rest[i] which means rest[i] = max(sell[i-1], rest[i-1]).
That made sure [buy, rest, buy] is never occurred.

A further observation is that and rest[i] <= sell[i] is also true therefore

rest[i] = sell[i-1]
Substitute this in to buy[i] we now have 2 functions instead of 3:

buy[i] = max(sell[i-2]-price, buy[i-1])
sell[i] = max(buy[i-1]+price, sell[i-1])
This is better than 3, but

we can do even better

Since states of day i relies only on i-1 and i-2 we can reduce the O(n) space to O(1).
And here we are at our final solution:

#71.44% 15ms
public class Solution {
    public int maxProfit(int[] prices) {
        int sell = 0, prev_sell = 0, buy = Integer.MIN_VALUE, prev_buy;
        for (int price : prices) {
            prev_buy = buy;
            buy = Math.max(prev_sell - price, prev_buy);
            prev_sell = sell;
            sell = Math.max(prev_buy + price, prev_sell);
        }
        return sell;
    }
}

#71.44% 15ms
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

346.13% 16ms
public class Solution {
    public int maxProfit(int[] prices) {
        int len= prices.length;
        if (len<=1) return 0;

        int[] cooldown = new int[len];
        int[] buy = new int[len];
        int[] sell= new int[len];

        cooldown[0]= 0;
        buy[0]=-prices[0];
        sell[0]= Integer.MIN_VALUE;

        for (int i=1; i<len;i++)
        {
            cooldown[i] = Math.max(cooldown[i-1], sell[i-1]);
            buy[i]= Math.max(buy[i-1],cooldown[i-1]-prices[i]);
            sell[i]= buy[i-1]+ prices[i];
        }

        return Math.max(sell[len-1], cooldown[len-1]);

    }
}
'''