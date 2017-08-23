__author__ = 'https://leetcode.com/problems/implement-trie-prefix-tree/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/implement-trie-prefix-tree.py
# Time:  O(n), per operation
# Space: O(1)
#
# Description: Leetcode # 208. Implement Trie (Prefix Tree)
#
# Implement a trie with insert, search, and startsWith methods.
#
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.
#
# Companies
# Google Uber Facebook Twitter Microsoft Bloomberg
# Related Topics
# Design Trie
# Similar Questions
# Add and Search Word - Data structure design Design Search Autocomplete System Replace Words
#
import unittest
class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.is_string = False
        self.leaves = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        cur = self.root
        for c in word:
            if not c in cur.leaves:
                cur.leaves[c] = TrieNode()
            cur = cur.leaves[c]
        cur.is_string = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        res, node = self.childSearch(word)
        if res:
            return node.is_string
        return False

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        return self.childSearch(prefix)[0]

    def childSearch(self, word):
        cur = self.root
        for c in word:
            if c in cur.leaves:
                cur = cur.leaves[c]
            else:
                return False, None
        return True, cur

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
Thought: https://leetcode.com/articles/implement-trie-prefix-tree/
#98.46% 154ms
public class Trie {
    TrieNode root;
    /** Initialize your data structure here. */
    public Trie() {
        root = new TrieNode();
    }

    /** Inserts a word into the trie. */
    public void insert(String word) {
        TrieNode cur = root;
        for (char c : word.toCharArray()) {
            if (cur.children[c -'a'] == null) {
                cur.children[c -'a'] = new TrieNode();
            }
            cur = cur.children[c -'a'];
        }
        cur.isWord = true;
        cur.word = word;
    }

    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        TrieNode node = findNode(word);
        return node != null && node.isWord;
    }

    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        TrieNode node = findNode(prefix);
        return node != null;
    }

    private TrieNode findNode(String word) {
        TrieNode cur = root;
        for (char c : word.toCharArray()) {
            if (cur.children[c -'a'] == null) {
                return null;
            }
            cur = cur.children[c -'a'];
        }
        return cur;
    }

    class TrieNode{
        TrieNode[] children;
        boolean isWord;
        String word;

        public TrieNode() {
            children = new TrieNode[26];
            isWord = false;
            word = null;
        }
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */

fullway:

#71.90% 177ms
class TrieNode {

    // R links to node children
    private TrieNode[] links;

    private final int R = 26;

    private boolean isEnd;

    public TrieNode() {
        links = new TrieNode[R];
    }

    public boolean containsKey(char ch) {
        return links[ch -'a'] != null;
    }
    public TrieNode get(char ch) {
        return links[ch -'a'];
    }
    public void put(char ch, TrieNode node) {
        links[ch -'a'] = node;
    }
    public void setEnd() {
        isEnd = true;
    }
    public boolean isEnd() {
        return isEnd;
    }
}

class Trie {
    private TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    // Inserts a word into the trie.
    public void insert(String word) {
        TrieNode node = root;
        for (int i = 0; i < word.length(); i++) {
            char currentChar = word.charAt(i);
            if (!node.containsKey(currentChar)) {
                node.put(currentChar, new TrieNode());
            }
            node = node.get(currentChar);
        }
        node.setEnd();
    }

    // search a prefix or whole key in trie and
    // returns the node where search ends
    private TrieNode searchPrefix(String word) {
        TrieNode node = root;
        for (int i = 0; i < word.length(); i++) {
           char curLetter = word.charAt(i);
           if (node.containsKey(curLetter)) {
               node = node.get(curLetter);
           } else {
               return null;
           }
        }
        return node;
    }

    // Returns if the word is in the trie.
    public boolean search(String word) {
       TrieNode node = searchPrefix(word);
       return node != null && node.isEnd();
    }

    // Returns if there is any word in the trie
    // that starts with the given prefix.
    public boolean startsWith(String prefix) {
        TrieNode node = searchPrefix(prefix);
        return node != null;
    }
}

# Use hashmap
# 17.13%, 223ms
class Trie {
    private class TrieNode {
        char c;
        HashMap<Character, TrieNode> children = new HashMap<>();
        boolean hasWord;
        public TrieNode() {

        }

        public TrieNode(char c) {
            this.c = c;
        }
    }

    private TrieNode root;
    /** Initialize your data structure here. */
    public Trie() {
        root = new TrieNode();
    }

    /** Inserts a word into the trie. */
    public void insert(String word) {
        if (word.length() == 0) {
            return;
        }

        if (search(word)) {
            return;
        }

        TrieNode curt = root;
        HashMap<Character, TrieNode> curtChildren = curt.children;
        char[] wordArr = word.toCharArray();
        for (int i = 0; i < wordArr.length; i++) {
            char curtChar = wordArr[i];
            if (!curtChildren.containsKey(curtChar)) {
                curtChildren.put(curtChar, new TrieNode(curtChar));
            }

            curt = curtChildren.get(curtChar);
            curtChildren = curt.children;

            if (i == wordArr.length - 1) {
                curt.hasWord = true;
            }
        }
    }

    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        TrieNode node = searchNode(word);
        if (node == null || !node.hasWord) {
            return false;
        }

        return true;
    }

    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        TrieNode node = searchNode(prefix);
        if (node != null) {
            return true;
        }

        return false;
    }

    private TrieNode searchNode(String word) {
        TrieNode curt = root;
        HashMap<Character, TrieNode> curtChildren = curt.children;
        char[] wordArr = word.toCharArray();
        for (int i = 0; i < wordArr.length; i++) {
            char curtChar = wordArr[i];
            if (!curtChildren.containsKey(curtChar)) {
                return null;
            }

            curt = curtChildren.get(curtChar);
            curtChildren = curt.children;
        }

        return curt;
    }
}
'''