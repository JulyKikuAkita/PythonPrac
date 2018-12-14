__source__ = 'https://leetcode.com/problems/paint-house/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/paint-house.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 265. Paint House II
#
# There are a row of n houses, each house can be painted with one of the three colors: red, blue or green.
# The cost of painting each house with a certain color is different.
# You have to paint all the houses such that no two adjacent houses have the same color.
#
# The cost of painting each house with a certain color is represented by a n x 3 cost matrix.
# For example, costs[0][0] is the cost of painting house 0 with color red;
# costs[1][2] is the cost of painting house 1 with color green, and so on...
# Find the minimum cost to paint all houses.
#
# Note:
# All costs are positive integers.
#
# Companies
# LinkedIn
# Related Topics
# Dynamic Programming
# Similar Questions
# House Robber House Robber II Paint House II Paint Fence
#

import unittest
# 24ms 92.47%
class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0

        min_costs = [costs[0], [0,0,0]]
        n = len(costs)
        for i in xrange(1, n):
            min_costs[i % 2][0] = costs[i][0] + min(min_costs[(i-1) % 2][1], min_costs[(i-1) % 2][2] )
            min_costs[i % 2][1] = costs[i][0] + min(min_costs[(i-1) % 2][0], min_costs[(i-1) % 2][2] )
            min_costs[i % 2][2] = costs[i][0] + min(min_costs[(i-1) % 2][0], min_costs[(i-1) % 2][1] )
        return min(min_costs[(n-1)%2])

# Time:  O(n)
# Space: O(n)
class Solution2(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        n = len(costs)
        for i in xrange(1, n):
            costs[i][0] += min(costs[i-1][1], costs[i-1][2])
            costs[i][1] += min(costs[i-1][0], costs[i-1][2])
            costs[i][2] += min(costs[i-1][0], costs[i-1][1])
        return min(costs[n-1])

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
The 1st row is the prices for the 1st house,
we can change the matrix to present sum of prices from the 2nd row.
i.e, the costs[1][0] represent minimum price to paint the second house red plus the 1st house.
Recursion: paintCurrentRed = min(paintPreviousGreen,paintPreviousBlue) + costs[i+1][0]

# 1ms 57.99%
class Solution {
    public int minCost(int[][] costs) {
        int[][] dp = new int[2][3];
        int cur = 0;
        for (int i = 0; i < costs.length; i++) {
            dp[cur][0] = Math.min(dp[1 - cur][1], dp[1 - cur][2]) + costs[i][0];
            dp[cur][1] = Math.min(dp[1 - cur][0], dp[1 - cur][2]) + costs[i][1];
            dp[cur][2] = Math.min(dp[1 - cur][0], dp[1 - cur][1]) + costs[i][2];
            cur = 1 - cur;
        }
        return Math.min(Math.min(dp[1 - cur][0], dp[1 - cur][1]), dp[1 - cur][2]);
    }
}

# 0ms 100%
class Solution {
    public int minCost(int[][] costs) {
        int n = costs.length;
        if(n == 0) return 0;
        int min0 = costs[0][0];
        int min1 = costs[0][1];
        int min2 = costs[0][2];
        int pre0 = 0, pre1 = 0, pre2 = 0;
        for(int i = 1; i < n; i++){
            pre0 = min0;
            pre1 = min1;
            pre2 = min2;
            min0 = costs[i][0] + Math.min(pre1, pre2);
            min1 = costs[i][1] + Math.min(pre0, pre2);
            min2 = costs[i][2] + Math.min(pre0, pre1);
        }
        return Math.min(min0, Math.min(min1, min2));
    }
}

# 1ms 57.99%
class Solution {
    public int minCost(int[][] costs) {
        if (costs == null || costs.length == 0 || costs[0].length != 3) {
            return 0;
        }
        int numOfHouse = costs.length;
        int[][] dp = new int[2][3];
        for (int i = 0; i < numOfHouse; i++) {
            for (int j = 0; j < 3; j++) {
                dp[i % 2][j] = Math.min(dp[(i + 1) % 2][(j + 1) % 3], dp[(i + 1) % 2][(j + 2) % 3]) + costs[i][j];
            }
        }
        return Math.min(Math.min(dp[(numOfHouse + 1) % 2][0], dp[(numOfHouse + 1) % 2][1]), dp[(numOfHouse + 1) % 2][2]);
    }
}
'''