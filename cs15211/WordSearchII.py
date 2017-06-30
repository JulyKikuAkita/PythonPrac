__source__ = 'https://leetcode.com/problems/word-search-ii/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/word-search-ii.py
# Time:  O(m * n * l)
# Space: O(l)
#
# Given a 2D board and a list of words from the dictionary, find all words in the board.
#
# Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells
# are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
#
# For example,
# Given words = ["oath","pea","eat","rain"] and board =
#
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# Return ["eat","oath"].
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.
# Companines
# Microsoft Google Airbnb
# Related Topics
# Backtracking Trie
# Similar question
# Word Search
#
class Trie(object):
    def __init__(self):
        self.isWord = False
        self.children = {}

    def insert(self, word):
        cur = self
        for w in word:
            if w not in cur.children:
                cur.children[w] = Trie()
            cur = cur.children[w]
        cur.isWord = True

class Solution(object):
    dir = (0,1), (0,-1), (1,0), (-1,0)
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        visited = [[False for j in xrange(len(board[0]))] for i in xrange(len(board))]
        root = Trie()
        for word in words:
            root.insert(word)

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                self.dfs(board, i, j, root, res, [], visited)
        return res

    def dfs(self, board, i, j, root,  res, tmp , visited):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j]:
            return
        if board[i][j] not in root.children:
            return

        tmp.append(board[i][j])
        trie_node = root.children[board[i][j]]
        if trie_node.isWord:
            res.append("".join(tmp))
            trie_node.isWord = False

        visited[i][j] = True;
        for d in self.dir:
            x = i + d[0]
            y = j + d[1]
            self.dfs(board, x, y, trie_node, res, tmp, visited)
        tmp.pop()
        visited[i][j] = False;


class Solution2(object):
    dir = (0,1), (0,-1), (1,0), (-1,0)
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        res = {}
        visited = [[False for j in xrange(len(board[0]))] for i in xrange(len(board))]
        root = Trie()
        for word in words:
            root.insert(word)

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                self.dfs(board, i, j, root, res, [], visited)
        return res.keys()

    def dfs(self, board, i, j, root,  res, tmp , visited):
        #if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j]:
        #    return
        if board[i][j] not in root.children:
            return
        tmp.append(board[i][j])
        trie_node = root.children[board[i][j]]
        if trie_node.isWord:
            res["".join(tmp)] = True
            #trie_node.isWord = False

        visited[i][j] = True;
        for d in self.dir:
            x = i + d[0]
            y = j + d[1]
            if x >= 0 and x < len(board) and y >= 0 and y < len(board[0]) and not visited[x][y]:
                self.dfs(board, x, y, trie_node, res, tmp, visited)
        tmp.pop()
        visited[i][j] = False;

#java
Java = '''
Thought: https://discuss.leetcode.com/topic/14256/my-simple-and-clean-java-code-using-dfs-and-trie
https://discuss.leetcode.com/topic/33246/java-15ms-easiest-solution-100-00

Backtracking + Trie
Intuitively, start from every cell and try to build a word in the dictionary.
Backtracking (dfs) is the powerful way to exhaust every possible ways.
Apparently, we need to do pruning when current character is not in any word.

How do we instantly know the current character is invalid? HashMap?
How do we instantly know what's the next valid character? LinkedList?
But the next character can be chosen from a list of characters. "Mutil-LinkedList"?
Combing them, Trie is the natural choice. Notice that:

TrieNode is all we need. search and startsWith are useless.
No need to store character at TrieNode. c.next[i] != null is enough.
Never use c1 + c2 + c3. Use StringBuilder.
No need to use O(n^2) extra space visited[m][n].
No need to use StringBuilder. Storing word itself at leaf node is enough.
No need to use HashSet to de-duplicate. Use "one time search" trie.
For more explanations, check out dietpepsi's blog.

Code Optimization
UPDATE: Thanks to @dietpepsi we further improved from 17ms to 15ms.

59ms: Use search and startsWith in Trie class like this popular solution.
33ms: Remove Trie class which unnecessarily starts from root in every dfs call.
30ms: Use w.toCharArray() instead of w.charAt(i).
22ms: Use StringBuilder instead of c1 + c2 + c3.
20ms: Remove StringBuilder completely by storing word instead of boolean in TrieNode.
20ms: Remove visited[m][n] completely by modifying board[i][j] = '#' directly.
18ms: check validity, e.g., if(i > 0) dfs(...), before going to the next dfs.
17ms: De-duplicate c - a with one variable i.
15ms: Remove HashSet completely. dietpepsi's idea is awesome.
The final run time is 15ms. Hope it helps!

The final run time is 15ms. Hope it helps!

# 24ms, 76%
public List<String> findWords(char[][] board, String[] words) {
    List<String> res = new ArrayList<>();
    TrieNode root = buildTrie(words);
    for (int i = 0; i < board.length; i++) {
        for (int j = 0; j < board[0].length; j++) {
            dfs (board, i, j, root, res);
        }
    }
    return res;
}

public void dfs(char[][] board, int i, int j, TrieNode p, List<String> res) {
    char c = board[i][j];
    if (c == '#' || p.next[c - 'a'] == null) return;
    p = p.next[c - 'a'];
    if (p.word != null) {   // found one
        res.add(p.word);
        p.word = null;     // de-duplicate
    }

    board[i][j] = '#';
    if (i > 0) dfs(board, i - 1, j ,p, res);
    if (j > 0) dfs(board, i, j - 1, p, res);
    if (i < board.length - 1) dfs(board, i + 1, j, p, res);
    if (j < board[0].length - 1) dfs(board, i, j + 1, p, res);
    board[i][j] = c;

    //same as
    #   board[i][j] = '#';
    #     for (int[] direction : DIRECTIONS) {
    #         int newI = i + direction[0];
    #         int newJ = j + direction[1];
    #         if (newI >= 0 && newI < m && newJ >= 0 && newJ < n && board[newI][newJ] != '#') {
    #             dfs(board, m, n, newI, newJ, result, node);
    #         }
    #     }
    #   board[i][j] = c;
}

public TrieNode buildTrie(String[] words) {
    TrieNode root = new TrieNode();
    for (String w : words) {
        TrieNode p = root;
        for (char c : w.toCharArray()) {
            int i = c - 'a';
            if (p.next[i] == null) p.next[i] = new TrieNode();
            p = p.next[i];
       }
       p.word = w;
    }
    return root;
}

class TrieNode {
    TrieNode[] next = new TrieNode[26];
    String word;
}

#######################################################################
#trie
#27ms 64%

public class Solution {
    public static final int[][] directions = new int[][] {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    public List<String> findWords(char[][] board, String[] words) {
        List<String> result = new ArrayList<>();
        if (board.length == 0 || words.length == 0) {
            return result;
        }
        int m = board.length;
        int n = board[0].length;
        Trie trie = new Trie();
        for (String word : words) {
            trie.addWord(word);
        }
        boolean[][] visited = new boolean[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                dfs(board, m, n, i, j, new StringBuilder(), trie.root, visited, result);
            }
        }
        return result;
    }

    private void dfs(char[][] board, int m, int n, int i, int j, StringBuilder sb, TrieNode node,
                        boolean[][] visited, List<String> result) {
        node = node.children[board[i][j] - 'a'];
        if (node == null) {
            return;
        }
        sb.append(board[i][j]);
        if (node.isWord) {
            result.add(sb.toString());
            node.isWord = false;
            // return  <- cannot return , fails below case
                                            // ["ab","cd"]
                                            // ["ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"]
        }
        visited[i][j] = true;
        for (int[] direction : directions) {
            int newI = i + direction[0];
            int newJ = j + direction[1];
            if (newI >= 0 && newI < m && newJ >= 0 && newJ < n && !visited[newI][newJ]) {
                dfs(board, m, n, newI, newJ, sb, node, visited, result);
            }
        }
        visited[i][j] = false;
        sb.deleteCharAt(sb.length() - 1);
    }
}

class TrieNode {
    public TrieNode[] children;
    public boolean isWord;

    public TrieNode() {
        children = new TrieNode[26];
        isWord = false;
    }
}

class Trie {
    public TrieNode root;

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
}
'''