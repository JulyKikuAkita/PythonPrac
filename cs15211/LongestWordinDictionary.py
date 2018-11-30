# coding=utf-8
import collections

__source__ = 'https://leetcode.com/problems/longest-word-in-dictionary/description/'
# Time:  O(m) sum of the length of words[i]
# Space: O(m) the space used by our trie
#
# Description: Leetcode # 720. Longest Word in Dictionary
#
# Given a list of strings words representing an English Dictionary,
# find the longest word in words that can be built one character at a time by other words in words.
# If there is more than one possible answer,
# return the longest word with the smallest lexicographical order.
#
# If there is no answer, return the empty string.
# Example 1:
# Input:
# words = ["w","wo","wor","worl", "world"]
# Output: "world"
# Explanation:
# The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
# Example 2:
# Input:
# words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# Output: "apple"
# Explanation:
# Both "apply" and "apple" can be built from other words in the dictionary.
# However, "apple" is lexicographically smaller than "apply".
# Note:
#
# All the strings in the input will only contain lowercase letters.
# The length of words will be in the range [1, 1000].
# The length of words[i] will be in the range [1, 30].
#

import unittest

#32 ms 100%
class Solution(object):
    def longestWord(self, words):
        ans=""
        wordset=set(words)
        for word in words:
            if len(word)>len(ans) or (len(ans)==len(word) and word<ans):
                if all(word[:k] in wordset for k in xrange(1,len(word))):
                    ans=word

        return ans

#48ms 65.44%
class Solution2(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        ans = ""
        wordset = set(words)
        words.sort(key = lambda c : (-len(c), c))
        for word in words:
            if all(word[:k] in wordset for k in xrange(1, len(word))):
                return word
        return ""

#With Trie:
#104ms 41.72%
class SolutionTrie(object):
    def longestWord(self, words):
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True

        for i, word in enumerate(words):
            reduce(dict.__getitem__, word, trie)[END] = i

        stack = trie.values()
        ans = ""
        while stack:
            cur = stack.pop()
            if END in cur:
                word = words[cur[END]]
                if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                    ans = word
                stack.extend([cur[letter] for letter in cur if letter != END])

        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/longest-word-in-dictionary/solution/

# 8ms 100%
# Approach #2: Trie + Depth-First Search [Accepted]
#
# Time complexity : O(∑w i2), where w_i is the length of words[i].
# This is the complexity to build the trie and to search it.
# If we used a BFS instead of a DFS, and ordered the children in an array,
# we could drop the need to check whether the candidate word at each node is better than the answer,
# by forcing that the last node visited will be the best answer.
#
# Space Complexity: O(∑w i0), the space used by our trie.

class Solution {
    public String longestWord(String[] words) {
        Trie trie = new Trie();
        for (String word : words) {
            trie.insert(word);
        }
        return dfs(trie.root, "");
    }

    class TrieNode{
        TrieNode [] base = new TrieNode[26];
        String word;
    }

    class Trie{
        TrieNode root;
        Trie() {
            root = new TrieNode();
            root.word = "";
        }

        void insert(String word) {
            TrieNode node = root;
            for (char c : word.toCharArray()) {
                if (node.base[c - 'a'] == null) node.base[c- 'a'] = new TrieNode();
                node = node.base[c- 'a'];
            }
            node.word = word;
        }
    }

    public String dfs(TrieNode node, String res) {
        if (node.word == null) return res;
        if (node.word.length() > res.length()) res = node.word;
        for (TrieNode child : node.base) {
            if (child != null) res = dfs(child, res);
        }
        return res;
    }
}

#8ms 100%
#BruceForce

Complexity Analysis
Time complexity : O(∑w i2), where w_i is the length of words[i].
Checking whether all prefixes of words[i] are in the set is O(∑wi2).
Space complexity : O(∑wi2) to create the substrings.

class Solution {
    public String longestWord(String[] words) {
        String res = "";
        Set<String> set = new HashSet();
        for (String word: words) {
            set.add(word);
        }

        for(String word: words) {
            if (isBetter(word, res) && contains(set, word)) res = word;
        }
        return res;
    }

    private boolean isBetter(String a, String b) {
        if (a.length() > b.length()) return true;
        else if (a.length() < b.length()) return false;

        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) > b.charAt(i)) return false;
            else if (a.charAt(i) < b.charAt(i)) return true;
        }
        return true;
    }

    private boolean contains(Set<String> set, String target) {
        for (int i = 1; i < target.length(); i++) {
            if (!set.contains(target.substring(0, i))) return false;
        }
        return true;
    }
}
'''