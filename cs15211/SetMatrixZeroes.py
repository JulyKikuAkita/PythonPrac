__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/set-matrix-zeroes.py
# Time:  O(m * n)
# Space: O(1)
# Array
#
# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
#
# Follow up:
# Did you use extra space?
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?
# Microsoft


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

#Java Solution
# http://www.programcreek.com/2012/12/leetcode-set-matrix-zeroes-java/

#test
if __name__ == "__main__":
    matrix = [ [1, 0, 1, 1]
             , [1, 1, 0, 1]
             , [1, 1, 1, 0]
             , [1, 1, 1, 1]]
    Solution().setZeroes(matrix)
    print matrix

#java
js = '''
public class Solution {
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


public class Solution {
     // using O(m+n) is easy, to enable O(1), we have to use the space within the matrix
    public void setZeroes(int[][] matrix) {
        if(matrix == null || matrix.length == 0)
            return;

        int rows = matrix.length;
        int cols = matrix[0].length;

        boolean empty_row0 = false;
        boolean empty_col0 = false;
        for(int i = 0; i < cols; i++){
            if(matrix[0][i] == 0){
                empty_row0 = true;
                break;
            }
        }

        for(int i = 0; i < rows; i++){
            if(matrix[i][0] == 0){
                empty_col0 = true;
                break;
            }
        }

        for(int i = 1; i < rows; i++) {
            for(int j =1; j<cols; j++){
                if(matrix[i][j] == 0){
                    matrix[0][j] = 0;
                    matrix[i][0] = 0;
                }
            }
        }

        for(int i = 1; i<rows; i++) {
            for (int j=1; j< cols; j++) {
                if(matrix[0][j] == 0 || matrix[i][0] == 0)
                    matrix[i][j] = 0;
            }
        }

        if(empty_row0){
            for(int i = 0; i < cols; i++){
                matrix[0][i] = 0;
            }
        }

        if(empty_col0){
            for(int i = 0; i < rows; i++){
                matrix[i][0] = 0;
            }
        }

    }
}
'''
