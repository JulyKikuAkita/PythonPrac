__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/bomb-enemy.py
# Time:  O(m * n)
# Space: O(m * n)
'''
Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Note that you can only put the bomb at an empty cell.

Example:
For the given grid

0 E 0 0
E 0 W E
0 E 0 0

return 3. (Placing a bomb at (1,1) kills 3 enemies)
Credits:
Special thanks to @memoryless for adding this problem and creating all test cases.

Hide Company Tags Google
Hide Tags Dynamic Programming

'''
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

#java

js = '''
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
'''