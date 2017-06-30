__source__ = 'https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/#/description'
# Time:  O(m*n*4)
# Space: O(m*n*4)
#
# Description:
# Given a 01 matrix M, find the longest line of consecutive one in the matrix.
# The line could be horizontal, vertical, diagonal or anti-diagonal.
#
# Example:
# Input:
# [[0,1,1,0],
#  [0,1,1,0],
#  [0,0,0,1]]
# Output: 3
# Hint: The number of elements in the given matrix will not exceed 10,000.
#
# Hide Company Tags Google
# Hide Tags Array

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
1. DP 67%
Note that each cell of the DP table only depends on the current row or previous row
so you can easily optimize the above algorithm to use only O(m) space.
public class Solution {
    public int longestLine(int[][] M) {
        int m = M.length, max = 0;
        if (m == 0) return max;
        int n = M[0].length;
        int[][][] dp = new int[m][n][4];
        for (int i = 0;i < m; i++) {
            for (int j = 0;j < n; j++) {
                if (M[i][j] == 0) continue;
                for (int k = 0; k < 4; k++) dp[i][j][k] = 1;
                    if (j > 0) dp[i][j][0] += dp[i][j-1][0]; // horizontal line
                    if (j > 0 && i > 0) dp[i][j][1] += dp[i-1][j-1][1]; // anti-diagonal line
                    if (i > 0) dp[i][j][2] += dp[i-1][j][2]; // vertical line
                    if (j < n-1 && i > 0) dp[i][j][3] += dp[i-1][j+1][3]; // diagonal line
                    max = Math.max(max, Math.max(dp[i][j][0], dp[i][j][1]));
                    max = Math.max(max, Math.max(dp[i][j][2], dp[i][j][3]));
            }
        }
        return max;
    }
}

2. 8.39%
public class Solution {
    int[][] DIRS = new int[][]{{1,0},{0,1},{1,1}, {1,-1}};
    public int longestLine(int[][] M) {

        if (M == null || M.length == 0) return 0;

        int count = 0;
        for (int i = 0 ; i < M.length; i++) {
            for (int j = 0; j < M[0].length; j++) {
                if (M[i][j] == 1) {
                    count = Math.max(getOneLineMax(M, i, j), count);
                }
            }
        }
        return count;
    }

    public int getOneLineMax(int[][] M, int i, int j) {
        int res = 1;
        for (int[] d : DIRS) {
            int x = i + d[0];
            int y = j + d[1];
            int count = 1;
            while (x >= 0 && x < M.length && y >= 0 && y < M[0].length && M[x][y] == 1) {
                count++;
                x += d[0];
                y += d[1];
            }
            res = Math.max(res, count);
        }
        return res;
    }
}
'''