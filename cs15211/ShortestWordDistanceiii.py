__source__ = 'https://leetcode.com/problems/shortest-word-distance-iii/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/shortest-word-distance-iii.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 245. Shortest Word Distance III
#
# This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.
#
# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
#
# word1 and word2 may be the same and they represent two individual words in the list.
#
# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#
# Given word1 = "makes", word2 = "coding", return 1.
# Given word1 = "makes", word2 = "makes", return 3.
#
# Note:
# You may assume word1 and word2 are both in the list.
#
# Companies
# LinkedIn
# Related Topics
# Array
# Similar Questions
# Shortest Word Distance Shortest Word Distance II
#
import unittest
class Solution:
    # @param {string[]} words
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def shortestWordDistance(self, words, word1, word2):
        dist = float("inf")
        i, index1, index2 = 0, None, None
        while i < len(words):
            if words[i] == word1:
                if index1 is not None:
                    dist = min(dist, abs(index1 - i))
                index1 = i
            elif words[i] == word2:
                index2 = i

            if index1 is not None and index2 is not None:
                dist = min(dist, abs(index1 - index2))
            i += 1
        return dist

# test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().shortestWordDistance("abcdefghi", "a", "i")
        print Solution().shortestWordDistance("aabcdefghiia", "a", "i")
        print Solution().shortestWordDistance("aaaabcaadefghii", "a", "i")

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/contains-duplicate/solution/
# 96.06% 1ms
public class Solution {
    public int shortestWordDistance(String[] words, String word1, String word2) {
        return word1.equals(word2) ? shortestWordSame(words, word1) : shortestWordNotSame(words, word1, word2);
    }

    private int shortestWordSame(String[] words, String word) {
        int prev = -1;
        int result = Integer.MAX_VALUE;
        for (int i = 0; i < words.length; i++) {
            if (words[i].equals(word)) {
                if (prev >= 0) {
                    result = Math.min(result, i - prev);
                }
                prev = i;
            }
        }
        return result;
    }

    private int shortestWordNotSame(String[] words, String word1, String word2) {
        int result = Integer.MAX_VALUE;
        int last1 = -1;
        int last2 = -1;
        for (int i = 0; i < words.length; i++) {
            if (words[i].equals(word1)) {
                last1 = i;
                if (last2 >= 0) {
                    result = Math.min(result, last1 - last2);
                }
            } else if (words[i].equals(word2)) {
                last2 = i;
                if (last1 >= 0) {
                    result = Math.min(result, last2 - last1);
                }
            }
        }
        return result == Integer.MAX_VALUE ? -1 : result;
    }
}

'''