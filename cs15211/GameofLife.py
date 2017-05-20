__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/game-of-life.py
# Time:  O(m * n)
# Space: O(1)

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
# Google TinyCo



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


# java
js = '''
public class Solution {
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
        if (row >= 0 && row < board.length && col >= 0 && col < board[0].length && (board[row][col] == 1 || board[row][col] == 2)) {
            return 1;
        } else {
            return 0;
        }
    }
}

public class Solution {
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
