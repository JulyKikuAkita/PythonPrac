__source__ = 'https://leetcode.com/problems/range-sum-query-2d-mutable/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/range-sum-query-2d-mutable.py
# Time:  ctor:   O(m * n)
#        update: O(logm * logn)
#        query:  O(logm * logn)
# Space: O(m * n)
#
# Description: Leetcode # 308. Range Sum Query 2D - Mutable
#
# Given a 2D matrix matrix, find the sum of the elements inside the rectangle
# defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# (ignore jpg)
# Range Sum Query 2D
# The above rectangle (with the red border) is defined by (row1, col1)
# = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.
#
# Example:
# Given matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]
#
# sumRegion(2, 1, 4, 3) -> 8
# update(3, 2, 2)
# sumRegion(2, 1, 4, 3) -> 10
# Note:
# The matrix is only modifiable by the update function.
# You may assume the number of calls to update and sumRegion function is distributed evenly.
# You may assume that row1 <= row2 and col1 <= col2.
#
# Companies
# Google
# Related Topics
# Binary Indexed Tree Segment Tree
# Similar Questions
# Range Sum Query 2D - Immutable Range Sum Query - Mutable
#
import unittest
# Binary Indexed Tree (BIT) solution.
class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if not matrix:
            return
        self.__matrix = matrix
        self.__bit = [[0] * (len(self.__matrix[0]) + 1) \
                      for _ in xrange(len(self.__matrix) + 1)]
        for i in xrange(1, len(self.__bit)):
            for j in xrange(1, len(self.__bit[0])):
                self.__bit[i][j] = matrix[i-1][j-1] + self.__bit[i-1][j] + \
                                   self.__bit[i][j-1] - self.__bit[i-1][j-1]
        for i in reversed(xrange(1, len(self.__bit))):
            for j in reversed(xrange(1, len(self.__bit[0]))):
                last_i, last_j = i - (i & -i), j - (j & -j)
                self.__bit[i][j] = self.__bit[i][j] - self.__bit[i][last_j] - \
                                   self.__bit[last_i][j] + self.__bit[last_i][last_j]

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        if val - self.__matrix[row][col]:
            self.__add(row, col, val - self.__matrix[row][col])
            self.__matrix[row][col] = val

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.__sum(row2, col2) - self.__sum(row2, col1 - 1) - \
               self.__sum(row1 - 1, col2) + self.__sum(row1 - 1, col1 - 1)

    def __sum(self, row, col):
        row += 1
        col += 1
        ret = 0
        i = row
        while i > 0:
            j = col
            while j > 0:
                ret += self.__bit[i][j]
                j -= (j & -j)
            i -= (i & -i)
        return ret

    def __add(self, row, col, val):
        row += 1
        col += 1
        i = row
        while i <= len(self.__matrix):
            j = col
            while j <= len(self.__matrix[0]):
                self.__bit[i][j] += val
                j += (j & -j)
            i += (i & -i)


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.update(1, 1, 10)
# numMatrix.sumRegion(1, 2, 3, 4)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://www.topcoder.com/community/data-science/data-science-tutorials/binary-indexed-trees/

1.
# BIT
# 34.82% 336ms
// time should be O(log(m) * log(n))
// Using 2D Binary Indexed Tree, 2D BIT Def:
// bit[i][j] saves the rangeSum of [i-(i&-i), i] x [j-(j&-j), j]
// note bit index == matrix index + 1
public class NumMatrix {

    int[][] tree;
    int[][] nums;
    int m;
    int n;

    public NumMatrix(int[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) return;
        m = matrix.length;
        n = matrix[0].length;
        tree = new int[m+1][n+1];
        nums = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                update(i, j, matrix[i][j]);
            }
        }
    }

    public void update(int row, int col, int val) {
        if (m == 0 || n == 0) return;
        int delta = val - nums[row][col];
        nums[row][col] = val;
        for (int i = row + 1; i <= m; i += i & (-i)) {
            for (int j = col + 1; j <= n; j += j & (-j)) {
                tree[i][j] += delta;
            }
        }
    }

    public int sumRegion(int row1, int col1, int row2, int col2) {
        if (m == 0 || n == 0) return 0;
        return sum(row2+1, col2+1) + sum(row1, col1) - sum(row1, col2+1) - sum(row2+1, col1);
    }

    public int sum(int row, int col) {
        int sum = 0;
        for (int i = row; i > 0; i -= i & (-i)) {
            for (int j = col; j > 0; j -= j & (-j)) {
                sum += tree[i][j];
            }
        }
        return sum;
    }
}

2.
# 22.13% 395ms
# Segment tree:

TreeNode root;
public NumMatrix(int[][] matrix) {
    if (matrix.length == 0) {
        root = null;
    } else {
        root = buildTree(matrix, 0, 0, matrix.length-1, matrix[0].length-1);
    }
}

public void update(int row, int col, int val) {
    update(root, row, col, val);
}

private void update(TreeNode root, int row, int col, int val) {
    if (root.row1 == root.row2 && root.row1 == row && root.col1 == root.col2 && root.col1 == col) {
        root.sum = val;
        return;
    }
    int rowMid = (root.row1 + root.row2) / 2;
    int colMid = (root.col1 + root.col2) / 2;
    TreeNode next;
    if (row <= rowMid) {
        if (col <= colMid) {
            next = root.c1;
        } else {
            next = root.c2;
        }
    } else {
        if (col <= colMid) {
            next = root.c3;
        } else {
            next = root.c4;
        }
    }
    root.sum -= next.sum;
    update(next, row, col, val);
    root.sum += next.sum;
}

public int sumRegion(int row1, int col1, int row2, int col2) {
    return sumRegion(root, row1, col1, row2, col2);
}

private int sumRegion(TreeNode root, int row1, int col1, int row2, int col2) {
    if (root.row1 == row1 && root.col1 == col1 && root.row2 == row2 && root.col2 == col2)
        return root.sum;
    int rowMid = (root.row1 + root.row2) / 2;
    int colMid = (root.col1 + root.col2) / 2;
    if (rowMid >= row2) {
        if (colMid >= col2) {
            return sumRegion(root.c1, row1, col1, row2, col2);
        } else if (colMid + 1 <= col1) {
            return sumRegion(root.c2, row1, col1, row2, col2);
        } else {
            return sumRegion(root.c1, row1, col1, row2, colMid) + sumRegion(root.c2, row1, colMid+1, row2, col2);
        }
    } else if (rowMid + 1 <= row1) {
        if (colMid >= col2) {
            return sumRegion(root.c3, row1, col1, row2, col2);
        } else if (colMid + 1 <= col1) {
            return sumRegion(root.c4, row1, col1, row2, col2);
        } else {
            return sumRegion(root.c3, row1, col1, row2, colMid) + sumRegion(root.c4, row1, colMid+1, row2, col2);
        }
    } else {
        if (colMid >= col2) {
            return sumRegion(root.c1, row1, col1, rowMid, col2) + sumRegion(root.c3, rowMid+1, col1, row2, col2);
        } else if (colMid + 1 <= col1) {
            return sumRegion(root.c2, row1, col1, rowMid, col2) + sumRegion(root.c4, rowMid+1, col1, row2, col2);
        } else {
            return sumRegion(root.c1, row1, col1, rowMid, colMid) + sumRegion(root.c2, row1, colMid+1, rowMid, col2) + sumRegion(root.c3, rowMid+1, col1, row2, colMid) + sumRegion(root.c4, rowMid+1, colMid+1, row2, col2);
        }
    }
}

private TreeNode buildTree(int[][] matrix, int row1, int col1, int row2, int col2) {
    if (row2 < row1 || col2 < col1)
        return null;
    TreeNode node = new TreeNode(row1, col1, row2, col2);
    if (row1 == row2 && col1 == col2) {
        node.sum = matrix[row1][col1];
        return node;
    }
    int rowMid = (row1 + row2) / 2;
    int colMid = (col1 + col2) / 2;
    node.c1 = buildTree(matrix, row1, col1, rowMid, colMid);
    node.c2 = buildTree(matrix, row1, colMid+1, rowMid, col2);
    node.c3 = buildTree(matrix, rowMid+1, col1, row2, colMid);
    node.c4 = buildTree(matrix, rowMid+1, colMid+1, row2, col2);
    node.sum += node.c1 != null ? node.c1.sum : 0;
    node.sum += node.c2 != null ? node.c2.sum : 0;
    node.sum += node.c3 != null ? node.c3.sum : 0;
    node.sum += node.c4 != null ? node.c4.sum : 0;
    return node;
}

public class TreeNode {
    int row1, row2, col1, col2, sum;
    TreeNode c1, c2, c3, c4;
    public TreeNode (int row1, int col1, int row2, int col2) {
        this.row1 = row1;
        this.col1 = col1;
        this.row2 = row2;
        this.col2 = col2;
        this.sum = 0;
    }
}

3.
#93.48% 271ms
different thinking:
We use colSums[i][j] = the sum of ( matrix[0][j], matrix[1][j], matrix[2][j],......,matrix[i - 1][j] ).

public class NumMatrix {
    private int[][] colSums;
    private int[][] matrix;

    public NumMatrix(int[][] matrix) {
        if(   matrix           == null
           || matrix.length    == 0
           || matrix[0].length == 0   ){
            return;
         }

         this.matrix = matrix;

         int m   = matrix.length;
         int n   = matrix[0].length;
         colSums = new int[m + 1][n];
         for(int i = 1; i <= m; i++){
             for(int j = 0; j < n; j++){
                 colSums[i][j] = colSums[i - 1][j] + matrix[i - 1][j];
             }
         }
    }
    //time complexity for the worst case scenario: O(m)
    public void update(int row, int col, int val) {
        for(int i = row + 1; i < colSums.length; i++){
            colSums[i][col] = colSums[i][col] - matrix[row][col] + val;
        }

        matrix[row][col] = val;
    }
    //time complexity for the worst case scenario: O(n)
    public int sumRegion(int row1, int col1, int row2, int col2) {
        int ret = 0;

        for(int j = col1; j <= col2; j++){
            ret += colSums[row2 + 1][j] - colSums[row1][j];
        }

        return ret;
    }
}

#73.76% 289ms
public class NumMatrix {

    private int[][] matrix, sum;
    public NumMatrix(int[][] matrix) {
        int m = matrix.length, n = m == 0 ? 0 : matrix[0].length;
        this.matrix = matrix;
        sum = new int[m][n+1];
        for(int i=0; i<m; i++) {
            for(int j=0; j<n; j++) {
                sum[i][j+1] = matrix[i][j] + sum[i][j];
            }
        }
    }

    public void update(int row, int col, int val) {
        int diff = val - matrix[row][col];
        matrix[row][col] = val;
        for(int j=col+1; j<sum[row].length; j++) {
            sum[row][j] += diff;
        }
    }

    public int sumRegion(int row1, int col1, int row2, int col2) {
        int res = 0;
        for(int i=row1; i<=row2; i++) {
            res += (sum[i][col2 + 1] - sum[i][col1]);
        }
        return res;
    }
}
'''