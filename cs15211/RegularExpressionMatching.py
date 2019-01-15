# coding=utf-8
__source__ = 'https://leetcode.com/problems/regular-expression-matching/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/regular-expression-matching.py
# Time:  O(m * n)
# Space: O(n)
# DP
# "*" cannot be the first char?
#
# Description: Leetcode # 10. Regular Expression Matching
#
# Given an input string (s) and a pattern (p),
# implement regular expression matching with support for '.' and '*'.
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
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
# isMatch("aa", "a*") -> true
# isMatch("aa", ".*") -> true
# isMatch("ab", ".*") -> true
# isMatch("aab", "c*a*b") -> true  #wildcard matching return False
# Companies
# Google Uber Airbnb Facebook Twitter
# Related Topics
# Dynamic Programming Backtracking String
# Similar Questions
# Wildcard Matching
#
import unittest
# dp with rolling window
class Solution(unittest.TestCase):
    # @return a boolean
    def isMatch(self, s, p):
        k = 3
        result = [[False for i in xrange(len(p) + 1)] for j in xrange(k )]
        print result

        result[0][0 ] = True
        for i in xrange(2, len(p) + 1):
            if p[i - 1] == '*':
                result[0][i] = result[0][i - 2]

        for i in xrange(1, len(s) + 1):
            if i > 1:
                result[0][0] = False
            for j in xrange(1, len(p) + 1):
                if p[j - 1] != '*':
                    result[i % k][j] = result[(i - 1) % k][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
                else:
                    result[i % k][j] = result[i % k][j-2] or (result[(i-1) % k][j] and (s[i-1] == p[j-2] or p[j-2]=='.'))

        return result[len(s) % k][len(p)]

    def test(self):
        self.assertTrue(self.isMatch("aab", "c*a*b"))
# dp
# Time:  O(m * n)
# Space: O(m * n)
class Solution2:
    # @return a boolean
    def isMatch(self, s, p):
        result = [[False for j in xrange(len(p)+ 1)] for i in xrange(len(s) + 1)]

        result[0][0] = True

        for i in xrange(2, len(p) + 1):
            if p[i - 1] == '*':
                result[0][i] = result[0][i - 2]

        for i in xrange(1, len(s) + 1):
            for j in xrange(1, len(p) + 1):
                if p[j - 1] != '*':
                    result[i][j] = result[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
                else:
                    result[i][j] = result[i][j - 2] or (result[i - 1][j]) and (s[i - 1] == p[j - 2] or p[j - 2] == '.')
        print result[-1][-1], result[len(s)][len(p)]
        return result[len(s)][len(p)]

# recursive
class Solution3:
    # @return a boolean
    def isMatch(self, s, p):
        if not p:
            return not s

        if len(p) == 1 or p[1] != '*':
            if len(s) > 0 and (p[0] == s[0] or p[0] == '.'):
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        else:
            while len(s) > 0 and (p[0] == s[0] or p[0] == '.'):
                if self.isMatch(s, p[2:]):
                    return True
                s = s[1:]
            return self.isMatch(s, p[2:])

# iteration
class Solution4:
    # @return a boolean
    def isMatch(self, s, p):
        p_ptr, s_ptr, last_s_ptr, last_p_ptr = 0, 0, -1, -1
        last_ptr= []
        while s_ptr < len(s):
            if p_ptr < len(p) and (p_ptr == len(p) - 1 or p[p_ptr + 1] != '*') and \
                    (s_ptr < len(s) ) and (p[p_ptr] == s[s_ptr] or p[p_ptr] == '.'):
                s_ptr += 1
                p_ptr += 1
            elif p_ptr < len(p) - 1 and (p_ptr != len(p) - 1 and p[p_ptr + 1] == '*'):
                p_ptr += 2
                last_ptr.append([s_ptr, p_ptr])
            elif last_ptr:
                [last_s_ptr, last_p_ptr] = last_ptr.pop()
                while last_ptr and p[last_p_ptr - 2] != s[last_s_ptr] and p[last_p_ptr - 2] != '.':
                    [last_s_ptr, last_p_ptr] = last_ptr.pop()

                if p[last_p_ptr - 2] == s[last_s_ptr] or p[last_p_ptr - 2] == '.':
                    last_s_ptr += 1
                    s_ptr = last_s_ptr
                    p_ptr = last_p_ptr
                    last_ptr .append([s_ptr, p_ptr])
                else:
                    return False
            else:
                return False

        while p_ptr < len(p) - 1 and p[p_ptr] == '.' and p[p_ptr+1] == '*':
            p_ptr += 2

        return p_ptr == len(p)


# First of all, this is one of the most difficulty problems. It is hard to handle many cases.
#
# The problem should be simplified to handle 2 basic cases:
#
# the second char of pattern is "*"
# the second char of pattern is not "*"
# For the 1st case, if the first char of pattern is not ".",
# the first char of pattern and string should be the same. Then continue to match the left part.
#
# For the 2nd case, if the first char of pattern is "." or first char of pattern == the first i char of string,
# continue to match the left.
#
# Be careful about the offset.
# 2376ms 12.40%
class Solution(object):
    def isMatch(self, text, pattern):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])

class TestMethods(unittest.TestCase):
    def test_Local(self):
        pass
        #test = SolutionOther()
        #print test.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")
        #print test.isMatchTLE("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")

if __name__ == "__main__":
    #print Solution().isMatch("abcd","d*")
    #print Solution().isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")
    #print Solution().isMatch("aa","a")
    #print Solution().isMatch("aa","aa")
    #print Solution().isMatch("aaa","aa")
    #print Solution().isMatch("aa", "a*")
    #print Solution2().isMatch("aa", ".*")
    #print Solution3().isMatch("ab", ".*")
    print Solution().isMatch("aab", "c*a*b")
    print Solution4().isMatch("aab", "c*a*b")

Java = '''
# Thought: https://leetcode.com/problems/regular-expression-matching/solution/
# Approach 1: Recursion
Complexity Analysis
Time Complexity: Let T, P be the lengths of the text and the pattern respectively. 
In the worst case, a call to match(text[i:], pattern[2j:]) will be made Choose (i + j) over i times, 
and strings of the order O(T−i) and O(P − 2 * j) will be made. 
Thus, the complexity has the order ∑ i=0T∑ j=0 P/2(i over i+j)O(T+P−i−2j). 
With some effort outside the scope of this article, we can show this is bounded by O((T+P)* 2^(T + P/ 2)) 
Space Complexity: For every call to match, we will create those strings as described above, 
possibly creating duplicates. If memory is not freed, this will also take a total of O((T+P)* 2^(T + P/ 2))
space, even though there are only order O(T^2 + P^2) unique suffixes of P and T that are actually required. 

# 149ms 11.38%
class Solution {
    public boolean isMatch(String s, String p) {
        if (p.isEmpty()) return s.isEmpty();
        boolean first_match = (!s.isEmpty() &&
                               (p.charAt(0) == s.charAt(0) || p.charAt(0) == '.'));
        if (p.length() >= 2 && p.charAt(1) == '*') {
            return isMatch(s, p.substring(2)) || (first_match && isMatch(s.substring(1), p));
        } else {
            return first_match && isMatch(s.substring(1), p.substring(1));
        }
    }
}

# Bottom-Up Variation
# Complexity Analysis
# Time Complexity: Let T, P be the lengths of the text and the pattern respectively. 
# The work for every call to dp(i, j) for i=0, ... ,T; j=0,...,P is done once, and it is O(1) work. 
# Hence, the time complexity is O(TP).
# Space Complexity: The only memory we use is the O(TP) boolean entries in our cache. 
# Hence, the space complexity is O(TP).

# 26ms 59.91%
class Solution {
    public boolean isMatch(String s, String p) {
        boolean[][] dp = new boolean[s.length() + 1][p.length() + 1];
        dp[s.length()][p.length()] = true;
        for (int i = s.length(); i >= 0; i--) {
            for (int j = p.length() - 1; j >= 0; j--) {
                boolean first_match = (i < s.length() && (p.charAt(j) == s.charAt(i) || p.charAt(j) == '.'));
                if (j + 1 < p.length() && p.charAt(j + 1) == '*') {
                    dp[i][j] = dp[i][j + 2] || first_match && dp[i + 1][j];
                } else {
                    dp[i][j] = first_match && dp[i + 1][j + 1];
                }
            }
        }
        return dp[0][0];
    }
}

https://discuss.leetcode.com/topic/40371/easy-dp-java-solution-with-detailed-explanation
This Solution use 2D DP. beat 90% solutions, very simple.
Here are some conditions to figure out, then the logic can be very straightforward.
1, If p.charAt(j) == s.charAt(i) :  dp[i][j] = dp[i-1][j-1];
2, If p.charAt(j) == '.' : dp[i][j] = dp[i-1][j-1];
3, If p.charAt(j) == '*':
   here are two sub conditions:
               1   if p.charAt(j-1) != s.charAt(i) : dp[i][j] = dp[i][j-2]  //in this case, a* only counts as empty
               2   if p.charAt(i-1) == s.charAt(i) or p.charAt(i-1) == '.':
                              dp[i][j] = dp[i-1][j]    //in this case, a* counts as multiple a
                           or dp[i][j] = dp[i][j-1]   // in this case, a* counts as single a
                           or dp[i][j] = dp[i][j-2]   // in this case, a* counts as empty
# 27ms 54.48%
class Solution {
    public boolean isMatch(String s, String p) {
        int lenS = s.length();
        int lenP = p.length();
        boolean[][] dp = new boolean[lenS + 1][lenP + 1];
        dp[0][0] = true;
        for (int i = 0; i <= lenS; i++) {
            for (int j = 1; j <= lenP; j++) {
                if (p.charAt(j - 1) == '.') {
                    dp[i][j] = i > 0 && dp[i-1][j - 1];
                } else if (p.charAt(j - 1) == '*') {
                    dp[i][j] = j - 1 > 0 && 
                    (dp[i][j - 2] || dp[i][j - 1] || 
                    (i > 0 && dp[i - 1][j] && (p.charAt(j - 2) == '.' || p.charAt(j - 2) == s.charAt(i - 1))));
                } else {
                    dp[i][j] = i > 0 && dp[i - 1][j - 1] && s.charAt(i - 1) == p.charAt(j - 1);
                }
            }
        }
        return dp[lenS][lenP];
    }
}

# 24ms 80.27% 
class Solution {
    public boolean isMatch(String s, String p) {
        if (s == null || p == null) {
            return false;
        }
        boolean[][] dp = new boolean[s.length()+1][p.length()+1];
        dp[0][0] = true;
        for (int i = 0; i < p.length(); i++) {
            if (p.charAt(i) == '*' && dp[0][i-1]) {
                dp[0][i+1] = true;
            }
        }
        for (int i = 0 ; i < s.length(); i++) {
            for (int j = 0; j < p.length(); j++) {
                if (p.charAt(j) == '.') {
                    dp[i+1][j+1] = dp[i][j];
                }
                if (p.charAt(j) == s.charAt(i)) {
                    dp[i+1][j+1] = dp[i][j];
                }
                if (p.charAt(j) == '*') {
                    if (p.charAt(j-1) != s.charAt(i) && p.charAt(j-1) != '.') {
                        dp[i+1][j+1] = dp[i+1][j-1];
                    } else {
                        dp[i+1][j+1] = (dp[i+1][j] || dp[i][j+1] || dp[i+1][j-1]);
                    }
                }
            }
        }
        return dp[s.length()][p.length()];
    }
}
'''
