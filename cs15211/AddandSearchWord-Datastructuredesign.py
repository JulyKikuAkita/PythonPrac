__author__ = 'July'
# Time:  O(min(n, h)), per operation
# Space: O(min(n, h))
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
# Facebook
# Backtracking Trie Design


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

#java
js = '''
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


public class WordDictionary {
    Trie trie;

    public WordDictionary() {
        trie = new Trie();
    }

    // Adds a word into the data structure.
    public void addWord(String word) {
        trie.addWord(word);
    }

    // Returns if the word is in the data structure. A word could
    // contain the dot character '.' to represent any one letter.
    public boolean search(String word) {
        return trie.search(word);
    }
}

class TrieNode {
    TrieNode[] children;
    boolean isWord;
    public TrieNode() {
        children = new TrieNode[26];
    }
}

class Trie {
    TrieNode root;
    public Trie() {
        root = new TrieNode();
    }

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

    public boolean search(String word) {
        return search(word, 0, root);
    }

    public boolean search(String word, int start, TrieNode cur) {
        for (int i = start; i < word.length(); i++) {
            char c = word.charAt(i);
            if (c == '.') {
                for (int j = 0; j < 26; j++) {
                    if (cur.children[j] != null && search(word, i + 1, cur.children[j])) {
                        return true;
                    }
                }
                return false;
            } else {
                int index = c - 'a';
                if (cur.children[index] == null) {
                    return false;
                } else {
                    cur = cur.children[index];
                }
            }
        }
        return cur.isWord;
    }
}

// Your WordDictionary object will be instantiated and called as such:
// WordDictionary wordDictionary = new WordDictionary();
// wordDictionary.addWord("word");
// wordDictionary.search("pattern");
'''