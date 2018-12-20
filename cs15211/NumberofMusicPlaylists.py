__source__ = 'https://leetcode.com/problems/number-of-music-playlists/'
# Time:  O()
# Space: O()
# DP
#
# Description: Leetcode # 920. Number of Music Playlists
#
# # our music player contains N different songs
# and she wants to listen to L (not necessarily different) songs during your trip.
# You create a playlist so that:
#
# Every song is played at least once
# A song can only be played again only if K other songs have been played
# Return the number of possible playlists.  As the answer can be very large,
# return it modulo 10^9 + 7.
#
# Example 1:
#
# Input: N = 3, L = 3, K = 1
# Output: 6
# Explanation: There are 6 possible playlists. [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1].
# Example 2:
#
# Input: N = 2, L = 3, K = 0
# Output: 6
# Explanation: There are 6 possible playlists. [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2], [1, 2, 2]
# Example 3:
#
# Input: N = 2, L = 3, K = 1
# Output: 2
# Explanation: There are 2 possible playlists. [1, 2, 1], [2, 1, 2]
#
# Note:
#
# 0 <= K < N <= L <= 100
#
import unittest

# 20ms 100%
class Solution(object):
    def numMusicPlaylists(self, N, L, K):
        """
        :type N: int
        :type L: int
        :type K: int
        :rtype: int
        """
        # dp[S] at time P = <S, P> as discussed in article
        dp = [1] * (L-N+1)
        for p in xrange(2, N-K+1):
            for i in xrange(1, L-N+1):
                dp[i] += dp[i-1] * p

        # Multiply by N!
        ans = dp[-1]
        for k in xrange(2, N+1):
            ans *= k
        return ans % (10**9 + 7)

# 20ms 100%
class Solution2(object):
    def numMusicPlaylists(self, N, L, K):
        """
        :type N: int
        :type L: int
        :type K: int
        :rtype: int
        """
        MOD = 10**9 + 7
        def inv(x):
            return pow(x, MOD-2, MOD)

        C = 1
        for x in xrange(1, N-K):
            C *= -x
            C %= MOD
        C = inv(C)

        ans = 0
        for k in xrange(1, N-K+1):
            ans += pow(k, L-K-1, MOD) * C
            C = C * (k - (N-K)) % MOD * inv(k) % MOD

        for k in xrange(1, N+1):
            ans = ans * k % MOD
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/number-of-music-playlists/solution/
#
Approach 1: Dynamic Programming
Complexity Analysis
Time Complexity: O(NL)
Space Complexity: O(NL)
(However, we can adapt this algorithm to only store the last row of dp to easily get O(L) space complexity.)

# 17ms 18.69%
class Solution {
    public int numMusicPlaylists(int N, int L, int K) {
        int MOD = 1_000_000_007;

        long[][] dp = new long[L+1][N+1];
        dp[0][0] = 1;
        for (int i = 1; i <= L; i++) {
            for(int j = 1; j <= N; j++) {
                dp[i][j] += dp[i-1][j-1] * (N - j + 1);
                dp[i][j] += dp[i-1][j] * Math.max(j - K, 0);
                dp[i][j] %= MOD;
            }
        }
        return (int) dp[L][N];
    }
}

Approach 2: Partitions + Dynamic Programming
Complexity Analysis
Time Complexity: O(NL)
Space Complexity: O(L)

# 4ms 99.86%
class Solution {
    public int numMusicPlaylists(int N, int L, int K) {
        int MOD = 1_000_000_007;

        // dp[S] at time P = <S, P> as discussed in article
        long[] dp = new long[L-N+1];
        Arrays.fill(dp, 1);
        for (int p = 2; p <= N-K; ++p)
            for (int i = 1; i <= L-N; ++i) {
                dp[i] += dp[i-1] * p;
                dp[i] %= MOD;
            }

        // Multiply by N!
        long ans = dp[L-N];
        for (int k = 2; k <= N; ++k)
            ans = ans * k % MOD;
        return (int) ans;
    }
}

Approach 3: Generating Functions
Complexity Analysis
Time Complexity: O(NlogL).
Space Complexity: O(1).
#only availble in python code
'''
