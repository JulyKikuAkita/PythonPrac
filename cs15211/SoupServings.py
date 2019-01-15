__source__ = 'https://leetcode.com/problems/soup-servings/'
# Time:  O(N^2)
# Space: O(N^2)
#
# Description: Leetcode # 808. Soup Servings
#
# There are two types of soup: type A and type B.
# Initially we have N ml of each type of soup. There are four kinds of operations:
#
#     Serve 100 ml of soup A and 0 ml of soup B
#     Serve 75 ml of soup A and 25 ml of soup B
#     Serve 50 ml of soup A and 50 ml of soup B
#     Serve 25 ml of soup A and 75 ml of soup B
#
# When we serve some soup, we give it to someone and we no longer have it.
# Each turn, we will choose from the four operations with equal probability 0.25.
# If the remaining volume of soup is not enough to complete the operation,
# we will serve as much as we can.
# We stop once we no longer have some quantity of both types of soup.
#
# Note that we do not have the operation where all 100 ml's of soup B are used first.
#
# Return the probability that soup A will be empty first,
# plus half the probability that A and B become empty at the same time.
#
#
# Example:
# Input: N = 50
# Output: 0.625
# Explanation:
# If we choose the first two operations, A will become empty first. For the third operation,
# A and B will become empty at the same time. For the fourth operation, B will become empty first.
# So the total probability of A becoming empty first plus half the probability that
# A and B become empty at the same time, is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.
#
# Notes:
#
#     0 <= N <= 10^9.
#     Answers within 10^-6 of the true value will be accepted as correct.
#
import unittest
# 60ms 21.28%
class Solution(object):
    def soupServings(self, N):
        """
        :type N: int
        :rtype: float
        """
        Q, R = divmod(N, 25)
        N = Q + (R > 0)
        if N >= 500: return 1

        memo = {}
        def dp(x, y):
            if (x, y) not in memo:
                if x <= 0 or y <= 0:
                    ans = 0.5 if x<=0 and y<=0 else 1.0 if x<=0 else 0.0
                else:
                    ans = 0.25 * (dp(x-4,y)+dp(x-3,y-1)+dp(x-2,y-2)+dp(x-1,y-3))
                memo[x, y] = ans
            return memo[x, y]

        return dp(N, N)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/soup-servings/solution/
#
Note: The most important hint in this problem for me is 
"Answers within 10^-6 of the true value will be accepted as correct.".
And when I get timed out or runtime error with my DP, 
I tried to print out results of each call for each N.
They are monotonically increasing, and getting closer and closer to 1.
If you print it out, you will observe that when it is as large as 5551 
the gap between the result and 1 is less than 10^-6.

Approach #1: Dynamic Programming [Accepted]
Complexity Analysis
Time Complexity: O(1). (There exists a constant C such that the algorithm never performs more than C steps.)
Space Complexity: O(1) (There exists a constant C such that the algorithm never uses more than C space.)

# 7ms 56.04%
class Solution {
    public double soupServings(int N) {
        N = N / 25 + ( N % 25 > 0 ? 1: 0);
        if (N > 500) return 1.0;
        
        double[][] memo = new double[N + 1][N + 1];
        for (int s = 0; s <= 2 * N; s++) {
            for (int i = 0; i <= N; i++) {
                int j = s - i;
                if (j < 0 || j > N) continue;
                double ans = 0.0;
                if (i == 0) ans = 1.0;
                if (i == 0 && j == 0) ans = 0.5;
                if (i > 0 && j > 0) {
                    ans = 0.25 * (memo[M(i-4)][j] + memo[M(i-3)][M(j-1)] +
                                  memo[M(i-2)][M(j-2)] + memo[M(i-1)][M(j-3)]);
                }
                memo[i][j] = ans;
            }
        }
        return memo[N][N];
    }
    
    private int M(int x) {
        return Math.max(0, x);
    }
}


# DFS + pruning
# 7ms 56.04%
class Solution {
    public double soupServings(int N) {
        if (N > 5000) return 1.0; // see Note
        return helper(N, N, new Double[N + 1][N + 1]);
    }
    
    private double helper(int A, int B, Double[][] memo) {
        if (A <= 0 && B <= 0) return 0.5; // base case 1
        if (A <= 0) return 1.0; // base case 2
        if (B <= 0) return 0.0; // base case 3
        if (memo[A][B] != null) return memo[A][B];
        int[] serveA = {100, 75, 50, 25};
        int[] serveB = {0, 25, 50, 75};
        memo[A][B] = 0.0;
        for (int i = 0; i < 4; i++) {
            memo[A][B] += helper(A - serveA[i], B - serveB[i], memo);
        }
        return memo[A][B] *= 0.25;
    }
}

# 2ms 100%
class Solution {
    public double soupServings(int N) {
        int n = N;
        if (n >= 10000) {
            return 1; // because you have 75% cost A more than B.
        }
        if (n % 25 != 0) {
            n = n / 25 + 1;
        } else {
            n = n / 25;
        }
        int[][] options = new int[][]{{4, 0}, {3, 1}, {2, 2}, {1, 3}};
        return dfs(n, n, options, new Double[n + 1][n + 1]);
    }
    private double dfs(int soupA, int soupB, int[][]options, Double[][] mem) {
        if (soupA <= 0) {
            if (soupB > 0) {
                return 1;
            }
            if (soupB <= 0) {
                return 0.5;
            }
        }
        if (soupB <= 0) {
            return 0;
        }
        if (mem[soupA][soupB] != null) {
            return mem[soupA][soupB];
        }
        // 4 options
        double res = 0.0;
        for (int i = 0; i < options.length; i++) {
            int nextA = soupA - options[i][0];
            int nextB = soupB - options[i][1];
            res += 0.25 * dfs(nextA, nextB, options, mem);
        }
        mem[soupA][soupB] = res;
        return res;
    }
}
'''
