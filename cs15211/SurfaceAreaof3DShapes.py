__source__ = 'https://leetcode.com/problems/surface-area-of-3d-shapes/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 892. Surface Area of 3D Shapes
#
# On a N * N grid, we place some 1 * 1 * 1 cubes.
#
# Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).
#
# Return the total surface area of the resulting shapes.
#
# Example 1:
#
# Input: [[2]]
# Output: 10
#
# Example 2:
#
# Input: [[1,2],[3,4]]
# Output: 34
#
# Example 3:
#
# Input: [[1,0],[0,2]]
# Output: 16
#
# Example 4:
#
# Input: [[1,1,1],[1,0,1],[1,1,1]]
# Output: 32
#
# Example 5:
#
# Input: [[2,2,2],[2,1,2],[2,2,2]]
# Output: 46
#
# Note:
#
#     1 <= N <= 50
#     0 <= grid[i][j] <= 50
#
import unittest

# 56ms 46.11%
class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        ans = 0
        for r in xrange(N):
            for c in xrange(N):
                if grid[r][c]:
                    ans += 2
                    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r,c+1)):
                        if 0 <= nr < N and 0 <= nc < N:
                            nval = grid[nr][nc]
                        else:
                            nval = 0
                        ans += max(grid[r][c] - nval, 0)
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/surface-area-of-3d-shapes/solution/
#
Approach 1: Square by Square
For each v = grid[r][c] > 0, count ans += 2, 
plus ans += max(v - nv, 0) for each neighboring value nv adjacent to grid[r][c].
Complexity Analysis
Time Complexity: O(N^2), where N is the number of rows (and columns) in the grid.
Space Complexity: O(1) 

# 7ms 83.22%
class Solution {
    public int surfaceArea(int[][] grid) {
        int[] dr = new int[]{0, 1, 0, -1};
        int[] dc = new int[]{1, 0, -1, 0};

        int N = grid.length;
        int ans = 0;
        
        for (int r = 0; r < N; ++r)
            for (int c = 0; c < N; ++c)
                if (grid[r][c] > 0) {
                    ans += 2;
                    for (int k = 0; k < 4; k++) {
                        int nr = r + dr[k];
                        int nc = c + dc[k];
                        int nv = 0;
                        if (0 <= nr && nr < N && 0 <= nc && nc < N) nv = grid[nr][nc];
                        ans += Math.max(grid[r][c] - nv, 0);
                    }
                }
                
       return ans; 
    }
}

# 5ms 100%
class Solution {
    public int surfaceArea(int[][] grid) {
        int n = grid.length;
        int res = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n ; j++) {
                int number = grid[i][j];
                if (number > 0) res += number * 4 + 2;
                if (i > 0) res -= Math.min(number, grid[i - 1][j]) * 2;
                if (j > 0) res -= Math.min(number, grid[i][j - 1]) * 2;
            }
        }
        return res;   
    }
}
'''
