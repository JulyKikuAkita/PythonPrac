__source__ = 'https://leetcode.com/problems/range-sum-query-2d-immutable/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/range-sum-query-2d-immutable.py
# Time:  ctor:   O(m * n),
#        lookup: O(1)
# Space: O(m * n)
#
# Description: Leetcode # 304. Range Sum Query 2D - Immutable
#
# Given a 2D matrix matrix, find the sum of the elements inside
# the rectangle defined by its upper left corner (row1, col1)
# and lower right corner (row2, col2).
#
# Range Sum Query 2D
# The above rectangle (with the red border) is defined by
# (row1, col1) = (2, 1) and (row2, col2) = (4, 3),
# which contains sum = 8.
#
# Example:
# Given matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]
#
# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12
#
# Note:
# You may assume that the matrix does not change.
# There are many calls to sumRegion function.
# You may assume that row1 <= row2 and col1 <= col2.
#
# Related Topics
# Dynamic Programming
# Similar Questions
# Range Sum Query - Immutable Range Sum Query 2D - Mutable
#
import unittest
class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if not matrix:
            return

        m, n = len(matrix), len(matrix[0])
        self.__sums = [[0 for _ in xrange(n + 1) ]for _ in xrange(m + 1)]

        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                self.__sums[i][j] = self.__sums[i][j-1] + matrix[i-1][j-1]

        for j in xrange(1, n+1):
            for i in xrange(1, m+1):
                self.__sums[i][j] += self.__sums[i-1][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.__sums[row2+1][col2+1] - self.__sums[row2+1][col1] - \
                self.__sums[row1][col2+1] + self.__sums[row1][col1]
# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        matrix = [
           [3, 0, 1, 4, 2],
           [5, 6, 3, 2, 1],
           [1, 2, 0, 1, 5],
           [4, 1, 0, 1, 7],
           [1, 0, 3, 0, 5]
         ]
        self.assertEqual(1, 1)
        numMatrix = NumMatrix(matrix)
        print numMatrix.sumRegion(0, 1, 2, 3)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/articles/range-sum-query-2d-immutable/

#97.22% 116ms
public class NumMatrix {
    int[][] sums;

    public NumMatrix(int[][] matrix) {
        int m = matrix.length;
        int n = m == 0 ? 0 : matrix[0].length;
        sums = new int[m + 1][n + 1];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                sums[i + 1][j + 1] = sums[i][j + 1] + sums[i + 1][j] - sums[i][j] + matrix[i][j];
            }
        }
    }

    public int sumRegion(int row1, int col1, int row2, int col2) {
        return sums[row2 + 1][col2 + 1] - sums[row1][col2 + 1] - sums[row2 + 1][col1] + sums[row1][col1];
    }
}


// Your NumMatrix object will be instantiated and called as such:
// NumMatrix numMatrix = new NumMatrix(matrix);
// numMatrix.sumRegion(0, 1, 2, 3);
// numMatrix.sumRegion(1, 2, 3, 4);
'''