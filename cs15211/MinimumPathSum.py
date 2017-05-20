__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/minimum-path-sum.py
# Time:  O(m * n)
# Space: O(m + n)
#
# Given a m x n grid filled with non-negative numbers,
# find a path from top left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#

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
#test
test = SolutionOther()
arr = [[2,3],[1,5]]

arr1 = [[1,3,1]
       ,[1,5,1]
       ,[4,2,1]]

arr2 = [[0,1]
       ,[1,0]]

print test.minPathSum(arr1)
if __name__ == "__main__":
    print Solution().minPathSum(arr1)
    #print Solution().minPathSum(arr2)
    #print Solution().minPathSum([[1,3,1]
    #                            ,[1,5,1]
    #                            ,[4,2,1]])