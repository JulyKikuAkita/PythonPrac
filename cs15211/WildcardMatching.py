__source__ = 'https://leetcode.com/problems/wildcard-matching/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/wildcard-matching.py
# Time:  O(m + n)
# Space: O(1)
# Greedy
#
# Description: Leetcode # 44. Wildcard Matching
#
# Implement wildcard pattern matching with support for '?' and '*'.
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
#
# The matching should cover the entire input string (not partial).
#
# The function prototype should be:
# bool isMatch(const char *s, const char *p)
#
# Some examples:
# isMatch("aa","a") -> false
# isMatch("aa","aa") -> true
# isMatch("aaa","aa") -> false
# isMatch("aa", "*") -> true
# isMatch("aa", "a*") -> true
# isMatch("ab", "?*") -> true
# isMatch("aab", "c*a*b") -> false
#
# Companies
# Google Snapchat Two Sigma Facebook Twitter
# Related Topics
# Dynamic Programming Backtracking Greedy String
# Similar Questions
# Regular Expression Matching
#
# iteration
import unittest
class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        p_ptr, s_ptr, last_s_ptr, last_p_ptr = 0, 0, -1, -1
        while s_ptr < len(s):
            if p_ptr < len(p) and (s[s_ptr] == p[p_ptr] or [p_ptr] == '?'):
                s_ptr += 1
                p_ptr += 1
            elif p_ptr < len(p) and p[p_ptr] == '*':
                p_ptr += 1
                last_s_ptr = s_ptr
                last_p_ptr = p_ptr
            elif last_p_ptr != -1:
                last_s_ptr += 1
                s_ptr = last_s_ptr
                p_ptr = last_p_ptr
            else:
                return False
        while p_ptr < len(p) and p[p_ptr] == '*':
            p_ptr += 1

        return p_ptr == len(p)

# dp with rolling window
# Time:  O(m * n)
# Space: O(m + n)
class Solution2:
    # @return a boolean
    def isMatch(self, s, p):
        k = 2
        result = [[False for j in xrange(len(p) + 1) ]for i in xrange(k)]
        #print result

        result[0][0] = True
        for i in xrange(1, len(p) + 1):
            if p[i-1] == '*':
                result[0][i] = result[0][i-1]

        for i in xrange(1, len(s) + 1):
            result[i % k][0] = False
            for j in xrange(1, len(p) + 1):
                if p[j-1] != '*':
                    result[i % k][j] = result[(i-1) % k][j-1] and (s[i-1] == p[j-1] or p[j-1] == '?')
                else:
                    result[i % k][j] = result[i % k ][j-1] or result[(i-1) % k][j]

        return result[len(s) % k][len(p)]

# dp
# Time:  O(m * n)
# Space: O(m * n)
class Solution3:
    # @return a boolean
    def isMatch(self, s, p):
        result = [[False for j in xrange(len(p) + 1)]for i in xrange(len(s) + 1)]
        result[0][0] = True
        for i in xrange(1, len(p) + 1):
            if p[i-1] == '*':
                result[0][i] = result[0][i-1]
        for i in xrange(1, len(s) + 1):
            result[i][0] = False
            for j in xrange(1, len(p)+1):
                if p[j-1] != '*':
                    result[i][j] = result[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '?')
                else:
                    result[i][j] = result[i][j-1] or result[i-1][j]
        return result[len(s)][len(p)]


# recursive, slowest, TLE
class Solution4:
    # @return a boolean
    def isMatch(self, s, p):
        if not p or not s:
            return not s and not p
        if p[0] != '*':
            if p[0] == s[0] or p[0] == '?':
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        else:
            while len(s) >0:
                if self.isMatch(s, p[1:]):
                    return True
                s = s[1:]
            return self.isMatch(s, p[1:])

# http://chaoren.is-programmer.com/posts/42771.html
# http://www.cnblogs.com/zuoyuan/p/3781872.html
class SolutionOther:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    # o(n)
    def isMatch(self, s, p):
        star = -1
        pPointer = sPointer = ss = 0

        while sPointer < len(s):
            print s[sPointer], ss
            if pPointer < len(p) and (s[sPointer] == p[pPointer] or p[pPointer] == '?'):
                sPointer += 1
                pPointer += 1
                continue
            if pPointer < len(p) and p[pPointer] == '*':
                star = pPointer
                pPointer += 1
                ss = sPointer
                continue
            if star != -1:
                pPointer = star+1
                ss += 1
                sPointer = ss
                continue
            return False

        while pPointer < len(p) and p[pPointer] == '*':
            print p[pPointer],  ss
            pPointer += 1

        if pPointer == len(p): return True
        return False

#test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        test = SolutionOther()
        #print test.isMatch("a", "aa") # false
        #print test.isMatch("aa","a") # false
        #print test.isMatch("aa","aa") # true
        #print test.isMatch("aaa","aa") # false
        #print test.isMatch("aa", "*") # true
        #print test.isMatch("aa", "a*") # true
        #print test.isMatch("ab", "?*") # true
        #print test.isMatch("aab", "c*a*b")

        #print Solution().isMatch("aaaabaaaab","a*b*b")
        #print Solution().isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")
        #print Solution().isMatch("aa","a")
        #print Solution().isMatch("aa","aa")
        #print Solution().isMatch("aaa","aa")
        #print Solution().isMatch("aa", "a*")
        #print Solution().isMatch("aa", "?*")
        #print Solution().isMatch("ab", "?*")
        print Solution2().isMatch("aab", "c*a*b")

if __name__ == '__main__':
    unittest.main()

Java = '''
Thought:
1. DP:
(i) p == s or p == ? : T
(ii) p == char != s : F
(iii) p == * : p = dp[i+1][j] || dp[i][j+1]

# 57ms 69.30%
class Solution {
    public boolean isMatch(String s, String p) {
        boolean[][] dp = new boolean[s.length() + 1][p.length() + 1];
        dp[s.length()][p.length()] = true;
        for (int i = p.length() - 1; i >= 0; i--) {
            if (p.charAt(i) == '*') dp[s.length()][i] = true;
            else break;
        }
        
        for (int i = s.length() - 1; i >= 0; i--) {
            for (int j = p.length() - 1; j >= 0; j--) {
                if (s.charAt(i) == p.charAt(j) || p.charAt(j) == '?') {
                    dp[i][j] = dp[i+ 1][j+1];
                } else if (p.charAt(j) == '*') {
                    dp[i][j] = dp[i + 1][j] || dp[i][j + 1];
                } else {
                    dp[i][j] = false;
                }       
            }
        }
        return dp[0][0];
    }
}

2. Thought:
I found this solution from http://yucoding.blogspot.com/2013/02/leetcode-question-123-wildcard-matching.html

The basic idea is to have one pointer for the string and one pointer for the pattern.
This algorithm iterates at most length(string) + length(pattern) times, for each iteration,
at least one pointer advance one step.

# 94.68% 29ms
class Solution {
    public boolean isMatch(String s, String p) {
        int lenS = 0;
        int lenP = 0;
        int match = 0, starIdx = -1;
        while (lenS < s.length()){
            // advancing both pointers
            if (lenP < p.length()  && (p.charAt(lenP) == '?' || s.charAt(lenS) == p.charAt(lenP))){
                lenS++;
                lenP++;
            }
            // * found, only advancing pattern pointer
            else if (lenP < p.length() && p.charAt(lenP) == '*'){
                starIdx = lenP;
                match = lenS;
                lenP++;
            }
           // last pattern pointer was *, advancing string pointer
            else if (starIdx != -1){
                lenP = starIdx + 1;
                match++;
                lenS = match;
            }
           //current pattern pointer is not star, last patter pointer was not *
           //characters do not match
            else return false;
        }

        //check for remaining characters in pattern
        while (lenP < p.length() && p.charAt(lenP) == '*') lenP++;

        return lenP == p.length();
    }
}

# 43ms 96.23%
class Solution {
    public boolean isMatch(String s, String p) {
        int i = 0, j = 0, starIdx = -1, iIdx = -1;
        while (i < s.length()) {
            if (j < p.length() && (p.charAt(j) == '?' || p.charAt(j) == s.charAt(i))) {
                i++;
                j++;
            } else if (j < p.length() && p.charAt(j) == '*') {
                starIdx = j;
                iIdx = i;
                j++;
            } else if (starIdx != -1) {
                j = starIdx + 1;
                i = iIdx + 1;
                iIdx++;
            } else {
                return false;
            }
        }
        while (j < p.length() && p.charAt(j) == '*') j++;
        return j == p.length();
    }
}
'''
