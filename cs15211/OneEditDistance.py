__source__ = 'https://leetcode.com/problems/one-edit-distance/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/one-edit-distance.py
# Time:  O(m + n)
# Space: O(1)
#
# Description: Leetcode # 161. One Edit Distance
#
# Given two strings S and T, determine if they are both one edit distance apart.
# Companies
# Snapchat Uber Facebook Twitter
# Related Topics
# String
# Similar Questions
# Edit Distance
#
import unittest
class Solution:
    # @param s, a string
    # @param t, a string
    # @return a boolean
    def isOneEditDistance(self, s, t):
        m, n = len(s), len(t)
        if m > n:
            return self.isOneEditDistance(t, s)
        if n - m > 1:
            return False

        i, shift = 0, n - m
        while i < m and s[i] == t[i]:
            i += 1
        if shift == 0:
            i +=1
        while i < m and s[i] == t[i + shift]:
            i += 1
        return i == m
#test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().isOneEditDistance("teacher", "acher")

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/contains-duplicate/solution/
Thought:
/*
 * There're 3 possibilities to satisfy one edit distance apart:
 *
 * 1) Replace 1 char:
      s: a B c
      t: a D c
 * 2) Delete 1 char from s:
      s: a D  b c
      t: a    b c
 * 3) Delete 1 char from t
      s: a   b c
      t: a D b c
 */
# 12.73%  3ms
class Solution {
    public boolean isOneEditDistance(String s, String t) {
        for (int i = 0; i < Math.min(s.length(), t.length()); i++) {
            if (s.charAt(i) != t.charAt(i)) {
                // s has the same length as t, so the only possibility is replacing one char in s and t
                if (s.length() == t.length()) {
                    return s.substring(i + 1).equals(t.substring(i + 1));
                // t is longer than s, so the only possibility is deleting one char from t
                } else if(s.length() < t.length()) {
                    return s.substring(i).equals(t.substring(i + 1));
                } else {  // s is longer than t, so the only possibility is deleting one char from s
                    return t.substring(i).equals(s.substring(i + 1));
                }
            }
        }
        //All previous chars are the same, the only possibility is deleting the end char in the longer one of s and t
        return Math.abs(s.length() - t.length()) == 1;
    }
}

#12.73% 3ms
public class Solution {
    public boolean isOneEditDistance(String s, String t) {
        if(Math.abs(s.length()-t.length()) > 1) return false;
        if(s.length() == t.length()) return isOneModify(s,t);
        if(s.length() > t.length()) return isOneDel(s,t);
        return isOneDel(t,s);
    }
    public boolean isOneDel(String s,String t){
        for(int i=0,j=0;i<s.length() && j<t.length();i++,j++){
            if(s.charAt(i) != t.charAt(j)){
                return s.substring(i+1).equals(t.substring(j));
            }
        }
        return true;
    }
    public boolean isOneModify(String s,String t){
        int diff =0;
        for(int i=0;i<s.length();i++){
            if(s.charAt(i) != t.charAt(i)) diff++;
        }
        return diff==1;
    }
}

# 49.86% 2ms
public class Solution {
    public boolean isOneEditDistance(String s, String t) {
        int m = s.length(), n = t.length();

        if(m < n) return isOneEditDistance(t, s);
        if(m - n > 1 ) return false;

        int i = 0;
        int shift = m - n;

        while(i < n && s.charAt(i) == t.charAt(i)){
            i++;
        }
        if(shift == 0) i++;
        while(i < n && s.charAt(i+shift) == t.charAt(i)){
            i++;
        }
        return i == n;
    }
}

#94.16% 1ms
class Solution {
    public boolean isOneEditDistance(String s, String t)
    {
        int len1 = s.length();
        int len2 = t.length();
        if (Math.abs(len1 - len2) > 1) return false;

        char[] chs = s.toCharArray();
        char[] cht = t.toCharArray();

        int i = 0, j = 0;
        while (i < len1 && j < len2)
        {
            if (chs[i] != cht[j])
            {
                if (len1 < len2) return s.substring(i).equals(t.substring(j+1));
                else if (len1 == len2) return s.substring(i+1).equals(t.substring(j+1));
                else return s.substring(i+1).equals(t.substring(j));
            }
            i++;
            j++;
        }

        return Math.abs(len1 - len2) == 1;
    }
}
'''