__source__ = 'https://leetcode.com/problems/count-different-palindromic-subsequences/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 730. Count Different Palindromic Subsequences
#
# Given a string S, find the number of different non-empty palindromic subsequences in S,
# and return that number modulo 10^9 + 7.
#
# A subsequence of a string S is obtained by deleting 0 or more characters from S.
#
# A sequence is palindromic if it is equal to the sequence reversed.
#
# Two sequences A_1, A_2, ... and B_1, B_2, ... are different if there is some i for which A_i != B_i.
#
# Example 1:
# Input:
# S = 'bccb'
# Output: 6
# Explanation:
# The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
# Note that 'bcb' is counted only once, even though it occurs twice.
# Example 2:
# Input:
# S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
# Output: 104860361
# Explanation:
# There are 3104860382 different non-empty palindromic subsequences, which is 104860361 modulo 10^9 + 7.
# Note:
#
# The length of S will be in the range [1, 1000].
# Each character S[i] will be in the set {'a', 'b', 'c', 'd'}.
#
import unittest

# 660ms 87.81%
class Solution(object):
    def countPalindromicSubsequences(self, S):
        """
        :type S: str
        :rtype: int
        """
        N = len(S)
        A = [ord(c) - ord('a') for c in S]
        prv = [None] * N
        nxt = [None] * N

        last = [None] * 4
        for i in xrange(N):
            last[A[i]] = i
            prv[i] = tuple(last)

        last = [None] * 4
        for i in xrange(N-1, -1, -1):
            last[A[i]] = i
            nxt[i] = tuple(last)

        MOD = 10**9 + 7
        memo = [[None] * N for _ in xrange(N)]
        def dp(i, j):
            if memo[i][j] is not None:
                return memo[i][j]
            ans = 1
            if i <= j:
                for x in xrange(4):
                    i0 = nxt[i][x]
                    j0 = prv[j][x]
                    if i <= i0 <= j:
                        ans += 1
                    if None < i0 < j0:
                        ans += dp(i0+1, j0-1)
            ans %= MOD
            memo[i][j] = ans
            return ans

        return dp(0, N-1) - 1

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/count-different-palindromic-subsequences/solution/
Approach #1 Dynamic Programming (using 3D array) [Accepted]
Complexity Analysis
Time complexity : O(N^2) where N is the length of the input string S. It takes quadratic time to fill up the DP table.
Space complexity : O(N^2) where N is the length of the input string S. The DP table takes quadratic space.

Let dp[x][i][j] be the answer for the substring S[i...j] where S[i] == S[j] == 'a'+x.
Note that since we only have 4 characters a, b, c, d, thus 0 <= x < 4. The DP formula goes as follows:

If S[i] != 'a'+x, then dp[x][i][j] = dp[x][i+1][j],
note that here we leave the first character S[i] in the window out due to our definition of dp[x][i][j].

If S[j] != 'a'+x, then dp[x][i][j] = dp[x][i][j-1],
leaving the last character S[j] out.

If S[i] == S[j] == 'a'+x, then dp[x][i][j] =
2 + dp[0][i+1][j-1] + dp[1][i+1][j-1] + dp[2][i+1][j-1] + dp[3][i+1][j-1].
When the first and last characters are the same,
we need to count all the distinct palindromes (for each of a,b,c,d)
within the sub-window S[i+1][j-1] plus the 2 palindromes contributed by the first and last characters.

Let n be the length of the input string S,
The final answer would be dp[0][0][n-1] + dp[1][0][n-1] + dp[2][0][n-1] + dp[3][0][n-1] mod 1000000007.

https://leetcode.com/problems/count-different-palindromic-subsequences/discuss/109514/c-on2-time-on-memory-with-explanation
If s[i] != x, then dp[len][i][x] = dp[len-1][i+1][x] (ignoring the first character in this window)
If s[i+len-1] != x then dp[len][i][x] = dp[len-1][i][x] (ignoring the last character in this window)
If both the first and last characters are x,
then we need to count the number of distinct palindromes in the sub-window from i+1 to i + len -2.
Need to be careful with how we count empty string.
Since we only need to subproblems of length len-1, len-2,
we only need to remember the solutions for the subproblems of length len, len-1, len-2.
This is needed to pass the max test case.

# 92ms 34%
class Solution {
    public int countPalindromicSubsequences(String S) {
        int n = S.length();
        int mod = 1000000007;
        int[][][] dp = new int[4][n][n];

        for (int i = n - 1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                for (int k = 0; k < 4; k++) {
                    char c = (char) ('a' + k);
                    if (j == i) {
                        if (S.charAt(i) == c) dp[k][i][j] = 1;
                        else dp[k][i][j] = 0;
                    } else {
                        // j > i
                        if (S.charAt(i) != c) dp[k][i][j] = dp[k][i+1][j];
                        else if (S.charAt(j) != c) dp[k][i][j] = dp[k][i][j-1];
                        else { // S[i] == S[j] == c
                            if (j == i + 1) dp[k][i][j] = 2; // "aa" : {"a", "aa"}
                            else { // length is > 2
                                dp[k][i][j] = 2;
                                for (int m = 0; m < 4; ++m) { // count each one within subwindows [i+1][j-1]
                                    dp[k][i][j] += dp[m][i+1][j-1];
                                    dp[k][i][j] %= mod;
                                }
                            }
                        }
                    }
                }
            }
        }
        int ans = 0;
        for (int k = 0; k < 4; ++k) {
          ans += dp[k][0][n-1];
          ans %= mod;
        }
        return ans;
    }
}


Approach #2: Dynamic Programming (using 2D array) [Accepted]
Complexity Analysis
Time Complexity: O(N^2, whereNN is the size of the string S.
Our calculation of prv and nxt happens in O(N) time, then our evaluation of dp with at most N^2
states is O(1)work per state.
Space Complexity: O(N^2), the size of memo.

# 52ms 82.25%
class Solution {
    int[][] memo, prv, nxt;
    byte[] A;
    int MOD = 1_000_000_007;

    public int countPalindromicSubsequences(String S) {
        int N = S.length();
        prv = new int[N][4];
        nxt = new int[N][4];
        memo = new int[N][N];
        for (int[] row: prv) Arrays.fill(row, -1);
        for (int[] row: nxt) Arrays.fill(row, -1);

        A = new byte[N];
        int ix = 0;
        for (char c: S.toCharArray()) {
            A[ix++] = (byte) ( c - 'a');
        }

        int[] last = new int[4];
        Arrays.fill(last, -1);
        for (int i = 0; i < N; i++) {
            last[A[i]] = i;
            for (int k = 0; k < 4; ++k)
                prv[i][k] = last[k];
        }

        Arrays.fill(last, -1);
        for (int i = N -1; i >= 0; i--) {
            last[A[i]] = i;
            for (int k = 0; k < 4; ++k)
                nxt[i][k] = last[k];
        }
        return dp(0, N-1) - 1;
    }

    private int dp(int i, int j) {
        if (memo[i][j] > 0) return memo[i][j];
        int ans = 1;
        if (i <= j) {
            for (int k = 0; k < 4; k++) {
                int i0 = nxt[i][k];
                int j0 = prv[j][k];
                if (i <= i0 && i0 <= j) ans++;
                if (-1 < i0 && i0 < j0) ans += dp(i0 + 1, j0 - 1);
                if (ans >= MOD) ans -= MOD;
            }
        }
        memo[i][j] = ans;
        return ans;
    }
}

# 25ms 97.25%
class Solution {
    public int countPalindromicSubsequences(String S) {
        int len = S.length(), m = (int) Math.pow(10, 9) + 7, ret = 0;
        char[] s = S.toCharArray();
        int[] dp = new int[len];

        for (int i = 0, sum = 0; i < len; i++) {
            for (int k = len - 1, interval = 0, preInterval = 1; k > i; k--) {
                if (s[k] == s[i]) {
                    int tmp = dp[k];
                    dp[k] = (interval + preInterval) % m;
                    preInterval = tmp;
                    interval = 0;
                } else {
                    interval += dp[k];
                    interval %= m;
                    sum += dp[k];
                    sum %= m;
                }
            }
            dp[i] = sum + 1;
            sum = 0;
        }

        for (int i = 0; i < len; i++) {
            ret += dp[i];
            ret %= m;
        }
        return ret;
    }
}

# 17ms 100%
class Solution {
    public int countPalindromicSubsequences(String S) {
        int mod = 1000000007;
        int n = S.length();
        char[] sChars = S.toCharArray();
        int[] counts = new int[n];

        for(int i = 0; i < n; i++) {
            char char1 = sChars[i] -= 'a';
            counts[i] = 1;
            long sum = 0;
            int[] tmp = new int[4];

            for(int j = i - 1; j >= 0; j--) {
                char char2 = sChars[j];
                int count = counts[j];
                if(char1 == char2) {
                    counts[j] = (int)((sum + 2) % mod);
                }
                sum += count - tmp[char2];
                tmp[char2] = count;
            }
        }

        int[] nums = new int[4];
        for(int i = n - 1; i >= 0; i--) {
            nums[sChars[i]] = counts[i];
        }

        long sum = 0;
        for(int cnt : nums) {
            sum += cnt;
        }

        return (int)(sum % mod);
    }
}

'''