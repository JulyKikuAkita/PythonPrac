__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/shortest-word-distance.py
'''
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = "coding", word2 = "practice", return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

Hide Company Tags LinkedIn

'''
# Time:  O(n)
# Space: O(1)

class Solution:
    # @param {string[]} words
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def shortestDistance(self, words, word1, word2):
        dist = float("inf")
        i, index1, index2 = 0, None, None

        while i < len(words):
            if words[i] == word1:
                index1 = i
            elif words[i] == word2:
                index2 = i

            if index1 is not None and index2 is not None:
                dist = min(dist, abs(index1 - index2))
            i += 1

        return dist

class Solution2(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        res = len(words)
        idx1 = float("-inf")
        idx2 = float("inf")
        for i, word in enumerate(words):
            if word == word1:
                idx1 = i
            if word == word2:
                idx2 = i
            res = min(res, abs(idx1-idx2))
        return res

# test
if __name__ == "__main__":
    print Solution().shortestDistance("abcdefghi", "a", "i")
    print Solution().shortestDistance("aabcdefghiia", "a", "i")
    print Solution().shortestWordDistance("aaaabcaadefghii", "a", "i")
#java
js = '''
public class Solution {
    public int shortestDistance(String[] words, String word1, String word2) {
        int index1 = -1;
        int index2 = -1;
        int result = Integer.MAX_VALUE;
        for (int i = 0; i < words.length; i++) {
            if (words[i].equals(word1)) {
                index1 = i;
                if (index2 >= 0) {
                    result = Math.min(result, index1 - index2);
                }
            } else if (words[i].equals(word2)) {
                index2 = i;
                if (index1 >= 0) {
                    result = Math.min(result, index2 - index1);
                }
            }
        }
        return result;
    }
}

public class Solution {
    public int shortestDistance(String[] words, String word1, String word2) {
        int res = Integer.MAX_VALUE;
        int idx1 = -1;
        int idx2 = -1;
        for(int i = 0; i < words.length; i++){
            if(words[i].equals(word1)) idx1 = i;
            else if(words[i].equals(word2)) idx2 = i;
            if(idx1 >= 0 && idx2 >= 0){
                res = Math.min(res, Math.abs(idx1-idx2));
            }
        }
        return res;
    }
}
'''