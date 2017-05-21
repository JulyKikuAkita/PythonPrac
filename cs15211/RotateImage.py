__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/rotate-image.py
# Time:  O(n^2)
# Space: O(1)
# Array
#
# You are given an n x n 2D matrix representing an image.
#
# Rotate the image by 90 degrees (clockwise).
#
# Follow up:
# Could you do this in-place?
#  Amazon Microsoft Apple
# Hide Tags Array

# https://discuss.leetcode.com/topic/15295/seven-short-solutions-1-to-7-lines
# Python 7 solutions

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
class Solution2:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        return list.reverse(x for x in zip(*matrix))

if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print Solution().rotate(matrix)

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
test = SolutionOther()
#print test.rotate([[1,2],[3,4]])
print test.rotate([[1,2,3],[4,5,6], [7,8,9]])

# https://leetcode.com/problems/rotate-image/#/solutions
java= '''
public class Solution {
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

public void rotate(int[][] matrix) {
    int n = matrix.length;
    // Reverse
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
'''