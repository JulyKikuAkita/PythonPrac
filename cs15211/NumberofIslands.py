__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/number-of-islands.py
# Time:  O(m * n)
# Space: O(m * n)
# DFS
# Floodfill Algorithm
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally
# or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# 11110
# 11010
# 11000
# 00000
# Answer: 1
#
# Example 2:
#
# 11000
# 11000
# 00100
# 00011
# Answer: 3
#

#idea is to merge individual islands
class Solution:
    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
        if grid == []:
            return 0
        row = len(grid)
        col = len(grid[0])
        used = [[False for j in xrange(col)] for i in xrange(row)]

        count = 0
        for i in xrange(row):
            for j in xrange(col):
                if grid[i][j] == '1' and not used[i][j]:
                    self.dfs(grid, used, row, col, i, j)
                    count += 1
        return count


    def dfs(self, grid, used, row, col, x, y):
        if grid[x][y] == '0' or used[x][y]:
            return 0
        used[x][y] = True

        if x != 0:
            self.dfs(grid, used, row, col, x - 1, y)
        if x != row -1:
            self.dfs(grid, used, row, col, x + 1, y)
        if y != 0 :
            self.dfs(grid, used, row, col, x, y - 1)
        if y != col - 1:
            self.dfs(grid, used, row, col, x, y + 1)

# java: http://www.programcreek.com/2014/04/leetcode-number-of-islands-java/
# idea is to merge individual islands
# not use visited
class Solution2:
    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        count = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == '1':
                    self.mergeIsland(grid, i, j )
                    count += 1
        print grid
        return count

    def mergeIsland(self, grid, i, j):
        if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1:
            return

        if grid[i][j] != '1':
            return

        grid[i][j] = '2'

        #if i != 0:
        self.mergeIsland(grid, i-1, j)
        #if i != len(grid) - 1:
        self.mergeIsland(grid, i+1, j)
        #if j != 0:
        self.mergeIsland(grid, i, j-1)
        #if j != len(grid[0]) - 1:
        self.mergeIsland(grid, i , j+1)


#test
grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]
if __name__ == "__main__":
    print Solution().numIslands(grid)
    print Solution2().numIslands(grid)