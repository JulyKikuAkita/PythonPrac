__source__ = 'https://leetcode.com/problems/regular-expression-matching/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/regular-expression-matching.py
# Time:  O(m * n)
# Space: O(n)
# DP
# "*" cannot be the first char?
#
# Implement regular expression matching with support for '.' and '*'.
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
# For the 2nd case, if the first char of pattern is "." or first char of pattern == the first i char of string, continue to match the left.
#
# Be careful about the offset.

#http://www.programcreek.com/2012/12/leetcode-regular-expression-matching-in-java/
class java_readable:
    # @return a boolean
    def isMatch(self, s, p):
        #base case
        if len(p) == 0:
            return len(s) == 0
        #special case
        if len(p) == 1:
            # // if the length of s is 0, return false
            if len(s) < 1:
                return False
            # if the first does not match, return false
            elif p[0] != s[0] and p[0] != '.':
                return False
            # otherwise, compare the rest of the string of s and p.
            else:
                return self.isMatch(s[1:], p[1:])

        #case 1: when the second char of p is not '*'
        if p[1] != '*':
            if len(s) < 1:
                return False
            if p[0] != s[0] and p[0] != '.':
                return False
            else:
                return self.isMatch(s[1:], p[1:])

        # case 2: when the second char of p is '*', complex case.
        else:
            # case 2.1: a char & '*' can stand for 0 element
            if self.isMatch(s, p[2:]):
                return True
            # case 2.2: a char & '*' can stand for 1 or more preceding element,
		        # so try every sub string
            i = 0
            while i < len(s) and s[i] == p[0] or p[0] == '.':
                if self.isMatch(s[i+1:], p[2:]):
                    return True
                i += 1
            return False



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

# http://www.cnblogs.com/zuoyuan/p/3781773.html
class SolutionOther:
    # @return a boolean
    #dp
    def isMatch(self, s, p):
        dp = [[False for i in range(len(p) + 1)] for j in range(len(s) +1)]
        dp[0][0] = True
        for i in range(1, len(p)+1):
            if p[i-1] == '*':
                if i >= 2:
                    dp[0][i] = dp[0][i-2]
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'))
                else:
                    dp[i][j] = dp[i-1][j-1] and s[i-1] == p[j-1]
        return dp[len(s)][len(p)]


    # Time Limit Exceeded
    def isMatchTLE(self, s, p):
        if len(p) == 0 : return len(s) == 0
        if len(p) == 1 or p[1] != '*' :
            if len(s) == 0 or (s[0] != p[0] and p[0] != '.'):
                return False
            return self.isMatchTLE(s[1:],p[1:])
        else:
            i = -1
            length = len(s)
            while i < length and (i<0 or p[0] == '.' or p[0] == s[i]):
                if self.isMatchTLE(s[i+1:], p[2:]): return True
                i += 1
            return False

#test
#test = SolutionOther()
#print test.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")
#print test.isMatchTLE("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")

#Java
Java = '''
Thought: https://discuss.leetcode.com/topic/40371/easy-dp-java-solution-with-detailed-explanation
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


# 40.59 %, 35ms
public class Solution {
    public boolean isMatch(String s, String p) {
        int lenS = s.length();
        int lenP = p.length();
        boolean[][] dp = new boolean[lenS + 1][lenP + 1];
        dp[0][0] = true;
        for (int i = 0; i <= lenS; i++) {
            for (int j = 1; j <= lenP; j++) {
                if (p.charAt(j - 1) == '.') {
                    dp[i][j] = i > 0 && dp[i - 1][j - 1];
                } else if (p.charAt(j - 1) == '*') {
                    dp[i][j] = j > 1 && (dp[i][j - 2] || dp[i][j - 1] || (i > 0 && dp[i - 1][j] && (p.charAt(j - 2) == '.' || p.charAt(j - 2) == s.charAt(i - 1))));
                } else {
                    dp[i][j] = i > 0 && dp[i - 1][j - 1] && s.charAt(i - 1) == p.charAt(j - 1);
                }
            }
        }
        return dp[lenS][lenP];
    }
}

# 45% - 81%
#80.07% 29ms
public class Solution {
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