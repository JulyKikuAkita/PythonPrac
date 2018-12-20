__source__ = 'https://leetcode.com/problems/repeated-substring-pattern/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/repeated-substring-pattern.py
# Time:  O(n)
# Space: O(n)
#
# Description: Leetcode # 459. Repeated Substring Pattern
#
# KMP im detailed code:
# http://www.geeksforgeeks.org/searching-for-patterns-set-2-kmp-algorithm/
#
# Given a non-empty string check if it can be constructed by taking a substring of it
# and appending multiple copies of the substring together.
# You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
#
# Example 1:
# Input: "abab"
#
# Output: True
#
# Explanation: It's the substring "ab" twice.
# Example 2:
# Input: "aba"
#
# Output: False
# Example 3:
# Input: "abcabcabcabc"
#
# Output: True
#
# Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
#
# Amazon Google
# Hide Tags String
# Hide Similar Problems (E) Implement strStr()
#
import unittest
# KMP solution.
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def getPrefix(pattern):
            prefix = [-1] * len(pattern)
            j = -1
            for i in xrange(1, len(pattern)):
                while j > -1 and pattern[j+1] != pattern[i]:
                    j =prefix[j]
                if pattern[j+1] == pattern[i]:
                    j += 1
                prefix[i] = j
            return prefix

        prefix = getPrefix(s)
        return prefix[-1] != -1 and (prefix[-1] + 1) % (len(s) - prefix[-1] -1) == 0

    # 24ms 99.78%
    def repeatedSubstringPattern2(self, str):
        """
        :type str: str
        :rtype: bool
        """
        if not str:
            return False

        ss = (str + str)[1:-1]
        print ss
        return ss.find(str) != -1

#Easy python solution with explaination
# Basic idea:
#
# First char of input string is first char of repeated substring
# Last char of input string is last char of repeated substring
# Let S1 = S + S (where S in input string)
# Remove 1 and last char of S1. Let this be S2
# If S exists in S2 then return true else false
# Let i be index in S2 where S starts then repeated substring length i + 1 and repeated substring S[0: i+1]
class Solution2(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False

        ss = (s + s)[1:-1]
        return ss.find(s) != -1

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# https://discuss.leetcode.com/topic/68210/from-intuitive-but-slow-to-really-fast-but-a-little-hard-to-comprehend
The length of the repeating substring must be a divisor of the length of the input string
Search for all possible divisor of str.length, starting for length/2
If i is a divisor of length, repeat the substring from 0 to i the number of times i is contained in s.length
If the repeated substring is equals to the input str return true

# 27ms 68.55%
class Solution {
    public boolean repeatedSubstringPattern(String s) {
        int l = s.length();
        for (int i = l /2 ; i >= 1; i--) {
            if (l % i == 0) {
                int m = l / i;
                String subS = s.substring(0, i);
                StringBuilder sb = new StringBuilder();
                for (int j = 0; j < m ; j++) {
                    sb.append(subS);
                }
                if (sb.toString().equals(s)) return true;
            }
        }
        return false;
    }
}

# KMP O(n)
# 16ms 85.75%
class Solution {
    //KMP
    public boolean repeatedSubstringPattern(String s) {
        int[] prefix = kmp(s);
        int len = prefix[s.length() - 1];
        int n = s.length();
        return (len > 0 && n % (n-len) == 0);
    }

    private int[] kmp(String s) {
        int len = s.length();
        int[] res = new int[len];
        char[] ch = s.toCharArray();
        int i = 0, j = 1;
        res[0] = 0;
        while( i < ch.length && j < ch.length) {
            if(ch[j] == ch[i]) {
                res[j] = i+1;
                i++;
                j++;
            }else {
                if (i == 0) {
                    res[j] = 0;
                    j++;
                }else {
                    i = res[i-1];
                }
            }
        }
        return res;
    }
}
'''
