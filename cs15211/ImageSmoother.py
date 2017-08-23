__source__ = 'https://leetcode.com/problems/image-smoother/description/'
# Time:  O(n^2)
# Space: O(n^2)
#
# Description: Leetcode # 661. Image Smoother
#
# Given a 2D integer matrix M representing the gray scale of an image,
# you need to design a smoother to make the gray scale of each cell
# becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself.
# If a cell has less than 8 surrounding cells, then use as many as you can.
#
# Example 1:
# Input:
# [[1,1,1],
#  [1,0,1],
#  [1,1,1]]
# Output:
# [[0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0]]
# Explanation:
# For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
# For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
# For the point (1,1): floor(8/9) = floor(0.88888889) = 0
#
# Note:
# The value in the given matrix is in the range of [0, 255].
# The length and width of the given matrix are in the range of [1, 150].
#
# Companies
# Amazon
# Related Topics
# Array
#
import unittest

class Solution(object):
    pass  # your function here


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
#83.51% 28ms
class Solution {
    public int[][] imageSmoother(int[][] M) {
        int[][] smoothMatrix = new int[M.length][M[0].length];
        for (int i = 0; i < M.length; i++) {
            for (int j = 0; j < M[0].length; j++) {
                smoothMatrix[i][j] = averageGrey(i, j, M);
            }
        }
        return smoothMatrix;
    }
    public int averageGrey(int x, int y, int[][] M) {
        int rows = M.length, cols = M[0].length;
        int ax = x - 1, ay = y - 1;
        int count = 0, grey = 0;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if ( ax >= 0 && ay >= 0 && ax < rows && ay < cols) {
                    count ++;
                    grey += M[ax][ay];
                }
                ay ++;
            }
            ax ++;
            ay = y - 1;

        }
        return (int) (grey / count);
    }
}

#97.71% 23ms
class Solution {
    public int[][] imageSmoother(int[][] M) {
        int m = M.length;
        int n = M[0].length;
        int[][] R = new int[m][n];
        if(m==1 && n==1){
           R[0][0]=M[0][0];
            return R;
        }
        if(m==1){
            for(int j=1;j<n-1;j++)
                R[0][j]=(M[0][j-1]+M[0][j]+M[0][j+1])/3;
            R[0][0] = (M[0][0]+M[0][1])/2;
            R[0][n-1] = (M[0][n-2]+M[0][n-1])/2;
            return R;
        }
        if(n==1){
            for(int i=1;i<m-1;i++)
                R[i][0]=(M[i-1][0]+M[i][0]+M[i+1][0])/3;
            R[0][0] = (M[0][0]+M[1][0])/2;
            R[m-1][0] = (M[m-2][0]+M[m-1][0])/2;
            return R;
        }
        for(int i=1;i<m-1;i++)
            for(int j=1;j<n-1;j++){
                R[i][j] = (M[i-1][j-1]+M[i-1][j]+M[i-1][j+1]+M[i][j-1]+M[i][j]+M[i][j+1]+M[i+1][j-1]+M[i+1][j]+M[i+1][j+1])/9;
            }
        for(int i=1;i<m-1;i++){
            R[i][0] = (M[i-1][0]+M[i-1][1]+M[i][0]+M[i][1]+M[i+1][0]+M[i+1][1])/6;
            R[i][n-1] = (M[i-1][n-2]+M[i-1][n-1]+M[i][n-2]+M[i][n-1]+M[i+1][n-2]+M[i+1][n-1])/6;
        }
        for(int j=1;j<n-1;j++){
            R[0][j] = (M[0][j-1]+M[0][j]+M[0][j+1]+M[1][j-1]+M[1][j]+M[1][j+1])/6;
            R[m-1][j] = (M[m-2][j-1]+M[m-2][j]+M[m-2][j+1]+M[m-1][j-1]+M[m-1][j]+M[m-1][j+1])/6;
        }
        R[0][0] = (M[0][0]+M[0][1]+M[1][0]+M[1][1])/4;
        R[0][n-1] = (M[0][n-2]+M[0][n-1]+M[1][n-2]+M[1][n-1])/4;
        R[m-1][0] = (M[m-2][0]+M[m-2][1]+M[m-1][0]+M[m-1][1])/4;
        R[m-1][n-1] = (M[m-2][n-2]+M[m-2][n-1]+M[m-1][n-2]+M[m-1][n-1])/4;
        return R;
    }
}
'''