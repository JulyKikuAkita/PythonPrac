__source__ = 'https://leetcode.com/problems/most-common-word/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 819. Most Common Word
#
# Given a paragraph and a list of banned words,
# return the most frequent word that is not in the list of banned words.
# It is guaranteed there is at least one word that isn't banned, and that the answer is unique.
#
# Words in the list of banned words are given in lowercase,
# and free of punctuation.  Words in the paragraph are not case sensitive.
# The answer is in lowercase.
#
# Example:
#
# Input:
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# Output: "ball"
# Explanation:
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"),
# and that "hit" isn't the answer even though it occurs more because it is banned.
#
#
# Note:
#
# 1 <= paragraph.length <= 1000.
# 1 <= banned.length <= 100.
# 1 <= banned[i].length <= 10.
# The answer is unique, and written in lowercase
# (even if its occurrences in paragraph may have uppercase symbols, and even if it is a proper noun.)
# paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
# There are no hyphens or hyphenated words.
# Words only consist of letters, never apostrophes or other punctuation symbols.
#
import unittest
import collections
import re
import operator

# 24ms 99.56%
class Solution:
    def mostCommonWord(self, paragraph, banned):
        count=collections.Counter(piece for piece in re.split('[ !?\',;.]',paragraph.lower()) if piece)
        banned=set(banned)
        return max((item for item in count.items() if item[0] not in banned),key=operator.itemgetter(1))[0]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/most-common-word/solution/

Complexity Analysis
Time Complexity: O(P + B), where P is the size of paragraph and B is the size of banned.
Space Complexity: O(P + B)), to store the count and the banned set.

# 7ms 94.80%
class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        paragraph += ".";

        Set<String> banset = new HashSet();
        for (String word: banned) banset.add(word);
        Map<String, Integer> count = new HashMap();

        String ans = "";
        int ansfreq = 0;

        StringBuilder word = new StringBuilder();
        for (char c: paragraph.toCharArray()) {
            if (Character.isLetter(c)) {
                word.append(Character.toLowerCase(c));
            } else if (word.length() > 0) {
                String finalword = word.toString();
                if (!banset.contains(finalword)) {
                    count.put(finalword, count.getOrDefault(finalword, 0) + 1);
                    if (count.get(finalword) > ansfreq) {
                        ans = finalword;
                        ansfreq = count.get(finalword);
                    }
                }
                word = new StringBuilder();
            }
        }

        return ans;
    }
}

# 33ms 34.60%
class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        Set<String> set = new HashSet();
        for (String ban : banned) set.add(ban.toLowerCase());
        Map<String, Integer> count = new HashMap();
        int curMax = Integer.MIN_VALUE;
        String ans = "";
        for (String w : paragraph.split("\\W+")) { //split string by all non alphbet
            String word = w.toLowerCase(); // alternatively, String.replaceAll("[^A-Za-z0-9 ]", "")
            //System.out.print(word + "  ||");

            if (!set.contains(word)) {
                count.put(word, count.getOrDefault(word, 0) + 1);
                if (count.get(word) > curMax) {
                    curMax = count.get(word);
                    ans = word;
                }
            }
        }
        return ans;
    }
}

# without String utility, with Trie and 2 pointers
# 5ms 99.96%
class Solution {
    private class Trie{
        Trie child[] = new Trie[26];
        boolean isBan;
        int count = 0;
    }

    Trie root = new Trie();
    Trie node;

    public String mostCommonWord(String paragraph, String[] banned) {
        //construct the ban tree;
        for (String s : banned) {
            node = root;
            for (char c : s.toCharArray()) {
                if (node.child[c - 'a'] == null) node.child[c - 'a'] = new Trie();
                node = node.child[c - 'a'];
            }
            node.isBan = true;
        }

        String lowerPara = paragraph.toLowerCase();
        int len = lowerPara.length(), maxCount = 0;
        String res = "";

        for (int i = 0, j =0; i < len && j < len; i = ++j) {
            node = root;
            while (j < len && lowerPara.charAt(j) >= 'a' && lowerPara.charAt(j) <= 'z') {
                if (node.child[lowerPara.charAt(j) - 'a'] == null) node.child[lowerPara.charAt(j) - 'a'] = new Trie();
                node = node.child[lowerPara.charAt(j) - 'a'];
                j++;
            }

            if (i < j && !node.isBan) {
                node.count++;
                if (node.count > maxCount) {
                    res = lowerPara.substring(i, j);
                    maxCount = node.count;
                }
            }
        }
        return res;
    }
}
'''
