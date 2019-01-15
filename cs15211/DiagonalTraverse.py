__source__ = 'https://leetcode.com/problems/diagonal-traverse/'
# Time:  O(m * n)
# Space: O(1)
#
# Description: 498. Diagonal Traverse
#
# Given a matrix of M x N elements (M rows, N columns),
# return all elements of the matrix in diagonal order as shown in the below image.
#
# Example:
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output:  [1,2,4,7,5,3,6,8,9]
# Explanation:
#
# Note:
# The total number of elements of the given matrix will not exceed 10,000.
# Hide Company Tags Google
#
import unittest
# 132ms 65.40%
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(matrix), len(matrix and matrix[0])
        return [matrix[i][d-i]
                for d in range(m+n-1)
                for i in range(max(0, d-n+1), min(d+1, m))[::d%2*2-1]]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
Walk patterns:

If out of bottom border (row >= m) then row = m - 1; col += 2; change walk direction.
if out of right border (col >= n) then col = n - 1; row += 2; change walk direction.
if out of top border (row < 0) then row = 0; change walk direction.
if out of left border (col < 0) then col = 0; change walk direction.
Otherwise, just go along with the current direction.
Time complexity: O(m * n), m = number of rows, n = number of columns.
Space complexity: O(1).

# 7ms 30.05%
class Solution {
    public int[] findDiagonalOrder(int[][] matrix) {
        if (matrix == null || matrix.length == 0) return new int[0];
        int m = matrix.length, n = matrix[0].length;

        int[] result = new int[m * n];
        int row = 0, col = 0, d = 0;
        int[][] dirs = {{-1, 1}, {1, -1}};

        for (int i = 0; i < m * n; i++) {
            result[i] = matrix[row][col];
            row += dirs[d][0];
            col += dirs[d][1];

            if (row >= m) { row = m - 1; col += 2; d = 1 - d;}
            if (col >= n) { col = n - 1; row += 2; d = 1 - d;}
            if (row < 0)  { row = 0; d = 1 - d;}
            if (col < 0)  { col = 0; d = 1 - d;}
        }

        return result;
    }
}
'''