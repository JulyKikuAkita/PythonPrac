__source__ = 'https://leetcode.com/problems/delete-operation-for-two-strings/#/description'
# Time:  O(m * n)
# Space: O(n)
#
# Description: 583. Delete Operation for Two Strings
#
# Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same,
# where in each step you can delete one character in either string.
#
# Example 1:
# Input: "sea", "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
# Note:
# The length of given words won't exceed 500.
# Characters in given words can only be lower-case letters.
# Hide Company Tags Google
# Hide Tags String
# Hide Similar Problems (H) Edit Distance

import unittest

# Let dp(i, j) be the answer for strings A[i:] and B[j:]. Let's try to compute it by a top-down dp:
#
# When i == len(A) or j == len(B), one of the strings is empty, so the answer is just the sum of the remaining lengths.
# When A[i] == B[j], the answer is just dp(i+1, j+1). For example,
# when evaluating the distance between "acai" and "apple", we only need to look at the distance between "cai" and "pple".
# When A[i] != B[j], then they both cannot be in the final word,
# so we either delete A[i] or B[j]. Thus, our answer is 1 + min(dp(i+1, j), dp(i, j+1)).

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], dp[i][j] + (word1[i] == word2[j]))
        return m + n - 2 * dp[m][n]

    def minDistance1(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if i == len(word1) or j == len(word2):
                    ans = len(word1) + len(word2) - i - j
                elif word1[i] == word2[j]:
                    ans = dp(i+1, j+1)
                else:
                    ans = 1 + min(dp(i+1, j), dp(i, j+1))
                memo[i, j] = ans
            return memo[i, j]
        return dp(0, 0)

    #We could have also attempted a bottom-up DP, as shown below.
    # 236ms 67.50%
    def minDistanceBU(self, word1, word2):
        M, N = len(word1), len(word2)
        dp = [[0] * (N+1) for _ in xrange(M+1)]

        for i in xrange(M):
            dp[i][-1] = M-i
        for j in xrange(N):
            dp[-1][j] = N-j

        for i in xrange(M-1, -1, -1):
            for j in xrange(N-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1])
        return dp[0][0]


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/delete-operation-for-two-strings/solution/

To make them identical, just find the longest common subsequence.
The rest of the characters have to be deleted from the both the strings,
which does not belong to longest common subsequence.

# 25ms 88.93%
class Solution {
    public int minDistance(String word1, String word2) {
        int dp[][] = new int[word1.length()+1][word2.length()+1];
         for(int i = 0; i <= word1.length(); i++) {
             for(int j = 0; j <= word2.length(); j++) {
                 if(i == 0 || j == 0) dp[i][j] = 0;
                 else dp[i][j] = (word1.charAt(i-1) == word2.charAt(j-1)) ? dp[i-1][j-1] + 1 : Math.max(dp[i-1][j], dp[i][j-1]);
             }
         }
         int val =  dp[word1.length()][word2.length()];
         return word1.length() - val + word2.length() - val;
    }
}

# other thinking - find the longest common subsequence, same as Edit Distance

# 27ms 82.25%
class Solution {
    public int minDistance(String word1, String word2) {
        int len1 = word1.length(), len2 = word2.length();
        if (len1 == 0) return len2;
        if (len2 == 0) return len1;

        // dp[i][j] stands for distance of first i chars of word1 and first j chars of word2
        int[][] dp = new int[len1 + 1][len2 + 1];
        for (int i = 0; i <= len1; i++)
            dp[i][0] = i;
        for (int j = 0; j <= len2; j++)
            dp[0][j] = j;

        for (int i = 1; i <= len1; i++) {
            for (int j = 1; j <= len2; j++) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1))
                    dp[i][j] = dp[i - 1][j - 1];
                else
                    dp[i][j] = Math.min(Math.min(dp[i - 1][j - 1] + 2, dp[i - 1][j] + 1), dp[i][j - 1] + 1);
            }
        }
        return dp[len1][len2];
    }
}
'''