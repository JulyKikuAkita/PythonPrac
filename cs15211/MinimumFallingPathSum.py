__source__ = 'https://leetcode.com/problems/minimum-falling-path-sum/'
# Time:  O()
# Space: O()
# DP
#
# Description: Leetcode # 931. Minimum Falling Path Sum
#
# Given a square array of integers A, we want the minimum sum of a falling path through A.
#
# A falling path starts at any element in the first row, and chooses one element from each row.
# The next row's choice must be in a column that is different from the previous row's column by at most one.
#
# Example 1:
#
# Input: [[1,2,3],[4,5,6],[7,8,9]]
# Output: 12
# Explanation:
# The possible falling paths are:
# [1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
# [2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
# [3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
# The falling path with the smallest sum is [1,4,7], so the answer is 12.
#
# Note:
#
# 1 <= A.length == A[0].length <= 100
# -100 <= A[i][j] <= 100
#
import unittest

# 44ms 72.71%
class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        while len(A) >= 2:
            row = A.pop()
            for i in xrange(len(row)):
                A[-1][i] += min(row[max(0,i-1): min(len(row), i+2)])
        return min(A[0])

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/minimum-falling-path-sum/solution/
Approach 1: Dynamic Programming
dp(r, c) = A[r][c] + min(dp(r+1, c-1), dp(r+1, c), dp(r+1, c+1))

Complexity Analysis
Time Complexity: O(N^2), where N is the length of A.
Space Complexity: O(1) in additional space complexity.

# 5ms 96.77%
class Solution {
    public int minFallingPathSum(int[][] A) {
        int N = A.length;
        for (int r = N - 2; r >= 0; r--) {
            for (int c = 0; c < N; c++) {
                // best = min(A[r+1][c-1], A[r+1][c], A[r+1][c+1])
                int best = A[r + 1][c];
                if ( c > 0) {
                    best = Math.min(best, A[r + 1][c - 1]);
                }

                if ( c + 1 < N) {
                    best = Math.min(best, A[r + 1][c + 1]);
                }
                A[r][c] += best;
            }
        }
        int ans = Integer.MAX_VALUE;
        for (int x : A[0]) ans = Math.min(ans, x);
        return ans;
    }
}

# 3ms 100%
class Solution {
    public int minFallingPathSum(int[][] A) {
        int m = A.length;
        int n = A[0].length;
        int[][] dp = new int[m][n];
        for (int i = 0; i < m; i++)
            Arrays.fill(dp[i], Integer.MIN_VALUE);
        int res = Integer.MAX_VALUE;
        for (int j = 0; j < n ; j++) {
            res = Math.min(res, helper(0, j , A , dp));
        }
        return res;
    }

    private int helper(int x, int y, int[][] A, int[][] dp) {
        if (x == A.length) return 0;
        if (dp[x][y] != Integer.MIN_VALUE) return dp[x][y];
        int res = A[x][y] + helper(x + 1, y, A, dp);
        if (y - 1 >= 0) {
            res = Math.min(res, A[x][y] + helper(x + 1, y - 1, A, dp));
        }
        if (y + 1 < A[0].length) {
            res = Math.min(res, A[x][y] + helper(x + 1, y + 1, A, dp));
        }
        dp[x][y] = res;
        return res;
    }
}
'''
