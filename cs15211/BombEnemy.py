__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/bomb-enemy.py
# Time:  O(m * n)
# Space: O(m * n)
#
# Description: Leetcode # 361. Bomb Enemy
#
# Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero),
# return the maximum enemies you can kill using one bomb.
# The bomb kills all the enemies in the same row and column
# from the planted point until it hits the wall since the wall is too strong to be destroyed.
# Note that you can only put the bomb at an empty cell.
#
# Example:
# For the given grid
#
# 0 E 0 0
# E 0 W E
# 0 E 0 0
#
# return 3. (Placing a bomb at (1,1) kills 3 enemies)
# Credits:
# Special thanks to @memoryless for adding this problem and creating all test cases.
#
# Companies
# Google
# Related Topics
# Dynamic Programming
#
import unittest
class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        result = 0
        if not grid or not grid[0]:
            return result

        down = [[0 for _ in xrange(len(grid[0]))] for _ in xrange(len(grid))]
        right = [[0 for _ in xrange(len(grid[0]))] for _ in xrange(len(grid))]
        for i in reversed(xrange(len(grid))):
            for j in reversed(xrange(len(grid[0]))):
                if grid[i][j] != 'W':
                    if i + 1 < len(grid):
                        down[i][j] = down[i + 1][j]
                    if j + 1 < len(grid[0]):
                        right[i][j] = right[i][j + 1]
                    if grid[i][j] == 'E':
                        down[i][j] += 1
                        right[i][j] += 1

        up = [0 for _ in xrange(len(grid[0]))]
        for i in xrange(len(grid)):
            left = 0
            for j in xrange(len(grid[0])):
                if grid[i][j] == 'W':
                    up[j], left = 0, 0
                elif grid[i][j] == 'E':
                    up[j] += 1
                    left += 1
                else:
                    result = max(result, left + up[j] + right[i][j] + down[i][j])
        return result

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
Walk through the matrix. At the start of each non-wall-streak (row-wise or column-wise),
count the number of hits in that streak and remember it. O(mn) time, O(n) space.

#50.07% 50ms
public class Solution {
    public int maxKilledEnemies(char[][] grid) {
        int result = 0;
        int m = grid.length;
        int n = m == 0 ? 0 : grid[0].length;
        int rowEnemyCount = 0;
        int[] colEnemyCount = new int[n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (j == 0 || grid[i][j] == 'W') {
                    rowEnemyCount = 0;
                    for (int k = grid[i][j] == 'W' ? j + 1 : 0; k < n; k++) {
                        if (grid[i][k] == 'E') {
                            rowEnemyCount++;
                        } else if (grid[i][k] == 'W') {
                            break;
                        }
                    }
                }
                if (i == 0 || grid[i][j] == 'W') {
                    colEnemyCount[j] = 0;
                    for (int k = grid[i][j] == 'W' ? i + 1 : 0; k < m; k++) {
                        if (grid[k][j] == 'E') {
                            colEnemyCount[j]++;
                        } else if (grid[k][j] == 'W') {
                            break;
                        }
                    }
                }
                if (grid[i][j] == '0') {
                    result = Math.max(result, rowEnemyCount + colEnemyCount[j]);
                }
            }
        }
        return result;
    }
}

#89.12% 38ms
public class Solution {
    public int maxKilledEnemies(char[][] grid) {
        if (grid == null || grid.length == 0 ||  grid[0].length == 0) return 0;
        int max = 0;
        int row = 0;
        int[] col = new int[ grid[0].length ];
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){
                if (grid[i][j] == 'W') continue;
                if (j == 0 || grid[i][j-1] == 'W'){
                     row = killedEnemiesRow(grid, i, j);
                }
                if (i == 0 || grid[i-1][j] == 'W'){
                     col[j] = killedEnemiesCol(grid,i,j);
                }
                if (grid[i][j] == '0'){
                    max = (row + col[j] > max) ? row + col[j] : max;
                }
            }

        }

        return max;
    }

    //calculate killed enemies for row i from column j
    private int killedEnemiesRow(char[][] grid, int i, int j){
        int num = 0;
        while (j < grid[0].length && grid[i][j] != 'W'){
            if (grid[i][j] == 'E') num++;
            j++;
        }
        return num;
    }
    //calculate killed enemies for  column j from row i
    private int killedEnemiesCol(char[][] grid, int i, int j){
        int num = 0;
        while (i < grid.length && grid[i][j] != 'W'){
            if (grid[i][j] == 'E') num++;
            i++;
        }
        return num;
    }
}

#99.59% 30ms
public class Solution {
    public int maxKilledEnemies(char[][] grid) {
        if( grid.length == 0) return 0;

        int[][] dp = new int[grid.length][grid[0].length];
        for (int i = 0; i < grid.length; i++) {
            int enm = 0, left = 0;
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 'E') enm ++;

                if (grid[i][j] == 'W') {
                    while (left < j) {
                        if (grid[i][left] == '0') dp[i][left] = enm;
                        left++;
                    }
                    enm = 0;
                }
            }

            while (left < grid[0].length) {
                if (grid[i][left] == '0') dp[i][left] = enm;
                left++;
            }
        }

        int res = 0;
        for (int j = 0; j < grid[0].length; j++) {
            int enm = 0, top = 0;
            for (int i = 0; i < grid.length; i++) {
                if (grid[i][j] == 'E') enm++;
                if (grid[i][j] == 'W') {
                    while (top < i) {
                        if (grid[top][j] == '0') {
                            dp[top][j] += enm;
                            res = Math.max(res, dp[top][j]);
                        }
                        top++;
                    }
                    enm = 0;
                }
            }
            while (top < grid.length) {
                if (grid[top][j] == '0') {
                    dp[top][j] += enm;
                    res = Math.max(res, dp[top][j]);
                }
                top++;
            }
        }
        return res;
    }
}
'''