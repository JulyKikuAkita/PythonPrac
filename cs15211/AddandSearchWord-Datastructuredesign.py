__source__ = 'https://leetcode.com/problems/add-and-search-word-data-structure-design/description/'
# Time:  O(min(n, h)), per operation
# Space: O(min(n, h))
#
# Description: Leetcode # 211. Add and Search Word - Data structure design
#
# Design a data structure that supports the following two operations:
#
# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string containing only letters a-z or ..
# A . means it can represent any one letter.
#
# For example:
#
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# Note:
# You may assume that all words are consist of lowercase letters a-z.
#
# You should be familiar with how a Trie works. If not, please work on this problem: Implement Trie (Prefix Tree) first.
# Companies
# Facebook
# Related Topics
# Backtracking Trie Design
# Similar Questions
# Implement Trie (Prefix Tree)
#
import unittest
class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.is_string = False
        self.leaves = {}

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        curr = self.root
        for c in word:
            if not c in curr.leaves:
                curr.leaves[c] = TrieNode()
            curr = curr.leaves[c]
        curr.is_string = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        return self.searchHelper(word, 0, self.root)

    def searchHelper(self, word, start, curr):
        if start == len(word):
            return curr.is_string
        if word[start] in curr.leaves:
            return self.searchHelper(word, start+1, curr.leaves[word[start]])
        elif word[start] == '.':
            for c in curr.leaves:
                if self.searchHelper(word, start+1, curr.leaves[c]):
                    return True

        return False

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: Trie
#
#41.50% 138ms  //implement TrieNode with map
public class WordDictionary {
    Trie root;

    public WordDictionary(){
        root = new Trie();
    }
    // Adds a word into the data structure.
    public void addWord(String word) {
        Trie cur = root;
        for(Character c: word.toCharArray()){
            if (cur.child.get(c) == null){
                cur.child.put(c, new Trie());
            }
            cur = cur.child.get(c);
        }
        cur.isEnd = true;
    }

    // Returns if the word is in the data structure. A word could
    // contain the dot character '.' to represent any one letter.
    public boolean search(String word) {
        Trie cur = root;
        return dfs(word, cur, 0);

    }

    private boolean dfs(String word, Trie cur, int idx){
        if( idx == word.length()){
            return cur.isEnd;
        }
        if(cur.child.get(word.charAt(idx)) != null){
            return dfs(word, cur.child.get(word.charAt(idx)), idx + 1);
        }else if(word.charAt(idx) == '.'){
            for(Trie node : cur.child.values()){
                if(dfs(word, node, idx + 1)){
                    return true;
                }
            }
        }
        return false;
    }
}

// Your WordDictionary object will be instantiated and called as such:
// WordDictionary wordDictionary = new WordDictionary();
// wordDictionary.addWord("word");
// wordDictionary.search("pattern");

class Trie{
    Map<Character, Trie> child;
    boolean isEnd;
    public Trie(){
        child = new HashMap<>();
        isEnd = false;
    }
}

#######################################################################################################################
#91.87% 102ms

class WordDictionary {
    private TrieNode root;

    /** Initialize your data structure here. */
    public WordDictionary() {
        root = new TrieNode();
    }

    /** Adds a word into the data structure. */
    public void addWord(String word) {
        TrieNode cur = root;
        for (int i = 0; i < word.length(); i++) {
            int index = word.charAt(i) - 'a';
            if (cur.children[index] == null) {
                cur.children[index] = new TrieNode();
            }
            cur = cur.children[index];
        }
        cur.isWord = true;
    }

    /** Returns if the word is in the data structure.
    A word could contain the dot character '.' to represent any one letter. */
    public boolean search(String word) {
        return search(word, 0, root);
    }

    private boolean search(String word, int wordIndex, TrieNode cur) {
        for (int i = wordIndex; i < word.length(); i++) {
            char c = word.charAt(i);
            if (c == '.') {
                //for (int j = 0; j < cur.children.length; j++) {
                for(char ch = 'a'; ch <= 'z'; ch++){
                    if (cur.children[ch - 'a'] != null && search(word, i + 1, cur.children[ch - 'a'])) {
                        return true;
                    }
                }
                return false;
            } else {
                cur = cur.children[c - 'a'];
                if (cur == null) {
                    return false;
                }
            }
        }
        return cur.isWord;
    }

    private class TrieNode {
        private TrieNode[] children;
        private boolean isWord;

        TrieNode() {
            children = new TrieNode[26];
        }
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */

#######################################################################################################################
# 124ms 56.48%
class WordDictionary {

    class Node{
        Node next[] = new Node[26];
        String word;
    }
    Node root;
    /** Initialize your data structure here. */
    public WordDictionary() {
        root = new Node();
    }

    /** Adds a word into the data structure. */
    public void addWord(String word) {
        Node p = root;
        for(char ch : word.toCharArray()){
            int i = ch - 'a';
            if(null == p.next[i]){
                p.next[i] = new Node();
            }
            p = p.next[i];
        }
        p.word = word;
    }

    /** Returns if the word is in the data structure.
    A word could contain the dot character '.' to represent any one letter. */
    public boolean search(String word) {
        return search(word.toCharArray(),0,root);
    }

    public static boolean search(char[] w, int n, Node node){
        if(w.length == n)
            return null != node.word;
        if('.' != w[n]){
            return node.next[w[n]-'a'] != null && search(w,n+1,node.next[w[n]-'a']);
        }else{
            for(int i = 0; i < 26; i++){
                if(null != node.next[i]){
                    if(search(w,n+1,node.next[i]))
                        return true;
                }
            }
        }
    return false;
    }
}
'''