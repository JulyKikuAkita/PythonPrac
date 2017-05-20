__author__ = 'July'
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
#
#  Microsoft Airbnb Google
# Backtracking Trie
# leetcode OT
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
js = '''
#trie
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