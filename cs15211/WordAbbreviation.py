__source__ = 'https://leetcode.com/problems/word-abbreviation/#/description'
# Time:  O()
# Space: O()
#
# Description: 527. Word Abbreviation
#
# Given an array of n distinct non-empty strings, you need to generate minimal possible abbreviations
# for every word following rules below.
# 1. Begin with the first character and then the number of characters abbreviated,
# which followed by the last character.
# 2. If there are any conflict, that is more than one words share the same abbreviation,
# a longer prefix is used instead of only the first character until making the map
# from word to abbreviation become unique. In other words,
# a final abbreviation cannot map to more than one original words.
# 3. If the abbreviation doesn't make the word shorter, then keep it as original.
#
# Example:
# Input: ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
# Output: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
# Note:
# Both n and the length of each word will not exceed 400.
# The length of each word is greater than 1.
# The words consist of lowercase English letters only.
# The return answers should be in the same order as the original array.
# Hide Company Tags Google Snapchat
# Hide Tags Sort String
# Hide Similar Problems (E) Valid Word Abbreviation (H) Minimum Unique Word Abbreviation

import unittest
import collections
# Call two words similar if they have the same first letter, last letter, and length.
# Only words that are similar are eligible to have the same abbreviation.
# This motivates us to group words by similarity (it is an equivalence relation.)
#
# For each group G of similar words, consider a word W.
# If it has a longest common prefix P with any other word X in G,
# then our abbreviation must contain a prefix of more than |P| characters. Sort G.
# It must be the case that the longest common prefix of W with any other word X in G
# must occur with words adjacent to W, so we only need to check those.
#
# 64ms 100%
class Solution(object):
    def wordsAbbreviation(self, dict):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
        def longest_common_prefix(a, b):
            i = 0
            while i < len(a) and i < len(b) and a[i] == b[i]:
                i += 1
            return i

        ans = [None for _ in dict]

        groups = collections.defaultdict(list)
        for index, word in enumerate(dict):
            groups[len(word), word[0], word[-1]].append((word, index))

        for (size, first, last), enum_words in groups.iteritems():
            enum_words.sort()
            lcp = [0] * len(enum_words)
            for i, (word, _) in enumerate(enum_words):
                if i:
                    word2, _ = enum_words[i-1]
                    p = longest_common_prefix(word, word2)
                    lcp[i] = max(lcp[i], p)
                    lcp[i-1] = max(lcp[i-1], p)

            for (word, index), p in zip(enum_words, lcp):
                delta = size - 2 - p
                if delta <= max(1, len(str(delta)) - 1):
                    ans[index] = word
                else:
                    ans[index] = word[:p+1] + str(delta) + last
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/word-abbreviation/solution/

Make abbreviation for each word.
Then, check each word, if there are some strings which have same abbreviation with it, increase the prefix.

# 52ms 38.13%
class Solution {
    public List<String> wordsAbbreviation(List<String> dict) {
        int len = dict.size();
        String[] ans = new String[len];
        int[] prefix = new int[len];
        for (int i = 0 ; i < len; i++) {
            prefix[i] = 1;
            ans[i] = makeAbbr(dict.get(i), 1); // make abbreviation for each string
        }

        for (int i = 0; i < len; i++) {
            while (true) {
                HashSet<Integer> set = new HashSet<>();
                for (int j = i + 1; j < len; j++) {
                    if (ans[j].equals(ans[i])) {
                        set.add(j); // check all strings with the same abbreviation
                    }
                }
                if (set.isEmpty()) break;
                set.add(i);
                for (int k : set) {
                    ans[k] = makeAbbr(dict.get(k), ++prefix[k]); // increase the prefix
                }
            }
        }
        return Arrays.asList(ans);
    }

    private String makeAbbr(String s, int k) {
        if (k >= s.length() - 2) return s;
        StringBuilder sb = new StringBuilder();
        sb.append(s.substring(0, k));
        sb.append(s.length() - 1 - k);
        sb.append(s.charAt(s.length() - 1));
        return sb.toString();
    }
}

'''