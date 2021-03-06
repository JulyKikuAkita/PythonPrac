__source__ = 'https://leetcode.com/problems/spiral-matrix-ii/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/spiral-matrix-ii.py
# Time:  O(n^2)
# Space: O(1)
#
# Description: Leetcode #  59. Spiral Matrix II
#
# Given an integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.
#
# For example,
# Given n = 3,
#
# You should return the following matrix:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]
#
# Related Topics
# Array
# Similar Questions
# Spiral Matrix
#

import unittest
class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        matrix = [[0 for j in xrange(n)] for i in xrange(n)]
        left, top, right,down = 0 , 0 , n-1, n-1
        num = 1

        while left<= right and top <= down:
            for j in xrange(left, right+1):
                matrix[top][j] = num
                num += 1
            top += 1

            for i in xrange(top, down+1):
                matrix[i][right] = num
                num += 1
            right -= 1

            for j in reversed(xrange(left,right+1)):
                if top <= down:  # top < down not working
                    matrix[down][j] = num
                    num += 1
            down -= 1

            for i in reversed(xrange(top, down+1)):
                if left <= right: # left < right not working
                    matrix[i][left] = num
                    num +=1
            left += 1
        return matrix

# http://chaoren.is-programmer.com/posts/43864.html
class SolutionOther:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        if n == 0: return []
        direct = 0 # 0 go right, 1 go down, 2 go left, 3 go up
        A = [[0 for i in xrange(n) ]for j in xrange(n)]
        up = left = 0
        down = right = n -1
        curr = 0
        while True:
            if direct == 0 :
                for i in xrange(left, right + 1):
                    curr += 1
                    A[up][i] = curr
                up += 1
            elif direct == 1:
                for i in xrange(up, down + 1):
                    curr += 1
                    A[i][right] = curr
                right -= 1
            elif direct == 2:
                for i in reversed(xrange(left, right + 1)):
                    curr += 1
                    A[down][i] = curr
                down -= 1
            else:
                for i in reversed(xrange(up, down + 1)):
                    curr += 1
                    A[i][left] = curr
                left += 1
            if curr >= n*n: return A
            direct = (direct + 1) % 4

    def generateMatrix2(self, n):
        if n == 0: return []
        matrix = [[0 for i in xrange(n) ]for j in xrange(n)]
        up =0
        down = len(matrix) -1
        left = 0
        right = len(matrix[0]) -1
        direct = 0
        count = 0

        while True:
            if direct == 0:
                for i in range(left, right+1):
                    count += 1
                    matrix[up][i] = count
                up += 1
            elif direct == 1:
                for i in range(up, down+1):
                    count += 1
                    matrix[i][right] = count
                right -= 1
            elif direct == 2:
                for i in range(right, left-1, -1):
                    count += 1
                    matrix[down][i] = count
                down -= 1
            if direct == 3:
                for i in range(down, up-1, -1):
                    count += 1
                    matrix[i][left] = count
                left += 1
            if count == n*n: return matrix
            direct = (direct+1) % 4

class TestMethods(unittest.TestCase):
    def test_Local(self):
        print Solution().generateMatrix(3)
        print Solution().generateMatrix(2)
        #test
        test = SolutionOther()
        #print test.generateMatrix(2)
        #print test.generateMatrix2(2)

if __name__ == '__main__':
    unittest.main()

Java = '''
Thought:

This is my solution for Spiral Matrix I,
https://oj.leetcode.com/discuss/12228/super-simple-and-easy-to-understand-solution.
If you can understand that, this one is a no brainer :)
Guess what? I just made several lines of change (with comment "//change")
from that and I have the following AC code:

# 1ms 100%
class Solution {
    public int[][] generateMatrix(int n) {
        // Declaration
        int[][] matrix = new int[n][n];

        // Edge Case
        if (n == 0) {
            return matrix;
        }

        // Normal Case
        int rowStart = 0;
        int rowEnd = n-1;
        int colStart = 0;
        int colEnd = n-1;
        int num = 1; //change

        while (rowStart <= rowEnd && colStart <= colEnd) {
            for (int i = colStart; i<= colEnd; i++) {
                matrix[rowStart][i] = num++;
            }
            rowStart++;

            for (int i = rowStart; i<= rowEnd; i++) {
                matrix[i][colEnd] = num++;
            }
            colEnd--;

            if (rowEnd >= rowStart) {
                for (int i = colEnd; i >= colStart; i--) {
                    matrix[rowEnd][i] = num++;
                }
                rowEnd--; //outside if loop is fine
            }

            if (colStart <= colEnd) {
                for (int i = rowEnd; i >= rowStart; i--) {
                    matrix[i][colStart] = num++;
                }
                colStart++; //outside if loop is fine
            }
        }
        return matrix;
    }
}

Obviously, you could merge colStart and colEnd into rowStart and rowEnd
because it is a square matrix. But this is easily extensible to matrices that are m*n.

# 1ms 100%
class Solution {
    public int[][] generateMatrix(int n) {
        if (n <= 0) {
            return new int[0][0];
        }
        int[][] result = new int[n][n];
        int count = 1;
        for (int i = 0; i < n / 2; i++) {
            for (int j = i; j < n - 1 - i; j++) {
                result[i][j] = count++;
            }
            for (int j = i; j < n - 1 - i; j++) {
                result[j][n - 1 - i] = count++;
            }
            for (int j = n - 1 - i; j > i; j--) {
                result[n - 1 - i][j] = count++;
            }
            for (int j = n - 1 - i; j > i; j--) {
                result[j][i] = count++;
            }
        }
        if ((n & 1) == 1) {
            result[n / 2][n / 2] = count;
        }
        return result;
    }
}
'''
