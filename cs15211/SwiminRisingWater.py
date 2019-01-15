__source__ = 'https://leetcode.com/problems/swim-in-rising-water/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 778. Swim in Rising Water
#
# On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j).
#
# Now rain starts to fall. At time t, the depth of the water everywhere is t.
# You can swim from a square to another 4-directionally adjacent square
# if and only if the elevation of both squares individually are at most t.
# You can swim infinite distance in zero time.
# Of course, you must stay within the boundaries of the grid during your swim.
#
# You start at the top left square (0, 0).
# What is the least time until you can reach the bottom right square (N-1, N-1)?
#
# Example 1:
#
# Input: [[0,2],[1,3]]
# Output: 3
# Explanation:
# At time 0, you are in grid location (0, 0).
# You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
#
# You cannot reach point (1, 1) until time 3.
# When the depth of water is 3, we can swim anywhere inside the grid.
#
# Example 2:
#
# Input: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
# Output: 16
# Explanation:
#  0  1  2  3  4
# 24 23 22 21  5
# 12 13 14 15 16
# 11 17 18 19 20
# 10  9  8  7  6
#
# The final route is marked in bold.
# We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
#
# Note:
#
#     2 <= N <= 50.
#     grid[i][j] is a permutation of [0, ..., N*N - 1].
#
import unittest
import heapq
# 92ms 57.69%
class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        seen = {(0, 0)}
        pq = [(grid[0][0], 0, 0)]
        ans = 0
        while pq:
            d, r, c = heapq.heappop(pq)
            ans = max(ans, d)
            if r == c == N-1: return ans
            for cr, cc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= cr < N and 0 <= cc < N and (cr, cc) not in seen:
                    heapq.heappush(pq, (grid[cr][cc], cr, cc))
                    seen.add((cr, cc))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/swim-in-rising-water/solution/
#
Approach #1: Heap [Accepted]
Complexity Analysis
Time Complexity: O(N^2 LogN) We may expand O(N^2) nodes, 
and each one requires O(LogN) time to perform the heap operations.
Space Complexity: O(N^2), the maximum size of the heap.

# 94ms 17.91%
class Solution {
    public int swimInWater(int[][] grid) {
        int N = grid.length;
        Set<Integer> seen = new HashSet();
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>((k1, k2) ->
                grid[k1 / N][k1 % N] - grid[k2 / N][k2 % N]);
        pq.offer(0);
        int ans = 0;
        int[] dr = new int[]{1, -1, 0, 0};
        int[] dc = new int[]{0, 0, 1, -1};
        
        while (!pq.isEmpty()) {
            int k = pq.poll();
            int r = k / N, c = k % N;
            ans = Math.max(ans, grid[r][c]);
            if (r == N-1 && c == N-1) return ans;
            
            for (int i = 0; i < 4; ++i) {
                int cr = r + dr[i], cc = c + dc[i];
                int ck = cr * N + cc;
                if (0 <= cr && cr < N && 0 <= cc && cc < N && !seen.contains(ck)) {
                    pq.offer(ck);
                    seen.add(ck);
                }

            }
        }
        throw null;
    }
}

Approach #2: Binary Search and DFS [Accepted]
Complexity Analysis
Time Complexity: O(N^2LogN). Our depth-first search during a call to possible isO(N^2), 
and we make up to O(LogN) of them.
Space Complexity: O(N^2), the maximum size of the stack.

# 74ms 33.06%
class Solution {
    public int swimInWater(int[][] grid) {
        int N = grid.length;
        int lo = grid[0][0], hi = N * N;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (!possible(mid, grid)) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }
    
    private boolean possible(int T, int[][] grid) {
        int N = grid.length;
        Set<Integer> seen = new HashSet();
        seen.add(0);
        int[] dr = new int[]{1, -1, 0, 0};
        int[] dc = new int[]{0, 0, 1, -1};

        Stack<Integer> stack = new Stack();
        stack.add(0);
        while (!stack.empty()) {
            int k = stack.pop();
            int r = k / N, c = k % N;
            if (r == N-1 && c == N-1) return true;
            for (int i = 0; i < 4; i++) {
                int cr = r + dr[i], cc = c + dc[i];
                int ck = cr * N + cc;
                if (0 <= cr && cr < N && 0 <= cc && cc < N && !seen.contains(ck) && grid[cr][cc] <= T) {
                    stack.add(ck);
                    seen.add(ck);
                }
            }
        }
        return false;
    }
}

# 5ms 97.80%
class Solution {
    
    private static int[][] DIRECTIONS = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    
    public int swimInWater(int[][] grid) {
        if (grid.length == 0 || grid[0].length == 0) {
            return 0;
        }
        int n = grid.length;
        int high = n * n - 1;
        int low = grid[0][0];
        while (low < high) {      
            int mid = low + (high - low) / 2;
            boolean[][] visited = new boolean[n][n];
            if (hasPath(grid, n, visited, 0, 0, mid)) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return high;
    }
    
    private boolean hasPath(int[][] grid, int n, boolean[][] visited, int i, int j, int waterLevel) {
        if (i == n - 1 && j == n - 1) {
            return true;
        }
        visited[i][j] = true;
        for (int[] direction: DIRECTIONS) {
            int x = direction[0] + i;
            int y = direction[1] + j;
            if (x >= 0 && x < n && y >= 0 && y < n && !visited[x][y] && grid[x][y] <= waterLevel) {
                if (hasPath(grid, n, visited, x, y, waterLevel)) {
                    return true;
                }
            }
        }
        return false;
    }
}

# 7ms 95.88%
class Solution {
    private static int[][] DIRS = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public int swimInWater(int[][] grid) {
        if (grid.length == 0 || grid[0].length == 0) return 0;
        int n = grid.length;
        int high = n * n - 1;
        int low = grid[0][0];
        while (low < high) {
            int mid = low + (high - low) / 2;
            boolean[][] visited = new boolean[n][n];
            if (hasPath(grid, n, visited, 0, 0, mid)) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return high;
    }
    
    private boolean hasPath(int[][] grid, int n, boolean[][] visited, int i, int j, int waterLevel) {
        if (i == n - 1 && j == n - 1) return true;
        visited[i][j] = true;
        for (int[] dir : DIRS) {
            int x = dir[0] + i;
            int y = dir[1] + j;
            if (x >= 0 && x < n && y >= 0 && y < n && !visited[x][y] && grid[x][y] <= waterLevel) {
                if (hasPath(grid, n, visited, x, y, waterLevel)) return true;
            }
        }
        return false;
    }
}
'''
