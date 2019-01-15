__source__ = 'https://leetcode.com/problems/strange-printer/'
# Time:  O(n^3)
# Space: O(n^2)
#
# Description: Leetcode # 664. Strange Printer
#
# There is a strange printer with the following two special requirements:
#
# The printer can only print a sequence of the same character each time.
# At each turn, the printer can print new characters starting from and ending at any places,
# and will cover the original existing characters.
# Given a string consists of lower English letters only,
# your job is to count the minimum number of turns the printer needed in order to print it.
#
# Example 1:
# Input: "aaabbb"
# Output: 2
# Explanation: Print "aaa" first and then print "bbb".
# Example 2:
# Input: "aba"
# Output: 2
# Explanation: Print "aaa" first and then print "b" from the second place of the string,
# which will cover the existing character 'a'.
# Hint: Length of the given string will not exceed 100.
#
# Companies
# NetEase
# Related Topics
# Dynamic Programming Depth-first Search
# Similar Questions
# Remove Boxes https://leetcode.com/problems/remove-boxes/description/
#
import unittest
# 1086 ms
class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        memo = {}
        def dp(i, j):
            if i > j: return 0
            if (i, j) not in memo:
                ans = dp(i+1, j) + 1
                for k in xrange(i+1, j+1):
                    if s[k] == s[i]:
                        ans = min(ans, dp(i, k-1) + dp(k+1, j))
                memo[i, j] = ans
            return memo[i, j]

        return dp(0, len(s) - 1)
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/strange-printer/solution/

# DP
# 19ms 89.56%
class Solution {
    public int strangePrinter(String s) {
       int n=s.length();
        if(n==0) return 0;
       int[][] dp=new int[n][n];
       for(int i=0;i<n;i++) dp[i][i]=1;


       for(int l=2;l<=n;l++){
           for(int i=0;i+l-1<n;i++){
              int j=i+l-1;
              dp[i][j]=dp[i][j-1]+1;

              for(int k=i;k<=j-1;k++){
                  if(s.charAt(j)==s.charAt(k)){
                      dp[i][j]=Math.min(dp[i][j],dp[i][k]+dp[k+1][j-1]);

                  }
              }
          }
       }
        return dp[0][n-1];
    }
}

# DFS
# 23ms 78.02%
class Solution {
     public int strangePrinter(String s) {
        if (s == null || s.length() <= 0) {
            return 0;
        }
        char c = (char) (s.charAt(0) - 1);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != c) {
                sb.append(s.charAt(i));
            }
            c = s.charAt(i);
        }
        return this.strangePrinter(sb.toString().toCharArray(), 0, sb.length() - 1, new int[sb.length()][sb.length()]);
    }

    public int strangePrinter(char[] cs, int left, int right, int[][] cache) {
        if (left < 0 || right >= cs.length || left > right) {
            return 0;
        } else if (cache[left][right] > 0) {
            return cache[left][right];
        } else if (left == right) {
            return 1;
        }

        int cnt = this.strangePrinter(cs, left, right - 1, cache) + 1;
        for (int i = right - 1; i >= left; i--) {
            if (cs[i] == cs[right]) {
                cnt = Integer.min(
                        cnt,
                        this.strangePrinter(cs, left, i, cache) + this.strangePrinter(cs, i + 1, right - 1, cache)
                );
            }
        }
        cache[left][right] = cnt;
        return cnt;
    }
}

'''
