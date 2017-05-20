__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/distinct-subsequences.py
# Time:  O(n^2)
# Space: O(n)
# DP
# still ??
#
# Given a string S and a string T, count the number of distinct subsequences of T in S.
#
# A subsequence of a string is a new string which is formed from the original string
# by deleting some (can be none) of the characters without disturbing the relative positions
# of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
#
# Here is an example:
# S = "rabbbit", T = "rabbit"
#
# Return 3.
#


class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        ways = [0 for _ in xrange(len(T) + 1)]
        ways[0] = 1
        for S_char in S:
            for j, T_char in reversed(list(enumerate(T))):  # why need to go reversed?
                                                            # consider s = ddd, t = dd, if not reversed, ans = 6 (x)
                                                            # if reversed, ans = 3 (o)
                if S_char == T_char:
                    ways[j + 1] += ways[j]
        return ways[len(T)]

'''
When you see string problem that is about subsequence or matching,
dynamic programming method should come to your mind naturally. The key is to find the changing condition.
'''
# http://www.programcreek.com/2013/01/leetcode-distinct-subsequences-total-java/
class Solution2:
    # @return an integer
    #dp. still no understand
    def numDistinct(self, S, T):
        dp = [[0 for i in range(len(T)+1)] for j in range(len(S)+1)]
        for j in range(len(S)+1):
            dp[j][0] = 1
        for i in range(1, len(S)+1):
            for j in range(1, min(i+1, len(T)+1)):
                if S[i-1] == T[j-1]:
                    dp[i][j] = dp [i-1][j] + dp[i-1][j-1]
                else:
                    dp[i][j] =dp[i-1][j]

        for i in xrange(len(dp)):
            print dp[i]

        return dp[len(S)][len(T)]

#TEST
test = Solution2()
#print test.numDistinct("ABB", "AB")
#print test.numDistinct("ABCDE", "ACE")
#print test.numDistinct("rabbbit", "rabbit")

if __name__ == "__main__":
    S = "rabbbit"
    T = "rabbit"
    #result1 = Solution().numDistinct(S, T)
    result2 = Solution2().numDistinct("ABB", "AB")
    print result2

#java
js = '''

public class Solution {
    public int numDistinct(String s, String t) {
        int lenS = s.length();
        int lenT = t.length();
        if (lenS < lenT) {
            return 0;
        }
        int[] dp = new int[lenT + 1];
        dp[0] = 1;
        for (int i = 0; i < lenS; i++) {
            for (int j = Math.min(i, lenT - 1); j >= 0; j--) {
                if (s.charAt(i) == t.charAt(j)) {
                    dp[j + 1] += dp[j];
                }
            }
        }
        return dp[lenT];
    }
}
'''