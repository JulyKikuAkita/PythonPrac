__source__ = 'https://leetcode.com/problems/number-of-distinct-islands/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 694. Number of Distinct Islands
#
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land)
# connected 4-directionally (horizontal or vertical.)
# You may assume all four edges of the grid are surrounded by water.
#
# Count the number of distinct islands. An island is considered to be the same
# as another if and only if one island can be translated (and not rotated or reflected) to equal the other.
#
# Example 1:
# 11000
# 11000
# 00011
# 00011
# Given the above grid map, return 1.
# Example 2:
# 11011
# 10000
# 00001
# 11011
# Given the above grid map, return 3.
#
# Notice that:
# 11
# 1
# and
#  1
# 11
# are considered different island shapes, because we do not consider reflection / rotation.
# Note: The length of each dimension in the given grid does not exceed 50.
#
# Companies
# Amazon
# Related Topics
# Hash Table Depth-first Search
# Similar Questions
# Number of Islands
#
import unittest
import collections
# 76ms 98.09%
class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        row = len(grid)
        col = len(grid[0])
        visited = [[0 for _ in range(col)] for _ in range(row)]
        def dfs(x, y, c_str):
            visited[x][y] = 1
            if x - 1 >= 0 and grid[x-1][y] == 1 and visited[x-1][y] == 0:
                c_str += 'u'
                c_str = dfs(x-1, y, c_str)
                c_str += 'o'
            if y + 1 < col and grid[x][y+1] == 1 and visited[x][y+1] == 0:
                c_str += 'r'
                c_str = dfs(x, y+1, c_str)
                c_str += 'o'
            if x + 1 < row and grid[x+1][y] == 1 and visited[x+1][y] == 0:
                c_str += 'd'
                c_str = dfs(x+1, y, c_str)
                c_str += 'o'
            if y - 1 >= 0 and grid[x][y-1] == 1 and visited[x][y-1] == 0:
                c_str += 'l'
                c_str = dfs(x, y-1, c_str)
                c_str += 'o'
            return c_str
        ans = 0
        str_set = set()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    shape_str = dfs(i, j, '')
                    if shape_str not in str_set:
                        ans += 1
                        str_set.add(shape_str)
        return ans

#68ms 99.28%
class Solution2(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        def dfs(i, j, posr, posc):
            coord.append((posr, posc))
            grid[i][j] = 0
            if i < m - 1 and grid[i + 1][j]:
                dfs(i + 1, j, posr + 1, posc)
            if i > 0 and grid[i - 1][j]:
                dfs(i - 1, j, posr - 1, posc)
            if j < n - 1 and grid[i][j + 1]:
                dfs(i, j + 1, posr, posc + 1)
            if j > 0 and grid[i][j - 1]:
                dfs(i, j - 1, posr, posc - 1)
        d = collections.Counter()
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j]:
                    coord = []
                    dfs(i, j, 0, 0)
                    d[tuple(coord)]+=1
        return len(d)
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/number-of-distinct-islands/solution/
Approach #1: Hash By Local Coordinates [Accepted]
Complexity Analysis
Time Complexity: O(R*C), where R is the number of rows in the given grid, and C is the number of columns. 
We visit every square once.
Space complexity: O(R*C), the space used by seen to keep track of visited squares, and shapes.

# 32ms 53.77%
class Solution {
    int[][] grid;
    boolean[][] seen;
    Set<Integer> shape;
    
    public void explore(int r, int c, int r0, int c0) {
        if (0 <= r && r < grid.length && 0 <= c && c < grid[0].length &&
                grid[r][c] == 1 && !seen[r][c]) {
            seen[r][c] = true;
            shape.add((r - r0) * 2 * grid[0].length + (c - c0));
            explore(r+1, c, r0, c0);
            explore(r-1, c, r0, c0);
            explore(r, c+1, r0, c0);
            explore(r, c-1, r0, c0);
        }
    }
    public int numDistinctIslands(int[][] grid) {
        this.grid = grid;
        seen = new boolean[grid.length][grid[0].length];
        Set shapes = new HashSet<HashSet<Integer>>();

        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[0].length; c++) {
                shape = new HashSet<Integer>();
                explore(r, c, r, c);
                if (!shape.isEmpty()) {
                    shapes.add(shape);
                }
            }
        }

        return shapes.size();
    }
}

# Approach #2: Hash By Path Signature [Accepted]
# Complexity Analysis
# Time and Space Complexity: O(R * C). The analysis is the same as in Approach #1.
# When we start a depth-first search on the top-left square of some island, 
# the path taken by our depth-first search will be the same if and only if the shape is the same.
# 50ms 39.12%
class Solution {
    int[][] grid;
    boolean[][] seen;
    ArrayList<Integer> shape;
    
    public int numDistinctIslands(int[][] grid) {
        this.grid = grid;
        seen = new boolean[grid.length][grid[0].length];
        Set shapes = new HashSet<ArrayList<Integer>>();
        
        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[0].length; c++) {
                shape = new ArrayList<Integer>();
                explore(r, c, 0);
                if (!shape.isEmpty()) shapes.add(shape);
            }
        }
        return shapes.size();
    }
    
    public void explore(int r, int c, int di) {
        if (0 <= r && r < grid.length && 0 <= c && c < grid[0].length && grid[r][c] == 1 && !seen[r][c]) {
            seen[r][c] = true;
            shape.add(di);
            explore(r+1, c, 1);
            explore(r-1, c, 2);
            explore(r, c+1, 3);
            explore(r, c-1, 4);
            shape.add(0);
        }
    }
}

# Rolling hash
# 19ms 99.84%
class Solution {
    public int numDistinctIslands(int[][] grid) {
        HashSet<Integer> set = new HashSet<>();
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1) {
                    int hash = dfs(grid, i, j, i, j, 17);
                    if (!set.contains(hash)) set.add(hash);
                }
            }
        }
        return set.size();
    }

    private int dfs(int[][] grid, int stx, int sty, int x, int y, int hash){
        if ( x < 0 || x >= grid.length || y < 0 || y >= grid[0].length || grid[x][y]!=1) return hash;
        grid[x][y] = 2;
        hash = hash * 31 + (x - stx) * grid.length + (y - sty);
        for (int i = -1; i < 2; i += 2) {
            hash = dfs(grid, stx, sty, x + i, y, hash);
            hash = dfs(grid, stx, sty, x, y + i, hash);
        }
        return hash;
    }
}
'''
