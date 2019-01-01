__source__ = 'https://leetcode.com/problems/score-after-flipping-matrix/'
# Time:  O(R * C)
# Space: O(1)
#
# Description: Leetcode # 861. Score After Flipping Matrix
# We have a two dimensional matrix A where each value is 0 or 1.
#
# A move consists of choosing any row or column, and toggling each value in that row or column:
# changing all 0s to 1s, and all 1s to 0s.
#
# After making any number of moves, every row of this matrix is interpreted as a binary number,
# and the score of the matrix is the sum of these numbers.
#
# Return the highest possible score.
#
#
# Example 1:
#
# Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# Output: 39
# Explanation:
# Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
# 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
#
#
#
# Note:
#
#     1 <= A.length <= 20
#     1 <= A[0].length <= 20
#     A[i][j] is 0 or 1.
#
import unittest

# 20ms 100%
class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        R, C = len(A), len(A[0])
        ans = 0
        for c in xrange(C):
            col = 0
            for r in xrange(R):
                col += A[r][c] ^ A[r][0]
            ans += max(col, R - col) * 2 ** (C - 1 - c)
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/score-after-flipping-matrix/solution/
#
Approach 1: Brute Force
Complexity Analysis
Time Complexity: O(2^R * R * C), where R,C is the number of rows and columns in the matrix.
Space Complexity: O(C) in additional space complexity.
In general, the score is increased by max(col_sum, R - col_sum) * (1 << (C-1-c)), 
where the factor (1 << (C-1-c)) is the power of 2 that each 1 contributes.

# 1057ms 1.91%
class Solution {
    public int matrixScore(int[][] A) {
        int R = A.length, C = A[0].length;
        int[] colsums = new int[C];
        for (int r = 0; r < R; ++r)
            for (int c = 0; c < C; ++c)
                colsums[c] += A[r][c];
        
        int ans = 0;
        for (int state = 0; state < (1<<R); ++state) {
            // Toggle the rows so that after, 'state' represents
            // the toggled rows.
            if (state > 0) {
                int trans = state ^ (state-1);
                for (int r = 0; r < R; ++r) {
                    if (((trans >> r) & 1) > 0) {
                        for (int c = 0; c < C; ++c) {
                            colsums[c] += A[r][c] == 1 ? -1 : 1;
                            A[r][c] ^= 1;
                        }
                    }
                }
            }
            // Calculate the score with the rows toggled by 'state'
            int score = 0;
            for (int c = 0; c < C; ++c){
                 score += Math.max(colsums[c], R - colsums[c]) * (1 << (C-1-c));
            }
            ans = Math.max(ans, score);
        }
        return ans;
    }
}

Approach 2: Greedy
Complexity Analysis
Time Complexity: O(R * C), R,C is the number of rows and columns in the matrix.
Space Complexity: O(1) in additional space complexity.
# maximizing the left-most digit is more important than any other digit.
# 3ms 100%
class Solution {
    public int matrixScore(int[][] A) {
        int R = A.length, C = A[0].length;
        int ans = 0;
        for (int c = 0; c < C; ++c) {
            int col = 0;
            for (int r = 0; r < R; r++) {
                col += A[r][c] ^ A[r][0];
            }
            ans += Math.max(col, R - col) * (1 << (C - 1 -c));
        }
        return ans;
    }
}

'''
