__source__ = 'https://leetcode.com/problems/minimum-path-sum/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/minimum-path-sum.py
# Time:  O(m * n)
# Space: O(m + n)
#
# Description: Leetcode # 64. Minimum Path Sum
#
# Given a m x n grid filled with non-negative numbers,
# find a path from top left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
# Related Topics
# Array Dynamic Programming
# Similar Questions
# Unique Paths Dungeon Game
#
import unittest
class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        sum = list(grid[0])
        print sum
        for j in xrange(1, len(grid[0])):
            sum[j] = sum[j - 1] + grid[0][j]
        for i in xrange(1, len(grid)):
            sum[0] += grid[i][0]
            for j in xrange(1, len(grid[0])):
                sum[j] = min(sum[j - 1], sum[j]) + grid[i][j]
        return sum[-1]

#2-D DP
class SolutionOther:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        from copy import copy, deepcopy
        dp = deepcopy(grid)
        #dp = grid[:] #this modified grid as well
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == 0 and j > 0:
                    dp[i][j] += dp[i][j-1]
                elif j == 0 and i > 0:
                    dp[i][j] += dp[i-1][j]
                elif i > 0 and j > 0:
                    dp[i][j] += min(dp[i][j-1],dp[i-1][j])
        #print dp
        #print grid
        return dp[len(dp)-1][len(dp[0])-1]

class TestMethods(unittest.TestCase):
    test = SolutionOther()
    arr = [[2,3],[1,5]]

    arr1 = [[1,3,1]
           ,[1,5,1]
           ,[4,2,1]]

    arr2 = [[0,1]
           ,[1,0]]

    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().minPathSum(self.arr1)
        #print Solution().minPathSum(arr2)
        #print Solution().minPathSum([[1,3,1]
        #                            ,[1,5,1]
        #                            ,[4,2,1]])

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/minimum-path-sum/solution/

Recursion relation:
dp(i, j)=grid(i,j)+min(dp(i+1,j),dp(i,j+1)) dp(i,j)=grid(i,j)+min(dp(i+1,j),dp(i,j+1))

# Naive:
# TLE
class Solution {
    public int calculate(int[][] grid, int i, int j) {
        if (i == grid.length || j == grid[0].length) return Integer.MAX_VALUE;
        if (i == grid.length - 1 && j == grid[0].length - 1) return grid[i][j];
        return grid[i][j] + Math.min(calculate(grid, i + 1, j), calculate(grid, i, j + 1));
    }
    public int minPathSum(int[][] grid) {
        return calculate(grid, 0, 0);
    }
}

Approach #4 Dynamic Programming (Without Extra Space) [Accepted]
# 4.67% 6ms
# Time:  O(m * n)
# Space: O(m * n)
# 9ms 14.42%
class Solution {
    public int minPathSum(int[][] grid) {
        int[][] dp = new int[grid.length][grid[0].length];
        for (int i = grid.length - 1; i >= 0; i--) {
            for (int j = grid[0].length - 1; j >= 0; j--) {
                if(i == grid.length - 1 && j != grid[0].length - 1)
                    dp[i][j] = grid[i][j] +  dp[i][j + 1];
                else if(j == grid[0].length - 1 && i != grid.length - 1)
                    dp[i][j] = grid[i][j] + dp[i + 1][j];
                else if(j != grid[0].length - 1 && i != grid.length - 1)
                    dp[i][j] = grid[i][j] + Math.min(dp[i + 1][j], dp[i][j + 1]);
                else
                    dp[i][j] = grid[i][j];
            }
        }
        return dp[0][0];
    }
}

Approach #3 Dynamic Programming 1D [Accepted]
# 84.80%, 3ms
class Solution {
    public int minPathSum(int[][] grid) {
        int m = grid.length;
        if (m == 0) {
            return 0;
        }
        int n = grid[0].length;
        int[] dp = new int[n];
        dp[0] = grid[0][0];
        for (int j = 1; j < n; j++) {
            dp[j] = dp[j - 1] + grid[0][j];
        }
        for (int i = 1; i < m; i++) {
            dp[0] += grid[i][0];
            for (int j = 1; j < n; j++) {
                dp[j] = Math.min(dp[j - 1], dp[j]) + grid[i][j];
            }
        }
        return dp[n - 1];
    }
}

'''
