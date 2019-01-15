__source__ = 'https://leetcode.com/problems/transform-to-chessboard/'
# Time:  O(N^2)
# Space: O(N)
#
# Description: Leetcode # 782. Transform to Chessboard
#
# An N x N board contains only 0s and 1s. In each move,
# you can swap any 2 rows with each other, or any 2 columns with each other.
#
# What is the minimum number of moves to transform the board into a "chessboard"
# - a board where no 0s and no 1s are 4-directionally adjacent?
# If the task is impossible, return -1.
#
# Examples:
# Input: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
# Output: 2
# Explanation:
# One potential sequence of moves is shown below, from left to right:
#
# 0110     1010     1010
# 0110 --> 1010 --> 0101
# 1001     0101     1010
# 1001     0101     0101
#
# The first move swaps the first and second column.
# The second move swaps the second and third row.
#
#
# Input: board = [[0, 1], [1, 0]]
# Output: 0
# Explanation:
# Also note that the board with 0 in the top left corner,
# 01
# 10
#
# is also a valid chessboard.
#
# Input: board = [[1, 0], [1, 0]]
# Output: -1
# Explanation:
# No matter what sequence of moves you make, you cannot end with a valid chessboard.
# Note:
#
# board will have the same number of rows and columns, a number in the range [2, 30].
# board[i][j] will be only 0s or 1s.
#

import unittest
import collections
class Solution(object):
    def movesToChessboard(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        N = len(board)
        ans = 0
        # For each count of lines from {rows, columns}...
        for count in (collections.Counter(map(tuple, board)),
                      collections.Counter(zip(*board))):

            # If there are more than 2 kinds of lines,
            # or if the number of kinds is not appropriate ...
            if len(count) != 2 or sorted(count.values()) != [N/2, (N+1)/2]:
                return -1

            # If the lines are not opposite each other, impossible
            line1, line2 = count
            if not all(x ^ y for x, y in zip(line1, line2)):
                return -1

            # starts = what could be the starting value of line1
            # If N is odd, then we have to start with the more
            # frequent element
            starts = [+(line1.count(1) * 2 > N)] if N%2 else [0, 1]

            # To transform line1 into the ideal line [i%2 for i ...],
            # we take the number of differences and divide by two
            ans += min(sum((i-x) % 2 for i, x in enumerate(line1, start))
                       for start in starts) / 2

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/transform-to-chessboard/solution/

Approach #1: Dimension Independence [Accepted]
Complexity Analysis
Time Complexity: O(N^2), where N is the number of rows (and columns) in board.
Space Complexity: O(N), the space used by count.

# 8ms 56.96%
class Solution {
    public int movesToChessboard(int[][] board) {
        int N = board.length;
        // count[code] = v, where code is an integer
        // that represents the row in binary, and v
        // is the number of occurrences of that row

        Map<Integer, Integer> count = new HashMap();
        for (int[] row: board) {
            int code = 0;
            for (int x : row) {
                code = 2 * code + x;
            }
            count.put(code, count.getOrDefault(code, 0) + 1);
        }

        int k1 = analyzeCount(count, N);
        if (k1 == -1) return -1;

        // count[code], as before except with columns
        count = new HashMap();
        for (int c = 0; c < N; c++) {
            int code = 0;
            for (int r = 0; r < N; r++) {
                code = 2 * code + board[r][c];
            }
            count.put(code, count.getOrDefault(code, 0) + 1);
        }
        int k2 = analyzeCount(count, N);
        return k2 >= 0 ? k1 + k2 : -1;
    }

    private int analyzeCount(Map<Integer, Integer> count, int N) {
        // Return -1 if count is invalid
        // Otherwise, return number of swaps required
        if (count.size() != 2) return -1;
        List<Integer> keys = new ArrayList(count.keySet());
        int k1 = keys.get(0), k2 = keys.get(1);

        // If lines aren't in the right quantity
        if (!(count.get(k1) == N / 2 && count.get(k2) == (N + 1) / 2) && !(count.get(k2) == N / 2 && count.get(k1) == (N + 1) / 2 ))
            return -1;
        // If lines aren't opposite
        if ((k1 ^ k2) != (1 << N) - 1)
            return -1;

        int Nones = (1 << N) - 1;
        int ones = Integer.bitCount(k1 & Nones);
        int cand = Integer.MAX_VALUE;
        if (N % 2 == 0 || ones * 2 < N) //zero start
            cand = Math.min(cand, Integer.bitCount(k1 ^ 0xAAAAAAAA & Nones) / 2);

        if (N % 2 == 0 || ones * 2 > N) // ones start
            cand = Math.min(cand, Integer.bitCount(k1 ^ 0x55555555 & Nones) / 2);
        return cand;
    }
}

# 8ms 56.96%
class Solution {
    public int movesToChessboard(int[][] board) {
        int N = board.length;
        // At the end we need to divide this by 2, because 1 swap is equal to 2 moves.
        int colToMove = 0, rowToMove = 0;
        int rowOneCnt = 0, colOneCnt = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                // because for corners are either 4 zeros or 4 ones or 2 zeros 2 ones, it should be 0.
                if ((board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]) == 1) {
                    return -1;
                }
            }
        }
        for (int i = 0; i < N; i++) {
            rowOneCnt += board[i][0];
            colOneCnt += board[0][i];
            // Assume we arrange row/col as this sequence: 0 1 0 1 0 1...
            rowToMove += board[i][0] == i % 2 ? 1 : 0;
            colToMove += board[0][i] == i % 2 ? 1 : 0;
        }

        if (rowOneCnt < N / 2 || colOneCnt < N / 2) { // there are less ones than required.
            return -1;
        }
        if (rowOneCnt > (N + 1) / 2 || colOneCnt > (N + 1) / 2) {  // there are way more ones.
            return -1;
        }

        if (N % 2 == 1) {
            // because we cannot make odd moves.
            if (rowToMove % 2 == 1) {
                rowToMove = N - rowToMove;
            }
            if (colToMove % 2 == 1) {
                colToMove = N - colToMove;
            }
        }
        else {
            rowToMove = Math.min(rowToMove, N - rowToMove);
            colToMove = Math.min(colToMove, N - colToMove);
        }

        return rowToMove / 2 + colToMove / 2;
    }
}

'''