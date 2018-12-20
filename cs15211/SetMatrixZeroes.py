__source__ = 'https://leetcode.com/problems/set-matrix-zeroes/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/set-matrix-zeroes.py
# Time:  O(m * n)
# Space: O(1)
# Array
#
# Description: Leetcode # 73. Set Matrix Zeroes
#
# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
#
# Follow up:
# Did you use extra space?
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?
# Companies
# Microsoft Amazon
# Related Topics
# Array
# Similar Questions
# Game of Life
#
import unittest
class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        first_col = reduce(lambda acc, i: acc or matrix[i][0] == 0, xrange(len(matrix)), False)
        first_row = reduce(lambda acc, j: acc or matrix[0][j] == 0, xrange(len(matrix[0])), False)

        for i in xrange(1, len(matrix)):
            for j in xrange(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0], matrix[0][j] = 0, 0

        for i in xrange(1, len(matrix)):
            for j in xrange(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_col:
            for i in xrange(len(matrix)):
                matrix[i][0] = 0

        if first_row:
            for j in xrange(len(matrix[0])):
                matrix[0][j] = 0

#http://www.cnblogs.com/zuoyuan/p/3769698.html
class SolutionOther:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        rownum = len(matrix)
        colnum = len(matrix[0])

        row = [ False for i in range(rownum)]
        col = [ False for i in range(colnum)]

        for i in range(rownum):
            for j in range(colnum):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True

        for i in range(rownum):
            for j in range(colnum):
                if row[i] or col[j]:
                    matrix[i][j] = 0

#test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        matrix = [ [1, 0, 1, 1]
             , [1, 1, 0, 1]
             , [1, 1, 1, 0]
             , [1, 1, 1, 1]]
        Solution().setZeroes(matrix)
        print matrix

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/set-matrix-zeroes/solution/

My idea is simple: store states of each row in the first of that row,
and store states of each column in the first of that column.
Because the state of row0 and the state of column0 would occupy the same cell,
I let it be the state of row0, and use another variable "col0" for column0.
In the first phase, use matrix elements to set states in a top-down way.
In the second phase, use states to set matrix elements in a bottom-up way.

# 1ms 100%
class Solution {
    public void setZeroes(int[][] matrix) {
        int m = matrix.length;
        if (m == 0) {
            return;
        }
        int n = matrix[0].length;
        if (n == 0) {
            return;
        }
        List<Integer> zeros = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 0) {
                    zeros.add(i * n + j);
                }
            }
        }
        for (int index : zeros) {
            int row = index / n;
            int col = index % n;
            for (int i = 0; i < m; i++) {
                matrix[i][col] = 0;
            }
            for (int j = 0; j < n; j++) {
                matrix[row][j] = 0;
            }
        }
    }
}

# 1ms 100%
class Solution {
    public void setZeroes(int[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) {
            return;
        }
        int m = matrix.length;
        int n = matrix[0].length;
        boolean isCol0Zero = false;
        for (int i = 0; i < m; i++) {
            isCol0Zero |= matrix[i][0] == 0;
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }
        for (int i = 1; i < m; i++) {
            if (matrix[i][0] == 0) {
                for (int j = 1; j < n; j++) {
                    matrix[i][j] = 0;
                }
            }
        }
        for (int j = 1; j < n; j++) {
            if (matrix[0][j] == 0) {
                for (int i = 1; i < m; i++) {
                    matrix[i][j] = 0;
                }
            }
        }
        if (matrix[0][0] == 0) {
            for (int j = 1; j < n; j++) {
                matrix[0][j] = 0;
            }
        }
        if (isCol0Zero) {
            for (int i = 0; i < m; i++) {
                matrix[i][0] = 0;
            }
        }
    }
}

'''
