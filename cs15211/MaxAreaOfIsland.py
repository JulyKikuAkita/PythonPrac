__source__ = 'https://leetcode.com/problems/max-area-of-island/description/'
# Time:  O(R* C)
# Space: O(R * C)
#
# Description: Leetcode # 695. Max Area of Island
#
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land)
# connected 4-directionally (horizontal or vertical.)
# You may assume all four edges of the grid are surrounded by water.
#
# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
#
# Example 1:
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
#
# Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
# Example 2:
# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# Note: The length of each dimension in the given grid does not exceed 50.
#
# Companies
# Intuit Twitch
# Related Topics
# Array Depth-first Search
# Similar Questions
# Number of Islands Island Perimeter
#
import unittest
#212 ms
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        grid = {i + j*1j: val for i, row in enumerate(grid) for j, val in enumerate(row)}
        def area(z):
            return grid.pop(z, 0) and 1 + sum(area(z + 1j**k) for k in range(4))
        return max(map(area, set(grid)))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/articles/max-area-of-island/
#DFS
#66.19% 39ms
class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int max_area = 0;
        for(int i =0; i<grid.length; i++)
            for(int j =0; j<grid[0].length; j++)
                if(grid[i][j] == 1)max_area = Math.max(max_area, AreaOfIsland(grid, i, j));
        return max_area;
    }

    private int AreaOfIsland(int[][] grid, int i, int j){
        int m = grid.length, n = grid[0].length;
        if( i >= 0 && i < m && j >= 0 && j < n && grid[i][j] == 1){
            grid[i][j] = 0;
            return 1 + AreaOfIsland(grid, i+1, j) + AreaOfIsland(grid, i-1, j) + AreaOfIsland(grid, i, j-1) + AreaOfIsland(grid, i, j+1);
        }
        return 0;
    }
}

#BFS #52ms
#18.27% 48ms
class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        boolean[][] seen = new boolean[grid.length][grid[0].length];
        int[] dr = new int[]{1, -1, 0, 0};
        int[] dc = new int[]{0, 0, 1, -1};

        int ans = 0;
        for (int r0 = 0; r0 < grid.length; r0++) {
            for (int c0 = 0; c0 < grid[0].length; c0++) {
                if (grid[r0][c0] == 1 && !seen[r0][c0]) {
                    int shape = 0;
                    Stack<int[]> stack = new Stack();
                    stack.push(new int[]{r0, c0});
                    seen[r0][c0] = true;
                    while (!stack.empty()) {
                        int[] node = stack.pop();
                        int r = node[0], c = node[1];
                        shape++;
                        for (int k = 0; k < 4; k++) {
                            int nr = r + dr[k];
                            int nc = c + dc[k];
                            if (0 <= nr && nr < grid.length &&
                                    0 <= nc && nc < grid[0].length &&
                                    grid[nr][nc] == 1 && !seen[nr][nc]) {
                                stack.push(new int[]{nr, nc});
                                seen[nr][nc] = true;
                            }
                        }
                    }
                    ans = Math.max(ans, shape);
                }
            }
        }
        return ans;
    }
}

#97.85% 34ms
class Solution {
    int res=0;
    private int dfs(int[][] grid, int x, int y){
        if(x<0 || y<0 || x>=grid.length || y>=grid[0].length || grid[x][y]!=1){
            return 0;
        }
        grid[x][y]=0;

        int till = 1+ dfs(grid,x+1,y)+dfs(grid,x,y+1)+dfs(grid,x,y-1)+dfs(grid,x-1,y);
        res = till>res?till:res;

        return till;

    }
    public int maxAreaOfIsland(int[][] grid) {
        for(int x=0;x<grid.length;x++){
            for(int y=0;y<grid[0].length;y++){
                dfs(grid, x,y);
            }
        }
        return res;
    }
}
'''