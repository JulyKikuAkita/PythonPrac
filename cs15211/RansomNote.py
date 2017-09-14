__source__ = 'https://leetcode.com/problems/ransom-note/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/ransom-note.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 383. Ransom Note
#
# Given an arbitrary ransom note string and another string containing letters
# from all the magazines, write a function that will return true if
# the ransom  note can be constructed from the magazines ;
# otherwise, it will return false.
#
# Each letter in the magazine string can only be used once in your ransom note.
#
# Note:
# You may assume that both strings contain only lowercase letters.
#
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
#
# Companies
# Apple
# Related Topics
# String
#
import unittest
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        counts = [0] * 26
        letters = 0

        for c in ransomNote:
            if counts[ord(c) - ord('a')] == 0:
                letters += 1
            counts[ord(c) - ord('a')] += 1

        for c in magazine:
            counts[ord(c) - ord('a')] -= 1
            if counts[ord(c) - ord('a')] == 0:
                letters -= 1
                if letters == 0:
                    break

        return letters == 0

# Time:  O(n)
# Space: O(1)
from collections import Counter

class Solution2(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        return not Counter(ransomNote) - Counter(magazine)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
#90.68% 13ms
public class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        int[] count = new int[128];
        for (char c : magazine.toCharArray()) {
            count[c]++;
        }
        for (char c : ransomNote.toCharArray()) {
            if (--count[c] < 0) {
                return false;
            }
        }
        return true;
    }
}
'''