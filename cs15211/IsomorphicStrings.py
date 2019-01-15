__source__ = 'https://leetcode.com/problems/isomorphic-strings/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/isomorphic-strings.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 205. Isomorphic Strings
#
# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character
# while preserving the order of characters. No two characters may map to
# the same character but a character may map to itself.
#
# For example,
# Given "egg", "add", return true.
#
# Given "foo", "bar", return false.
#
# Given "paper", "title", return true.
#
# Note:
# You may assume both s and t have the same length.
#
# Companies
# LinkedIn
# Related Topics
# Hash Table
# Similar Questions
# Word Pattern
#
import unittest
from itertools import izip  # Generator version of zip.

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s2t, t2s = {}, {}
        for p, w in izip(s, t):
            if w not in s2t and p not in t2s:
                s2t[w] = p
                t2s[p] = w
            elif w not in s2t or s2t[w] != p:
                # Contradict mapping.
                return False
        return True

# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        return self.halfIsom(s, t) and self.halfIsom(t, s)

    def halfIsom(self, s, t):
        lookup = {}
        for i in xrange(len(s)):
            if s[i] not in lookup:
                lookup[s[i]] = t[i]
            elif lookup[s[i]] != t[i]:
                return False
        return True

class Solution3:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        dicts, dictt = {}, {}
        for i in xrange(len(s)):
            if s[i] in dicts and dicts[s[i]] != t[i]:
                return False
            if t[i] in dictt and dictt[t[i]] != s[i]:
                return False

            dicts[s[i]] = t[i]
            dictt[t[i]] = s[i]
        return True

# test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().isIsomorphic("aa", "ab")
        print Solution().isIsomorphic("aa", "bb")

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# 5ms 83.78%
class Solution {
    public boolean isIsomorphic(String s1, String s2) {
        int[] m = new int[512];
        for (int i = 0; i < s1.length(); i++) {
            if (m[s1.charAt(i)] != m[s2.charAt(i)+256]) return false;
            m[s1.charAt(i)] = m[s2.charAt(i)+256] = i+1;
        }
        return true;
    }
}

# 7ms 75.18%
class Solution {
    public boolean isIsomorphic(String s, String t) {
        int[]s_bucket=new int[256];
        int[]t_bucket=new int[256];
        for(int i=0;i<s.length();i++){
            if(s_bucket[s.charAt(i)]!=t_bucket[t.charAt(i)]) return false;
            s_bucket[s.charAt(i)]=i+1;
            t_bucket[t.charAt(i)]=i+1;
        }
        return true;
    }
}

# Same as above
# 4ms 91.72%
class Solution {
    public boolean isIsomorphic(String s, String t) {
        int[] s_bucket = new int[256];
        int[] t_bucket = new int[256];
        Arrays.fill(s_bucket, -1);
        Arrays.fill(t_bucket, -1);

        for (int i = 0; i < s.length(); i++) {
            if (s_bucket[s.charAt(i)] != t_bucket[t.charAt(i)]) return false;
            s_bucket[s.charAt(i)] = i ;
            t_bucket[t.charAt(i)] = i ;
        }
        return true;
    }
}

# 4ms 91.72%
class Solution {
    public boolean isIsomorphic(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        } else if (s.length() == 0) {
            return true;
        }
        char[] mapping = new char[128];
        boolean[] isVisited = new boolean[128];
        for (int i = 0; i < s.length(); i++) {
            char charS = s.charAt(i);
            char charT = t.charAt(i);
            if (mapping[charS] == 0) {
                if (isVisited[charT]) {
                    return false;
                } else {
                    mapping[charS] = charT;
                    isVisited[charT] = true;
                }
            } else if (mapping[charS] != charT) {
                return false;
            }
        }
        return true;
    }
}

# 10ms 59.25%
class Solution {
    public boolean isIsomorphic(String s, String t) {
        if(s == null || s.length() <= 1) return true;
        HashMap<Character, Character> map = new HashMap<Character, Character>();
        for(int i = 0 ; i< s.length(); i++){
            char a = s.charAt(i);
            char b = t.charAt(i);
            if(map.containsKey(a)){
                 if(map.get(a).equals(b))
                continue;
                else
                return false;
            }else{
                if(!map.containsValue(b))
                map.put(a,b);
                else return false;
            }
        }
        return true;
    }
}
'''