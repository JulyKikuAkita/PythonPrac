__source__ = 'https://leetcode.com/problems/transpose-matrix/'
# Time:  O(R*C), where R and C are the number of rows and columns in the given matrix A.
# Space: O(R*C)
#
# Description: Leetcode # 867. Transpose Matrix
#
# Given a matrix A, return the transpose of A.
#
# The transpose of a matrix is the matrix flipped over it's main diagonal,
# switching the row and column indices of the matrix.
#
#
# Example 1:
#
# Input: [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
# Example 2:
#
# Input: [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]
#
#
# Note:
#
# 1 <= A.length <= 1000
# 1 <= A[0].length <= 1000
#
import unittest

#60ms 43.14%
class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        R, C = len(A), len(A[0])
        ans = [[None] * R for _ in xrange(C)]
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                ans[c][r] = val
        return ans;

class Solution2(object):
    def transpose(self, A):
        #Alternative Solution:
        return zip(*A)

#68ms 26.16%

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/transpose-matrix/solution/
# 2ms 100%
class Solution {
    public int[][] transpose(int[][] A) {
        if (A.length == 0) return A;
        int r = A.length;
        int c = A[0].length;
        int[][] result = new int[c][r];
        for (int i = 0; i < c; i++) {
            for (int j = 0; j < r; j++) {
                result[i][j] = A[j][i];
            }
        }
        return result;
    }
}

class Solution {
    public int[][] transpose(int[][] A) {
        int row = A.length;
        int col = A[0].length;
        int[][] ans = new int[col][row];

        int i = 0, j = 0;
        for (int[] rows: A) {
            i = 0;
            for (int num: rows) {
                ans[i][j] = num;
                i++;
            }
            j++;
        }
        return ans;
    }
}
'''