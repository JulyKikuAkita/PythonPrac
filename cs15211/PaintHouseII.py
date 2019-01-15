__source__ = 'https://leetcode.com/problems/paint-house-ii/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/paint-house-ii.py
# Time:  O(n * k)
# Space: O(k)
#
# Description: Leetcode # 265. Paint House II
#
# There are a row of n houses, each house can be painted with one of the k colors.
# The cost of painting each house with a certain color is different.
# You have to paint all the houses such that no two adjacent houses have the same color.
#
# The cost of painting each house with a certain color is represented by a n x k cost matrix.
# For example, costs[0][0] is the cost of painting house 0 with color 0;
# costs[1][2] is the cost of painting house 1 with color 2, and so on...
# Find the minimum cost to paint all houses.
#
# Note:
# All costs are positive integers.
#
# Follow up:
# Could you solve it in O(nk) runtime?
#
# Companies
# Facebook
# Related Topics
# Dynamic Programming
# Similar Questions
# Product of Array Except Self Sliding Window Maximum Paint House Paint Fence
#
import unittest
# 32ms 90.57%
class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        return min(reduce(self.combine, costs) if costs else 0)

    def combine(self, tmp, secrow):
        #print tmp, secrow
        smallest, k, i  = min(tmp), len(tmp), tmp.index(min(tmp))
        tmp, tmp[i] = [smallest] * k, min(tmp[:i] + tmp[i+1:])
        return map(sum, zip(tmp, secrow))

# 68ms 24.53%
class Solution2(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0

        n = len(costs)
        k = len(costs[0])
        dp = [costs[0], [0] * k]

        for i in xrange(1, n):
            smallest, second_smallest = float("inf"), float("inf")
            for j in xrange(k):
                if dp[(i-1) % 2][j] < smallest:
                    smallest, second_smallest = dp[(i-1) % 2][j], smallest
                elif dp[(i-1) % 2][j] < second_smallest:
                    second_smallest = dp[(i-1) % 2][j]
            for j in xrange(k):
                min_j = smallest if dp[(i-1) % 2][j] != smallest else second_smallest
                dp[i % 2][j] = min_j + costs[i][j]
        return min(dp[(n-1)%2])

class Solution3(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs :
            return 0

        dp = [[ 0 for i in xrange(len(costs[0]))] for j in xrange(len(costs))]

        for i in xrange(len(costs[0])):
            dp[0][i] = costs[0][i]

        min1 = float("inf")
        min2 = float("inf")
        for i in xrange(1, len(dp)):
            min1 = dp[i-1].index(min(dp[i-1]))
            min2 = dp[i-1].index(sorted(dp[i-1])[1])
            print min1, min2
            for j in xrange(len(dp[0])):
                if j == min1:
                    dp[i][j] = dp[i-1][min2]
                elif j == min2:
                    dp[i][j] = dp[i-1][min1]
                else:
                    dp[i][j] = min(dp[i-1][min1], dp[i-1][min2])
                dp[i][j] += costs[i][j]
        #print  min(dp[len(dp)-1]), dp
        return min(dp[len(dp)-1])

#test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        costs = [[1,2,3], [2,4,5],[7,8,9]]
        print Solution().minCostII(costs)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

dp[i][j] represents the min paint cost from house 0 to house i when house i use color j;
The formula will be dp[i][j] = Math.min(any k!= j| dp[i-1][k]) + costs[i][j].

Take a closer look at the formula, we don't need an array to represent dp[i][j],
we only need to know the min cost to the previous house of any color and
if the color j is used on previous house to get prev min cost,
use the second min cost that are not using color j on the previous house.
So I have three variable to record: prevMin, prevMinColor, prevSecondMin.
and the above formula will be translated into:
dp[currentHouse][currentColor] = (currentColor ==
prevMinColor? prevSecondMin: prevMin) + costs[currentHouse][currentColor].

# 5ms 27.61%
class Solution {
    public int minCostII(int[][] costs) {
        if (costs == null || costs.length == 0 || costs[0].length == 0) {
            return 0;
        }
        int numberOfHouses = costs.length;
        int numberOfColors = costs[0].length;
        if (numberOfHouses > 1 && numberOfColors == 1) {
            return 0;
        }
        int[][] dp = new int[2][numberOfColors];
        for (int i = 0; i < numberOfHouses; i++) {
            int smallest = Integer.MAX_VALUE;
            int secondSmallest = Integer.MAX_VALUE;
            for (int j = 0; j < numberOfColors; j++) {
                if (dp[(i + 1) % 2][j] <= smallest) {
                    secondSmallest = smallest;
                    smallest = dp[(i + 1) % 2][j];
                } else if (dp[(i + 1) % 2][j] < secondSmallest) {
                    secondSmallest = dp[(i + 1) % 2][j];
                }
            }
            for (int j = 0; j < numberOfColors; j++) {
                if (numberOfColors != 1 && dp[(i + 1) % 2][j] == smallest) {
                    dp[i % 2][j] = secondSmallest + costs[i][j];
                } else {
                    dp[i % 2][j] = smallest + costs[i][j];
                }
            }
        }
        int result = Integer.MAX_VALUE;
        for (int j = 0; j < numberOfColors; j++) {
            result = Math.min(result, dp[(numberOfHouses + 1) % 2][j]);
        }
        return result;
    }
}

# 4ms 36.74%
class Solution {
    public int minCostII(int[][] costs) {
        if (costs == null || costs.length == 0) return 0;

        int n = costs.length, k = costs[0].length;
        // min1 is the index of the 1st-smallest cost till previous house
        // min2 is the index of the 2nd-smallest cost till previous house
        int min1 = -1, min2 = -1;

        for (int i = 0; i < n; i++) {
            int last1 = min1, last2 = min2;
            min1 = -1; min2 = -1;

            for (int j = 0; j < k; j++) {
                if (j != last1) {
                    // current color j is different to last min1
                    costs[i][j] += last1 < 0 ? 0 : costs[i - 1][last1];
                } else {
                    costs[i][j] += last2 < 0 ? 0 : costs[i - 1][last2];
                }

                // find the indices of 1st and 2nd smallest cost of painting current house i
                if (min1 < 0 || costs[i][j] < costs[i][min1]) {
                    min2 = min1; min1 = j;
                } else if (min2 < 0 || costs[i][j] < costs[i][min2]) {
                    min2 = j;
                }
            }
        }

        return costs[n - 1][min1];
    }
}

# 3ms 66.12%
class Solution {
    public int minCostII(int[][] costs) {
        if (costs.length == 0) {
            return 0;
        }

        int prevMin = 0;
        int prevSecMin = 0;
        int prevMinIndex = -1;
        for (int i = 0; i < costs.length; i++) {
            int min = Integer.MAX_VALUE;
            int secMin = Integer.MAX_VALUE;
            int minIndex = -1;
            for (int j = 0; j < costs[i].length; j++) {
                int value = costs[i][j] + (j == prevMinIndex ? prevSecMin : prevMin);
                if (minIndex == -1 || value < min) {
                    secMin = min;
                    min = value;
                    minIndex = j;
                } else if (value < secMin) {
                    secMin = value;
                }
            }

            prevMin = min;
            prevSecMin = secMin;
            prevMinIndex = minIndex;
        }

        return prevMin;
    }
}
'''