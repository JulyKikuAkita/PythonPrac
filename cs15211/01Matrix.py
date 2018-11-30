__source__ = 'https://leetcode.com/problems/01-matrix/#/description'
# Time:  O( m * n)
# Space: O( m * n)
#
# Description: Leetcode # 542. 01 Matrix
#
# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
#
# The distance between two adjacent cells is 1.
# Example 1:
# Input:
#
# 0 0 0
# 0 1 0
# 0 0 0
# Output:
# 0 0 0
# 0 1 0
# 0 0 0
# Example 2:
# Input:
#
# 0 0 0
# 0 1 0
# 1 1 1
# Output:
# 0 0 0
# 0 1 0
# 1 2 1
#
# Note:
# The number of elements of the given matrix will not exceed 10,000.
# There are at least one 0 in the given matrix.
# The cells are adjacent in only four directions: up, down, left and right.
# Hide Company Tags Google
# Hide Tags Depth-first Search Breadth-first Search

import unittest
# Based on @qswawrq's solution which only considers down/right paths
# (meaning a combination of only down and right moves, from some 0 to some 1) and up/left paths.
# When I realized why that works, I realized that we don't even need paths like down,right,down,right.
# We can instead go just down,down,right,right or right,right,down,down.
# Just one turn (change of direction). It's the same length, and all of the intermediate cells must be 1
# because otherwise down,right,down,right wouldn't have been an optimal path in the first place.
#
# So in my solution I simply optimize in each direction, one after the other.
# For this I "optimize rightwards" and "rotate the matrix by 90 degrees" four times.
# Then I have covered every pair of directions, which is enough to cover every straight path and every single-turn path.
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        answer = [[10000 * x for x in row] for row in matrix]
        for _ in range(4):
            for row in answer:
                for j in range(1, len(row)):
                    row[j] = min(row[j], row[j-1] + 1)
            answer = map(list, zip(*answer[::-1]))
        return answer

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/01-matrix/solution/
https://leetcode.com/articles/01-matrix/
General idea is BFS. Some small tricks:

At beginning, set cell value to Integer.MAX_VALUE if it is not 0.
If newly calculated distance >= current distance, then we don't need to explore that cell again.

#BFS
public class Solution {
    public int[][] updateMatrix(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;

        Queue<int[]> queue = new LinkedList<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 0) {
                    queue.offer(new int[] {i, j});
                }
                else {
                    matrix[i][j] = Integer.MAX_VALUE;
                }
            }
        }

        int[][] dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            for (int[] d : dirs) {
                int r = cell[0] + d[0];
                int c = cell[1] + d[1];
                if (r < 0 || r >= m || c < 0 || c >= n ||
                    matrix[r][c] <= matrix[cell[0]][cell[1]] + 1) continue;
                //same as if (r >= 0 && r < m && c >= 0 && c < n && matrix[r][c] > matrix[cell[0]][cell[1]] + 1 )
                queue.add(new int[] {r, c});
                matrix[r][c] = matrix[cell[0]][cell[1]] + 1;
            }
        }

        return matrix;
    }
}

#DP 88%
public class Solution {
    public int[][] updateMatrix(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;

        int[][] dist = new int[m][n];
        for (int[] row : dist) {
            Arrays.fill(row, 999); //or big number if Integer.MAX_VALUE overflow
        }

        //First pass: check for left and top
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 0) {
                    dist[i][j] = 0;
                } else {
                    if (i > 0)
                        dist[i][j] = Math.min(dist[i][j], dist[i - 1][j] + 1);
                    if (j > 0)
                        dist[i][j] = Math.min(dist[i][j], dist[i][j - 1] + 1);
                }
            }
        }

        //Second pass: check for bottom and right
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                if (i < m - 1)
                    dist[i][j] = Math.min(dist[i][j], dist[i + 1][j] + 1);
                if (j < n - 1)
                    dist[i][j] = Math.min(dist[i][j], dist[i][j + 1] + 1);
            }
        }
        return dist;
    }
}
'''