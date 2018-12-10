# coding=utf-8
__source__ = 'https://leetcode.com/problems/verifying-an-alien-dictionary/'
# Time:  O(N)
# Space: O(1)
#
# Description: Leetcode # 953. Verifying an Alien Dictionary
#
# In an alien language, surprisingly they also use english lowercase letters,
# but possibly in a different order.
# The order of the alphabet is some permutation of lowercase letters.
#
# Given a sequence of words written in the alien language, and the order of the alphabet,
# return true if and only if the given words are sorted lexicographicaly in this alien language.
#
# Example 1:
#
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
# Example 2:
#
# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1],
# hence the sequence is unsorted.
# Example 3:
#
# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match,
# and the second string is shorter (in size.)
# According to lexicographical rules "apple" > "app",
# because 'l' > '∅', where '∅' is defined as the blank character
# which is less than any other character (More info).
#
#
# Note:
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# All characters in words[i] and order are english lowercase letters.
#
import unittest
# 28ms 100%
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        order_index = {c: i for i, c in enumerate(order)}

        for i in xrange(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]

            # Find the first difference word1[k] != word2[k].
            for k in xrange(min(len(word1), len(word2))):
                # If they compare badly, it's not sorted.
                if word1[k] != word2[k]:
                    if order_index[word1[k]] > order_index[word2[k]]:
                        return False
                    break
            else:
                # If we didn't find a first difference, the
                # words are like ("app", "apple").
                if len(word1) > len(word2):
                    return False
        return True

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/verifying-an-alien-dictionary/solution/

Approach 1: Check Adjacent Words
Complexity Analysis
Time Complexity: O(C), where C is the total content of words.
Space Complexity: O(1)

# 4ms 100%
class Solution {
    public boolean isAlienSorted(String[] words, String order) {
        int[] map = new int[26];
        for (int i = 0; i < 26; i++) {
            map[order.charAt(i) - 'a'] = i;
        }
        if (words == null || words.length <= 1) return true;
        for (int i = 1; i < words.length; i++) {
            if (comp(words[i - 1], words[i], map)) {     // true if words[i-1] > words[i]
                return false;
            }
        }
        return true;
    }

    private boolean comp(String a, String b, int[] map) {
        int alen = a.length(), blen = b.length(), minlen = Math.min(alen, blen);
        char[] as = a.toCharArray(), bs = b.toCharArray();
        for (int i = 0; i < minlen; i++) {
            if (map[as[i] - 'a'] < map[bs[i] - 'a']) return false;
            else if (map[as[i] - 'a'] == map[bs[i] - 'a']) continue;
            else return true;
        }
        return alen > blen;
    }
}

'''