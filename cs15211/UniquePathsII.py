__source__ = 'https://leetcode.com/problems/unique-paths-ii/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/unique-paths-ii.py
# Time:  O(m * n)
# Space: O(m + n)
# DP
#
# Description: Leetcode # 63. Unique Paths II
#
# Follow up for "Unique Paths":
#
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
#
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
#
# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.
#
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# The total number of unique paths is 2.
#
# Note: m and n will be at most 100.
#
# Companies
# Bloomberg
# Related Topics
# Array Dynamic Programming
# Similar Questions
# Unique Paths
#
import unittest
class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        m ,n = len(obstacleGrid), len(obstacleGrid[0])
        ways = [0] * n

        if obstacleGrid[0][0] == 0:
            ways[0] = 1

        for j in xrange(1, n):
            if obstacleGrid[0][j] == 1:
                ways[j] = 0
            else:
                ways[j] = ways[j - 1]

        for i in xrange(1, m):
            if obstacleGrid[i][0] == 1:
                ways[0] = 0
            for j in xrange(1, n):
                if obstacleGrid[i][j] == 1:
                    ways[j] = 0
                else:
                    ways[j] += ways[j - 1]
        return ways[n - 1]

class SolutionLeetcode:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        m ,n = len(obstacleGrid), len(obstacleGrid[0])
        if m == 0:
            return 0
        dp = [[ 0 for i in xrange(n+1)] for j in xrange(m+1)]
        dp[m-1][n] = 1

        for i in reversed(xrange(m)):
            for j in reversed(xrange(n)):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][j+1] + dp[i+1][j]
        return dp[0][0]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        obstacleGrid = [
                      [0,0,0],
                      [0,1,0],
                      [0,0,0]
                   ]
        print Solution().uniquePathsWithObstacles(obstacleGrid)
        print SolutionLeetcode().uniquePathsWithObstacles(obstacleGrid)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/unique-paths-ii/solution/

# 0ms 100%
class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int width = obstacleGrid[0].length;
        int[] dp = new int[width];
        dp[0] = 1;
        for (int[] row : obstacleGrid) {
            for (int j = 0; j < width; j++) {
                if (row[j] == 1)
                    dp[j] = 0;
                else if (j > 0)
                    dp[j] += dp[j - 1];
            }
        }
        return dp[width - 1];
    }
}

# 0ms 100%
class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
        if (m == 0) {
            return 0;
        }
        int n = obstacleGrid[0].length;
        int[] dp = new int[n];
        for (int i = 0; i < n; i++) {
            if (obstacleGrid[0][i] == 1) {
                break;
            }
            dp[i] = 1;
        }
        for (int i = 1; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (j == 0) {
                    if (obstacleGrid[i][j] == 1) {
                        dp[j] = 0;
                    }
                } else {
                    dp[j] = obstacleGrid[i][j] == 1 ? 0 : dp[j - 1] + dp[j];
                }
            }
        }
        return dp[n - 1];
    }
}

# 2D DP
# 0ms 100%
class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        if (obstacleGrid == null || obstacleGrid.length == 0 || obstacleGrid[0].length == 0) {
            return 0;
        }

        int[][] matrix = new int[obstacleGrid.length][obstacleGrid[0].length];
        for (int i = 0; i < obstacleGrid.length; i++) {
            if (obstacleGrid[i][0] == 0) {
                matrix[i][0] = 1;
            } else {
                break;
            }
        }
        for (int j = 0; j < obstacleGrid[0].length; j++) {
            if (obstacleGrid[0][j] == 0) {
                matrix[0][j] = 1;
            } else {
                break;
            }
        }
        for (int i = 1; i < obstacleGrid.length; i++) {
            for (int j = 1; j < obstacleGrid[0].length; j++) {
                matrix[i][j] = obstacleGrid[i][j] == 0 ? matrix[i - 1][j] + matrix[i][j - 1] : 0;
            }
        }

        return matrix[matrix.length - 1][matrix[0].length - 1];
    }
}
'''