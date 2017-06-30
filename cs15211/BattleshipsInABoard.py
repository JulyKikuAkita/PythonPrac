__source__ = 'https://github.com/kamyu104/LeetCode/blob/master/Python/battleships-in-a-board.py'
# Time:  O(m * n)
# Space: O(1)
#
#
# Description:
# Given an 2D board, count how many different battleships are in it.
# The battleships are represented with 'X's, empty slots are represented with '.'s.
# You may assume the following rules:
#
# You receive a valid board, made of only battleships or empty slots.
# Battleships can only be placed horizontally or vertically. In other words,
# they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column),
# where N can be of any size.
# At least one horizontal or vertical cell separates between two battleships -
# there are no adjacent battleships.
#
# Example:
# X..X
# ...X
# ...X
# In the above board there are 2 battleships.
# Invalid Example:
# ...X
# XXXX
# ...X
# This is not a valid board - as battleships will always have a cell separating between them.
# Your algorithm should not modify the value of the board.
# Follow up:
# Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?
#
# Hide Company Tags Microsoft

import unittest

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board or not board[0]:
            return 0

        cnt = 0
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                cnt += int(board[i][j] == 'X' and \
                       (i == 0 or board[i - 1][j] != 'X') and \
                       (j == 0 or board[i][j - 1] != 'X'))
        return cnt

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
Going over all cells, we can count only those that are the "first" cell of the battleship.
First cell will be defined as the most top-left cell. We can check for first cells by only counting cells
that do not have an 'X' to the left and do not have an 'X' above them.

public class Solution {
    public int countBattleships(char[][] board) {
        if (board == null || board.length == 0) return 0;
        int m = board.length, n = board[0].length;
        int count = 0;

        for (int i = 0; i < m ;i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == '.') continue;
                if (i > 0 && board[i-1][j] == 'X') continue;
                if (j > 0 && board[i][j-1] == 'X') continue;
                count++;
            }
        }
        return count;
    }

    public int countBattleships2(char[][] board) {
        if (board == null || board.length == 0 || board[0].length == 0) return 0;
        int R = board.length, C = board[0].length, cnt = 0;
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (board[i][j] == 'X'
                    && (i == 0 || board[i - 1][j] == '.')
                    && (j == 0 || board[i][j - 1] == '.'))
                    cnt++;
            }
        }

        return cnt;
    }
}
'''