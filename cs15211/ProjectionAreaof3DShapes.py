__source__ = 'https://leetcode.com/problems/projection-area-of-3d-shapes/'
# Time:  O(N^2)
# Space: O(1)
#
# Description: Leetcode # 883. Projection Area of 3D Shapes
#
# On a N * N grid, we place some 1 * 1 * 1 cubes that are axis-aligned with the x, y, and z axes.
#
# Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).
#
# Now we view the projection of these cubes onto the xy, yz, and zx planes.
#
# A projection is like a shadow, that maps our 3 dimensional figure to a 2 dimensional plane.
#
# Here, we are viewing the "shadow" when looking at the cubes from the top, the front, and the side.
#
# Return the total area of all three projections.
#
# Example 1:
#
# Input: [[2]]
# Output: 5
# Example 2:
#
# Input: [[1,2],[3,4]]
# Output: 17
# Explanation:
# Here are the three projections ("shadows") of the shape made with each axis-aligned plane.
#
# Example 3:
#
# Input: [[1,0],[0,2]]
# Output: 8
# Example 4:
#
# Input: [[1,1,1],[1,0,1],[1,1,1]]
# Output: 14
# Example 5:
#
# Input: [[2,2,2],[2,1,2],[2,2,2]]
# Output: 21
#
#
# Note:
#
# 1 <= grid.length = grid[0].length <= 50
# 0 <= grid[i][j] <= 50
#
import unittest

# 36ms 43.16%
class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        ans = 0

        for i in xrange(N):
            best_row = 0
            best_col = 0
            for j in xrange(N):
                if grid[i][j]: ans += 1
                best_row = max(best_row, grid[i][j])
                best_col = max(best_col, grid[j][i])

            ans += best_row + best_col
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/projection-area-of-3d-shapes/solution/
Approach 1: Mathematical
Complexity Analysis
Time Complexity: O(N^2), where N is the length of grid.
Space Complexity: O(1).

# 4ms 100%
class Solution {
    public int projectionArea(int[][] grid) {
        int N = grid.length;
        int ans = 0;

        for (int i = 0; i < N;  ++i) {
            int bestRow = 0;  // largest of grid[i][j]
            int bestCol = 0;  // largest of grid[j][i]
            for (int j = 0; j < N; ++j) {
                if (grid[i][j] > 0) ans++;  // top shadow
                bestRow = Math.max(bestRow, grid[i][j]);
                bestCol = Math.max(bestCol, grid[j][i]);
            }
            ans += bestRow + bestCol;
        }

        return ans;
    }
}


'''