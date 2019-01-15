__source__ = 'https://leetcode.com/problems/domino-and-tromino-tiling/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 790. Domino and Tromino Tiling
#
# We have two types of tiles: a 2x1 domino shape, and an "L" tromino shape.
# These shapes may be rotated.
#
# XX  <- domino
#
# XX  <- "L" tromino
# X
# Given N, how many ways are there to tile a 2 x N board? Return your answer modulo 10^9 + 7.
#
# (In a tiling, every square must be covered by a tile.
# Two tilings are different if and only if there are two 4-directionally adjacent cells on the board
# such that exactly one of the tilings has both squares occupied by a tile.)
#
# Example:
# Input: 3
# Output: 5
# Explanation:
# The five different ways are listed below, different letters indicates different tiles:
# XYZ XXZ XYY XXY XYY
# XYZ YYZ XZZ XYY XXY
# Note:
#
# N  will be in range [1, 1000].
#
import unittest

# 24ms 74.71%
class Solution(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        MOD = 10**9 + 7
        dp = [1, 0, 0, 0]
        for _ in xrange(N):
            ndp = [0, 0, 0, 0]
            ndp[0b00] = (dp[0b00] + dp[0b11]) % MOD
            ndp[0b01] = (dp[0b00] + dp[0b10]) % MOD
            ndp[0b10] = (dp[0b00] + dp[0b01]) % MOD
            ndp[0b11] = (dp[0b00] + dp[0b01] + dp[0b10]) % MOD
            dp = ndp
        return dp[0]

# 24ms 74.71%
class Solution2(object):
    def numTilings(self, N):
        MOD = 10**9 + 7

        def matrix_mult(A, B):
            ZB = zip(*B)
            return [[sum(a * b for a, b in zip(row, col)) % MOD
                     for col in ZB] for row in A]

        def matrix_expo(A, K):
            if K == 0:
                return [[+(i==j) for j in xrange(len(A))]
                        for i in xrange(len(A))]
            if K == 1:
                return A
            elif K % 2:
                return matrix_mult(matrix_expo(A, K-1), A)
            B = matrix_expo(A, K/2)
            return matrix_mult(B, B)

        T = [[1, 0, 0, 1],
             [1, 0, 1, 0],
             [1, 1, 0, 0],
             [1, 1, 1, 0]]
        return matrix_expo(T, N)[0][0]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/domino-and-tromino-tiling/solution/
Approach #1: Dynamic Programming [Accepted]
Complexity Analysis
Time Complexity: O(N). We update the state N times.
Space Complexity: O(1).

# 3ms 58.75%
class Solution {
    public int numTilings(int N) {
        int MOD = 1_000_000_007;
        long[] dp = new long[]{1, 0, 0, 0};
        for (int i = 0; i < N; i++) {
            long[] ndp = new long[4];
            ndp[0b00] = (dp[0b00] + dp[0b11]) % MOD;
            ndp[0b01] = (dp[0b00] + dp[0b10]) % MOD;
            ndp[0b10] = (dp[0b00] + dp[0b01]) % MOD;
            ndp[0b11] = (dp[0b00] + dp[0b01] + dp[0b10]) % MOD;
            dp = ndp;
        }
        return (int) dp[0];
    }
}

Approach #2: Matrix Exponentiation
Complexity Analysis
Time Complexity: O(logN). We perform O(logN) multiplications.
Space Complexity: O(logN), the size of the recursive call stack.

# 2ms 100%
class Solution {
    int MOD = 1_000_000_007;
    public int numTilings(int N) {
        int[][] T = new int[][]{{1,0,0,1},{1,0,1,0},{1,1,0,0},{1,1,1,0}};
        return matrixExpo(T, N)[0][0];
    }

    private int[][] matrixMult(int[][] A, int[][] B) {
        int[][] ans = new int[A.length][A.length];
        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < B[0].length; j++) {
                long entry = 0;
                for (int k = 0; k < B.length; k++)
                    entry += (long) A[i][k] * (long) B[k][j] % MOD;
                ans[i][j] = (int) (entry % MOD);
            }
        }
        return ans;
    }

    private int[][] matrixExpo(int[][] A, int pow) {
        int[][] ans = new int[A.length][A.length];
        for (int i = 0; i < A.length; i++) ans[i][i] = 1;
        if (pow == 0) return ans;
        if (pow == 1) return A;
        if (pow % 2 == 1) return matrixMult(matrixExpo(A, pow-1), A);
        int[][] B = matrixExpo(A, pow / 2);
        return matrixMult(B, B);
    }
}

'''