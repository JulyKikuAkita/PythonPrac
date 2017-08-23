__source__ = 'https://leetcode.com/problems/maximal-square/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/maximal-square.py
# Time:  O(n^2)
# Space: O(n)
#
# Description: Leetcode # 221. Maximal Square
#
# Given a 2D binary matrix filled with 0's and 1's,
# find the largest square containing all 1's and return its area.
#
# For example, given the following matrix:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# Return 4.
#
# Companies
# Apple Airbnb Facebook
# Related Topics
# Dynamic Programming
# Similar Questions
# Maximal Rectangle
#
import unittest
# DP with sliding window.
class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        m, n = len(matrix) , len(matrix[0])
        size = [[ 0 for j in xrange(n)] for i in xrange(2)]
        max_size = 0

        for j in xrange(n):
            if matrix[0][j] == '1':
                size[0][j] = 1
            max_size = max(max_size, size[0][j])

        for i in xrange(1, m):
            if matrix[i][0] == '1':
                size[i % 2][0] = 1
            else:
                size[i % 2][0] = 0

            for j in xrange(1, n):
                if matrix[i][j] == '1':
                    size[i % 2][j] = min(size[i % 2][j - 1], size[(i - 1) % 2][j], size[(i - 1) % 2][j - 1]) + 1
                    max_size = max(max_size, size[i % 2][j])
                else:
                    size[i % 2][j] = 0
        return max_size *max_size

# Time:  O(n^2)
# Space: O(n^2)
# DP.
class Solution2:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        size = [[0 for j in xrange(n)] for i in xrange(m)]
        max_size = 0

        for j in xrange(n):
            if matrix[0][j] == '1':
                size[0][j] = 1
            max_size = max(max_size, size[0][j])

        for i in xrange(1, m):
            if matrix[i][0] == '1':
                size[i][0] = 1
            else:
                size[i][0] = 0
            for j in xrange(1, n):
                if matrix[i][j] == '1':
                    size[i][j] = min(size[i][j-1], size[i-1][j], size[i-1][j-1]) + 1
                    max_size = max(max_size, size[i][j])
                else:
                    size[i][j] = 0
        return max_size * max_size

# Time:  O(n^2)
# Space: O(n^2)
# DP.
class Solution3:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        H, W = 0, 1
        # DP table stores (h, w) for each (i, j).
        table = [[[0, 0] for j in xrange(len(matrix[0]))] for i in xrange(len(matrix))]

        for i in reversed(xrange(len(matrix))):
            for j in reversed(xrange(len(matrix[i]))):
                # Find the largest h such that (i, j) to (i + h - 1, j) are feasible.
                # Find the largest w such that (i, j) to (i, j + w - 1) are feasible.
                if matrix[i][j] == '1':
                    h, w = 1, 1
                    if i + 1 < len(matrix):
                        h = table[i+1][j][H] + 1
                    if j + 1 < len(matrix[i]):
                        w = table[i][j+1][W] + 1
                    table[i][j] = [h,w]
        # A table stores the length of largest square for each (i, j).
        s = [[0 for j in xrange(len(matrix[0]))] for i in xrange(len(matrix))]
        max_square_area = 0
        for i in reversed(xrange(len(matrix))):
            for j in reversed(xrange(len(matrix[i]))):
                side = min(table[i][j][H], table[i][j][W])
                if matrix[i][j] == '1':
                    # Get the length of largest square with bottom-left corner (i, j).
                    if i + 1 < len(matrix) and j + 1 < len(matrix[j + 1]):
                        side = min(s[i + 1][j + 1] + 1, side)
                    s[i][j] = side
                    max_square_area = max(max_square_area, side * side)
        return max_square_area

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/maximal-square/solution/

# 25.79% 13ms
public class Solution {
    public int maximalSquare(char[][] matrix) {
        int m = matrix.length;
        int n = m == 0 ? 0 : matrix[0].length;
        if (m == 0 || n == 0) {
            return 0;
        }
        int[][] dp = new int[2][n + 1];
        int result = 0;
        int cur = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == '1') {
                    dp[cur][j + 1] = Math.min(Math.min(dp[1 - cur][j], dp[cur][j]), dp[1 - cur][j + 1]) + 1;
                    result = Math.max(result, dp[cur][j + 1]);
                } else {
                    dp[cur][j + 1] = 0;
                }
            }
            cur = 1 - cur;
        }
        return result * result;
    }
}

#70.45% 11ms
public class Solution {
    public int maximalSquare(char[][] matrix) {
        if ( matrix == null || matrix.length == 0 ) return 0;

        int m = matrix.length;
        int n = matrix[0].length;

        int max = 0;
        int[][] dp = new int[m][n];

        for (int i = 0; i < m ;i++){
            if (matrix[i][0] == '1'){
                dp[i][0] = 1;
                max = 1;
            }
        }

        for (int i = 0; i< n; i++){
            if (matrix[0][i] == '1'){
                dp[0][i] = 1;
                max = 1;
            }
        }

        for (int i = 1; i < m ;i++){
            for(int j = 1; j < n; j++){
                if (matrix[i][j] == '0' ) {
                    dp[i][j] = 0;
                }else{
                    dp[i][j] = Math.min(dp[i-1][j-1], Math.min(dp[i][j-1], dp[i-1][j])) + 1;
                    max = Math.max(max, dp[i][j]);
                }
            }
        }
        return max * max;
    }
}

'''
