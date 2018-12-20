__source__ = 'https://leetcode.com/problems/largest-plus-sign/'
# Time:  O(N^2) as the work we do under two nested for loops is O(1)O(1).
# Space: O(N^2) the size of dp[][]
# DP
#
# Description: Leetcode # 764. Largest Plus Sign
#
# In a 2D grid from (0, 0) to (N-1, N-1), every cell contains a 1,
# except those cells in the given list mines which are 0.
# What is the largest axis-aligned plus sign of 1s contained in the grid?
# Return the order of the plus sign. If there is none, return 0.
#
# An "axis-aligned plus sign of 1s of order k" has some center grid[x][y] = 1
# along with 4 arms of length k-1 going up, down, left, and right, and made of 1s.
# This is demonstrated in the diagrams below.
# Note that there could be 0s or 1s beyond the arms of the plus sign,
# only the relevant area of the plus sign is checked for 1s.
#
# Examples of Axis-Aligned Plus Signs of Order k:
#
# Order 1:
# 000
# 010
# 000
#
# Order 2:
# 00000
# 00100
# 01110
# 00100
# 00000
#
# Order 3:
# 0000000
# 0001000
# 0001000
# 0111110
# 0001000
# 0001000
# 0000000
# Example 1:
#
# Input: N = 5, mines = [[4, 2]]
# Output: 2
# Explanation:
# 11111
# 11111
# 11111
# 11111
# 11011
#
# In the above grid, the largest plus sign can only be order 2.  One of them is marked in bold.
# Example 2:
#
# Input: N = 2, mines = []
# Output: 1
# Explanation:
# There is no plus sign of order 2, but there is of order 1.
# Example 3:
#
# Input: N = 1, mines = [[0, 0]]
# Output: 0
# Explanation:
# There is no plus sign, so return 0.
# Note:
#
# N will be an integer in the range [1, 500].
# mines will have length at most 5000.
# mines[i] will be length 2 and consist of integers in the range [0, N-1].
# (Additionally, programs submitted in C, C++, or C# will be judged with a slightly smaller time limit.)
#
import unittest

# 81.19% 1584ms
class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        banned = {tuple(mine) for mine in mines}
        dp = [[0] * N for _ in xrange(N)]
        ans = 0

        for r in xrange(N):
            count = 0
            for c in xrange(N):
                count = 0 if (r,c) in banned else count + 1
                dp[r][c] = count

            count = 0
            for c in xrange(N-1, -1, -1):
                count = 0 if (r,c) in banned else count + 1
                if count < dp[r][c]:
                    dp[r][c] = count

        for c in xrange(N):
            count = 0
            for r in xrange(N):
                count = 0 if (r,c) in banned else count + 1
                if count < dp[r][c]:
                    dp[r][c] = count

            count = 0
            for r in xrange(N-1, -1, -1):
                count = 0 if (r,c) in banned else count + 1
                if count < dp[r][c]:
                    dp[r][c] = count
                if dp[r][c] > ans:
                    ans = dp[r][c]
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/largest-plus-sign/solution/
#
# Brute force TLE
class Solution {
    public int orderOfLargestPlusSign(int N, int[][] mines) {
         Set<Integer> set = new HashSet();
        for (int[] mine : mines) set.add(mine[0] * N + mine[1]);
        int ans = 0;
        for (int r = 0; r < N; ++r) {
            for (int c = 0; c < N; ++c) {
                int k = 0;
                while (k <= r && r < N - k && k <= c && c < N-k
                       && !set.contains((r - k) * N + c)
                       && !set.contains((r + k) * N + c)
                       && !set.contains(r * N + c - k)
                       && !set.contains(r * N + c + k))
                      k++;
                ans = Math.max(ans, k);
            }
        }
        return ans;
    }
}

Complexity Analysis
Time Complexity: O(N^2), as the work we do under two nested for loops is O(1)O(1).
Space Complexity: O(N^2), the size of dp.

# 80.42% 96ms
class Solution {
    public int orderOfLargestPlusSign(int N, int[][] mines) {
        int[][] grid = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                grid[i][j] = N;
            }
        }
        for (int[] mine: mines) grid[mine[0]][mine[1]] = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0, l = 0, r = 0, u = 0, d = 0, k = N -1; j < N; j++, k--) {
                grid[i][j] = Math.min(grid[i][j], grid[i][j] == 0 ? (l = 0) : (l = l + 1));
                grid[i][k] = Math.min(grid[i][k], grid[i][k] == 0 ? (r = 0) : (r = r + 1));
                grid[j][i] = Math.min(grid[j][i], grid[j][i] == 0 ? (u = 0) : (u = u + 1));
                grid[k][i] = Math.min(grid[k][i], grid[k][i] == 0 ? (d = 0) : (d = d + 1));
            }
        }
        int ret = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                ret = Math.max(ret, grid[i][j]);
            }
        }
        return ret;
    }
}


'''
