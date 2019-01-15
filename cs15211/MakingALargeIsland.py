__source__ = 'https://leetcode.com/problems/making-a-large-island/'
# Time:  O(N^2)
# Space: O(N^2)
#
# Description: Leetcode # 827. Making A Large Island
#
# In a 2D grid of 0s and 1s, we change at most one 0 to a 1.
#
# After, what is the size of the largest island? (An island is a 4-directionally connected group of 1s).
#
# Example 1:
#
# Input: [[1, 0], [0, 1]]
# Output: 3
# Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
#
# Example 2:
#
# Input: [[1, 1], [1, 0]]
# Output: 4
# Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
#
# Example 3:
#
# Input: [[1, 1], [1, 1]]
# Output: 4
# Explanation: Can't change any 0 to 1, only one island with area = 4.
#
# Notes:
#
#     1 <= grid.length = grid[0].length <= 50.
#     0 <= grid[i][j] <= 1.
#
import unittest

# 80ms 73.64%
class Solution(object):
    def largestIsland(self, grid):
        N = len(grid)

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < N and 0 <= nc < N:
                    yield nr, nc

        def dfs(r, c, index):
            ans = 1
            grid[r][c] = index
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    ans += dfs(nr, nc, index)
            return ans

        area = {}
        index = 2
        for r in xrange(N):
            for c in xrange(N):
                if grid[r][c] == 1:
                    area[index] = dfs(r, c, index)
                    index += 1

        ans = max(area.values() or [0])
        for r in xrange(N):
            for c in xrange(N):
                if grid[r][c] == 0:
                    seen = {grid[nr][nc] for nr, nc in neighbors(r, c) if grid[nr][nc] > 1}
                    ans = max(ans, 1 + sum(area[i] for i in seen))
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/making-a-large-island/solution/
#
Approach #1: (Naive) Depth First Search [Time Limit Exceeded]
Complexity Analysis
Time Complexity: O(N^4), where N is the length and width of the grid.
Space Complexity: O(N^2), the additional space used in the depth first search by stack and seen.

# TLE ~ 608ms 1.08%
class Solution {
    int[] dr = new int[]{-1, 0, 1, 0};
    int[] dc = new int[]{0, -1, 0, 1};

    public int largestIsland(int[][] grid) {
        int N = grid.length;

        int ans = 0;
        boolean hasZero = false;
        for (int r = 0; r < N; ++r)
            for (int c = 0; c < N; ++c)
                if (grid[r][c] == 0) {
                    hasZero = true;
                    grid[r][c] = 1;
                    ans = Math.max(ans, check(grid, r, c));
                    grid[r][c] = 0;
                }

        return hasZero ? ans : N*N;
    }

    public int check(int[][] grid, int r0, int c0) {
        int N = grid.length;
        Stack<Integer> stack = new Stack();
        Set<Integer> seen = new HashSet();
        stack.push(r0 * N + c0);
        seen.add(r0 * N + c0);

        while (!stack.isEmpty()) {
            int code = stack.pop();
            int r = code / N, c = code % N;
            for (int k = 0; k < 4; ++k) {
                int nr = r + dr[k], nc = c + dc[k];
                if (!seen.contains(nr * N + nc) && 0 <= nr && nr < N &&
                        0 <= nc && nc < N && grid[nr][nc] == 1) {
                    stack.push(nr * N + nc);
                    seen.add(nr * N + nc);
                }
            }
        }

        return seen.size();
    }
}

Approach #2: Component Sizes [Accepted]
Complexity Analysis
Time Complexity: O(N^2), where N is the length and width of the grid.
Space Complexity: O(N^2), the additional space used in the depth first search by area.

# 14ms 91.76%
class Solution {
    int[][] directions = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    public int largestIsland(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[][] ids = new int[m][n];
        int[][] area = new int[m][n];
        Map<Integer, Integer> map = new HashMap<>();
        int id = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int[] sum = new int[1];
                if (grid[i][j] == 1 && ids[i][j] == 0) {
                    id++;
                    dfs(grid, ids, id, i, j, m, n, sum);
                    map.put(id, sum[0]);
                }
            }
        }
        int result = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0) {
                    int currentArea = 0;
                    Set<Integer> set = new HashSet<>();
                    for (int k = 0; k < directions.length; k++) {
                        int nextX = i + directions[k][0];
                        int nextY = j + directions[k][1];
                        if (nextX >= 0 && nextX < m && nextY >= 0 && nextY < n && grid[nextX][nextY] == 1 && !set.contains(ids[nextX][nextY]) ) {
                            currentArea += map.get(ids[nextX][nextY]);
                            set.add(ids[nextX][nextY]);
                        }
                    }
                        currentArea += 1;
                    result = Math.max(result, currentArea);
                }
            }
        }
        if (result == 0) {
            for (Map.Entry<Integer, Integer> e : map.entrySet()) {
                result += e.getValue();
            }
        }
        return result;
    }
    private void dfs(int[][] grid, int[][] ids, int id, int x, int y, int m, int n, int[] sum) {
        sum[0]++;
        ids[x][y] = id;
        for (int i = 0; i < directions.length; i++) {
            int nextX = x + directions[i][0];
            int nextY = y + directions[i][1];
            if (nextX >= 0 && nextX < m && nextY >= 0 && nextY < n && grid[nextX][nextY] == 1 && ids[nextX][nextY] == 0) {
                dfs(grid, ids, id, nextX, nextY, m, n, sum);
            }
        }
        return;
    }
}

# https://leetcode.com/problems/making-a-large-island/discuss/127015/C%2B%2B-O(n*m)-15-ms-colorful-islands
# Same as coloring each existing island without using extra id[]
# 28ms 41.15%
class Solution {
    public int largestIsland(int[][] grid) {
        Map<Integer, Integer> map = new HashMap<>(); //Key: color, Val: size of island painted of that color
        map.put(0, 0); //We won't paint island 0, hence make its size 0, we will use this value later   
        int n = grid.length; 
        int colorIndex = 2; //0 and 1 is already used in grid, hence we start colorIndex from 2 
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    int size = paint(grid, i, j, colorIndex);
                    map.put(colorIndex, size);
                    colorIndex++;
                }
            }
        }
        
        //If there is no island 0 from grid, res should be the size of islands of first color
        //If there is no island 1 from grid, res should be 0 
        int res = map.getOrDefault(2, 0); 
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0) {
                    Set<Integer> set = new HashSet(); //We use a set to avoid repeatly adding islands with the same color
                    //If current island is at the boundary, we add 0 to the set, whose value is 0 in the map
                    set.add(i > 0 ? grid[i - 1][j] : 0);
                    set.add(j > 0 ? grid[i][j - 1] : 0);
                    set.add(i < n - 1 ? grid[i + 1][j] : 0);
                    set.add(j < n - 1 ? grid[i][j + 1] : 0);
                    
                    int newSize = 1; //We need to count current island as well, hence we init newSize with 1
                    for (int color : set) newSize += map.get(color);
                    res = Math.max(res, newSize);
                }
            }
        }
         return res;
    }
    
    private int paint(int[][] grid, int i, int j, int color) {
        if (i < 0 || j < 0 || i >= grid.length || j >= grid[0].length || grid[i][j] != 1) return 0;
        grid[i][j] = color;
        return 1 + paint(grid, i + 1, j, color) + paint(grid, i - 1, j , color) 
                 + paint(grid, i, j + 1, color) + paint(grid, i, j - 1, color);
    }
}

# Union find, same idea as above
# 20ms 97.92%
class Solution {
    private int[] id;
    private int[] size;
    private int[] dx = new int[]{1, 0, -1, 0};
    private int[] dy = new int[]{0, -1, 0, 1};
    private int max;
    
    public int largestIsland(int[][] grid) {
        if (grid == null) return 0;
        int rows = grid.length;
        int cols = grid[0].length;
        id = new int[rows * cols];
        size = new int[rows * cols];
        for (int i = 0; i < rows * cols; i++) {
            id[i] = i;
            size[i] = 1;
        }
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] != 0) {
                    max = Math.max(max, 1);
                    if (i > 0 && grid[i - 1][j] != 0) {
                        union((i - 1) * cols + j, i * cols + j);
                    }
                    if (j > 0 && grid[i][j - 1] != 0) {
                        union(i * cols + (j - 1), i * cols + j);
                    }
                }
            }
        }
        
         for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 0) {
                    Set<Integer> visited = new HashSet<>();
                    int currSize = 1;
                    for (int k = 0; k < 4; k++) {
                        int x = i + dx[k], y = j + dy[k];
                        if (x >= 0 && x < rows && y >= 0 && y < cols && grid[x][y] != 0) {
                            int rootId = root(x * cols + y);
                            if (!visited.contains(rootId)) {
                                visited.add(rootId);
                                currSize += size[rootId];
                            }
                        }
                    }
                    max = Math.max(max, currSize);
                }      
            }
        }
        return max;
    }
    
    private int root(int i) {
        if (i == id[i]) return i;
        return root(id[i]);
    }
    
    private void union(int p, int q) {
        int rootP = root(p);
        int rootQ = root(q);
        if (rootP == rootQ) return;
        if (size[rootP] < size[rootQ]) {
            id[rootP] = rootQ;
            size[rootQ] += size[rootP];
            max = Math.max(max, size[rootQ]);
        } else {
            id[rootQ] = rootP;
            size[rootP] += size[rootQ];
            max = Math.max(max, size[rootP]);
        }
    }
}

'''
