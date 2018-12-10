__source__ = 'https://leetcode.com/problems/design-tic-tac-toe/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/design-tic-tac-toe.py
# Time:  O(1), per move.
# Space: O(n^2)
#
# Description: Leetcode # 348. Design Tic-Tac-Toe
#
# Design a Tic-tac-toe game that is played between two players on a n x n grid.
#
# You may assume the following rules:
#
# A move is guaranteed to be valid and is placed on an empty block.
# Once a winning condition is reached, no more moves is allowed.
# A player who succeeds in placing n of their marks in a horizontal, vertical,
# or diagonal row wins the game.
# Example:
# Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.
#
# TicTacToe toe = new TicTacToe(3);
#
# toe.move(0, 0, 1); -> Returns 0 (no one wins)
# |X| | |
# | | | |    // Player 1 makes a move at (0, 0).
# | | | |
#
# toe.move(0, 2, 2); -> Returns 0 (no one wins)
# |X| |O|
# | | | |    // Player 2 makes a move at (0, 2).
# | | | |
#
# toe.move(2, 2, 1); -> Returns 0 (no one wins)
# |X| |O|
# | | | |    // Player 1 makes a move at (2, 2).
# | | |X|
#
# toe.move(1, 1, 2); -> Returns 0 (no one wins)
# |X| |O|
# | |O| |    // Player 2 makes a move at (1, 1).
# | | |X|
#
# toe.move(2, 0, 1); -> Returns 0 (no one wins)
# |X| |O|
# | |O| |    // Player 1 makes a move at (2, 0).
# |X| |X|
#
# toe.move(1, 0, 2); -> Returns 0 (no one wins)
# |X| |O|
# |O|O| |    // Player 2 makes a move at (1, 0).
# |X| |X|
#
# toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
# |X| |O|
# |O|O| |    // Player 1 makes a move at (2, 1).
# |X|X|X|
# Follow up:
# Could you do better than O(n2) per move() operation?
#
# Companies
# Google Microsoft
# Related Topics
# Design
#

import unittest

class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.__rows = [[0, 0] for _ in xrange(n)]
        self.__cols = [[0, 0] for _ in xrange(n)]
        self.__diagonal = [0, 0]
        self.__anti_diagonal = [0, 0]


    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        i = player - 1
        self.__rows[row][i] += 1
        self.__cols[col][i] += 1
        if row == col:
            self.__diagonal[i] += 1
        if col == len(self.__rows) - row - 1:
            self.__anti_diagonal[i] += 1
        if any([self.__rows[row][i] == len(self.__rows), \
                self.__cols[col][i] == len(self.__cols), \
                self.__diagonal[i] == len(self.__rows), \
                self.__anti_diagonal[i] == len(self.__cols)]):
            return player

        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# 89ms 11.50%
class TicTacToe {
    private int[][] board;
    private int winner;

    /** Initialize your data structure here. */
    public TicTacToe(int n) {
        board = new int[n][n];
    }

    /** Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins. */
    public int move(int row, int col, int player) {
        if (winner != 0) {
            return winner;
        }
        if (board[row][col] != 0) {
            throw new IllegalArgumentException("Invalid move.");
        }
        board[row][col] = player;
        if (isOver(row, col, player)) {
            winner = player;
            return winner;
        } else {
            return 0;
        }
    }

    private boolean isOver(int row, int col, int player) {
        return isRowOver(row, player) || isColOver(col, player) || isDiagonalOver(row, col, player) || isBackwardDiagonalOver(row, col, player);
    }

    private boolean isRowOver(int row, int player) {
        for (int j = 0; j < board[0].length; j++) {
            if (board[row][j] != player) {
                return false;
            }
        }
        return true;
    }

    private boolean isColOver(int col, int player) {
        for (int i = 0; i < board.length; i++) {
            if (board[i][col] != player) {
                return false;
            }
        }
        return true;
    }

    private boolean isDiagonalOver(int row, int col, int player) {
        if (row != col) {
            return false;
        }
        for (int i = 0; i < board.length; i++) {
            if (board[i][i] != player) {
                return false;
            }
        }
        return true;
    }

    private boolean isBackwardDiagonalOver(int row, int col, int player) {
        if (row + col != board.length - 1) {
            return false;
        }
        for (int i = 0; i < board.length; i++) {
            if (board[i][board.length - i - 1] != player) {
                return false;
            }
        }
        return true;
    }
}

/**
 * Your TicTacToe object will be instantiated and called as such:
 * TicTacToe obj = new TicTacToe(n);
 * int param_1 = obj.move(row,col,player);
 */

# 64ms 69.05%
class TicTacToe {

    /** Initialize your data structure here. */
    int[] rows;
    int[] cols;
    int dig;
    int antdig;
    int size;

    public TicTacToe(int n) {
        rows = new int[n];
        cols = new int[n];
        dig = 0;
        antdig = 0;
        size = n;
    }

    /** Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins. */
    public int move(int row, int col, int player) {
        int[] tag = {1, -1};
        rows[row] += tag[player - 1];
        cols[col] += tag[player - 1];

        if (row == col) {
            dig += tag[player - 1];
        }

        if (row + col == size - 1) {
            antdig += tag[player - 1];
        }

        if (rows[row] == size || cols[col] == size || dig == size || antdig == size) {
            return 1;
        }

        if (rows[row] == -size || cols[col] == -size || dig == -size || antdig == -size) {
            return 2;
        }

        return 0;
    }
}
'''