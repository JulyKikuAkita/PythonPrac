__source__ = 'https://leetcode.com/problems/new-21-game/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 837. New 21 Game
#
# Alice plays the following game, loosely based on the card game "21".
#
# Alice starts with 0 points, and draws numbers while she has less than K points.
# During each draw, she gains an integer number of points randomly from the range [1, W], where W is an integer.
# Each draw is independent and the outcomes have equal probabilities.
#
# Alice stops drawing numbers when she gets K or more points.
# What is the probability that she has N or less points?
#
# Example 1:
#
# Input: N = 10, K = 1, W = 10
# Output: 1.00000
# Explanation:  Alice gets a single card, then stops.
# Example 2:
#
# Input: N = 6, K = 1, W = 10
# Output: 0.60000
# Explanation:  Alice gets a single card, then stops.
# In 6 out of W = 10 possibilities, she is at or below N = 6 points.
# Example 3:
#
# Input: N = 21, K = 17, W = 10
# Output: 0.73278
# Note:
#
# 0 <= K <= N <= 10000
# 1 <= W <= 10000
# Answers will be accepted as correct if they are within 10^-5 of the correct answer.
# The judging time limit has been reduced for this question.
#
import unittest

class Solution(object):
    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        dp = [0.0] * (N + W + 1)
        # dp[x] = the answer when Alice has x points
        for k in xrange(K, N + 1):
            dp[k] = 1.0

        S = min(N - K + 1, W)
        # S = dp[k+1] + dp[k+2] + ... + dp[k+W]
        for k in xrange(K - 1, -1 , -1):
            dp[k] = S / float(W)
            S += dp[k] - dp[k + W]
        return dp[0]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/new-21-game/solution/
# DP
Complexity Analysis
Time and Space Complexity: O(N + W)
Note that we can reduce the time complexity to O(max(K,W))
and the space complexity to O(W) by only keeping track of the last W values of dp, but it isn't required.

#13ms 66.74%

class Solution {
    public double new21Game(int N, int K, int W) {
        double[] dp = new double[N + W + 1];
        // dp[x] = the answer when Alice has x points
        for (int k = K; k <= N; ++k)
            dp[k] = 1.0;

        double S = Math.min(N - K + 1, W);
        // S = dp[k+1] + dp[k+2] + ... + dp[k+W]
        for (int k = K - 1; k >= 0; --k) {
            dp[k] = S / W;
            S += dp[k] - dp[k + W];
        }
        return dp[0];
    }
}
'''