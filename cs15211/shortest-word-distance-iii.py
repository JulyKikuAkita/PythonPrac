__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/shortest-word-distance-iii.py
'''
This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = "makes", word2 = "coding", return 1.
Given word1 = "makes", word2 = "makes", return 3.

Linkedln

Note:
You may assume word1 and word2 are both in the list.
'''
# Time:  O(n)
# Space: O(1)
# LinkedIn


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
if __name__ == "__main__":
    print Solution().shortestWordDistance("abcdefghi", "a", "i")
    print Solution().shortestWordDistance("aabcdefghiia", "a", "i")
    print Solution().shortestWordDistance("aaaabcaadefghii", "a", "i")

#java
js = '''
public class Solution {
    public int shortestWordDistance(String[] words, String word1, String word2) {
        int res = Integer.MAX_VALUE;
        int id1 = -1;
        int id2 = -1;

        int i = 0;
        while(i < words.length){
            if(word1.equals(words[i])){
                if (id1 >= 0){
                    res = Math.min(res, Math.abs(id1 - i));
                }
                id1 = i;
            }
            else if(word2.equals(words[i])){
                id2 = i;
            }
            if(id1 >= 0 && id2 >= 0){
                res = Math.min(res, Math.abs(id1 - id2));
            }
            i++;

        }
        return res;


    }
}

public class Solution {
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