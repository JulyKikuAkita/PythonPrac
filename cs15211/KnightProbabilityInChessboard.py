__source__ = 'https://leetcode.com/problems/knight-probability-in-chessboard/description/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 688. Knight Probability in Chessboard
#
# On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves.
# The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).
#
# A chess knight has 8 possible moves it can make, as illustrated below.
# Each move is two squares in a cardinal direction, then one square in an orthogonal direction.
#
#
# Each time the knight is to move, it chooses one of eight possible moves uniformly at random
# (even if the piece would go off the chessboard) and moves there.
#
# The knight continues moving until it has made exactly K moves or has moved off the chessboard.
# Return the probability that the knight remains on the board after it has stopped moving.
#
# Example:
# Input: 3, 2, 0, 0
# Output: 0.0625
# Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
# From each of those positions, there are also two moves that will keep the knight on the board.
# The total probability the knight stays on the board is 0.0625.
# Note:
# N will be between 1 and 25.
# K will be between 0 and 100.
# The knight always initially starts on the board.
#
# Companies
# Goldman Sachs
# Related Topics
# Dynamic Programming
# Similar Questions
# Out of Boundary Paths
#
import unittest
#305ms
class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        dp = [[0] * N for _ in xrange(N)]
        dp[r][c] = 1
        for _ in xrange(K):
            dp2 = [[0] * N for _ in xrange(N)]
            for r, row in enumerate(dp):
                for c, val in enumerate(row):
                    for dr, dc in ((2,1),(2,-1),(-2,1),(-2,-1),
                                   (1,2),(1,-2),(-1,2),(-1,-2)):
                        if 0 <= r + dr < N and 0 <= c + dc < N:
                            dp2[r+dr][c+dc] += val / 8.0
            dp = dp2
        return sum(map(sum, dp))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/articles/knight-probability-in-chessboard/
# 16ms
class Solution {
    int[][] moves = {{1, 2}, {1, -2}, {2, 1}, {2, -1}, {-1, 2}, {-1, -2}, {-2, 1}, {-2, -1}};
    public double knightProbability(int N, int K, int r, int c) {
        int len = N;
        double dp0[][] = new double[len][len];
        for(double[] row : dp0) Arrays.fill(row, 1);
        for(int l = 0; l < K; l++) {
            double[][] dp1 = new double[len][len];
            for(int i = 0; i < len; i++) {
                for(int j = 0; j < len; j++) {
                    for(int[] move : moves) {
                        int row = i + move[0];
                        int col = j + move[1];
                        if(isLegal(row, col, len)) dp1[i][j] += dp0[row][col];
                    }
                }
            }
            dp0 = dp1;
        }
        return dp0[r][c] / Math.pow(8, K);
    }
    private boolean isLegal(int r, int c, int len) {
        return r >= 0 && r < len && c >= 0 && c < len;
    }
}

# 31ms
class Solution {
    public double knightProbability(int N, int K, int sr, int sc) {
        int[] dr = new int[]{-1, -1, 1, 1, -2, -2, 2, 2};
        int[] dc = new int[]{2, -2, 2, -2, 1, -1, 1, -1};

        int[] index = new int[N * N];
        int t = 0;
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                if (r * N + c == canonical(r, c, N)) {
                    index[r * N + c] = t;
                    t++;
                } else {
                    index[r * N + c] = index[canonical(r, c, N)];
                }
            }
        }

        double[][] T = new double[t][t];
        int curRow = 0;
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                if (r * N + c == canonical(r, c, N)) {
                    for (int k = 0; k < 8; k++) {
                        int cr = r + dr[k], cc = c + dc[k];
                        if (0 <= cr && cr < N && 0 <= cc && cc < N) {
                            T[curRow][index[canonical(cr, cc, N)]] += 0.125;
                        }
                    }
                    curRow++;
                }
            }
        }

        double[] row = matrixExpo(T, K)[index[sr*N + sc]];
        double ans = 0.0;
        for (double x: row) ans += x;
        return ans;
    }

    public int canonical(int r, int c, int N) {
        if (2*r > N) r = N-1-r;
        if (2*c > N) c = N-1-c;
        if (r > c) {
            int t = r;
            r = c;
            c = t;
        }
        return r * N + c;
    }
    public double[][] matrixMult(double[][] A, double[][] B) {
        double[][] ans = new double[A.length][A.length];
        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < B[0].length; j++) {
                for (int k = 0; k < B.length; k++) {
                    ans[i][j] += A[i][k] * B[k][j];
                }
            }
        }
        return ans;
    }
    public double[][] matrixExpo(double[][] A, int pow) {
        double[][] ans = new double[A.length][A.length];
        for (int i = 0; i < A.length; i++) ans[i][i] = 1;
        if (pow == 0) return ans;
        if (pow == 1) return A;
        if (pow % 2 == 1) return matrixMult(matrixExpo(A, pow-1), A);
        double[][] B = matrixExpo(A, pow / 2);
        return matrixMult(B, B);
    }
}
'''