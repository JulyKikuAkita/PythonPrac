__source__ = 'https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/longest-increasing-path-in-a-matrix.py
# Time:  O(m * n)
# Space: O(m * n)
#
# Description: Leetcode #  329. Longest Increasing Path in a Matrix
#
# Given an integer matrix, find the length of the longest increasing path.
#
# From each cell, you can either move to four directions: left, right, up
# or down. You may NOT move diagonally or move outside of the boundary
# (i.e. wrap-around is not allowed).
#
# Example 1:
#
# nums = [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ]
# Return 4
# The longest increasing path is [1, 2, 6, 9].
#
# Example 2:
#
# nums = [
#   [3,4,5],
#   [3,2,6],
#   [2,2,1]
# ]
# Return 4
# The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
#
# Companies
# Google
# Related Topics
# Depth-first Search Topological Sort Memoization
#
import unittest
# DFS + Memorization solution.
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0

        def longestpath(matrix, i, j, max_lengths):
            if max_lengths[i][j]:
                return max_lengths[i][j]
            max_depth = 0
            directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            for d in directions:
                x, y = i + d[0], j + d[1]
                if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and \
                   matrix[x][y] < matrix[i][j]:
                    max_depth = max(max_depth, longestpath(matrix, x, y, max_lengths));
            max_lengths[i][j] = max_depth + 1
            return max_lengths[i][j]
        res = 0
        max_lengths = [[0 for _ in xrange(len(matrix[0]))] for _ in xrange(len(matrix))]
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                res = max(res, longestpath(matrix, i, j, max_lengths))
        return res

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/articles/longest-increasing-path-matrix/
#87.19% 14ms
public class Solution {
    public static final int[][] DIRECTIONS = new int[][] {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    public int longestIncreasingPath(int[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) {
            return 0;
        }
        int m = matrix.length;
        int n = matrix[0].length;
        int[][] longestPath = new int[m][n];
        for (int[] path : longestPath) {
            Arrays.fill(path, -1);
        }
        int result = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                result = Math.max(result, dfs(matrix, longestPath, m, n, i, j));
            }
        }
        return result + 1;
    }

    private int dfs(int[][] matrix, int[][] longestPath, int m, int n, int i, int j) {
        if (longestPath[i][j] >= 0) {
            return longestPath[i][j];
        }
        int result = 0;
        for (int[] direction : DIRECTIONS) {
            int newI = i + direction[0];
            int newJ = j + direction[1];
            if (newI >= 0 && newI < m && newJ >= 0 && newJ < n && matrix[newI][newJ] > matrix[i][j]) {
                result = Math.max(result, dfs(matrix, longestPath, m, n, newI, newJ) + 1);
            }
        }
        longestPath[i][j] = result;
        return result;
    }
}

#14.17% 39ms
// Topological Sort Based Solution
// An Alternative Solution
public class Solution {
    private static final int[][] dir = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    private int m, n;
    public int longestIncreasingPath(int[][] grid) {
        int m = grid.length;
        if (m == 0) return 0;
        int n = grid[0].length;
        // padding the matrix with zero as boundaries
        // assuming all positive integer, otherwise use INT_MIN as boundaries
        int[][] matrix = new int[m + 2][n + 2];
        for (int i = 0; i < m; ++i)
            System.arraycopy(grid[i], 0, matrix[i + 1], 1, n);

        // calculate outdegrees
        int[][] outdegree = new int[m + 2][n + 2];
        for (int i = 1; i <= m; ++i)
            for (int j = 1; j <= n; ++j)
                for (int[] d: dir)
                    if (matrix[i][j] < matrix[i + d[0]][j + d[1]])
                        outdegree[i][j]++;

        // find leaves who have zero out degree as the initial level
        n += 2;
        m += 2;
        List<int[]> leaves = new ArrayList<>();
        for (int i = 1; i < m - 1; ++i)
            for (int j = 1; j < n - 1; ++j)
                if (outdegree[i][j] == 0) leaves.add(new int[]{i, j});

        // remove leaves level by level in topological order
        int height = 0;
        while (!leaves.isEmpty()) {
            height++;
            List<int[]> newLeaves = new ArrayList<>();
            for (int[] node : leaves) {
                for (int[] d:dir) {
                    int x = node[0] + d[0], y = node[1] + d[1];
                    if (matrix[node[0]][node[1]] > matrix[x][y])
                        if (--outdegree[x][y] == 0)
                            newLeaves.add(new int[]{x, y});
                }
            }
            leaves = newLeaves;
        }
        return height;
    }
}
'''