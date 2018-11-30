__source__ = 'https://leetcode.com/problems/sentence-similarity/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 734. Sentence Similarity
#
# Given two sentences words1, words2 (each represented as an array of strings),
# and a list of similar word pairs pairs, determine if two sentences are similar.
#
# For example, "great acting skills" and "fine drama talent" are similar,
# if the similar word pairs are pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]].
#
# Note that the similarity relation is not transitive.
# For example, if "great" and "fine" are similar, and "fine" and "good" are similar,
#  "great" and "good" are not necessarily similar.
#
# However, similarity is symmetric. For example, "great" and "fine"
# being similar is the same as "fine" and "great" being similar.
#
# Also, a word is always similar with itself.
# For example, the sentences words1 = ["great"],
# words2 = ["great"], pairs = [] are similar,
# even though there are no specified similar word pairs.
#
# Finally, sentences can only be similar if they have the same number of words.
# So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].
#
# Note:
#
# The length of words1 and words2 will not exceed 1000.
# The length of pairs will not exceed 2000.
# The length of each pairs[i] will be 2.
# The length of each words[i] and pairs[i][j] will be in the range [1, 20].
#
import unittest

#100% 20ms
class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        pairset = set(map(tuple, pairs))

        return all(w1 == w2 or (w1, w2) in pairset or (w2, w1) in pairset for w1, w2 in zip(words1, words2))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/sentence-similarity/solution/
#
# Complexity Analysis
# Time Complexity: O(N+P), where N is the maximum length of words1 and words2, and P is the length of pairs.
# Space Complexity: O(P)), the size of pairs.
# Intermediate objects created in evaluating whether a pair of words are similar are created one at a time,
# so they don't take additional space.
#

#3ms 100%
class Solution {
    public boolean areSentencesSimilar(String[] words1, String[] words2, String[][] pairs) {
        if (words1.length != words2.length) return false;
        Set<String> pairset = new HashSet();
        for (String[] pair: pairs) {
            pairset.add(pair[0] + "#" + pair[1]);
        }

        for(int i = 0; i < words1.length; ++i) {
            if (!words1[i].equals(words2[i]) &&
               !pairset.contains(words1[i] + "#" + words2[i]) &&
               !pairset.contains(words2[i] + "#" + words1[i]))
                return false;
        }
        return true;
    }
}


# 2ms 100%
class Solution {
    public boolean areSentencesSimilar(String[] words1, String[] words2, String[][] pairs) {
        if (words1.length != words2.length) return false;
        for (int i = 0; i < words1.length; i++){
            int found = 0;
            if (!words1[i].equals(words2[i])){
                for (int j = 0; j < pairs.length; j++){
                    if (words1[i].equals(pairs[j][0]) && words2[i].equals(pairs[j][1])){
                        found = 1;
                        break;
                    }
                    if (words1[i].equals(pairs[j][1]) && words2[i].equals(pairs[j][0])){
                        found = 1;
                        break;
                    }
                }
                if (found == 0)
                    return false;
            }
        }
        return true;
    }
}
'''