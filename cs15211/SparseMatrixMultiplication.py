__author__ = 'https://leetcode.com/problems/sparse-matrix-multiplication/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/sparse-matrix-multiplication.py
# Time:  O(m * n * l), A is m x n matrix, B is n x l matrix
# Space: O(m * l)
#
# Description: Leetcode # 311. Sparse Matrix Multiplication
#
# Given two sparse matrices A and B, return the result of AB.
#
# You may assume that A's column number is equal to B's row number.
#
# Example:
#
# A = [
#   [ 1, 0, 0],
#   [-1, 0, 3]
# ]
#
# B = [
#   [ 7, 0, 0 ],
#   [ 0, 0, 0 ],
#   [ 0, 0, 1 ]
# ]
#
#
#      |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
# AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
#                   | 0 0 1 |
# Companies
# Facebook LinkedIn
# Related Topics
# Hash Table
#

# Time:  O(m * n * l), A is m x n matrix, B is n x l matrix
# Space: O(m * l)
import unittest
# 92ms 73.21%
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n , l = len(A), len(B), len(B[0])
        res = [[0 for _ in xrange(l)] for _ in xrange(m)]
        for i in xrange(m):
            for k in xrange(n):
                if A[i][k]:
                    for j in xrange(l):
                        res[i][j] += A[i][k] * B[k][j]
        return res

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
#
# 28ms 97.85%
class Solution {
    public int[][] multiply(int[][] A, int[][] B) {
        if (A.length == 0 || B.length == 0) {
            return new int[0][0];
        }
        int[][] result = new int[A.length][B[0].length];
        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < A[0].length; j++) {
                if (A[i][j] != 0) {
                    for (int k = 0; k < B[0].length; k++) {
                        result[i][k] += A[i][j] * B[j][k];
                    }
                }
            }
        }
        return result;
    }
}

# 90ms 36.69%
class Solution {
    public int[][] multiply(int[][] A, int[][] B) {
        if (A == null || A.length == 0 || A[0].length == 0 || B.length == 0 || B[0].length == 0 || A[0].length != B.length) {
            return new int[0][0];
        }
        int[][] result = new int[A.length][B[0].length];
        Map<Integer, List<Integer>> notZeroItemsA = getNotZeroItems(A, false);
        Map<Integer, List<Integer>> notZeroItemsB = getNotZeroItems(B, true);
        for (int key : notZeroItemsA.keySet()) {
            if (notZeroItemsB.containsKey(key)) {
                for (int i : notZeroItemsA.get(key)) {
                    for (int j : notZeroItemsB.get(key)) {
                        result[i][j] += A[i][key] * B[key][j];
                    }
                }
            }
        }
        return result;
    }

    private Map<Integer, List<Integer>> getNotZeroItems(int[][] matrix, boolean trans) {
        Map<Integer, List<Integer>> map = new HashMap<>();
        if (trans) {
            // For B
            for (int i = 0; i < matrix.length; i++) {
                for (int j = 0; j < matrix[0].length; j++) {
                    if (matrix[i][j] != 0) {
                        if (!map.containsKey(i)) {
                            map.put(i, new ArrayList<Integer>());
                        }
                        map.get(i).add(j);
                    }
                }
            }
        } else {
            // For A
            for (int i = 0; i < matrix.length; i++) {
                for (int j = 0; j < matrix[0].length; j++) {
                    if (matrix[i][j] != 0) {
                        if (!map.containsKey(j)) {
                            map.put(j, new ArrayList<Integer>());
                        }
                        map.get(j).add(i);
                    }
                }
            }
        }
        return map;
    }
}
'''
