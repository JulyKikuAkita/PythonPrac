__author__ = 'July'
'''
https://github.com/kamyu104/LeetCode/blob/master/Python/paint-house-ii.py
There are a row of n houses, each house can be painted with one of the k colors.
The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix.
For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Follow up:
Could you solve it in O(nk) runtime?

Hide Company Tags Facebook
'''


# Time:  O(n * k)
# Space: O(k)

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
if __name__ == "__main__":
    costs = [[1,2,3], [2,4,5],[7,8,9]]
    print Solution().minCostII(costs)


#java
js = '''
public class Solution {
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
'''