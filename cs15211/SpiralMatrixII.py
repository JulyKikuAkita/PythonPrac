__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/spiral-matrix-ii.py
# Time:  O(n^2)
# Space: O(1)
#
# Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
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
# Microsoft


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

if __name__ == "__main__":
    print Solution().generateMatrix(3)
    print Solution().generateMatrix(2)

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

#test
test = SolutionOther()
#print test.generateMatrix(2)
#print test.generateMatrix2(2)

#java
js = '''


public class Solution {
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