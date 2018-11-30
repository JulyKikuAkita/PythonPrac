__source__ = 'https://leetcode.com/problems/toeplitz-matrix/'
# Time:  O()
# Space: O()
#
# Note: two coordinates are on the same diagonal if and only if r1 - c1 == r2 - c2.
#
# Description: Leetcode # 766. Toeplitz Matrix  //diagonal-constant matrix
#
# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
#
# Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
#
#
# Example 1:
#
# Input:
# matrix = [
#   [1,2,3,4],
#   [5,1,2,3],
#   [9,5,1,2]
# ]
# Output: True
# Explanation:
# In the above grid, the diagonals are:
# "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
# In each diagonal all elements are the same, so the answer is True.
# Example 2:
#
# Input:
# matrix = [
#   [1,2],
#   [2,2]
# ]
# Output: False
# Explanation:
# The diagonal "[1, 2]" has different elements.
#
# Note:
#
# matrix will be a 2D array of integers.
# matrix will have a number of rows and columns in range [1, 20].
# matrix[i][j] will be integers in range [0, 99].
#
# Follow up:
#
# What if the matrix is stored on disk,
# and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
# What if the matrix is so large that you can only load up a partial row into the memory at once?
#
import unittest

#32ms 74.31%
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        return all(r == 0 or c == 0 or matrix[r-1][c-1] == val
                   for r, row in enumerate(matrix)
                   for c, val in enumerate(row))

# 28ms 99.87%
class Solution2(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        groups = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r-c not in groups:
                    groups[r-c] = val
                elif groups[r-c] != val:
                    return False
        return True

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/toeplitz-matrix/solution/


# Approach #1: Group by Category [Accepted]
# Note: two coordinates are on the same diagonal if and only if r1 - c1 == r2 - c2.

Complexity Analysis
Time Complexity: O(M*N) (Recall in the problem statement that M, N are the number of rows and columns in matrix.)
Space Complexity: O(M+N)

#16ms 69.07%
class Solution {
    public boolean isToeplitzMatrix(int[][] matrix) {
        Map<Integer, Integer> groups = new HashMap();
        for (int r = 0; r < matrix.length; r++) {
            for (int c = 0; c < matrix[0].length; c++) {
                if (!groups.containsKey(r - c)) {
                    groups.put(r - c, matrix[r][c]);
                } else if (groups.get(r - c) != matrix[r][c]) return false;
            }
        }
        return true;
    }
}


Approach #2: Compare With Top-Left Neighbor [Accepted]
Complexity Analysis
Time Complexity: O(M*N), as defined in the problem statement.
Space Complexity: O(1)

#13ms 88.26%
class Solution {
    public boolean isToeplitzMatrix(int[][] matrix) {
        for (int r = 0; r < matrix.length; ++r) {
            for (int c = 0; c < matrix[0].length; ++c) {
                if (r > 0 && c > 0 && matrix[r - 1][c - 1] != matrix[r][c]) return false;
            }
        }
        return true;
    }
}

'''