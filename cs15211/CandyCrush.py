__source__ = ' https://leetcode.com/problems/candy-crush/'
# Time:  O((R*C)^2)
# Space: O(1)
#
# Description: Leetcode # 723. Candy Crush
#
# This question is about implementing a basic elimination algorithm for Candy Crush.
#
# Given a 2D integer array board representing the grid of candy,
# different positive integers board[i][j] represent different types of candies.
# A value of board[i][j] = 0 represents that the cell at position (i, j) is empty.
# The given board represents the state of the game following the player's move.
# Now, you need to restore the board to a stable state by crushing candies according to the following rules:
#
# If three or more candies of the same type are adjacent vertically or horizontally,
# "crush" them all at the same time - these positions become empty.
# After crushing all candies simultaneously,
# if an empty space on the board has candies on top of itself,
# then these candies will drop until they hit a candy or bottom at the same time.
# (No new candies will drop outside the top boundary.)
# After the above steps, there may exist more candies that can be crushed.
# If so, you need to repeat the above steps.
# If there does not exist more candies that can be crushed (ie. the board is stable),
# then return the current board.
# You need to perform the above rules until the board becomes stable,
# then return the current board.
#
#
#
# Example:
#
# Input:
# board =
# [[110,5,112,113,114],
# [210,211,5,213,214],
# [310,311,3,313,314],
# [410,411,412,5,414],
# [5,1,512,3,3],
# [610,4,1,613,614],
# [710,1,2,713,714],
# [810,1,2,1,1],
# [1,1,2,2,2],
# [4,1,4,4,1014]]
#
# Output:
# [[0,0,0,0,0],
# [0,0,0,0,0],
# [0,0,0,0,0],
# [110,0,0,0,114],
# [210,0,0,0,214],
# [310,0,0,113,314],
# [410,0,0,213,414],
# [610,211,112,313,614],
# [710,311,412,613,714],
# [810,411,512,713,1014]]
#
# Explanation:
#
# Note:
#
# The length of board will be in the range [3, 50].
# The length of board[i] will be in the range [3, 50].
# Each board[i][j] will initially start as an integer in the range [1, 2000].
import unittest

#96ms 95.48%
# idea, optimize by
# https://leetcode.com/problems/candy-crush/discuss/109220/155-ms-Python-with-detailed-explanation-beat-100
# if we drop vertically, it would be very slow
# it's better to rotate the board and drop horizontally
# Rotate the board will make the drop operation much easier.
# That being said, instead of move all non-zero value to the end of each column,
# the drop operation becomes move all non-zero value to the beginning of each row.
class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        board = map(list, zip(*reversed(board)))  # rotate clock-wise 90 degree

        while True:
            to_crash = self.get_candidates(board)
            if not to_crash:
                break
            else:
                self.crash(board, to_crash)
                self.drop(board)

        board = list(reversed(map(list, zip(*board))))  # rotate counter-clock 90
        return board

    def get_candidates(self, board):
        m, n = len(board), len(board[0])
        to_crash = set()
        # horizontal
        for i in range(m):
            for j in range(2, n):
                if board[i][j] and board[i][j] == board[i][j-1] == board[i][j-2]:
                    to_crash |= {(i, j), (i, j-1), (i, j-2)}
        # vertical
        for j in range(n):
            for i in range(2, m):
                if board[i][j] and board[i][j] == board[i-1][j] == board[i-2][j]:
                    to_crash |= {(i, j), (i-1, j), (i-2, j)}
        return to_crash

    def crash(self, board, to_crash):
        for i, j in to_crash:
            board[i][j] = 0

    def drop(self, board):
        n = len(board[0])
        for i, row in enumerate(board):
            row = filter(None, row)
            board[i] = row + [0] * (n - len(row))


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/candy-crush/solution/
Approach #1: Ad-Hoc [Accepted]

#14ms 51%
class Solution {
    public int[][] candyCrush(int[][] board) {
        int R = board.length, C = board[0].length;
        boolean todo = false;
        for(int r = 0; r < R; ++r) {
            for (int c = 0; c + 2 < C; ++c) {
                int v = Math.abs(board[r][c]);
                if ( v != 0 && v == Math.abs(board[r][c+1]) && v == Math.abs(board[r][c+2])) {
                    board[r][c] = board[r][c+1] = board[r][c+2] = -v;
                    todo = true;
                }
            }
        }

        for (int r = 0; r + 2 < R; ++r) {
            for (int c = 0; c < C; ++c) {
                int v = Math.abs(board[r][c]);
                if (v != 0 && v == Math.abs(board[r + 1][c]) && v == Math.abs(board[r+2][c])) {
                    board[r][c] = board[r+1][c] = board[r+2][c] = -v;
                    todo = true;
                }
            }
        }

        for (int c = 0; c < C; ++c) {
            int wr = R - 1;
            for (int r = R - 1; r >= 0; --r) {
                if (board[r][c] > 0) board[wr--][c] = board[r][c];
            }
            while (wr >= 0) board[wr--][c] = 0;
        }

        return todo ? candyCrush(board) : board;
    }
}

# Complexity Analysis
# Time Complexity: O((R*C)^2), where R,C is the number of rows and columns in board.
# We need O(R*C) to scan the board, and we might crush only 3 candies repeatedly.
# Space Complexity: O(1) additional complexity, as we edit the board in place.
#
# 8ms 98.49%
class Solution {
    public int[][] candyCrush(int[][] board) {
        if (board == null || board.length == 0) return board;
        int rows = board.length;
        int cols = board[0].length;

        boolean canCrush = true;
        while (canCrush) {
            canCrush = false;
            // 1. Check if we can find candies of the same type
            //that are adjacent vertically or horizontally to crush

            for (int row = 0; row < rows; row++) {
                for (int col = 0; col < cols; col++) {
                    int v = Math.abs(board[row][col]);
                    if (v == 0) continue;

                    // Verify Horizontal
                    if (col < cols - 2 && Math.abs(board[row][col+1]) == v
                                       && Math.abs(board[row][col+2]) == v) {
                        canCrush = true;
                        int index = col;
                        while (index < cols && Math.abs(board[row][index]) == v) {
                            board[row][index++] = -v;
                        }
                    }

                    // Verify Vertical
                    if (row < rows -2 && Math.abs(board[row+1][col]) == v
                                      && Math.abs(board[row+2][col]) == v) {
                        canCrush = true;
                        int index = row;
                        while (index < rows && Math.abs(board[index][col]) == v) {
                            board[index++][col] = -v;
                        }
                    }
                }
            }

            if (canCrush) {
                // 2. Handle the candy drop
                for (int col = 0 ; col < cols; col++) {
                    int targetRow = rows - 1;
                    for (int row = rows - 1; row >= 0; row--) {
                        if (board[row][col] > 0) {
                            board[targetRow--][col] = board[row][col];
                        }
                    }

                    // Reset the following candies to 0
                    for (int index = targetRow; index >= 0; index--) {
                        board[index][col] = 0;
                    }
                }
            }
        }
        return board;
    }
}
'''