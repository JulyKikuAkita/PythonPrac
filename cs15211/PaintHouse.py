__author__ = 'July'
'''
# https://github.com/kamyu104/LeetCode/blob/master/Python/paint-house.py
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green.
The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix.
For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Hide Company Tags LinkedIn

'''

# Time:  O(n)
# Space: O(1)

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

#java
js = '''
public class Solution {
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