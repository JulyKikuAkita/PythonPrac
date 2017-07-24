__source__ = 'https://leetcode.com/problems/word-search/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/word-search.py
# Time:  O(m * n * 3^p)
# Space: O(m * n + p)
# DFS
# floodfill
#
# Description: Leetcode # 79. Word Search
#
# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring.
# The same letter cell may not be used more than once.
#
# For example,
# Given board =
#
# [
#   "ABCE",
#   "SFCS",
#   "ADEE"
# ]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.
#
# Companines
# Microsoft Bloomberg Facebook
# Related Topics
# Array Backtracking
# Similar question
# Word Search II
#
import unittest
class SolutionSlow(object):
    dir = (0,1), (0,-1),(1,0),(-1,0)
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        if not board:
            return False

        m = len(board)
        n = len(board[0])
        visited = [[False for _ in xrange(n)] for _ in xrange(m)]

        for i in xrange(m):
            for j in xrange(n):
                if self.dfs(board, word, i, j, visited, 0):
                    return True
        return False

    def dfs(self, board, word, i, j, visited, idx):
        if idx == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j] or idx > len(word) or board[i][j] != word[idx]:
            return False

        visited[i][j] = True
        for p, q in self.dir:
            x= i + p
            y = j + q
            if self.dfs(board, word, x, y, visited, idx + 1) :
                return True
        visited[i][j] = False
        return False

class Solution2:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        visited = [[ False for j in xrange(len(board[0]))] for i in xrange(len(board))]

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.existRecu(board, word, 0, i , j , visited):
                    return True
        return False

    def existRecu(self, board, word, cur, i, j, visited):
        if cur == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j] or board[i][j] != word[cur]:
            return False

        visited[i][j] = True
        result = self.existRecu(board, word, cur + 1, i + 1, j, visited) or \
                 self.existRecu(board, word, cur + 1, i - 1, j, visited) or \
                 self.existRecu(board, word, cur + 1, i , j + 1, visited) or \
                 self.existRecu(board, word, cur + 1, i , j - 1, visited)
        visited[i][j] = False

        return result

# http://www.cnblogs.com/zuoyuan/p/3769767.html
class SolutionOther:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):

        if len(word) == 0:
            return True

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if (self.dfs(i, j, word[1:], board)):
                        return True
        return False


    def dfs(self, x, y, word, board):

        if len(word) == 0:
            return True
        #up
        if x > 0 and board[x-1][y] == word[0]:
            tmp = board[x][y]
            board[x][y] = '#'
            if self.dfs(x-1, y, word[1:], board):
                return True
            board[x][y] = tmp
        #left
        if y > 0 and board[x][y-1] == word[0]:
            tmp = board[x][y]
            board[x][y] = '#'
            if self.dfs(x, y-1, word[1:], board):
                return True
            board[x][y] = tmp

        #down
        if x < len(board) -1 and board[x+1][y] == word[0]:
            tmp = board[x][y]
            board[x][y] = '#'
            if self.dfs(x+1, y, word[1:], board):
                return True
            board[x][y] = tmp


        #right
        if y < len(board[0]) -1 and board[x][y+1] == word[0]:
            tmp = board[x][y]
            board[x][y] = '#'
            if self.dfs(x, y+1, word[1:], board):
                return True
            board[x][y] = tmp


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        board = [
              "ABCE",
              "SFCS",
              "ADEE"
        ]
        print Solution2().exist(board, "ABCCED")
        print Solution2().exist(board, "SFCS")
        print Solution2().exist(board, "ABCB")

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
# DFS
#44.16% 15ms
public class Solution {
    public static final int[][] DIRECTIONS = new int[][] {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    public boolean exist(char[][] board, String word) {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] == word.charAt(0) &&
                    search(board, word, 1, i, j)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean search(char[][] board, String word, int index, int row, int col) {
        if (index == word.length()) {
            return true;
        }
        char c = board[row][col];
        board[row][col] = '*';
        for (int[] direction : DIRECTIONS) {
            int newRow = row + direction[0];
            int newCol = col + direction[1];
            if (newRow >= 0 && newRow < board.length && newCol >= 0 && newCol < board[0].length &&
                board[newRow][newCol] == word.charAt(index)) {
                if (search(board, word, index + 1, newRow, newCol)) {
                    return true;
                }
            }
        }
        board[row][col] = c;
        return false;
    }
}

#BFS + DFS:
# 78.97% 11ms
public class Solution {
    public boolean exist(char[][] board, String word) {
        return bt(board,new boolean[board.length][board[0].length], 0,word,0,0);


    }
    private boolean bt(char[][] board, boolean[][] usd, int index, String word, int row,int col)
    {
        if(index==word.length()) return true;
        else if(index==0)
        {
            for(int i=0;i<board.length;i++)
            {
                for(int j=0;j<board[0].length;j++)
                {
                    if(board[i][j]==word.charAt(0))
                    {
                        usd[i][j] = true;
                        if(bt(board,usd,1,word,i,j)) return true;
                        usd[i][j] = false;
                    }
                }
            }
        }
        else
        {
            char ch = word.charAt(index);
            if(row-1>=0 && !usd[row-1][col] && board[row-1][col] == ch)
            {
                usd[row-1][col] = true;
                if(bt(board,usd,index+1,word,row-1,col)) return true;
                usd[row-1][col] = false;
            }
            if(col-1>=0 && !usd[row][col-1] && board[row][col-1] ==ch)
            {
                usd[row][col-1] = true;
                if(bt(board,usd,index+1,word,row,col-1)) return true;
                usd[row][col-1] = false;
            }
            if(row+1<board.length && !usd[row+1][col] && board[row+1][col] == ch)
            {
                usd[row+1][col] = true;
                if(bt(board,usd,index+1,word,row+1,col)) return true;
                usd[row+1][col] = false;
            }
            if(col+1<board[0].length && !usd[row][col+1] && board[row][col+1] ==ch)
            {
                usd[row][col+1] = true;
                if(bt(board,usd,index+1,word,row,col+1)) return true;
                usd[row][col+1] = false;
            }
            return false;
        }
        return false;
    }
}

# 99.06% 7ms
class Solution {
    public boolean exist(char[][] board, String word) {
        char[] charArray = word.toCharArray();

       for (int x = 0; x < board.length; x ++) {
           for (int y = 0; y < board[x].length; y ++) {
             if (checkNextBit(board, charArray, x, y, 0)) {
                 return true;
             }
           }
       }

        return false;
    }

    private boolean checkNextBit(char[][] board, char[] charArray, int x, int y, int index) {
        if (index == charArray.length) return true;

        if (x < 0 || y < 0 || x == board.length || y == board[0].length) return false;

        if (charArray[index] != board[x][y]) return false;

        board[x][y] ^= 256;
        if (checkNextBit(board, charArray, x + 1, y, index + 1)
           || checkNextBit(board, charArray, x, y + 1, index + 1)
           || checkNextBit(board, charArray, x - 1, y, index + 1)
           || checkNextBit(board, charArray, x, y - 1, index + 1)) {
            return true;
        }
        else {
            board[x][y] ^= 256;
        }

        return false;
    }
}
'''