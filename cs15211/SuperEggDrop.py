# coding=utf-8
__source__ = 'https://leetcode.com/problems/super-egg-drop/'
# Time:  O(KlongN)
# Space: O(NK)
# DP
# dp(K,N)= min(max(dp(K−1,X−1),dp(K,N−X))))
# 1≤X≤N
#
# Description: Leetcode # 887. Super Egg Drop
#
# You are given K eggs, and you have access to a building with N floors from 1 to N.
#
# Each egg is identical in function, and if an egg breaks, you cannot drop it again.
#
# You know that there exists a floor F with 0 <= F <= N such that any egg dropped at a floor higher than F will break,
# and any egg dropped at or below floor F will not break.
#
# Each move, you may take an egg (if you have an unbroken one) and drop it from any floor X (with 1 <= X <= N).
#
# Your goal is to know with certainty what the value of F is.
#
# What is the minimum number of moves that you need to know with certainty what F is,
# regardless of the initial value of F?
#
#
# Example 1:
#
# Input: K = 1, N = 2
# Output: 2
# Explanation:
# Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
# Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty that F = 1.
# If it didn't break, then we know with certainty F = 2.
# Hence, we needed 2 moves in the worst case to know what F is with certainty.
# Example 2:
#
# Input: K = 2, N = 6
# Output: 3
# Example 3:
#
# Input: K = 3, N = 14
# Output: 4
#
#
# Note:
#
# 1 <= K <= 100
# 1 <= N <= 10000
#
import unittest

# 20ms 100%
class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        # O(K) memory, O(KlogN) computation
        dp = [1] * (K+1)
        dp[0] = 0
        steps = 1
        while dp[K] < N:
            for j in range(K, 0, -1):
                dp[j] += dp[j-1] + 1
            steps += 1
        return steps

        # dp = {(1, i) : 1 for i in range(1, K+1)}
        # dp[(1, 0)] = 0
        # j = 1
        # while dp[(j, K)] < N:
        #     j += 1
        #     dp[(j, 0)] = 0
        #     for i in range(1, K+1):
        #         dp[(j, i)] = dp[(j-1, i-1)] + dp[(j-1, i)] + 1
        # print dp
        # return j

# 20ms 100%
class SolutionBinominal(object):
    def superEggDrop(self, K, N):
        def f(x):
            ans = 0
            r = 1
            for i in range(1, K+1):
                r *= x-i+1
                r //= i
                ans += r
                if ans >= N: break
            return ans

        lo, hi = 1, N
        while lo < hi:
            mi = (lo + hi) // 2
            if f(mi) < N:
                lo = mi + 1
            else:
                hi = mi
        return lo

# 2200 ms 11.11%
class SolutionBottomUpDP(object):
    def superEggDrop(self, K, N):

        # Right now, dp[i] represents dp(1, i)
        dp = range(N+1)

        for k in xrange(2, K+1):
            # Now, we will develop dp2[i] = dp(k, i)
            dp2 = [0]
            x = 1
            for n in xrange(1, N+1):
                # Let's find dp2[n] = dp(k, n)
                # Increase our optimal x while we can make our answer better.
                # Notice max(dp[x-1], dp2[n-x]) > max(dp[x], dp2[n-x-1])
                # is simply max(T1(x-1), T2(x-1)) > max(T1(x), T2(x)).
                while x < n and max(dp[x-1], dp2[n-x]) > \
                                max(dp[x], dp2[n-x-1]):
                    x += 1

                # The final answer happens at this x.
                dp2.append(1 + max(dp[x-1], dp2[n-x]))

            dp = dp2

        return dp[-1]
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/super-egg-drop/solution/

# Approach 1: Dynamic Programming with Binary Search
Complexity Analysis
Time Complexity: O(K *NlogN)
Space Complexity: O(K * N)

# 152ms 12.44%
class Solution { //K eggs, N floors
    Map<Integer, Integer> memo = new HashMap();
    public int superEggDrop(int K, int N) {
        return dp(K, N);
    }

    private int dp(int K, int N) {
        if (!memo.containsKey(N * 100 + K)) {
            int ans;
            if (N == 0) ans = 0;
            else if (K == 1) ans = N;
            else {
                int lo = 1, hi = N;
                while (lo + 1 < hi) {
                    int x = (lo + hi) / 2;
                    int t1 = dp(K - 1, x - 1);
                    int t2 = dp(K, N - x);

                    if (t1 < t2) lo = x;
                    else if (t1 > t2) hi = x;
                    else lo = hi = x;
                }
                ans = 1 + Math.min(Math.max(dp(K - 1, lo - 1), dp(K, N-lo)),
                                   Math.max(dp(K - 1, hi - 1), dp(K, N - hi)));
            }
            memo.put(N * 100 + K, ans);
        }
        return memo.get(N * 100 + K);
    }
}


# Approach 2: Dynamic Programming with Optimality Criterion (bottom-up)
#
# Complexity Analysis
# Time Complexity: O(K * N).
# Space Complexity: O(N).

# 26ms 34.45%
class Solution {
    public int superEggDrop(int K, int N) {
        // Right now, dp[i] represents dp(1, i)
        int[] dp = new int[N+1];
        for (int i = 0; i <= N; ++i) dp[i] = i;

        for (int k = 2; k <= K; ++k) {
            // Now, we will develop dp2[i] = dp(k, i)
            int[] dp2 = new int[N + 1];
            int x = 1;
            for (int n = 1; n <= N; ++n) {
                // Let's find dp2[n] = dp(k, n)
                // Increase our optimal x while we can make our answer better.
                // Notice max(dp[x-1], dp2[n-x]) > max(dp[x], dp2[n-x-1])
                // is simply max(T1(x-1), T2(x-1)) > max(T1(x), T2(x)).
                while (x < n && Math.max(dp[x - 1], dp2[n - x]) > Math.max(dp[x], dp2[n-x-1])) x++;
                // The final answer happens at this x.
                dp2[n] = 1 + Math.max(dp[x-1], dp2[n-x]);
            }
            dp = dp2;
        }
        return dp[N];
    }
}

Approach 3: Mathematical

# 4ms 100%
class Solution {
    public int superEggDrop(int K, int N) {
        int lo = 1, hi = N;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (f(mid, K, N) < N) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }

    private int f(int x, int K, int N) {
        int ans = 0, r = 1;
        for (int i = 1; i <= K; i++) {
            r *= x - i + 1;
            r /= i;
            ans += r;
            if (ans > N) break;
        }
        return ans;
    }
}

# DP:
https://leetcode.com/problems/super-egg-drop/discuss/158974/C%2B%2BJavaPython-2D-and-1D-DP-O(KlogN)
# Drop eggs is a very classical problem.
# Some people may come up with idea O(KN^2)
# where dp[K][N] = 1 + max(dp[K - 1][i - 1],dp[K][N - i]) for i in 1...N.
# However this idea is very brute force, for the reason that you check all possiblity.
#
# So I consider this problem in a different way:
# dp[M][K]means that, given K eggs and M moves,
# what is the maximum number of floor that we can check.
#
# The dp equation is:
# dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1,
# which means we take 1 move to a floor,
# if egg breaks, then we can check dp[m - 1][k - 1] floors.
# if egg doesn't breaks, then we can check dp[m - 1][k - 1] floors.
#
# dp[m][k] is similar to the number of combinations and it increase exponentially to N
#
# Time Complexity:
# O(KlogN) Time, O(NK) Space

# think of example 3, with binary search, split at 7th fl,
# it then become 2 sub questions, the lower level one is example 2
# example 2 split at mid, third fl, and it become part of example 1
class Solution {
    // 2-d DP
    # 8ms 75.45%
    public int superEggDrop(int K, int N) {
        int[][] floors = new int[K + 1][N + 1];
        for (int j = 1; j < N + 1; j++) {
            for (int i = 1; i < K + 1; i++) {
                floors[i][j] = floors[i-1][j-1] + floors[i][j-1] + 1;
                if (floors[i][j] >= N) return j;
            }
        }
        return N;
    }

    //100% - 1d dp: Dynamic Program
    # 5ms 86.63%
    public int superEggDrop(int K, int N) {
        int[] floors = new int[K+1];

        int moves = 0;
        while ( floors[K] < N ){
            moves++;
            for ( int i = K; i >= 1; i--){
                floors[i] = floors[i] + floors[i-1] + 1; //example 3 = example2 + 1
            }
        }
        return moves;
    }

}

'''
