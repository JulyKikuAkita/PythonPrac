__source__ = 'https://leetcode.com/problems/shortest-word-distance-ii/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/shortest-word-distance-ii.py
# Time:  init: O(n), lookup: O(a + b), a, b is occurences of word1, word2
# Space: O(n)
#
# Description: Leetcode # 244. Shortest Word Distance II
#
# This is a follow up of Shortest Word Distance.
# The only difference is now you are given the list of words
# and your method will be called repeatedly many times with different parameters.
# How would you optimize it?
#
# Design a class which receives a list of words in the constructor,
# and implements a method that takes two words word1 and word2
# and return the shortest distance between these two words in the list.
#
# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#
# Given word1 = "coding", word2 = "practice", return 3.
# Given word1 = "makes", word2 = "coding", return 1.
#
# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
#
# Companies
# LinkedIn
# Related Topics
# Hash Table Design
# Similar Questions
# Merge Two Sorted Lists Shortest Word Distance Shortest Word Distance III
#
import unittest
import collections
# Time:  init: O(n), lookup: O(a + b), a, b is occurences of word1, word2
# Space: O(n)
class WordDistance:
    # initialize your data structure here.
    # @param {string[]} words
    def __init__(self, words):
        self.wordIndex = collections.defaultdict(list)
        for i in xrange(len(words)):
            self.wordIndex[words[i]].append(i)

    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    # Adds a word into the data structure.
    def shortest(self, word1, word2):
        indexes1 = self.wordIndex[word1]
        indexes2 = self.wordIndex[word2]

        i, j, dist = 0, 0, float("inf")
        while i < len(indexes1) and j < len(indexes2):
            dist = min(dist, abs(indexes1[i] - indexes2[j]))
            if indexes1[i] < indexes2[j]:
                i += 1
            else:
                j += 1

        return dist

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
# 71.77% 154ms
public class WordDistance {
    private Map<String, List<Integer>> wordMap;

    public WordDistance(String[] words) {
        wordMap = new HashMap<>();
        for (int i = 0; i < words.length; i++) {
        /*
            if (!wordMap.containsKey(words[i])) {
                wordMap.put(words[i], new ArrayList<>());
            }
        */
            wordMap.putIfAbsent(word, new ArrayList<> ());
            wordMap.get(words[i]).add(i);
        }
    }

    public int shortest(String word1, String word2) {
        List<Integer> list1 = wordMap.get(word1);
        List<Integer> list2 = wordMap.get(word2);
        int size1 = list1.size();
        int size2 = list2.size();
        if (list1 == null || size1 == 0 || list2 == null || size2 == 0) {
            return 0;
        }
        int i = 0;
        int j = 0;
        int result = Integer.MAX_VALUE;
        while (true) {
            int index1 = list1.get(i);
            int index2 = list2.get(j);
            if (index1 > index2) {
                result = Math.min(result, index1 - index2);
                j++;
                if (j == size2) {
                    break;
                }
            } else {
                result = Math.min(result, index2 - index1);
                i++;
                if (i == size1) {
                    break;
                }
            }
        }
        return result;
    }
}

// Your WordDistance object will be instantiated and called as such:
// WordDistance wordDistance = new WordDistance(words);
// wordDistance.shortest("word1", "word2");
// wordDistance.shortest("anotherWord1", "anotherWord2");
'''