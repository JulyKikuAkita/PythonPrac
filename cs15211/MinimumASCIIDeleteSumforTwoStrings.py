__source__ = 'https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/'
# Time:  O(m * n)
# Space: O(m * n)
#
# DP: dp[i][s2.length()] = dp[i+1][s2.length()] + s1.codePointAt(i).
#
# Description: Leetcode # 712. Minimum ASCII Delete Sum for Two Strings
#
# Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.
#
# Example 1:
# Input: s1 = "sea", s2 = "eat"
# Output: 231
# Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
# Deleting "t" from "eat" adds 116 to the sum.
# At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
# Example 2:
# Input: s1 = "delete", s2 = "leet"
# Output: 403
# Explanation: Deleting "dee" from "delete" to turn the string into "let",
# adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
# At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
# If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
# Note:
#
# 0 < s1.length, s2.length <= 1000.
# All elements of each string will have an ASCII value in [97, 122].
#

import unittest

#85.47% 464ms
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        dp = [[0] * (len(s2) + 1) for _ in xrange(len(s1) + 1)]

        for i in xrange(len(s1) -1, -1, -1):
            dp[i][len(s2)] = dp[i+1][len(s2)] + ord(s1[i])

        for j in xrange(len(s2) -1, -1, -1):
            dp[len(s1)][j] = dp[len(s1)][j+1] + ord(s2[j])

        for i in xrange(len(s1) -1, -1, -1):
            for j in xrange(len(s2) -1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j] + ord(s1[i]), dp[i][j+1] + ord(s2[j]))
        return dp[0][0]

# 380ms 91.45%
# total ascii sum - max(dp sum)
class Solution2(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        n1,n2 = len(s1), len(s2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in xrange(n1):
            for j in xrange(n2):
                if s1[i] == s2[j]:
                    dp[i+1][j+1] = dp[i][j] + 2 * ord(s1[i])
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

        ttl = 0
        for c in s1:
            ttl += ord(c)
        for c in s2:
            ttl += ord(c)
        return ttl - dp[n1][n2]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/solution/
# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/discuss/108811/JavaDP(With-Explanation)
#
# LC 72 Edit Distance and LC 524 Longest Word through Deleting share the same idea as this one.
#
# Complexity Analysis
# Time Complexity: O(M*N), where M,N are the lengths of the given strings.
# We use nested for loops: each loop is O(M) and O(N) respectively.
# Space Complexity: O(M*N), the space used by dp.
#
# 12ms 100%
# one dimension DP
#
class Solution {
    public int minimumDeleteSum(String s1, String s2) {
        int m = s1.length(), n = s2.length();
        char[] sa1 = s1.toCharArray();
        char[] sa2 = s2.toCharArray();
        int[] dp = new int[n+1];

        for (int j = 1; j <= n; j++) {
            dp[j] = dp[j - 1] + sa2[j-1];
        }

        for (int i = 1; i<= m; i++) {
            int t1 = dp[0];
            dp[0] += sa1[i-1];
            for (int j = 1; j <= n; j++) {
                int t2 = dp[j];
                if (sa1[i - 1] == sa2[j-1]) dp[j] = t1;
                else {
                    dp[j] = Math.min(dp[j] + sa1[i-1], dp[j-1] + sa2[j-1]);
                }
                t1 = t2;
            }
        }
        return dp[n];
    }
}

# 33ms 44.06%
class Solution {
    public int minimumDeleteSum(String s1, String s2) {
        int[][] dp = new int[s1.length() + 1][s2.length() + 1];

        for (int i = s1.length() - 1; i >= 0; i--) {
         dp[i][s2.length()] = dp[i + 1][s2.length()] + s1.codePointAt(i);
        }

        for (int j = s2.length() - 1; j >= 0; j--) {
            dp[s1.length()][j] = dp[s1.length()][j+1] + s2.codePointAt(j);
        }

        for (int i = s1.length() - 1; i >= 0; i--) {
            for (int j = s2.length() - 1; j >= 0; j--) {
                if (s1.charAt(i) == s2.charAt(j)) {
                    dp[i][j] = dp[i+1][j+1];
                } else {
                    dp[i][j] = Math.min(dp[i+1][j] + s1.codePointAt(i),
                                        dp[i][j+1] + s2.codePointAt(j));
                }
            }
        }
        return dp[0][0];
    }
}
'''