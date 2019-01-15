__source__ = 'https://github.com/kamyu104/LeetCode/blob/master/Python/concatenated-words.py'
# https://leetcode.com/problems/concatenated-words/#/description
# Time:  O(n * l^2)
# Space: O(n * l)
#
# Description: Leetcode #472. Concatenated Words
#
# Given a list of words, please write a program that returns
# all concatenated words in the given list of words.
#
# A concatenated word is defined as a string that is comprised entirely of
# at least two shorter words in the given array.
#
# Example:
# Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
#
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
#
# Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
#  "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
# "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
# Note:
# The number of elements of the given array will not exceed 10,000
# The length sum of elements in the given array will not exceed 600,000.
# All the input string will only include lower case letters.
# The returned elements order does not matter.
#
# Dynamic Programming Trie Depth-first Search
# Hide Similar Problems (H) Word Break II
#
import unittest
# 1280ms 37.40%
class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        lookup = set(words)
        result = []
        for word in words:
            dp = [False] * (len(word)+1)
            dp[0] = True
            for i in xrange(len(word)):
                if not dp[i]:
                    continue

                for j in xrange(i+1, len(word)+1):
                    if j - i < len(word) and word[i:j] in lookup:
                        dp[j] = True

                if dp[len(word)]:
                    result.append(word)
                    break
        return result

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''

# Thought:
1.
# Do you still remember how did you solve this problem? https://leetcode.com/problems/word-break/
#
# If you do know one optimized solution for above question is using DP,
# this problem is just one more step further.
# We iterate through each word and see if it can be formed by using other words.
#
# Of course it is also obvious that a word can only be formed by words shorter than it.
# So we can first sort the input by length of each word,
# and only try to form one word by using words in front of it.
# DP
# 341ms 25.80%
class Solution {
    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        List<String> result = new ArrayList<>();
        Set<String> preWords = new HashSet<>();
        Arrays.sort(words, ((String s1, String s2) -> s1.length() - s2.length()));
        /* lambda for
        Arrays.sort(words, new Comparator<String>() {
            public int compare (String s1, String s2) {
                return s1.length() - s2.length();
            }
        });
        */

        for (int i = 0; i < words.length; i++) {
            if (canForm(words[i], preWords)) {
                result.add(words[i]);
            }
            preWords.add(words[i]);
        }
        return result;
    }

    private static boolean canForm(String word, Set<String> dict) {
        if (dict.isEmpty()) return false;
        boolean[] dp = new boolean[word.length() + 1];
        dp[0] = true;
        for (int i = 0 ; i <= word.length(); i++) {
            for (int j = 0; j < i; j++) {
                if (!dp[j]) continue;
                if (dict.contains(word.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[word.length()];
    }
}

2.
# Trie
# 65ms 81.02%
class Solution {
    private final static int R = 26;
    private Node mRoot = new Node();

    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        List<String> res = new ArrayList<>();
        if (words == null || words.length == 0) return res;
        for (String word: words) { addWords(word);}
        for (String word : words) {
            if (isConcatenated(word, 0, 0)) res.add(word);
        }
        return res;
    }

    private boolean isConcatenated(String word, int idx, int counts) {
        Node node = mRoot;

        for (int i = idx; i < word.length() ;i++) {
            char c = word.charAt(i);
            if (node.mKey[c - 'a'] == null) return false;
            if (node.mKey[c - 'a'].mIsWord) {
                if ( i == word.length() - 1) return counts >= 1;
                if (isConcatenated(word, i + 1, counts + 1)) return true;
            }
            node = node.mKey[c - 'a'];
        }
        return false;
    }

    private void addWords(String word) {
        Node node = mRoot;
        for (char c : word.toCharArray()) {
            if (node.mKey[c - 'a'] == null) {
                node.mKey[c - 'a'] = new Node();
            }
            node = node.mKey[c - 'a'];
        }
        node.mIsWord = true;
    }

    class Node{
        boolean mIsWord;
        Node[] mKey;
        public Node() {
            mIsWord = false;
            mKey = new Node[R];
        }
    }
}

# Trie + DFS
# 59ms 89.13%
class Solution {
    private TrieNode root;
    private List<String> result;

    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        root = new TrieNode();
        result = new ArrayList<>();

        for (String word : words) {
            addWord(word);
        }
        dfs(root, 0);
        return result;
    }

    class TrieNode {
        TrieNode[] children;
        String word;
        boolean isEnd;
        boolean combo; //if this word is a combination of simple words
        boolean added; //if this word is already added in result
        public TrieNode() {
            this.children = new TrieNode[26];
            this.word = new String();
            this.isEnd = false;
            this.combo = false;
            this.added = false;
        }
    }

    private void addWord(String str) {
        if (str == null || str.length() == 0) return;
        TrieNode node = root;
        for (char c : str.toCharArray()) {
            if (node.children[c-'a'] == null) {
                node.children[c-'a'] = new TrieNode();
            }
            node = node.children[c-'a'];
        }
        node.isEnd = true;
        node.word = str;
    }

    private void dfs(TrieNode node, int multi) {
        //multi counts how many single words combined in this word
        if (node.isEnd && !node.added && multi > 1) {
            node.combo = true;
            node.added = true;
            result.add(node.word);
        }
        searchWord(node, root, multi);
    }

    private void searchWord(TrieNode node1, TrieNode node2, int multi) {
        if (node2.combo) return;
        if (node2.isEnd) {
            //take the pointer of node2 back to root
            dfs(node1, multi+1);
        }
        for (int i = 0; i < 26 ; i++) {
            if (node1.children[i] != null && node2.children[i] != null) {
                searchWord(node1.children[i], node2.children[i], multi);
            }
        }
    }
}

'''