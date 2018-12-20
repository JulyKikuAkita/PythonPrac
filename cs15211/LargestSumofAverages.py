__source__ = 'https://leetcode.com/problems/largest-sum-of-averages/'
# Time:  O(K*N^2)
# Space: O(N)
#
# Description: Leetcode # 813. Largest Sum of Averages
#
# We partition a row of numbers A into at most K adjacent (non-empty) groups,
# then our score is the sum of the average of each group.
# What is the largest score we can achieve?
#
# Note that our partition must use every number in A,
# and that scores are not necessarily integers.
#
# Example:
# Input:
# A = [9,1,2,3,9]
# K = 3
# Output: 20
# Explanation:
# The best choice is to partition A into [9], [1, 2, 3], [9].
# The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
# We could have also partitioned A into [9, 1], [2], [3, 9], for example.
# That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.
#
# Note:
#
#     1 <= A.length <= 100.
#     1 <= A[i] <= 10000.
#     1 <= K <= A.length.
#     Answers within 10^-6 of the correct answer will be accepted as correct.
#
import unittest
# 21.85% 572ms
class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        P = [0]
        for x in A: P.append(P[-1] + x)
        def average(i, j):
            return (P[j] - P[i]) / float(j - i)

        N = len(A)
        dp = [average(i, N) for i in xrange(N)]
        for k in xrange(K-1):
            for i in xrange(N):
                for j in xrange(i+1, N):
                    dp[i] = max(dp[i], average(i, j) + dp[j])
        return dp[0]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/largest-sum-of-averages/solution/
#
Approach #1: Dynamic Programming [Accepted]
Complexity Analysis
Time Complexity: O(K*N^2), where N is the length of A.
Space Complexity: O(N), the size of dp.

dp(i, k) = max(average(i, N), max_{j > i}(average(i, j) + dp(j, k-1))).
We can calculate average a little bit faster by remembering prefix sums. 
If P[x+1] = A[0] + A[1] + ... + A[x], then average(i, j) = (P[j] - P[i]) / (j - i).

# 16ms 25.86%
class Solution {
    public double largestSumOfAverages(int[] A, int K) {
        int n = A.length;
        double[] P = new double[n + 1];
        for (int i = 0; i < n ; i++) {
            P[i + 1] = P[i] + A[i];
        }
        
        double[] dp = new double[n];
        for (int i = 0; i < n; i++) {
            dp[i] = (P[n] - P[i]) / ( n - i);
        }
        
        for (int k = 0; k < K - 1; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = i + 1; j < n; j++) {
                    dp[i] = Math.max(dp[i], (P[j]-P[i]) / (j-i) + dp[j]);
                }
            }
        }
        return dp[0];
    }
}

# Memorization
# 4ms 100%
class Solution {
    public double largestSumOfAverages(int[] A, int K) {
        int n = A.length;
    	int[] sums = new int[A.length + 1];
        for (int i = 1; i <= n; i++) {
            sums[i] = sums[i - 1] + A[i - 1];
        }
        return helper(A, K, 0, sums, new double[n][K + 1]);
    }
    
    private double helper(int[] A, int k, int start, int[] sums, double[][] dp) {
        if (k == 1) return (sums[A.length] - sums[start]) / (double) (A.length - start);
        if (dp[start][k] != 0) return dp[start][k];
        double sum = 0.0, res = 0;
        int length = 0;
        for (int i = start; i <= A.length - k; i++) {
            sum += A[i];
            length++;
            res = Math.max(res, helper(A, k - 1, start + length, sums, dp) + sum / length);
        }
        dp[start][k] = res;
        return res;
        
    }
}
'''
