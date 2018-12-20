__source__ = 'https://leetcode.com/problems/number-of-islands/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/number-of-islands.py
# Time:  O(m * n)
# Space: O(m * n)
# DFS
# Floodfill Algorithm
#
# Description: Leetcode # 200. Number of Islands
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally
# or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# 11110
# 11010
# 11000
# 00000
# Answer: 1
#
# Example 2:
#
# 11000
# 11000
# 00100
# 00011
# Answer: 3
#
# Companies
# Amazon Microsoft Google Facebook Zenefits
# Related Topics
# Depth-first Search Breadth-first Search Union Find
# Similar Questions
# Surrounded Regions Walls and Gates Number of Islands II Number of Connected Components in an Undirected Graph

#idea is to merge individual islands
import unittest
class Solution:
    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
        if grid == []:
            return 0
        row = len(grid)
        col = len(grid[0])
        used = [[False for j in xrange(col)] for i in xrange(row)]

        count = 0
        for i in xrange(row):
            for j in xrange(col):
                if grid[i][j] == '1' and not used[i][j]:
                    self.dfs(grid, used, row, col, i, j)
                    count += 1
        return count


    def dfs(self, grid, used, row, col, x, y):
        if grid[x][y] == '0' or used[x][y]:
            return 0
        used[x][y] = True

        if x != 0:
            self.dfs(grid, used, row, col, x - 1, y)
        if x != row -1:
            self.dfs(grid, used, row, col, x + 1, y)
        if y != 0 :
            self.dfs(grid, used, row, col, x, y - 1)
        if y != col - 1:
            self.dfs(grid, used, row, col, x, y + 1)

# java: http://www.programcreek.com/2014/04/leetcode-number-of-islands-java/
# idea is to merge individual islands
# not use visited
class Solution2:
    # @param grid, a list of list of characters
    # @return an integer
    def numIslands(self, grid):
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        count = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == '1':
                    self.mergeIsland(grid, i, j )
                    count += 1
        print grid
        return count

    def mergeIsland(self, grid, i, j):
        if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1:
            return

        if grid[i][j] != '1':
            return

        grid[i][j] = '2'

        #if i != 0:
        self.mergeIsland(grid, i-1, j)
        #if i != len(grid) - 1:
        self.mergeIsland(grid, i+1, j)
        #if j != 0:
        self.mergeIsland(grid, i, j-1)
        #if j != len(grid[0]) - 1:
        self.mergeIsland(grid, i , j+1)

# 172ms 9.08%
class Solution3(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def merge(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                grid[i][j] = '0'
                map(merge, (i+1, i-1, i, i), (j,j,j+1,j-1))
                return 1
            return 0
        return sum(merge(i, j) for i in xrange(len(grid)) for j in xrange(len(grid[0])))
#test
grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().numIslands(grid)
        print Solution2().numIslands(grid)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/number-of-islands/solution/

# BFS 
# 9ms 15.83%
class Solution {
    private static final int[][] DIRECTIONS = new int[][] {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};

    public int numIslands(char[][] grid) {
        int result = 0;
        int m = grid.length;
        int n = m == 0 ? 0 : grid[0].length;
        if (m == 0 || n == 0) {
            return 0;
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    grid[i][j] = '2';
                    bfs(grid, i, j);
                    result++;
                }
            }
        }
        return result;
    }

    private void bfs(char[][] grid, int i, int j) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(i * grid[0].length + j);
        while (!queue.isEmpty()) {
            int cur = queue.poll();
            int curI = cur / grid[0].length;
            int curJ = cur % grid[0].length;
            for (int[] direction : DIRECTIONS) {
                int newI = curI + direction[0];
                int newJ = curJ + direction[1];
                if (newI >= 0 && newI < grid.length && newJ >= 0 && newJ < grid[0].length && grid[newI][newJ] == '1') {
                    grid[newI][newJ] = '2';
                    queue.add(newI * grid[0].length + newJ);
                }
            }
        }
    }
}


2. DFS:
# 4ms 78.12%
class Solution {
    private static final int[][] DIRECTIONS = new int[][] {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};

    public int numIslands(char[][] grid) {
        int result = 0;
        int m = grid.length;
        int n = m == 0 ? 0 : grid[0].length;
        if (m == 0 || n == 0) {
            return 0;
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    grid[i][j] = '2';
                    dfs(grid, i, j);
                    result++;
                }
            }
        }
        return result;
    }

    private void dfs(char[][] grid, int i, int j) {
        for (int[] direction : DIRECTIONS) {
            int newI = i + direction[0];
            int newJ = j + direction[1];
            if (newI >= 0 && newI < grid.length && newJ >= 0 && newJ < grid[0].length && grid[newI][newJ] == '1') {
                grid[newI][newJ] = '2';
                dfs(grid, newI, newJ);
            }
        }
    }
}

# Union Find
# 7ms 28.60%
class Solution {
    public int numIslands(char[][] grid) {
        if(grid.length == 0 || grid[0].length == 0) return 0;
        int m = grid.length, n = grid[0].length;
        UF uf = new UF(m, n, grid);

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if(grid[i][j] == '0') continue;
                int p = i * n + j;
                int q;
                if (i > 0 && grid[i-1][j] == '1') {
                    q = p - n;
                    uf.union(p,q);
                }
                if (i < m-1 && grid[i+1][j] == '1') {
                    q = p + n;
                    uf.union(p, q);
                }
                if (j > 0 && grid[i][j-1] == '1') {
                    q = p - 1;
                    uf.union(p,q);
                }
                if (j < n - 1 && grid[i][j+1] == '1') {
                    q = p + 1;
                    uf.union(p, q);
                }
            }
        }
        return uf.count;
    }

    class UF{
        public int count = 0;
        public int[] id = null;

        public UF(int m, int n, char[][] grid) {
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (grid[i][j] == '1') count++;
                }
            }
            id = new int[m * n];
            for (int i = 0; i < m*n ;i++) {
                id[i] = i;
            }
        }

        public int find(int p) {
            while (p != id[p]) {
                id[p] = id[id[p]];
                p = id[p];
            }
            return p;
        }

        public boolean isConnected(int p, int q) {
            int pRoot = find(p);
            int qRoot = find(q);
            if (pRoot != qRoot) return false;
            else return true;
        }

        public void union(int p, int q) {
            int pRoot = find(p);
            int qRoot = find(q);
            if (pRoot == qRoot) return;
            id[pRoot] = qRoot;
            count--;
        }
    }
}

# 3ms 100%
class Solution {
    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0 || grid[0].length == 0) {
            return 0;
        }
        int count = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1') {
                    count++;
                    fill(grid, i, j);
                }
            }
        }
        return count;
    }

    private void fill(char[][] grid, int row, int col) {
        if (row < 0 || row >= grid.length || col < 0 || col >= grid[0].length || grid[row][col] == '0') {
            return;
        }
        grid[row][col] = '0';
        fill(grid, row - 1, col);
        fill(grid, row + 1, col);
        fill(grid, row, col - 1);
        fill(grid, row, col + 1);
    }
}
'''
