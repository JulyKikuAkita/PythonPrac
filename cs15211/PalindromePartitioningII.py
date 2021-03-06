__source__ = 'https://leetcode.com/problems/palindrome-partitioning-ii/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/palindrome-partitioning-ii.py
# Time:  O(n^2)
# Space: O(n^2)
# DP
#
# Description: Leetcode # 132. Palindrome Partitioning II
#
# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return the minimum cuts needed for a palindrome partitioning of s.
#
# For example, given s = "aab",
# Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
#
# Related Topics
# Dynamic Programming
# Similar Questions
# Palindrome Partitioning
#
import unittest
class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        lookup = [[False for j in xrange(len(s))] for i in xrange(len(s))]
        mincut = [len(s) - 1 - i for i in xrange(len(s) + 1)]
        print mincut
        for i in reversed(xrange(len(s))):
            for j in xrange(i, len(s)):
                if s[i] == s[j] and (j - i < 2 or lookup[i + 1][j - 1]):
                    lookup[i][j] = True
                    mincut[i] = min(mincut[i], mincut[j + 1] + 1)
                #print i, j, lookup, mincut

        return mincut[0]

# http://www.programcreek.com/2014/04/leetcode-palindrome-partitioning-ii-java/
class SolutionJava:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        lookup = [[False for j in xrange(len(s))] for i in xrange(len(s))]
        mincut = [i for i in xrange(len(s) + 1)] # set maximum # of cut
        print mincut

        for j in (xrange(len(s))):
            for i in xrange(j + 1):
                if s[i] == s[j] and (j - i < 2 or lookup[i + 1][j - 1]):
                    lookup[i][j] = True
                    if i > 0: # if need to cut, add 1 to the previous cut[i-1]
                        mincut[j] = min(mincut[j], mincut[i - 1] + 1)
                    else:
                        mincut[j] = 0  # if [0...j] is palindrome, no need to cut
        return mincut[j]

class SolutionOther:
    # @param s, a string
    # @return an integer
    #http://www.cnblogs.com/zuoyuan/p/3758783.html
    def minCut(self, s):
        dp = [ 0 for i in range(len(s)+ 1)]
        p = [[False for i in range(len(s))] for j in range(len(s))]

        #print dp, p

        for i in range(len(s)+1):
            dp[i] = len(s) - i
        #print dp
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (((j-i) < 2 ) or p[i+1][j-1]):
                    p[i][j] = True
                    dp[i] = min(1+dp[j+1], dp[i])
        #            print i, j, p, dp
        return dp[0]-1

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        #print Solution().partition("aab")
        #print DP().partition("aab")
        print Solution().minCut("aab")
        print SolutionJava().minCut("aab")

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

Easiest Java DP Solution (97.36%)
This can be solved by two points:

cut[i] is the minimum of cut[j - 1] + 1 (j <= i), if [j, i] is palindrome.
If [j, i] is palindrome, [j + 1, i - 1] is palindrome, and c[j] == c[i].
The 2nd point reminds us of using dp (caching).

a   b   a   |   c  c
                j  i
       j-1  |  [j, i] is palindrome
   cut(j-1) +  1
Hope it helps!

# 9ms 79.58%
class Solution {
    public int minCut(String s) {
        char[] c = s.toCharArray();
        int[] cut = new int[c.length];
        boolean[][] dp = new boolean[c.length][c.length];

        for (int i = 0; i < c.length ;i++) {
            int min = i;
            for (int j = 0; j <= i; j++) {
                if (c[j] == c[i] && ((j + 1 > i - 1 || dp[j+1][i-1]))) {
                    dp[j][i] = true;
                    min = j == 0? 0 : Math.min(min, cut[j - 1] + 1);
                }
            }
            cut[i] = min;
        }
        return cut[c.length - 1];
    }
}

# 9ms 79.58%
class Solution {
    public int minCut(String s) {
        int[] dp = new int[s.length() + 1];
        for (int i = 0; i <= s.length(); i++) {
            dp[i] = i - 1;
        }
        for (int i = 0; i < s.length(); i++) {
            for (int j = 0; i + j < s.length() && i - j >= 0 && s.charAt(i + j) == s.charAt(i - j); j++) {
                dp[i + j + 1] = Math.min(dp[i + j + 1], dp[i - j] + 1);
            }
            for (int j = 0; i + j < s.length() && i - j - 1 >= 0 && s.charAt(i + j) == s.charAt(i - j - 1); j++) {
                dp[i + j + 1] = Math.min(dp[i + j + 1], dp[i - j - 1] + 1);
            }
        }
        return dp[s.length()];
    }
}

# Expand from center
# 2ms 98.41%
class Solution {
    public int minCut(String s) {
        int[] cuts = new int[s.length() + 1];
        for (int i = 0; i <= s.length(); i++) {
            cuts[i] = i - 1;
        }
        for (int i = 0; i < s.length(); i++) {
            check(s, i, i, cuts);
            check(s, i, i + 1, cuts);
        }
        return cuts[s.length()];
    }

    public void check(String s, int i, int j, int[] cuts) {
        while (i >= 0 && j < s.length() && s.charAt(i) == s.charAt(j)) {
            cuts[j + 1] = Math.min(cuts[j + 1], cuts[i] + 1);
            i--;
            j++;
        }
    }
}

# bruteForce with 131. Palindrome Partitioning
# input = "ababababababababababababcbabababababababababababa"
# TLE
class Solution {
    int min = Integer.MAX_VALUE;
    public int minCut(String s) {
        List<List<String>> res = new ArrayList();
        List<String> tmp = new ArrayList();
        helper(res, tmp, 0, s);
        return min;
    }
    public void helper(List<List<String>> res, List<String> tmp, int idx, String s) {
        if (idx == s.length()) {
            res.add(new ArrayList(tmp));
            min = Math.min(min, tmp.size() - 1);
            return;
        }
        
        for (int i = idx; i < s.length(); i++) {
            if (isValid(s, idx, i)) {
                tmp.add(s.substring(idx, i + 1));
                helper(res, tmp, i + 1, s);
                tmp.remove(tmp.size() - 1);
            }
        }
    }
    
    public boolean isValid(String s, int i, int j) {
        while (i < j) {
            if (s.charAt(i) != s.charAt(j)) return false;
            i++;
            j--;
        }
        return true;
    }
}
'''
