__source__ = 'https://github.com/kamyu104/LeetCode/blob/master/Python/valid-word-abbreviation.py'
# Time:  O(n)
# Space: O(1)
#
# Description:
# https://leetcode.com/problems/valid-word-abbreviation/#/description
# Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.
#
# A string such as "word" contains only the following valid abbreviations:
#
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
# Notice that only the above abbreviations are valid abbreviations of the string "word".
# Any other string is not a valid abbreviation of "word".
#
# Note:
# Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.
#
# Example 1:
# Given s = "internationalization", abbr = "i12iz4n":
#
# Return true.
# Example 2:
# Given s = "apple", abbr = "a2e":
#
# Return false.
# Hide Company Tags Google
# Hide Tags String
# Hide Similar Problems (H) Minimum Unique Word Abbreviation (H) Word Abbreviation

import unittest
import re

class Solution(object):

    # 48ms 3.78%
    def validWordAbbreviation2(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        return bool(re.match(re.sub('([1-9]\d*)', r'.{\1}', abbr) + '$', word))

    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i , digit = 0, 0
        for c in abbr:
            if c.isdigit():
                if digit == 0 and c == '0':
                    return False
                digit *= 10
                digit += int(c)
            else:
                if digit:
                    i += digit
                    digit = 0
                if i >= len(word) or word[i] != c:
                    return False
                i += 1
        if digit:
            i += digit

        return i == len(word)


# your function here

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# 21ms 4.52%
class Solution {
    public boolean validWordAbbreviation(String word, String abbr) {
        return word.matches(abbr.replaceAll("[1-9]\\d*", ".{$0}"));
    }
}

# 15ms 21.86%
class Solution {
    public boolean validWordAbbreviation(String word, String abbr) {
        int i =0, j = 0;
        while (i < word.length() && j < abbr.length()) {
            if (word.charAt(i) == abbr.charAt(j)) {
                i++;
                j++;
                continue;
            }
            if (abbr.charAt(j) <= '0' || abbr.charAt(j) > '9') {
                return false;
            }
            int start = j;
            while (j < abbr.length() && abbr.charAt(j) >= '0' && abbr.charAt(j) <= '9') {
                j++;
            }
            int num = Integer.valueOf(abbr.substring(start, j));
            i += num;
        }
        return i == word.length() && j == abbr.length();
    }
}

'''