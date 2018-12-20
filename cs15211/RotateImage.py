__source__ = 'https://leetcode.com/problems/rotate-image/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/rotate-image.py
# Time:  O(n^2)
# Space: O(1)
# Array
#
# Description: Leetcode # 48. Rotate Image
#
# You are given an n x n 2D matrix representing an image.
#
# Rotate the image by 90 degrees (clockwise).
#
# Follow up:
# Could you do this in-place?
#
# Companies
# Amazon Microsoft Apple
# Related Topics
# Array
#
# https://discuss.leetcode.com/topic/15295/seven-short-solutions-1-to-7-lines
# Python 7 solutions

import unittest
# Time:  O(n^2)
# Space: O(1)
class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)
        # do a anti-diagonal mirror  (0,1) ->(1,2) ; (0,0) -> (2,2)
        for i in xrange(n):
            for j in xrange(n - i):
                matrix[i][j], matrix[n-1-j][n-1-i] = matrix[n-1-j][n-1-i], matrix[i][j]

        # do a horizontal mirror (0,0) -> (2,0) ; then done
        for i in xrange(n/2):
            for j in xrange(n):
                matrix[i][j], matrix[n-1-i][j] = matrix[n-1-i][j], matrix[i][j]

        return matrix

    def rotate2(self, matrix):
        n = len(matrix)
        matrix.reverse()
        for i in xrange(n):
            for j in xrange(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# Time:  O(n^2)
# Space: O(n^2)
# 32ms 26.15%
class Solution2:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        return list.reverse(x for x in zip(*matrix))

class SolutionOther:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        L = len(matrix)
        R = (L+1)//2
        for x in range(0, R):

            for y in range(0, L-R):
                #(x,y)->(y,l-1-x)->(l-1-x,l-1-y)->(l-1-y,x)
                print L,R ,x, y ,matrix[x][y], matrix[y][L-1-x], matrix[L-1-x][L-1-y],matrix[L-1-y][x]
                matrix[x][y], matrix[y][L-1-x], matrix[L-1-x][L-1-y],matrix[L-1-y][x] \
                = matrix[L-1-y][x], matrix[x][y], matrix[y][L-1-x],matrix[L-1-x][L-1-y]
                print "y=", y, matrix
        return matrix

#test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        test = SolutionOther()
        #print test.rotate([[1,2],[3,4]])
        print test.rotate([[1,2,3],[4,5,6], [7,8,9]])
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        print Solution().rotate(matrix)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/rotate-image/solution/

# 2ms 32.93%
class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        for (int i = 0; i < (n + 1) / 2; i++) {
            for (int j = i; j < n - i - 1; j++) {
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[n - j - 1][i];
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1];
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1];
                matrix[j][n - i - 1] = tmp;
            }
        }
    }
}

# 1ms 100%
class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        // Reverse row
        for (int i = 0; i < n / 2; ++i) {
            int j = n - 1 - i;
            int[] cache = matrix[i];
            matrix[i] = matrix[j];
            matrix[j] = cache;
        }
        // Transpose
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int cache = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = cache;
            }
        }
    }
}

/*
 * clockwise rotate
 * first reverse up to down, then swap the symmetry
 * 1 2 3     7 8 9     7 4 1
 * 4 5 6  => 4 5 6  => 8 5 2
 * 7 8 9     1 2 3     9 6 3
*/
void rotate(vector<vector<int> > &matrix) {
    reverse(matrix.begin(), matrix.end());
    for (int i = 0; i < matrix.size(); ++i) {
        for (int j = i + 1; j < matrix[i].size(); ++j)
            swap(matrix[i][j], matrix[j][i]);
    }
}

/*
 * anticlockwise rotate
 * first reverse left to right, then swap the symmetry
 * 1 2 3     3 2 1     3 6 9
 * 4 5 6  => 6 5 4  => 2 5 8
 * 7 8 9     9 8 7     1 4 7
*/
void anti_rotate(vector<vector<int> > &matrix) {
    for (auto vi : matrix) reverse(vi.begin(), vi.end());
    for (int i = 0; i < matrix.size(); ++i) {
        for (int j = i + 1; j < matrix[i].size(); ++j)
            swap(matrix[i][j], matrix[j][i]);
    }
}
'''
