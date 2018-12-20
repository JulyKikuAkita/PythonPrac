__source__ = 'https://leetcode.com/problems/shortest-word-distance-iii/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/shortest-word-distance-iii.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 245. Shortest Word Distance III
#
# This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.
#
# Given a list of words and two words word1 and word2,
# return the shortest distance between these two words in the list.
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
import collections
import unittest
# 32ms 43.84%
class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not words or len(words) == 0:
            return 0
        d = collections.defaultdict(list)
        for i, word in enumerate(words):
            d[word].append(i)

        res = 0x7FFFFFFF
        l1 = d[word1]
        l2 = d[word2]

        for idx1 in l1:
            for idx2 in l2:
                if idx1 != idx2:
                    res = min(res, abs(idx1-idx2))
        return res

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
# Thought: 

# 0ms 100%
class Solution {
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

# 0ms 100%
class Solution {
    public int shortestWordDistance(String[] words, String word1, String word2) {
        int minDistance = Integer.MAX_VALUE;
        int index1 = -1;
        int index2 = -1;
        if (word1.equals(word2)) {
            for (int i = 0; i < words.length; i++) {
                if (words[i].equals(word1)) {
                    index1 = index2;
                    index2 = i;
                    minDistance = calculateMin(minDistance, index1, index2);
                }
            }
        } else {
            for (int i = 0; i < words.length; i++) {
                if (words[i].equals(word1)) {
                    index1 = i;
                } else if (words[i].equals(word2)) {
                    index2 = i;
                } else {
                    continue;
                }
                minDistance = calculateMin(minDistance, index1, index2);
            }
        }
        return minDistance;
    }
    
    private int calculateMin(int currMin, int index1, int index2) {
        if (index1 == -1 || index2 == -1) {
            return currMin;
        }
        return Math.min(currMin, Math.abs(index1 - index2));
    }
}
'''
