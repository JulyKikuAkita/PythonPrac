__source__ = 'https://leetcode.com/problems/word-search-ii/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/word-search-ii.py
# Time:  O(m * n * l)
# Space: O(l)
#
# Description: Leetcode # 212. Word Search II
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
#
# Return ["eat","oath"].
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.
# Companies
# Microsoft Google Airbnb
# Related Topics
# Backtracking Trie
# Similar Questions
# Word Search
#
import unittest
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

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

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


# 93.23% 20ms
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

    //# //same as but this is only 59.98% 27ms
    //# board[i][j] = '#';
    //# for (int[] direction : DIRECTIONS) {
    //#     int newI = i + direction[0];
    //#     int newJ = j + direction[1];
    //#     if (newI >= 0 && newI < board.length && newJ >= 0 && newJ < board[0].length && board[newI][newJ] != '#') {
    //#         dfs(board, newI, newJ, p, res);
    //#     }
    //# }
    //# board[i][j] = c;
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
#63.94% 26ms

public class Solution {
    private static final int[][] DIRECTIONS = new int[][] {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    public List<String> findWords(char[][] board, String[] words) {
        List<String> result = new ArrayList<>();
        TrieNode root = new TrieNode();
        int m = board.length;
        int n = m == 0 ? 0 : board[0].length;
        if (m == 0 || n == 0) {
            return result;
        }
        for (String word : words) {
            addWord(root, word);
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                dfs(board, m, n, i, j, result, root);
            }
        }
        return result;
    }

    private void dfs(char[][] board, int m, int n, int i, int j, List<String> result, TrieNode node) {
        char c = board[i][j];
        if (node.children[c - 'a'] == null) {
            return;
        }
        board[i][j] = '#';
        node = node.children[c - 'a'];
        if (node.word != null) {
            result.add(node.word);
            node.word = null;
        }
        for (int[] direction : DIRECTIONS) {
            int newI = i + direction[0];
            int newJ = j + direction[1];
            if (newI >= 0 && newI < m && newJ >= 0 && newJ < n && board[newI][newJ] != '#') {
                dfs(board, m, n, newI, newJ, result, node);
            }
        }
        board[i][j] = c;
    }

    private void addWord(TrieNode root, String word) {
        for (int i = 0; i < word.length(); i++) {
            int index = word.charAt(i) - 'a';
            if (root.children[index] == null) {
                root.children[index] = new TrieNode();
            }
            root = root.children[index];
        }
        root.word = word;
    }

    private class TrieNode {
        private TrieNode[] children;
        private String word;
        TrieNode() {
            children = new TrieNode[26];
        }
    }
}

#99.63%  17ms
public class Solution {
    class Node{
        Node[] child;
        Node parent;
        String s;
        int count;
        public Node(){
            this.child=new Node[26];
            this.count=0;
        }
    }
    public void buildTrie(String s,Node root){
        Node curr=root;
        for(int i=0;i<s.length();i++){
            curr.count++;
            char ch=s.charAt(i);
            if(curr.child[ch-'a']==null){
                curr.child[ch-'a']=new Node();
                curr.child[ch-'a'].parent=curr;
            }
            curr=curr.child[ch-'a'];
        }
        curr.s=s;
    }

    public List<String> findWords(char[][] board, String[] words) {
        Node root=new Node();
        for(int i=0;i<words.length;i++){
            buildTrie(words[i],root);
        }
        boolean[][] visited=new boolean[board.length][board[0].length];
        List<String> res=new ArrayList<String>();
        for(int i=0;i<board.length;i++){
            for(int j=0;j<board[0].length;j++){
                search(board,i,j,root,visited,res);
            }
        }
        return res;
    }
    public void search(char[][] board,int r,int c,Node curr,boolean[][] visited,List<String> res){
        if(curr==null||curr.child[board[r][c]-'a']==null||curr.count==0){
            return ;
        }
        if(curr.child[board[r][c]-'a'].s!=null){
            res.add(curr.child[board[r][c]-'a'].s);
            curr.child[board[r][c]-'a'].s=null;
            Node temp=curr;
            while(temp!=null){
                temp.count--;
                temp=temp.parent;
            }
        }
        visited[r][c]=true;
        curr=curr.child[board[r][c]-'a'];
        if(r-1>=0&&!visited[r-1][c]){
            search(board,r-1,c,curr,visited,res);
        }
        if(r+1<board.length&&!visited[r+1][c]){
            search(board,r+1,c,curr,visited,res);
        }
        if(c-1>=0&&!visited[r][c-1]){
            search(board,r,c-1,curr,visited,res);
        }
        if(c+1<board[0].length&&!visited[r][c+1]){
            search(board,r,c+1,curr,visited,res);
        }
        visited[r][c]=false;
    }
}
'''