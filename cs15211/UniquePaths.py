__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/unique-paths.py
# Time:  O(m * n)
# Space: O(m + n)
# DP
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?
#
# Note: m and n will be at most 100.
#

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


#test
if __name__ == '__main__':
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

#java
js = '''
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

public class Solution {
    public int uniquePaths(int m, int n) {
        int[][] dp = new int[m+1][n+1];
        for(int[] row: dp)
            Arrays.fill(row, -1);
        dp[0][0] = 1;
        return dfs(0,0,m,n,dp);
    }

    private int dfs(int r, int c, int m, int n, int[][] dp){
        if( r == m-1 || c == n - 1) return 1;
        if( r >= m || c >= n) return 0;
        if(dp[r+1][c] == -1 ) dp[r+1][c] = dfs(r+1, c, m, n, dp);
        if(dp[r][c+1] == -1 ) dp[r][c+1] = dfs(r, c + 1, m, n, dp);
        return dp[r+1][c] + dp[r][c+1];

    }
}
'''