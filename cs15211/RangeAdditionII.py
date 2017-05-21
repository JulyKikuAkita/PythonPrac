__source__ = 'https://leetcode.com/problems/range-addition-ii/#/description'
# Time:  O(n)
# Space: O(1)
#
# Description:
# Given an m * n matrix M initialized with all 0's and several update operations.
#
# Operations are represented by a 2D array,
# and each operation is represented by an array with two positive integers a and b,
# which means M[i][j] should be added by one for all 0 <= i < a and 0 <= j < b.
#
# You need to count and return the number of maximum integers in the matrix after performing all the operations.
#
# Example 1:
# Input:
# m = 3, n = 3
# operations = [[2,2],[3,3]]
# Output: 4
# Explanation:
# Initially, M =
# [[0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0]]
#
# After performing [2,2], M =
# [[1, 1, 0],
#  [1, 1, 0],
#  [0, 0, 0]]
#
# After performing [3,3], M =
# [[2, 2, 1],
#  [2, 2, 1],
#  [1, 1, 1]]
#
# So the maximum integer in M is 2, and there are four of it in M. So return 4.
# Note:
# The range of m and n is [1,40000].
# The range of a is [1,m], and the range of b is [1,n].
# The range of operations size won't exceed 10,000.
# Hide Company Tags IXL
# Hide Tags Math
# Hide Similar Problems (M) Range Addition

# Explanation:
# Say the operations are [(x_1, y_1), (x_2, y_2), ..., (x_n, y_n)].
# The top left square is clearly incremented by every operation.
# If some square (x, y) has x >= x_i, then it will not be marked by operation i.
# So all squares (x, y) with x >= min_i(x_i) do not get marked.
#
# Thus, when there is at least one operation, all squares (x, y) with 0 <= x < min(x_1, x_2, ..., x_n)
#  and 0 <= y < min(y_1, y_2, ..., y_n) get marked; and there are min_i(x_i) * min_i(y_i) of them.
# If there are no operations, then what is marked is the entire board.

import unittest
class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m * n
        X, Y = zip(*ops)
        return min(X) * min(Y)


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/articles/range-addition-ii/
Time complexity : O(x). Single traversal of all operations is done. xx refers to the number of operations.
Space complexity : O(1). No extra space is used.
public class Solution {
    public int maxCount(int m, int n, int[][] ops) {
        if (ops == null || ops.length == 0) {
            return m * n;
        }

        int row = Integer.MAX_VALUE, col = Integer.MAX_VALUE;
        for(int[] op : ops) {
            row = Math.min(row, op[0]);
            col = Math.min(col, op[1]);
        }

        return row * col;
    }
}
'''