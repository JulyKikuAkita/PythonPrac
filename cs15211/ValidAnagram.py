__source__ = 'https://leetcode.com/problems/valid-anagram/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/valid-anagram.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 242. Valid Anagram
#
# Given two strings s and t, write a function to
# determine if t is an anagram of s.
#
# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.
#
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Companies
# Amazon Uber Yelp
# Related Topics
# Hash Table Sort
# Similar Questions
# Group Anagrams Palindrome Permutation Find All Anagrams in a String
#
import unittest
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        count = {}

        for c in s:
            if c.lower() in count:
                count[c.lower()] += 1
            else:
                count[c.lower()] = 1

        for c in t:
            if c.lower() in count:
                count[c.lower()] -= 1
            else:
                count[c.lower()] = -1

            if count[c.lower()] < 0:
                return False
        return True

# Time:  O(nlogn)
# Space: O(n)
class Solution2:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().isAnagram('a', 'a')

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/valid-anagram/solution/
#
# 4ms 71.69%
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        int[] count = new int[26];
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
        }
        for (int i = 0; i < t.length(); i++) {
            count[t.charAt(i) - 'a']--;
        }
        for (int i = 0; i < 26; i++) {
            if (count[i] != 0) {
                return false;
            }
        }
        return true;
    }
}

Approach #1 (Sorting) [Accepted]
# Time:  O(nlogn)
# Space: O(1)

#7ms 41.66%
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        char[] str1 = s.toCharArray();
        char[] str2 = t.toCharArray();
        Arrays.sort(str1);
        Arrays.sort(str2);
        return Arrays.equals(str1, str2);
    }
}

# 3ms 81.95%
class Solution {
    public boolean isAnagram(String s, String t) {
        int [] alp = new int[26];
        for(int i = 0;i<s.length();i++) alp[s.charAt(i) - 'a']++;
        for(int i = 0;i<t.length();i++) alp[t.charAt(i) - 'a']--;
        for(int i : alp) if(i!=0) return false;

        return true;

    }
}

# 6ms 49.29%
class Solution {
    public boolean isAnagram(String s, String t) {
        return Arrays.equals(countCharacters(s), countCharacters(t));
    }

    private int[] countCharacters(String s) {
        int[] count = new int[26];
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
        }
        return count;
    }
}
'''