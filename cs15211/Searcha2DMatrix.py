__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/search-a-2d-matrix.py
# Time:  O(logm + logn)
# Space: O(1)
# Binary Search
#
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# For example,
#
# Consider the following matrix:
#
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return true.
#

class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        i, j = 0, m * n
        while i < j:
            mid = (i + j) /2
            val = matrix[mid / n][mid % n]
            if val == target:
                return True
            elif val < target:
                i = mid + 1
            else:
                j = mid
        return False


if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    print Solution().searchMatrix(matrix, 3)

class SolutionOther:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        begin, end = 0, len(matrix)*len(matrix[0])-1

        while (begin <= end):
            mid = begin +((end - begin) >> 1)
            temp = matrix[mid // len(matrix[0])][mid % len(matrix[0])]
            print mid, temp
            if temp < target:
                begin = mid +1
            elif temp > target:
                end = mid -1
            else :
                return True
        return False


#test
test = SolutionOther()
matrix = \
[
[1,   3,  5,  7],
[10, 11, 16, 20],
[23, 30, 34, 50]
]
#print test.searchMatrix(matrix, 49)
print test.searchMatrix(matrix, 0)
#print 11 >> 2 # // 4
#print 11 >> 1 # // 2

#java
js = '''
public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length;
        if (m == 0) {
            return false;
        }
        int n = matrix[0].length;
        if (n == 0) {
            return false;
        }
        int start = 0;
        int end = matrix.length - 1;
        while (start <= end) {
            int mid = start + (end - start) / 2;
            if (matrix[mid][0] <= target && target <= matrix[mid][n - 1]) {
                return searchRow(matrix, mid, target);
            } else if (matrix[mid][0] > target) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        return false;
    }

    private boolean searchRow(int[][] matrix, int row, int target) {
        int start = 0;
        int end = matrix[row].length;
        while (start <= end) {
            int mid = start + (end - start) / 2;
            if (matrix[row][mid] > target) {
                end = mid - 1;
            } else if (matrix[row][mid] < target) {
                start = mid + 1;
            } else {
                return true;
            }
        }
        return false;
    }
}
'''