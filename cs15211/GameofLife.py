__source__ = 'https://leetcode.com/problems/game-of-life/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/game-of-life.py
# Time:  O(m * n)
# Space: O(1)
#
# Description: Leetcode # 289. Game of Life
#
# According to the Wikipedia's article:
# "The Game of Life, also known simply as Life,
# is a cellular automaton devised by the British
# mathematician John Horton Conway in 1970."
#
# Given a board with m by n cells, each cell has
# an initial state live (1) or dead (0).
# Each cell interacts with its eight neighbors
# (horizontal, vertical, diagonal)
# using the following four rules
# (taken from the above Wikipedia article):
#
# - Any live cell with fewer than two live neighbors dies,
#   as if caused by under-population.
# - Any live cell with two or three live neighbors lives
#   on to the next generation.
# - Any live cell with more than three live neighbors dies,
#   as if by over-population..
# - Any dead cell with exactly three live neighbors
#   becomes a live cell, as if by reproduction.
#
# Write a function to compute the next state
# (after one update) of the board given its current state.
#
# Follow up:
# - Could you solve it in-place? Remember that the board needs
#   to be updated at the same time: You cannot update some cells
#   first and then use their updated values to update other cells.
# - In this question, we represent the board using a 2D array.
#   In principle, the board is infinite, which would cause problems
#   when the active area encroaches the border of the array.
#   How would you address these problems?
#
# Companies
# Google Snapchat Dropbox Two Sigma
# Related Topics
# Array
# Similar Questions
# Set Matrix Zeroes
#
import unittest
# 32ms 13.72%
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        m = len(board)
        n = len(board[0]) if m else 0

        for i in xrange(m):
            for j in xrange(n):
                count = 0
                ## Count live cells in 3x3 block.
                for I in xrange(max(i-1, 0), min(i+2, m)):
                    for J in xrange(max(j-1, 0), min(j+2, n)):
                        count += board[I][J] & 1

                # if (count == 4 && board[i][j]) means:
                #     Any live cell with three live neighbors lives.
                # if (count == 3) means:
                #     Any live cell with two live neighbors.
                #     Any dead cell with exactly three live neighbors lives.

                if (count == 4 and board[i][j]) or count == 3:
                    board[i][j] |= 2 #Mark as live

        for i in xrange(m):
            for j in xrange(n):
                board[i][j] >>= 1 # Update to the next state

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

To solve it in place, we use 2 bits to store 2 states:

[2nd bit, 1st bit] = [next state, current state]

- 00  dead (next) <- dead (current)
- 01  dead (next) <- live (current)
- 10  live (next) <- dead (current)
- 11  live (next) <- live (current)
In the beginning, every cell is either 00 or 01.
Notice that 1st state is independent of 2nd state.
Imagine all cells are instantly changing from the 1st to the 2nd state, at the same time.
Let's count # of neighbors from 1st state and set 2nd state bit.
Since every 2nd state is by default dead, no need to consider transition 01 -> 00.
In the end, delete every cell's 1st state by doing >> 1.
For each cell's 1st bit, check the 8 pixels around itself, and set the cell's 2nd bit.

Transition 01 -> 11: when board == 1 and lives >= 2 && lives <= 3.
Transition 00 -> 10: when board == 0 and lives == 3.
To get the current state, simply do

board[i][j] & 1
To get the next state, simply do

board[i][j] >> 1

# 1ms 100%
class Solution {
    public void gameOfLife(int[][] board) {
        if (board == null || board.length == 0) return;
        int m = board.length, n = board[0].length;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int lives = liveNeighbors(board, m, n, i, j);

                // In the beginning, every 2nd bit is 0;
                // So we only need to care about when will the 2nd bit become 1.
                if (board[i][j] == 1 && lives >= 2 && lives <= 3) {
                    board[i][j] = 3; // Make the 2nd bit 1: 01 ---> 11
                }
                if (board[i][j] == 0 && lives == 3) {
                    board[i][j] = 2; // Make the 2nd bit 1: 00 ---> 10
                }
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                board[i][j] >>= 1;  // Get the 2nd state.
            }
        }
    }

    public int liveNeighbors(int[][] board, int m, int n, int i, int j) {
        int lives = 0;
        for (int x = Math.max(i - 1, 0); x <= Math.min(i + 1, m - 1); x++) {
            for (int y = Math.max(j - 1, 0); y <= Math.min(j + 1, n - 1); y++) {
                lives += board[x][y] & 1;
            }
        }
        lives -= board[i][j] & 1;
        return lives;
    }
}

# 2ms 55.44%
class Solution {
    public void gameOfLife(int[][] board) {
        if (board == null || board.length == 0 || board[0].length == 0) {
            return;
        }
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                int num = liveNeighborNum(board, i, j);
                if (board[i][j] == 1) {
                    if (num < 2 || num > 3) {
                        board[i][j] = 2;
                    }
                } else {
                    if (num == 3) {
                        board[i][j] = 3;
                    }
                }
            }
        }
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                board[i][j] %= 2;
            }
        }
    }

    private int liveNeighborNum(int[][] board, int row, int col) {
        int count = 0;
        count += isLive(board, row - 1, col - 1);
        count += isLive(board, row - 1, col);
        count += isLive(board, row - 1, col + 1);
        count += isLive(board, row, col - 1);
        count += isLive(board, row, col + 1);
        count += isLive(board, row + 1, col - 1);
        count += isLive(board, row + 1, col);
        count += isLive(board, row + 1, col + 1);
        return count;
    }

    private int isLive(int[][] board, int row, int col) {
        if (row >= 0 && row < board.length && col >= 0 && col < board[0].length
        && (board[row][col] == 1 || board[row][col] == 2)) {
            return 1;
        } else {
            return 0;
        }
    }
}

# 2ms 55.44%
class Solution {
    public void gameOfLife(int[][] board) {
        int m = board.length;
        int n = board[0].length;

        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                int count = 0;
                for(int x = Math.max(0, i-1); x < Math.min(m, i+2) ; x++){
                    for(int y = Math.max(0, j-1); y < Math.min(n, j+2) ; y++){
                        count += board[x][y] & 1;
                    }
                }

                if (count == 3 || (count == 4 && board[i][j] != 0)){
                    board[i][j] |= 2;
                }
            }
        }

        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                board[i][j] >>= 1;
            }

        }
    }
}
'''
