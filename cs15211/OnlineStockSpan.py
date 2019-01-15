__source__ = 'https://leetcode.com/problems/online-stock-span/'
# Time:  O(N)
# Space: O(N)
#
# Description: Leetcode # 901. Online Stock Span
#
# Write a class StockSpanner which collects daily price quotes for some stock,
# and returns the span of that stock's price for the current day.
#
# The span of the stock's price today is defined as the maximum number of consecutive days
# (starting from today and going backwards)
# for which the price of the stock was less than or equal to today's price.
#
# For example, if the price of a stock over the next 7 days were
# [100, 80, 60, 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].
#
# Example 1:
#
# Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
# Output: [null,1,1,1,2,1,4,6]
# Explanation:
# First, S = StockSpanner() is initialized.  Then:
# S.next(100) is called and returns 1,
# S.next(80) is called and returns 1,
# S.next(60) is called and returns 1,
# S.next(70) is called and returns 2,
# S.next(60) is called and returns 1,
# S.next(75) is called and returns 4,
# S.next(85) is called and returns 6.
#
# Note that (for example) S.next(75) returned 4, because the last 4 prices
# (including today's price of 75) were less than or equal to today's price.
#
#
# Note:
#
# Calls to StockSpanner.next(int price) will have 1 <= price <= 10^5.
# There will be at most 10000 calls to StockSpanner.next per test case.
# There will be at most 150000 calls to StockSpanner.next across all test cases.
# The total time limit for this problem has been reduced by 75% for C++, and 50% for all other languages.
#
import unittest

# 368ms 26.90%
class StockSpanner(object):
    def __init__(self):
        self.stack = []

    def next(self, price):
        weight = 1
        while self.stack and self.stack[-1][0] <= price:
            weight += self.stack.pop()[1]
        self.stack.append((price, weight))
        return weight

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/online-stock-span/solution/
Approach 1: Stack
Complexity Analysis
Time Complexity: O(Q), where Q is the number of calls to StockSpanner.next.
In total, there are Q pushes to the stack, and at most Q pops.
Space Complexity: O(Q)

# 168ms 22.85%
class StockSpanner {
    Stack<Integer> prices, weights;

    public StockSpanner() {
        prices = new Stack();
        weights = new Stack();
    }

    public int next(int price) {
        int w = 1;
        while (!prices.isEmpty() && prices.peek() <= price) {
            prices.pop();
            w += weights.pop();
        }
        prices.push(price);
        weights.push(w);
        return w;
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner obj = new StockSpanner();
 * int param_1 = obj.next(price);
 */

# 116ms 87.20%
class StockSpanner {
    Node[] stack;
    int p;
    public StockSpanner() {
        stack = new Node[10001];
        p = -1;
    }

    public int next(int price) {
        Node n = new Node(price, 1);
        while ( p >= 0 && stack[p].val <= price) {
            n.count += stack[p--].count;
        }
        stack[++p] = n;
        return n.count;
    }

    class Node {
        int val;
        int count;
        public Node(int val, int count) {
            this.val = val;
            this.count = count;
        }
    }
}
'''