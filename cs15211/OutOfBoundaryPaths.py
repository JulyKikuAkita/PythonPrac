__source__ = 'https://leetcode.com/problems/out-of-boundary-paths/#/description'
# Time:  O(N * m * n)
# Space: O(N * m * n)
#
# Description:
# There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball, you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down, left, right). However, you can at most move N times. Find out the number of paths to move the ball out of grid boundary. The answer may be very large, return it after mod 109 + 7.
#
# Example 1:
# Input:m = 2, n = 2, N = 2, i = 0, j = 0
# Output: 6
# Explanation:
#
# Example 2:
# Input:m = 1, n = 3, N = 3, i = 0, j = 1
# Output: 12
# Explanation:
#
# Note:
# Once you move the ball out of boundary, you cannot move it back.
# The length and height of the grid is in range [1,50].
# N is in range [0,50].
# Hide Company Tags Baidu
# Hide Tags Dynamic Programming Depth-first Search

import unittest

# At time t, let's maintain cur[r][c] = the number of paths to (r, c) with t moves,
# and nxt[r][c] = the number of paths to (r, c) with t+1 moves.
#
# A ball at (r, c) at time t, can move in one of four directions.
# If it stays on the board, then it contributes to a path that takes t+1 moves.
# If it falls off the board, then it contributes to the final answe
class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        MOD = 10**9 + 7
        nxt = [[0] * n for _ in xrange(m)]
        nxt[i][j] = 1

        ans = 0
        for time in xrange(N):
            cur = nxt
            nxt = [[0] * n for _ in xrange(m)]
            for r, row in enumerate(cur):
                for c, val in enumerate(row):
                    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                        if 0 <= nr < m and 0 <= nc < n:
                            nxt[nr][nc] += val
                            nxt[nr][nc] %= MOD
                        else:
                            ans += val
                            ans %= MOD

        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/articles/out-of-boundary-paths/
# Approach #2 Recursion with memoization [Accepted]
# We can remove this redundancy by making use of a memoization array, memomemo.
# memo[i][j][k]memo[i][j][k] is used to store the number of possible moves leading to a path
# out of the boundary if the current position is given by the indices (i, j)(i,j) and number of moves left is kk.
#
# Thus, now if a function call with some parameters is repeated,
# the memomemo array will already contain valid values corresponding to that function call
# resulting in pruning of the search space.
#

#DFS
public class Solution {
    int M=1000000007;
    public int findPaths(int m, int n, int N, int i, int j) {
        int[][][] memo=new int[m][n][N+1];
        for(int[][] l:memo)
            for(int[] sl:l)
                Arrays.fill(sl,-1);
        return findPaths(m,n,N,i,j,memo);
    }
    public int findPaths(int m, int n, int N, int i, int j,int[][][] memo) {
        if(i==m || j==n || i<0 ||j<0)
            return 1;
        if(N==0)
            return 0;
        if(memo[i][j][N]>=0)
            return memo[i][j][N];
        memo[i][j][N]=((findPaths(m,n,N-1,i-1,j,memo)+findPaths(m,n,N-1,i+1,j,memo))%M+(findPaths(m,n,N-1,i,j-1,memo)+findPaths(m,n,N-1,i,j+1,memo))%M)%M;
        return memo[i][j][N];
    }
}

#DP:
public class Solution {
    public int findPaths(int m, int n, int N, int x, int y) {
        int M = 1000000000 + 7;
        int dp[][] = new int[m][n];
        dp[x][y] = 1;
        int count = 0;
        for (int moves = 1; moves <= N; moves++) {
            int[][] temp = new int[m][n];
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (i == m - 1)
                        count = (count + dp[i][j]) % M;
                    if (j == n - 1)
                        count = (count + dp[i][j]) % M;
                    if (i == 0)
                        count = (count + dp[i][j]) % M;
                    if (j == 0)
                        count = (count + dp[i][j]) % M;
                    temp[i][j] = (((i > 0 ? dp[i - 1][j] : 0) + (i < m - 1 ? dp[i + 1][j] : 0)) % M + ((j > 0 ? dp[i][j - 1] : 0) + (j < n - 1 ? dp[i][j + 1] : 0)) % M) % M;
                }
            }
            dp = temp;
        }
        return count;
    }
}
'''