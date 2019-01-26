__source__ = 'https://leetcode.com/problems/unique-paths-iii/'
# Time:  O(4^(R*C)), where R,C are the number of rows and columns in the grid.
# Space: O(R*C)
#
# Description: Leetcode # 980. Unique Paths III
#
# On a 2-dimensional grid, there are 4 types of squares:
#
# 1 represents the starting square.  There is exactly one starting square.
# 2 represents the ending square.  There is exactly one ending square.
# 0 represents empty squares we can walk over.
# -1 represents obstacles that we cannot walk over.
# Return the number of 4-directional walks from the starting square to the ending square,
# that walk over every non-obstacle square exactly once.
#
# Example 1:
#
# Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# Output: 2
# Explanation: We have the following two paths:
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
# 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
# Example 2:
#
# Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
# Output: 4
# Explanation: We have the following four paths:
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
# 2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
# 3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
# 4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
# Example 3:
#
# Input: [[0,1],[2,0]]
# Output: 0
# Explanation:
# There is no path that walks over every empty square exactly once.
# Note that the starting and ending square can be anywhere in the grid.
#
# Note:
#
# 1 <= grid.length * grid[0].length <= 20
#
import unittest
# 48ms 100%
class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R, C = len(grid), len(grid[0])

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] % 2 == 0:
                    yield nr, nc

        todo = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val != -1: todo += 1
                if val == 1: sr, sc = r, c
                if val == 2: tr, tc = r, c

        self.ans = 0
        def dfs(r, c, todo):
            todo -= 1
            if todo < 0: return
            if r == tr and c == tc:
                if todo == 0:
                    self.ans += 1
                return

            grid[r][c] = -1
            for nr, nc in neighbors(r, c):
                dfs(nr, nc, todo)
            grid[r][c] = 0

        dfs(sr, sc, todo)
        return self.ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/unique-paths-iii/solution/
# Approach 1: Backtracking DFS
# Complexity Analysis
# Time Complexity: O(4^(R*C)), where R,C are the number of rows and columns in the grid. 
# (We can find tighter bounds, but such a bound is beyond the scope of this article.)
# Space Complexity: O(R*C) 
# I see a O(4 * 3^(R*C)) or O(3^(R*C)) bound. On each call to the DFS, 
# there are 4 possible branches (up, down, left, right). 
# However only the starting state has 4 possible branches. 
# For DFS calls after the first one, 1 of the 4 branches points to the direction you came from. 
# Since you are only allowed to visit nodes once, 
# this branch will terminate immediately hence there's only 3 valid branches to explore.
# 2ms 100%
class Solution {
    int ans;
    int[][] grid;
    int tr, tc;
    int[] dr = new int[]{0, -1, 0, 1};
    int[] dc = new int[]{1, 0, -1, 0};
    int R, C;

    public int uniquePathsIII(int[][] grid) {
        this.grid = grid;
        R = grid.length;
        C = grid[0].length;

        int todo = 0;
        int sr = 0, sc = 0;
        for (int r = 0; r < R; ++r)
            for (int c = 0; c < C; ++c) {
                if (grid[r][c] != -1) {
                    todo++;
                }

                if (grid[r][c] == 1) {
                    sr = r;
                    sc = c;
                } else if (grid[r][c] == 2) {
                    tr = r;
                    tc = c;
                }
            }

        ans = 0;
        dfs(sr, sc, todo);
        return ans;
    }

    public void dfs(int r, int c, int todo) {
        todo--;
        if (todo < 0) return;
        if (r == tr && c == tc) {
            if (todo == 0) ans++;
            return;
        }

        grid[r][c] = 3;
        for (int k = 0; k < 4; ++k) {
            int nr = r + dr[k];
            int nc = c + dc[k];
            if (0 <= nr && nr < R && 0 <= nc && nc < C) {
                if (grid[nr][nc] % 2 == 0)
                    dfs(nr, nc, todo);
            }
        }
        grid[r][c] = 0;
    }
}

# Approach 2: Dynamic Programming
# Complexity Analysis
# Time Complexity: O(R * C * 2^(R*C), where R, C are the number of rows and columns in the grid.
# Space Complexity: O(R * C). 
# 135ms 100% 

class Solution {
    int ans;
    int[][] grid;
    int R, C;
    int tr, tc, target;
    int[] dr = new int[]{0, -1, 0, 1};
    int[] dc = new int[]{1, 0, -1, 0};
    Integer[][][] memo;

    public int uniquePathsIII(int[][] grid) {
        this.grid = grid;
        R = grid.length;
        C = grid[0].length;
        target = 0;

        int sr = 0, sc = 0;
        for (int r = 0; r < R; ++r)
            for (int c = 0; c < C; ++c) {
                if (grid[r][c] % 2 == 0)
                    target |= code(r, c);

                if (grid[r][c] == 1) {
                    sr = r;
                    sc = c;
                } else if (grid[r][c] == 2) {
                    tr = r;
                    tc = c;
                }
            }

        memo = new Integer[R][C][1 << R*C];
        return dp(sr, sc, target);
    }

    public int code(int r, int c) {
        return 1 << (r * C + c);
    }

    public Integer dp(int r, int c, int todo) {
        if (memo[r][c][todo] != null)
            return memo[r][c][todo];

        if (r == tr && c == tc) {
            return todo == 0 ? 1 : 0;
        }

        int ans = 0;
        for (int k = 0; k < 4; ++k) {
            int nr = r + dr[k];
            int nc = c + dc[k];
            if (0 <= nr && nr < R && 0 <= nc && nc < C) {
                if ((todo & code(nr, nc)) != 0)
                    ans += dp(nr, nc, todo ^ code(nr, nc));
            }
        }
        memo[r][c][todo] = ans;
        return ans;
    }
}

# https://leetcode.com/problems/unique-paths-iii/discuss/221946/JavaPython-Brute-Force-Backstracking
# Backtracking
# 2ms 100%
class Solution {
    int res = 0, empty = 1, sx, sy, ex, ey;
    public int uniquePathsIII(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0) empty++;
                else if (grid[i][j] == 1) {
                    sx = i;
                    sy = j;
                } else if (grid[i][j] == 2) {
                    ex = i;
                    ey = j;
                }
            }
        }
        dfs(grid, sx, sy);
        return res;
    }
    
    private void dfs(int[][] grid, int x0, int y0) {
        if (x0 < 0 || x0 >= grid.length || y0 < 0 || y0 >= grid[0].length || grid[x0][y0] < 0) return;
        if (x0 == ex && y0 == ey && empty == 0) {
            res++;
            return;
        }
        grid[x0][y0] = -2;
        empty--;
        for (int i = -1; i < 2; i += 2) {
            dfs(grid, x0 + i, y0);
            dfs(grid, x0, y0 + i);
        }
        grid[x0][y0] = 0;
        empty++;
    }
}

# 10ms 100%
class Solution {
    private int m, n, numEmpty;
    private static final int[][] directions = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    
    public int uniquePathsIII(int[][] grid) {
        int startX = 0, startY = 0, endX = 0, endY = 0;
        m = grid.length; 
        n = grid[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    startX = i;
                    startY = j;
                } else if (grid[i][j] == 2) {
                    endX = i;
                    endY = j;
                } else if (grid[i][j] == 0) {
                    numEmpty++;
                }
            }
        }
        Set<Integer> visited = new HashSet<>();
        visited.add(startX * n + startY);
        return countPaths(startX, startY, visited, endX, endY, grid);
    }
    
    private int countPaths(int x, int y, Set<Integer> visited, int endX, int endY, int[][] grid) {
        if (x == endX && y == endY && visited.size() - 2 == numEmpty) return 1;
        int count = 0;
        for (int[] dir : directions) {
            int nx = x + dir[0];
            int ny = y + dir[1];
            if (nx < 0 || nx >= m || ny < 0 || ny >= n || grid[x][y] == -1 ) continue;
            if (!visited.contains(nx * n + ny)) {
                visited.add(nx * n + ny);
                count += countPaths(nx, ny, visited, endX, endY, grid);
                visited.remove(nx * n + ny);
            }
        }
        return count;
    }

}
'''
