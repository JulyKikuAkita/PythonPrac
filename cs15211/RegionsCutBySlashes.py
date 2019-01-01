# coding=utf-8
__source__ = 'https://leetcode.com/problems/regions-cut-by-slashes/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 959. Regions Cut By Slashes
#
# In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space.
# These characters divide the square into contiguous regions.
#
# (Note that backslash characters are escaped, so a \ is represented as "\\".)
#
# Return the number of regions.
#
# Example 1:
#
# Input:
# [
#   " /",
#   "/ "
# ]
# Output: 2
# Explanation: The 2x2 grid is as follows:
#
# Example 2:
#
# Input:
# [
#   " /",
#   "  "
# ]
# Output: 1
# Explanation: The 2x2 grid is as follows:
#
# Example 3:
#
# Input:
# [
#   "\\/",
#   "/\\"
# ]
# Output: 4
# Explanation: (Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.)
# The 2x2 grid is as follows:
#
# Example 4:
#
# Input:
# [
#   "/\\",
#   "\\/"
# ]
# Output: 5
# Explanation: (Recall that because \ characters are escaped, "/\\" refers to /\, and "\\/" refers to \/.)
# The 2x2 grid is as follows:
#
# Example 5:
#
# Input:
# [
#   "//",
#   "/ "
# ]
# Output: 3
# Explanation: The 2x2 grid is as follows:
#
# Note:
#
#     1 <= grid.length == grid[0].length <= 30
#     grid[i][j] is either '/', '\', or ' '.
#
import unittest

# 396ms 27.27%
class DSU:
    def __init__(self, N):
        self.p = range(N)

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr

class Solution(object):
    def regionsBySlashes(self, grid):
        N = len(grid)
        dsu = DSU(4 * N * N)
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                root = 4 * (r*N + c)
                if val in '/ ':
                    dsu.union(root + 0, root + 1)
                    dsu.union(root + 2, root + 3)
                if val in '\ ':
                    dsu.union(root + 0, root + 2)
                    dsu.union(root + 1, root + 3)

                # north/south
                if r+1 < N: dsu.union(root + 3, (root+4*N) + 0)
                if r-1 >= 0: dsu.union(root + 0, (root-4*N) + 3)
                # east/west
                if c+1 < N: dsu.union(root + 2, (root+4) + 1)
                if c-1 >= 0: dsu.union(root + 1, (root-4) + 2)
        return sum(dsu.find(x) == x for x in xrange(4*N*N))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/regions-cut-by-slashes/solution/
#
Approach 1: Union-Find
Complexity Analysis
Time Complexity: O(N * N * α(N)), where N is the length of the grid, and α is the Inverse-Ackermann function 
(if we were to use union-find by rank.)
Space Complexity: O(N * N)

# Union Find
# 24ms 24.18%
class Solution {
    class DSU {
        int[] parent;
        public DSU (int N) {
            parent = new int[N];
            for (int i = 0; i < N; i++) parent[i] = i;
        }
        
        public int find(int x) {
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        }
        
        public void union(int x, int y) {
            parent[find(x)] = find(y);
        }
    }
    
    public int regionsBySlashes(String[] grid) {
        int N = grid.length;
        DSU dsu = new DSU(4 * N * N);
        for (int r = 0; r < N; ++r) {
            for (int c = 0; c < N; ++c) {
                int root = 4 * ( r * N + c);
                char val = grid[r].charAt(c);
                if (val != '\\') {
                    dsu.union(root + 0, root + 1);
                    dsu.union(root + 2, root + 3);
                }
                if (val != '/') {
                    dsu.union(root + 0, root + 2);
                    dsu.union(root + 1, root + 3);
                }
                
                // north south
                if (r + 1 < N) dsu.union(root + 3, (root + 4 * N) + 0);
                if (r - 1 >= 0) dsu.union(root + 0, (root - 4 * N) + 3);
                
                // east west
                if (c + 1 < N) dsu.union(root + 2, (root + 4) + 1);
                if (c - 1 >= 0) dsu.union(root + 1, (root - 4) + 2);
            }
        }
        
        int ans = 0;
        for (int x = 0; x < 4 * N * N; ++x) {
            if (dsu.find(x) == x) ans++;
        }
        return ans;
    }
}

# Union Find
# 16ms 57.68%
class Solution {
    class DSU {
        int[] parent;
        public DSU (int N) {
            parent = new int[N];
            for (int i = 0; i < N; i++) parent[i] = i;
        }
        
        public int find (int x) {
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        }
        
        public void union(int x, int y) {
            parent[find(x)] = find(y);
        }
        
    }
    
    public int regionsBySlashes(String[] grid) {
        int N = grid.length;
        int num_csg = 1;
        if (N == 0) return 0;
        DSU dsu = new DSU((N + 1) * (N + 1));
        int x, y;
        for (int i = 0; i <= N; i++) {
            dsu.union(0, i);
            dsu.union(0, N * (N + 1) + i);
            dsu.union(0, i * (N + 1));
            dsu.union(0, (i + 1) * (N + 1) - 1);
        }
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (grid[i].charAt(j) != ' ') {
                    if (grid[i].charAt(j) == '/') {
                        x = i * (N + 1) + j + 1;
                        y = (i + 1) * (N + 1) + j;
                    } else {
                        x = i * (N + 1) + j;
                        y = ( i + 1) * (N + 1) + j + 1;
                    }
                    if (dsu.find(x) == dsu.find(y)) {
                        num_csg++;
                    } else {
                        dsu.union(x, y);
                    }
                } 
            }
        }
        return num_csg;
    }
    
}

# DFS
# 14ms 69.61%
class Solution {
    private static final int NORTH = 0, WEST = 1, EAST = 2, SOUTH = 3;
    
    public int regionsBySlashes(String[] grid) {
        final int N = grid.length;
        int color = 0;
        final boolean[][][] visited = new boolean[4][N][N];

        for (int i = 0; i < N; i++) {
          for (int j = 0; j < N; j++) {
            for (int k = 0; k < 4; k++) {
              if (!visited[k][i][j]) {
                dfs(grid, visited, i, j, k);
                color++;
              }
            }
          }
        }
        return color;
    }
    
      private static void dfs(final String[] grid, final boolean[][][] visited, final int i, final int j, final int k) {
          final int N = grid.length;
          if (i < 0 || j < 0 || i >= N || j >= N || visited[k][i][j] || k >= 4) return;
          final char chr = grid[i].charAt(j);
          if (chr == '\\') {
              if (k == NORTH || k == EAST) {
                  visited[NORTH][i][j] = visited[EAST][i][j] = true;
                  dfs(grid, visited, i - 1, j, SOUTH);
                  dfs(grid, visited, i, j + 1, WEST);
              } else {
                  visited[SOUTH][i][j] = visited[WEST][i][j] = true;
                  dfs(grid, visited, i + 1, j, NORTH);
                  dfs(grid, visited, i, j - 1, EAST);
              }
          } else if ( chr == '/') {
              if (k == NORTH || k == WEST) {
                  visited[NORTH][i][j] = visited[WEST][i][j] = true;
                  dfs(grid, visited, i - 1, j, SOUTH);
                  dfs(grid, visited, i, j - 1, EAST);
              } else {
                  visited[SOUTH][i][j] = visited[EAST][i][j] = true;
                  dfs(grid, visited, i + 1, j , NORTH);
                  dfs(grid, visited, i, j + 1, WEST);
              }
          } else {
              assert chr == ' ';
              for (int kk = 0; kk < 4; kk++) visited[kk][i][j] = true;
              dfs(grid, visited, i + 1, j , NORTH);
              dfs(grid, visited, i - 1, j, SOUTH);
              dfs(grid, visited, i, j + 1, WEST);
              dfs(grid, visited, i, j - 1, EAST);
          }
      }
}
'''
