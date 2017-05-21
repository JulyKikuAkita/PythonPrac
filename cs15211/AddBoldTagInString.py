__source__ = 'https://leetcode.com/problems/add-bold-tag-in-string/#/description'
# Time:  O()
# Space: O()
#
# Description:
# Given a string s and a list of strings dict,
# you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict.
# If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag.
# Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.
#
# Example 1:
# Input:
# s = "abcxyz123"
# dict = ["abc","123"]
# Output:
# "<b>abc</b>xyz<b>123</b>"
# Example 2:
# Input:
# s = "aaabbcc"
# dict = ["aaa","aab","bc"]
# Output:
# "<b>aaabbc</b>c"
#
# Note:
# The given dict won't contain duplicates, and its length won't exceed 100.
# All the strings in input have length in range [1, 1000].
# Hide Company Tags Google
# Hide Tags String
# Hide Similar Problems (M) Merge Intervals (H) Tag Validator
#

# We put all the words in our given wordlist into a trie.
# Then, let's paint any letter in our string that should be bolded.
# For every starting position i in our string, let's find the longest word that S[i:] starts with,
# and paint S[i:i+len(word)].
#
# Afterwards, we have a boolean array where paint[i] = True iff S[i] is bolded.
# Let's write our letters from left to right.
# If we are on a bolded letter and there is an unbolded letter to the left (or if we are at the leftmost letter),
# we should start a <b> tag. Similarly for </b> tags:
# they start when our bolded letter has an unbolded right neighbor (or we are at the right-most letter.)

import unittest

class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        paint = [False] * len(s)
        for i in xrange(len(s)):
            block = s[i:]
            for word in dict:
                if block.startswith(word):
                    paint[i:i+len(word)] = [True] * len(word)

        ans = []
        for i, u in enumerate(s):
            if paint[i] and (i == 0 or not paint[i-1]):
                ans.append('<b>')
            ans.append(u)
            if paint[i] and (i == len(s) - 1 or not paint[i+1]):
                ans.append('</b>')

        return "".join(ans)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
Use a boolean array to mark if character at each position is bold or not.
After that, things will become simple.

public class Solution {
    public String addBoldTag(String s, String[] dict) {
        boolean[] bold = new boolean[s.length()];
        for (String d: dict) {
            for (int i = 0; i <= s.length() - d.length(); i++) {
                if (s.substring(i, i + d.length()).equals(d)) {
                    for (int j = i; j < i + d.length(); j++)
                        bold[j] = true;
                }
            }
        }
        StringBuilder res = new StringBuilder();
        for (int i = 0; i < s.length();) {
            if (bold[i]) {
                res.append("<b>");
                while (i < s.length() && bold[i])
                    res.append(s.charAt(i++));
                res.append("</b>");
            } else
                res.append(s.charAt(i++));
        }
        return res.toString();
    }
}
'''