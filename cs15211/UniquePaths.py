__source__ = 'https://leetcode.com/problems/unique-paths/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/unique-paths.py
# Time:  O(m * n)
# Space: O(m + n)
# DP
#
# Description: Leetcode # 62. Unique Paths
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?
#
# Note: m and n will be at most 100.
# Companies
# Bloomberg
# Related Topics
# Array Dynamic Programming
# Similar Questions
# Unique Paths II Minimum Path Sum Dungeon Game
#
import unittest
class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        if m < n:
            return self.uniquePaths(n ,m)
        ways = [1] * n

        for i in xrange(1, m):
            for j in xrange(1, n):
                ways[j] += ways[j -1]
                print i, j ,ways
        return ways[n -1]

#Permutation/Combination solution is C (m+n-2, m-1)
# C(5,3) = 5!/(3! * 2!) = (5*4*3)/(3*2*1)
# P(5,3) = 5!/2! = 5*4*3

from operator import mul    # or mul=lambda x,y:x*y
from fractions import Fraction
class SolutionMATHcombintaion:
    # @return an integer
    def uniquePaths(self, m, n):
        return self.combination(m+n-2,n-1)

    def combination(self, n, k):
        mul=lambda x, y : x * y
        return int( reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1) )

    def permutation(self, n, k):

        return int(reduce(lambda x, y : x * y, range(n, n-k, -1), 1 ))

class SolutionLeetcode:
    # @return an integer
    def uniquePaths(self, m, n):
        dp = [[ 0 for j in xrange(n + 1)] for i in xrange(m + 1)]
        dp[m-1][n] = 1
        for i in reversed(xrange(m)):
            for j in reversed(xrange(n)):
                dp[i][j] = dp[i+1][j] + dp[i][j+1]
        return dp[0][0]

#ineffeicient (better with memoization)
class SolutionLeetcodeBackTrack:
    # @return an integer
    def uniquePaths(self, m, n):
        return self.backtrack(0,0,m,n)

    def backtrack(self, r, c, m ,n):
        if (r == m -1) and (c == n-1):
            return 1
        if r >= m or c >= n:
            return 0
        return self.backtrack(r+1, c, m, n) + self.backtrack(r, c+1, m ,n)

#ineffeicient (better with memoization)
class SolutionLeetcodeBackTrackMemoization:
    # @return an integer
    def uniquePaths(self, m, n):
        mat = [[-1 for j in xrange(n+1)] for i in xrange(m+1)]
        mat[m][n] = 0
        return self.backtrackM(0,0,m,n, mat)

    def backtrackM(self, r, c, m ,n, mat):
        if (r == m-1) and (c == n-1):
            return 1
        if r >= m or c >= n:
            return 0
        if mat[r+1][c] == -1:
            mat[r+1][c] = self.backtrackM(r+1, c, m ,n , mat)
        if mat[r][c+1] == -1:
            mat[r][c+1] = self.backtrackM(r, c+1, m ,n ,mat)
        return mat[r+1][c] + mat[r][c+1]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

        #print Fraction(10-4, 4+1)
        #print Solution().uniquePaths(5,1)
        #print Solution().uniquePaths(2,1)
        print SolutionMATHcombintaion().uniquePaths(5,3)
        print SolutionLeetcode().uniquePaths(5,3)
        print SolutionLeetcodeBackTrack().uniquePaths(5,3)
        print SolutionLeetcodeBackTrackMemoization().uniquePaths(5,3)

        for n in range(4):
            print '_'.join('%1d'%SolutionMATHcombintaion().combination(n,k) for k in range(n+1)).center(50)

        #print SolutionMATHcombintaion().permutation(5,3)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
This is a fundamental DP problem. First of all, let's make some observations.

Since the robot can only move right and down, when it arrives at a point, there are only two possibilities:

It arrives at that point from above (moving down to that point);
It arrives at that point from left (moving right to that point).
Thus, we have the following state equations:
suppose the number of paths to arrive at a point (i, j) is denoted as P[i][j],
it is easily concluded that P[i][j] = P[i - 1][j] + P[i][j - 1].

The boundary conditions of the above equation occur at the leftmost column (P[i][j - 1] does not exist)
and the uppermost row (P[i - 1][j] does not exist). These conditions can be handled by initialization
(pre-processing) --- initialize P[0][j] = 1, P[i][0] = 1 for all valid i, j. Note the initial value is 1 instead of 0!

# DP
# 79.18% 0ms
public class Solution {
    public int uniquePaths(int m, int n) {
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[j] += dp[j - 1];
            }
        }
        return dp[n - 1];
    }
}

# DP
# 5.28% 1ms
public class Solution {
    public int uniquePaths(int m, int n) {
        int[][] dp = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j <n ;j ++) {
                if (i ==0 | j== 0) dp[i][j] = 1;
                else dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        return dp[m-1][n-1];
    }
}

# dfs
# 5.28% 1ms
public class Solution {
    public int uniquePaths(int m, int n) {
        Integer[][]map = map = new Integer[m][n];
        return dfs(m - 1, n - 1, map);
    }

    private int dfs(int m, int n, Integer[][] map) {
        if (m == 0 || n == 0) return 1;
        if (map[m][n] != null) return map[m][n];
        int sum = dfs(m-1, n, map) + dfs(m, n-1, map);
        return map[m][n] = sum;
    }
}


# Math:
(m + n) ! / m! n1

public class Solution {
    public int uniquePaths(int m, int n) {
        if(m == 1 || n == 1)
            return 1;
        m--;
        n--;
        if(m < n) {              // Swap, so that m is the bigger number
            m = m + n;
            n = m - n;
            m = m - n;
        }
        long res = 1;
        int j = 1;
        for(int i = m+1; i <= m+n; i++, j++){       // Instead of taking factorial, keep on multiply & divide
            res *= i;
            res /= j;
        }

        return (int)res;
    }
}

'''