__source__ = 'https://leetcode.com/problems/number-of-islands/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/number-of-islands.py extension
# Time:  O(m * n)
# Space: O(m * n)
# DFS
# Floodfill Algorithm
#
# Description: Leetcode # 200. Number of Islands
#
# Given a 2d grid map of '1's (land) and '0's (water), return the largest area of the island.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally
# or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# 11110
# 11010
# 11000
# 00000
# Answer: 9
#
# Example 2:
#
# 11000
# 11000
# 00100
# 00011
# Answer: 4
#
# Companies
# Twitch
#
import unittest


class Solution(object):
    pass  # your function here


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:

public class Solution {
    private static final int[][] DIRECTIONS = new int[][] {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};
    int island = 1;
    public int numIslands(char[][] grid) {
        int m = grid.length;
        int n = m == 0 ? 0 : grid[0].length;
        int cnt = 0;
        if (m == 0 || n == 0) {
            return 0;
        }
        List<Integer> area = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    grid[i][j] = '2';
                    dfs(grid, i, j);
                    cnt = Math.max(cnt, island);
                    island = 0;
                }
            }
        }
        return cnt;
    }

    private void dfs(char[][] grid, int i, int j) {
        for (int[] direction : DIRECTIONS) {
            int newI = i + direction[0];
            int newJ = j + direction[1];
            if (newI >= 0 && newI < grid.length && newJ >= 0 && newJ < grid[0].length && grid[newI][newJ] == '1') {
                grid[newI][newJ] = '2';
                island++;
                dfs(grid, newI, newJ);
            }
        }
    }
}
'''