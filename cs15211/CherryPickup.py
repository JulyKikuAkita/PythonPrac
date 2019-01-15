# coding=utf-8
__source__ = 'https://leetcode.com/problems/cherry-pickup/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 741. Cherry Pickup
#
# In a N x N grid representing a field of cherries, each cell is one of three possible integers.
#
# 0 means the cell is empty, so you can pass through;
# 1 means the cell contains a cherry, that you can pick up and pass through;
# -1 means the cell contains a thorn that blocks your way.
# Your task is to collect maximum number of cherries possible by following the rules below:
#
# Starting at the position (0, 0) and reaching (N-1, N-1)
# by moving right or down through valid path cells (cells with value 0 or 1);
# After reaching (N-1, N-1), returning to (0, 0) by moving left or up through valid path cells;
# When passing through a path cell containing a cherry, you pick it up and the cell becomes an empty cell (0);
# If there is no valid path between (0, 0) and (N-1, N-1), then no cherries can be collected.
# Example 1:
# Input: grid =
# [[0, 1, -1],
#  [1, 0, -1],
#  [1, 1,  1]]
# Output: 5
# Explanation:
# The player started at (0, 0) and went down, down, right right to reach (2, 2).
# 4 cherries were picked up during this single trip,
# and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
# Then, the player went left, up, up, left to return home, picking up one more cherry.
# The total number of cherries picked up is 5, and this is the maximum possible.
# Note:
#
# grid is an N by N 2D array, with 1 <= N <= 50.
# Each grid[i][j] is an integer in the set {-1, 0, 1}.
# It is guaranteed that grid[0][0] and grid[N-1][N-1] are not -1.
#
import unittest

#332ms 98.44%
class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[-1][-1] == -1: return 0

        # set up cache
        self.grid = grid
        self.memo = {}
        self.N = len(grid)

        return max(self.dp(0, 0, 0, 0), 0)

    def dp(self, i1, j1, i2, j2):
        # already stored: return
        if (i1, j1, i2, j2) in self.memo: return self.memo[(i1, j1, i2, j2)]

        # end states: 1. out of grid 2. at the right bottom corner 3. hit a thorn
        N = self.N
        if i1 == N or j1 == N or i2 == N or j2 == N: return -1
        if i1 == N-1 and j1 == N-1 and i2 == N-1 and j2 == N-1: return self.grid[-1][-1]
        if self.grid[i1][j1] == -1 or self.grid[i2][j2] == -1: return -1

        # now can take a step in two directions at each end, which amounts to 4 combinations in total
        dd = self.dp(i1+1, j1, i2+1, j2)
        dr = self.dp(i1+1, j1, i2, j2+1)
        if (i1,j1) != (i2,j2):
            rd = self.dp(i1, j1+1, i2+1, j2)
        else:
            rd = -1
        rr = self.dp(i1, j1+1, i2, j2+1)
        maxComb = max([dd, dr, rd, rr])

        # find if there is a way to reach the end
        if maxComb == -1:
            out = -1
        else:
            # same cell, can only count this cell once
            if i1 == i2 and j1 == j2:
                out = maxComb + self.grid[i1][j1]
            # different cell, can collect both
            else:
                out = maxComb + self.grid[i1][j1] + self.grid[i2][j2]

        # cache result
        self.memo[(i1, j1, i2, j2)] = out
        return out

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/cherry-pickup/solution/
Approach #1: Greedy [Wrong Answer]
Complexity Analysis
Time Complexity: O(N^2), where N is the length of grid.
Our dynamic programming consists of two for-loops of length N.
Space Complexity: O(N^2), the size of dp.



Approach #2: Dynamic Programming (Top Down) [Accepted]
Complexity Analysis
Time Complexity: O(N^3), where N is the length of grid. Our dynamic programming has O(N^3) states.
Space Complexity: O(N^3), the size of memo.

Algorithm

Let dp[r1][c1][c2] be the most number of cherries obtained by two people starting at (r1, c1)
and (r2, c2) and walking towards (N-1, N-1) picking up cherries, where r2 = r1+c1-c2.

If grid[r1][c1] and grid[r2][c2] are not thorns, then the value of dp[r1][c1][c2] is (grid[r1][c1] + grid[r2][c2]),
plus the maximum of dp[r1+1][c1][c2], dp[r1][c1+1][c2], dp[r1+1][c1][c2+1], dp[r1][c1+1][c2+1] as appropriate.
We should also be careful to not double count in case (r1, c1) == (r2, c2).

Why did we say it was the maximum of dp[r+1][c1][c2] etc.?
It corresponds to the 4 possibilities for person 1 and 2 moving down and right:

Person 1 down and person 2 down: dp[r1+1][c1][c2];
Person 1 right and person 2 down: dp[r1][c1+1][c2];
Person 1 down and person 2 right: dp[r1+1][c1][c2+1];
Person 1 right and person 2 right: dp[r1][c1+1][c2+1];

#22ms 85.36%
class Solution {
    int[][][] memo;
    int[][] grid;
    int N;
    public int cherryPickup(int[][] grid) {
        this.grid = grid;
        N = grid.length;
        memo = new int[N][N][N];
        for (int[][] layer: memo)
            for (int[] row: layer)
                Arrays.fill(row, Integer.MIN_VALUE);
        return Math.max(0, dp(0, 0, 0));
    }
    public int dp(int r1, int c1, int c2) {
        int r2 = r1 + c1 - c2;
        if (N == r1 || N == r2 || N == c1 || N == c2 ||
                grid[r1][c1] == -1 || grid[r2][c2] == -1) {
            return -999999;
        } else if (r1 == N-1 && c1 == N-1) {
            return grid[r1][c1];
        } else if (memo[r1][c1][c2] != Integer.MIN_VALUE) {
            return memo[r1][c1][c2];
        } else {
            int ans = grid[r1][c1];
            if (c1 != c2) ans += grid[r2][c2];
            ans += Math.max(Math.max(dp(r1, c1+1, c2+1), dp(r1+1, c1, c2+1)),
                            Math.max(dp(r1, c1+1, c2), dp(r1+1, c1, c2)));
            memo[r1][c1][c2] = ans;
            return ans;
        }
    }
}

Approach #3: Dynamic Programming (Bottom Up) [Accepted]
Complexity Analysis
Time Complexity: O(N^3), where N is the length of grid. We have three for-loops of size O(N).
Space Complexity: O(N^2), the sizes of dp and dp2.

# 21ms 89.64%
class Solution {
    public int cherryPickup(int[][] grid) {
        int N = grid.length;
        int[][] dp = new int[N][N];
        for (int[] row: dp) Arrays.fill(row, Integer.MIN_VALUE);
        dp[0][0] = grid[0][0];

        for (int t = 1; t <= 2*N - 2; ++t) {
            int[][] dp2 = new int[N][N];
            for (int[] row: dp2) Arrays.fill(row, Integer.MIN_VALUE);

            for (int i = Math.max(0, t-(N-1)); i <= Math.min(N-1, t); ++i) {
                for (int j = Math.max(0, t-(N-1)); j <= Math.min(N-1, t); ++j) {
                    if (grid[i][t-i] == -1 || grid[j][t-j] == -1) continue;
                    int val = grid[i][t-i];
                    if (i != j) val += grid[j][t-j];
                    for (int pi = i-1; pi <= i; ++pi)
                        for (int pj = j-1; pj <= j; ++pj)
                            if (pi >= 0 && pj >= 0)
                                dp2[i][j] = Math.max(dp2[i][j], dp[pi][pj] + val);
                }
            }
            dp = dp2;
        }
        return Math.max(0, dp[N-1][N-1]);
    }
}

#17ms 100%
class Solution {
    public int cherryPickup(int[][] grid) {
        int N = grid.length, M = (N << 1) - 1;
        int[][] dp = new int[N][N];
        dp[0][0] = grid[0][0];

        for (int n = 1; n < M; n++) {
            for (int i = N - 1; i >= 0; i--) {
                for (int p = N - 1; p >= 0; p--) {
                    int j = n - i, q = n - p;
                    if (j < 0 || j >= N || q < 0 || q >= N || grid[i][j] < 0 || grid[p][q] < 0) {
                        dp[i][p] = -1;
                        continue;
                    }

                    if (i > 0) dp[i][p] = Math.max(dp[i][p], dp[i - 1][p]);
                    if (p > 0) dp[i][p] = Math.max(dp[i][p], dp[i][p - 1]);
                    if (i > 0 && p > 0) dp[i][p] = Math.max(dp[i][p], dp[i - 1][p - 1]);

                    if (dp[i][p] >= 0)
                        dp[i][p] += grid[i][j] + (i != p ? grid[p][q] : 0);
                }
            }
        }
        return Math.max(dp[N - 1][N - 1], 0);
    }
}

#33ms 51.07%
class Solution {
    public int cherryPickup(int[][] grid) {
        int N = grid.length;
        int totalSteps = N * 2 - 1;
        // 两人同时出发，一个人的坐标是 i,j   另一个人坐标是 p,q
        // dp分别记录 i 和 p
        // 注意， 比如 dp[i][q - 1] 背后隐含了一层另外两个坐标， i j-1 q-1 p
        int[][] dp = new int[N][N];
        dp[0][0] = grid[0][0];

        for (int step = 1; step < totalSteps; step++) {
            // 就像背包问题，想重复利用更小的index的信息，就要从大到小。
            // 这样就不需要一个额外的dp2了。

            // 优化 i 和 p 的范围， 剪枝。 step - i <= N - 1
            int lower = Math.max(0, step - N + 1);
            for (int i = N - 1; i >= lower; i--) {
                for (int p = N - 1; p >= lower; p--) {
                    int j = step - i, q = step - p;
                    // out of bound, continue.
                    if (j < 0 || j >= N || q < 0 || q >= N || grid[i][j] < 0 || grid[p][q] < 0) {
                        dp[i][p] = -1;
                        continue;
                    }
                    if (i > 0) {
                        dp[i][p] = Math.max(dp[i - 1][p], dp[i][p]);
                    }
                    if (p > 0) {
                        dp[i][p] = Math.max(dp[i][p - 1], dp[i][p]);
                    }
                    if (i > 0 && p > 0) {
                        dp[i][p] = Math.max(dp[i][p], dp[i - 1][p - 1]);
                    }

                    if (dp[i][p] >= 0) {
                        dp[i][p] += grid[i][j];
                        if (i != p) {  // 如果两个人不在同一个位置
                            dp[i][p] += grid[p][q];
                        }
                    }
                }
            }
        }

        return dp[N - 1][N - 1] > 0 ? dp[N - 1][N - 1] : 0;
    }
}
'''