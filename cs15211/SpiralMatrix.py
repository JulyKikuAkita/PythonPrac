__source__ = 'https://leetcode.com/problems/spiral-matrix/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/spiral-matrix.py
# Time:  O(m * n)
# Space: O(1)
# Array
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# For example,
# Given the following matrix:
#
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].
#  Microsoft Google Uber
# Hide Tags Array
# Hide Similar Problems (M) Spiral Matrix II
#

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if matrix == []:
            return []
        result = []
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        while left <= right and top <= bottom:
            for j in xrange(left, right+1):
                result.append(matrix[top][j])
            for i in xrange(top + 1, bottom):
                result.append(matrix[i][right])
            for j in reversed(xrange(left,right + 1)):
                if top < bottom:
                    result.append(matrix[bottom][j])
            for i in reversed(xrange(top + 1, bottom)):
                if left < right:
                    result.append(matrix[i][left])
            left, right, top, bottom = left +1, right -1, top + 1, bottom -1

        return result

    def spiralOrder2(self, matrix):
        result = []
        if matrix == []:
            return result

        left, top , down, right = 0, 0, len(matrix) - 1, len(matrix[0]) - 1
        while top <= down and left <= right:
            for j in xrange(left, right + 1):
                result.append(matrix[top][j])
            top += 1
            for i in xrange(top, down + 1):
                result.append(matrix[i][right])
            right -=1
            for j in reversed(xrange(left,right + 1)):
                if top <= down:
                    result.append(matrix[down][j])
            down -=1
            for i in reversed(xrange(top, down + 1)):
                if left <= right:
                    result.append(matrix[i][left])
            left += 1

        return result

    def spiralOrder3(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        return matrix and list(matrix.pop(0)) + self.spiralOrder(zip(*matrix)[::-1])

class SolutionOther:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return []
        res = []
        maxUp = maxLeft = 0
        maxDown = len(matrix) - 1
        maxRight = len(matrix[0]) - 1
        direct = 0 # 0 go right, 1 go down, 2 go left, 3 go up

        while True:
            if direct == 0: #go right
                for i in xrange(maxLeft, maxRight+1) :
                    res.append(matrix[maxUp][i])
                maxUp += 1
            elif direct == 1: #go down
                for i in xrange(maxUp, maxDown+1) :
                    res.append(matrix[i][maxRight])
                maxRight -= 1
            elif direct == 2: # go left
                for i in reversed(xrange(maxLeft,maxRight+1)):
                    res.append(matrix[maxDown][i])
                maxDown -= 1
            else: #go up
                for i in reversed(xrange(maxUp, maxDown+1)):
                    res.append(matrix[i][maxLeft])
                maxLeft += 1
            if maxUp > maxDown or maxLeft > maxRight:
                return res

            direct = (direct + 1) % 4

if __name__ == "__main__":
    matrix = [
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
    ]
    #print Solution().spiralOrder(matrix)
    #print SolutionOther().spiralOrder(matrix)
    print Solution().spiralOrder([[2,3]])
    print SolutionOther().spiralOrder([[2,3]])

#java
java = '''
This is a very simple and easy to understand solution. I traverse right and increment rowBegin,
then traverse down and decrement colEnd, then I traverse left and decrement rowEnd,
and finally I traverse up and increment colBegin.

The only tricky part is that when I traverse left or up I have to check whether the row
or col still exists to prevent duplicates.

public class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {

        List<Integer> res = new ArrayList<Integer>();

        if (matrix.length == 0) {
            return res;
        }

        int rowBegin = 0;
        int rowEnd = matrix.length-1;
        int colBegin = 0;
        int colEnd = matrix[0].length - 1;

        while (rowBegin <= rowEnd && colBegin <= colEnd) {
            // Traverse Right
            for (int j = colBegin; j <= colEnd; j ++) {
                res.add(matrix[rowBegin][j]);
            }
            rowBegin++;

            // Traverse Down
            for (int j = rowBegin; j <= rowEnd; j ++) {
                res.add(matrix[j][colEnd]);
            }
            colEnd--;

            if (rowBegin <= rowEnd) {
                // Traverse Left
                for (int j = colEnd; j >= colBegin; j --) {
                    res.add(matrix[rowEnd][j]);
                }
            }
            rowEnd--;

            if (colBegin <= colEnd) {
                // Traver Up
                for (int j = rowEnd; j >= rowBegin; j --) {
                    res.add(matrix[j][colBegin]);
                }
            }
            colBegin ++;
        }

        return res;
    }
}

public class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return result;
        }
        int m = matrix.length;
        int n = matrix[0].length;
        for (int i = 0; i < m / 2 && i < n / 2; i++) {
            for (int j = i; j < n - 1 - i; j++) {
                result.add(matrix[i][j]);
            }
            for (int j = i; j < m - 1 - i; j++) {
                result.add(matrix[j][n - 1 - i]);
            }
            for (int j = n - 1 - i; j > i; j--) {
                result.add(matrix[m - 1 - i][j]);
            }
            for (int j = m - 1 - i; j > i; j--) {
                result.add(matrix[j][i]);
            }
        }
        if (m <= n && (m & 1) == 1) {
            for (int i = m / 2; i < n - m / 2; i++) {
                result.add(matrix[m / 2][i]);
            }
        } else if (n <= m && (n & 1) == 1) {
            for (int i = n / 2; i < m - n / 2; i++) {
                result.add(matrix[i][n / 2]);
            }
        }
        return result;
    }
}
'''