__author__ = 'July'
# Given a string s, find the longest palindromic subsequence's length in s.
# You may assume that the maximum length of s is 1000.
#
# Example 1:
# Input:
#
# "bbbab"
# Output:
# 4
# One possible longest palindromic subsequence is "bbbb".
# Example 2:
# Input:
#
# "cbbd"
# Output:
# 2
# One possible longest palindromic subsequence is "bb".
# Hide Company Tags Amazon Uber
# Hide Tags Dynamic Programming
# Hide Similar Problems (M) Longest Palindromic Substring
#
# Python DP O(n) space O(n^2) time
# Idea:
# dp[i][j] = longest palindrome subsequence of s[i to j].
# If s[i] == s[j], dp[i][j] = 2 + dp[i+1][j - 1]
# Else, dp[i][j] = max(dp[i+1][j], dp[i][j-1])
#
# Rolling array O(2n) space

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[1] * 2 for _ in range(n)]
        for j in xrange(1, len(s)):
            for i in reversed(xrange(0, j)):
                if s[i] == s[j]:
                    dp[i][j%2] = 2 + dp[i + 1][(j - 1)%2] if i + 1 <= j - 1 else 2
                else:
                    dp[i][j%2] = max(dp[i + 1][j%2], dp[i][(j - 1)%2])
        return dp[0][(n-1)%2]

#Further improve space to O(n)

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [1] * n
        for j in xrange(1, len(s)):
            pre = dp[j]
            for i in reversed(xrange(0, j)):
                tmp = dp[i]
                if s[i] == s[j]:
                    dp[i] = 2 + pre if i + 1 <= j - 1 else 2
                else:
                    dp[i] = max(dp[i + 1], dp[i])
                pre = tmp
        return dp[0]

java = '''
Straight forward Java DP solution
dp[i][j]: the longest palindromic subsequence's length of substring(i, j)
State transition:
dp[i][j] = dp[i+1][j-1] + 2 if s.charAt(i) == s.charAt(j)
otherwise, dp[i][j] = Math.max(dp[i+1][j], dp[i][j-1])
Initialization: dp[i][i] = 1

public class Solution {
    public int longestPalindromeSubseq(String s) {
        int[][] dp = new int[s.length()][s.length()];

        for (int i = s.length() - 1; i >= 0; i--) {
            dp[i][i] = 1;
            for (int j = i+1; j < s.length(); j++) {
                if (s.charAt(i) == s.charAt(j)) {
                    dp[i][j] = dp[i+1][j-1] + 2;
                } else {
                    dp[i][j] = Math.max(dp[i+1][j], dp[i][j-1]);
                }
            }
        }
        return dp[0][s.length()-1];
    }
}
Top bottom recursive method with memoization

public class Solution {
    public int longestPalindromeSubseq(String s) {
        return helper(s, 0, s.length() - 1, new Integer[s.length()][s.length()]);
    }

    private int helper(String s, int i, int j, Integer[][] memo) {
        if (memo[i][j] != null) {
            return memo[i][j];
        }
        if (i > j)      return 0;
        if (i == j)     return 1;

        if (s.charAt(i) == s.charAt(j)) {
            memo[i][j] = helper(s, i + 1, j - 1, memo) + 2;
        } else {
            memo[i][j] = Math.max(helper(s, i + 1, j, memo), helper(s, i, j - 1, memo));
        }
        return memo[i][j];
    }
}

1. O(n^2) brute force - OT
public class Solution {
    public int longestPalindromeSubseq(String s) {
        return helper(0, s.length()-1, s);
    }

    public int helper(int l, int r, String s) {
        if (l == r) return 1;
        if (l > r) return 0;
        if(s.charAt(l) == s.charAt(r)) {
            return 2 + helper(l+1, r-1, s);
        }else {
            return Math.max(helper(l+1, r, s), helper(l, r-1, s));
        }
    }
}

2. O(n^2) Memorization - OT
import javafx.util.Pair;
public class Solution {
    public int longestPalindromeSubseq(String s) {
        HashMap<Pair<Integer,Integer>, Integer> map = new HashMap<Pair<Integer,Integer>, Integer>();
        return helper(0, s.length()-1, s, map);
    }

    public int helper(int l, int r, String s, HashMap map) {
        if (l == r) return 1;
        if (l > r) return 0;
        Pair<Integer,Integer> p = new Pair<Integer,Integer>(l, r);
        if (map.containsKey(p)) {
            return (int)map.get(p);
        }
        int val;
        if(s.charAt(l) == s.charAt(r)) {
            val = 2 + helper(l+1, r-1, s, map);
        }else {
            val = Math.max(helper(l+1, r, s, map), helper(l, r-1, s, map));
        }
        map.put(p, val);
        return val;
    }
}

3. O(n^2) dp
public class Solution {
    public int longestPalindromeSubseq(String s) {
        int n = s.length();
        int[][] dp = new int[n + 1][n];
        for (int i = 0; i < n; i++) {
            dp[1][i] = 1;
        }
        for ( int i = 2 ; i <= n; i++) {
            for (int j = 0; j < n - i + 1; j++) {
                if (s.charAt(j) == s.charAt(i+j-1)) {
                    dp[i][j] = 2 + dp[i-2][j+1];
                } else {
                    dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j+1]);
                }

            }
        }
        return dp[n][0];
    }
}

'''