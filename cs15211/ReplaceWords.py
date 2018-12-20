__source__ = 'https://leetcode.com/problems/replace-words/'
# Time:  O(m) words in sentences
# Space: O(m) words in sentences
#
# Description: Leetcode # 648. Replace Words
#
# In English, we have a concept called root, which can be followed by some other words
# to form another longer word - let's call this word successor.
# For example, the root an, followed by other, which can form another word another.
#
# Now, given a dictionary consisting of many roots and a sentence.
# You need to replace all the successor in the sentence with the root forming it.
# If a successor has many roots can form it, replace it with the root with the shortest length.
#
# You need to output the sentence after the replacement.
#
# Example 1:
# Input: dict = ["cat", "bat", "rat"]
# sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"
# Note:
# The input will only have lower-case letters.
# 1 <= dict words number <= 1000
# 1 <= sentence words number <= 1000
# 1 <= root length <= 100
# 1 <= sentence words length <= 1000
# Companies
# Uber
# Related Topics
# Hash Table Trie
# Similar Questions
# Implement Trie (Prefix Tree)

import collections
import unittest
# 1. We can check the prefixes directly. For each word in the sentence,
# we'll look at successive prefixes and see if we saw them before.
# 2. We could also use a trie. We'll insert each root in the trie.
# Then, for each word in the sentence,
# we'll replace it with the first root we encounter upon traversal of the trie.
#
# 304ms 32.65%
class Solution1(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        rootset = set(dict)

        def replace(word):
            for i in xrange(1, len(word)):
                if word[:i] in rootset:
                    return word[:i]
            return word

        return " ".join(map(replace, sentence.split()))

# 136ms
class Solution2(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()
        END = True
        for root in dict:
            cur = trie
            for letter in root:
                cur = cur[letter]
            cur[END] = root

        def replace(word):
            cur = trie
            for letter in word:
                if letter not in cur: break
                cur = cur[letter]
                if END in cur:
                    return cur[END]
            return word

        return " ".join(map(replace, sentence.split()))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/replace-words/solution/

1. Hashset:
# 222ms 18.78%
class Solution {
    public String replaceWords(List<String> dict, String sentence) {
        if (dict == null || dict.size() == 0) return sentence;
        Set<String> set = new HashSet<>();
        for (String s : dict) set.add(s);

        StringBuilder sb = new StringBuilder();
        String[] words = sentence.split("\\s+");

        for (String word : words) {
            String prefix = "";
            for (int i = 1; i <= word.length(); i++) {
                prefix = word.substring(0, i);
                if (set.contains(prefix)) break;
            }
            sb.append(" " + prefix);
        }
        return sb.deleteCharAt(0).toString(); //otherwise " the cat was rat by the bat"
    }
}

# 22ms 71.41%
class Solution {
    public String replaceWords(List<String> dict, String sentence) {
        String[] tokens = sentence.split(" ");
        TrieNode trie = buildTrie(dict);
        return replaceWords(tokens, trie);
    }

    private String replaceWords(String[] tokens, TrieNode root) {
        StringBuilder stringBuilder = new StringBuilder();
        for (String token : tokens) {
            stringBuilder.append(getShortestReplacement(token, root));
            stringBuilder.append(" ");
        }
        return stringBuilder.substring(0, stringBuilder.length()-1);
    }

    private String getShortestReplacement(String token, final TrieNode root) {
        TrieNode temp = root;
        StringBuilder stringBuilder = new StringBuilder();
        for (char c : token.toCharArray()) {
            stringBuilder.append(c);
            if (temp.children[c - 'a'] != null) {
                if (temp.children[c - 'a'].isWord) {
                    return stringBuilder.toString();
                }
                temp = temp.children[c - 'a'];
            } else {
                return token;
            }
        }
        return token;
    }

    private TrieNode buildTrie(List<String> dict) {
        TrieNode root = new TrieNode();
        for (String word : dict) {
            TrieNode temp = root;
            for (char c : word.toCharArray()) {
                if (temp.children[c - 'a'] == null) {
                    temp.children[c - 'a'] = new TrieNode();
                }
                temp = temp.children[c - 'a'];
            }
            temp.isWord = true;
        }
        return root;
    }

    public class TrieNode {
        TrieNode[] children;
        boolean isWord;

        public TrieNode() {
            this.children = new TrieNode[26];
            this.isWord = false;
        }
    }
}

# Trie, build tree with dfs
# 112ms 29.31%
class Solution {
    public String replaceWords(List<String> dict, String sentence) {
        Trie trie = new Trie(256); //cannot use 26, array out of bound when build tree
        dict.forEach(s -> trie.buildTree(s));
        List<String> res = new ArrayList<>();
        Arrays.stream(sentence.split(" ")).forEach(str -> res.add(trie.getPrefix(str)));
        return res.stream().collect(Collectors.joining(" "));
    }

    class Trie{
        int R;
        TrieNode root;

        public Trie(int r) {
            R = r;
            root = new TrieNode();
        }

        public String getPrefix(String word) {
            int len = searchWordDFS(root, word, -1);
            return len < 1 ? word : word.substring(0, len);
        }

        private int searchWordDFS(TrieNode root, String word, int res) {
            if (root == null || word.isEmpty()) return 0;
            if (root.isWord) return res + 1;
            return searchWordDFS(root.map[word.charAt(0)], word.substring(1), res + 1);
        }

        public void buildTree(String word) {
            buildTreeDFS(root, word);
        }

        private void buildTreeDFS(TrieNode root, String word) {
            if (word.isEmpty()) {
                root.isWord = true;
                return;
            }
            if (root.map[word.charAt(0)] == null) root.map[word.charAt(0)] = new TrieNode();
            buildTreeDFS(root.map[word.charAt(0)], word.substring(1));
        }

        private class TrieNode{
            TrieNode[] map;
            boolean isWord;
            public TrieNode() {
                map = new TrieNode[R];
                isWord = false;
            }
        }
    }
}
'''
