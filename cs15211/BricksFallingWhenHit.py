# coding=utf-8
__source__ = 'https://leetcode.com/problems/bricks-falling-when-hit/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 803. Bricks Falling When Hit
#
# We have a grid of 1s and 0s; the 1s in a cell represent bricks.
# A brick will not drop if and only if it is directly connected to the top of the grid,
# or at least one of its (4-way) adjacent bricks will not drop.
#
# We will do some erasures sequentially.
# Each time we want to do the erasure at the location (i, j),
# the brick (if it exists) on that location will disappear,
# and then some other bricks may drop because of that erasure.
#
# Return an array representing the number of bricks that will drop after each erasure in sequence.
#
# Example 1:
# Input:
# grid = [[1,0,0,0],[1,1,1,0]]
# hits = [[1,0]]
# Output: [2]
# Explanation:
# If we erase the brick at (1, 0), the brick at (1, 1) and (1, 2) will drop.
# So we should return 2.
# Example 2:
# Input:
# grid = [[1,0,0,0],[1,1,0,0]]
# hits = [[1,1],[1,0]]
# Output: [0,0]
# Explanation:
# When we erase the brick at (1, 0), the brick at (1, 1) has already disappeared due to the last move.
# So each erasure will cause no bricks dropping.
# Note that the erased brick (1, 0) will not be counted as a dropped brick.
#
#
# Note:
#
# The number of rows and columns in the grid will be in the range [1, 200].
# The number of erasures will not exceed the area of the grid.
# It is guaranteed that each erasure will be different from any other erasure, and located inside the grid.
# An erasure may refer to a location with no brick - if it does, no bricks drop.
#
import unittest

#312ms 79.14%
def dfs(bricks, row, col):
    if bricks[row][col] != 1:
        return
    bricks[row][col] = 2
    if row - 1 >= 0 and bricks[row - 1][col] == 1:
        dfs(bricks, row - 1, col)
    if col - 1 >= 0 and bricks[row][col - 1] == 1:
        dfs(bricks, row, col - 1)
    if row + 1 < len(bricks) and bricks[row + 1][col] == 1:
        dfs(bricks, row + 1, col)
    if col + 1 < len(bricks[0]) and bricks[row][col + 1] == 1:
        dfs(bricks, row, col + 1)
    return

def addComponent(bricks, row, col, cnt):
    # print row, col
    if bricks[row][col] != 1:
        return
    bricks[row][col] = 2
    cnt[0] += 1
    if row - 1 >= 0 and bricks[row - 1][col] == 1:
        addComponent(bricks, row - 1, col, cnt)
    if col - 1 >= 0 and bricks[row][col - 1] == 1:
        addComponent(bricks, row, col - 1, cnt)
    if row + 1 < len(bricks) and bricks[row + 1][col] == 1:
        addComponent(bricks, row + 1, col, cnt)
    if col + 1 < len(bricks[0]) and bricks[row][col + 1] == 1:
        addComponent(bricks, row, col + 1, cnt)
    return

def connectedNeighbor(bricks, row, col):
    if row == 0:
        return True
    if row - 1 >= 0 and bricks[row - 1][col] == 2:
        return True
    if row + 1 < len(bricks) and bricks[row + 1][col] == 2:
        return True
    if col - 1 >= 0 and bricks[row][col - 1] == 2:
        return True
    if col + 1 < len(bricks[0]) and bricks[row][col + 1] == 2:
        return True
    return False

class Solution(object):
    def hitBricks(self, bricks, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        for hit in hits:
            r, c = hit
            bricks[r][c] -= 1
        m, n = len(bricks), len(bricks[0])
        for i in range(n):
            # start from each bricks from ceiling, label
            # connected bricks as 2
            dfs(bricks, 0, i)
        res = []
        for i in range(len(hits) - 1, -1, -1):
            hit = hits[i]
            bricks[hit[0]][hit[1]] += 1
            if bricks[hit[0]][hit[1]] != 1:
                res.append(0)
            elif not connectedNeighbor(bricks, hit[0], hit[1]):
                res.append(0)
            else:
                cnt = [-1]
                addComponent(bricks, hit[0], hit[1], cnt)
                res.append(cnt[0])
            # print bricks
        return res[::-1]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/bricks-falling-when-hit/solution/
Approach #1: Reverse Time and Union-Find [Accepted]
Complexity Analysis
Time Complexity: O(N∗Q∗α(N∗Q)), where N = R*C is the number of grid squares,
Q is the length of hits, and α is the Inverse-Ackermann function.
# inverse Ackermann function
# (algorithm)
# Definition: A function of two parameters whose value grows very, very slowly.
Space Complexity: O(N)

#17ms 29.27%
class Solution {
    public int[] hitBricks(int[][] grid, int[][] hits) {
        int R = grid.length, C = grid[0].length;
        int[] dr = {1, 0, -1, 0};
        int[] dc = {0, 1, 0, -1};

        int[][] A = new int[R][C];
        for (int r = 0; r < R; r++) {
            A[r] = grid[r].clone();
        }

        for (int[] hit : hits) {
            A[hit[0]][hit[1]] = 0;
        }

        DSU dsu = new DSU(R * C + 1);
        for (int r = 0; r < R; r++) {
            for (int c = 0 ; c < C; c++) {
                if (A[r][c] == 1) {
                    int i = r * C + c;
                    if (r == 0) {
                        dsu.union(i, R * C);
                    }
                    if (r > 0 && A[r-1][c] == 1) {
                        dsu.union(i, (r - 1) * C + c);
                    }
                    if (c > 0 && A[r][c-1] == 1) {
                        dsu.union(i, r * C + (c - 1));
                    }
                }
            }
        }

        int t = hits.length;
        int[] ans = new int[t--];

        while (t >= 0) {
            int r = hits[t][0];
            int c = hits[t][1];
            int preRoof = dsu.top();

            if (grid[r][c] == 0) t--;
            else {
                int i = r * C + c;
                for (int k = 0; k < 4; k++) {
                    int nr = r + dr[k];
                    int nc = c + dc[k];
                    if (0 <= nr && nr < R && 0 <= nc && nc < C && A[nr][nc] == 1) {
                        dsu.union(i, nr * C + nc);
                    }
                }
                if (r == 0) dsu.union(i, R * C);
                A[r][c] = 1;
                ans[t--] = Math.max(0, dsu.top() - preRoof - 1);
            }
        }
        return ans;
    }
}

class DSU {
    int[] parent;
    int[] rank;
    int[] sz;

    public DSU(int N) {
        parent = new int[N];
        for (int i = 0; i < N; ++i)
            parent[i] = i;
        rank = new int[N];
        sz = new int[N];
        Arrays.fill(sz, 1);
    }

    public int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }

    public void union(int x, int y) {
        int xr = find(x), yr = find(y);
        if (xr == yr) return;

        if (rank[xr] < rank[yr]) {
            int tmp = yr;
            yr = xr;
            xr = tmp;
        }
        if (rank[xr] == rank[yr])
            rank[xr]++;

        parent[yr] = xr;
        sz[xr] += sz[yr];
    }

    public int size(int x) {
        return sz[find(x)];
    }

    public int top() {
        return size(sz.length - 1) - 1;
    }
}

# Union FIND
// Union Find：去掉hit，每一块连起来。再加上hit，看增加了多少个

# 12ms 61.04%
class Solution {
    class UnionFind{
        int[] parent;
        int[] count;

        public UnionFind(int len) {
            parent = new int[len];
            count = new int[len];
            for (int i = 0; i < len ; i++) {
                parent[i] = i;
                count[i] = 1;
            }
        }

        public int find(int x) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        }

        public void union(int a, int b) {
            int parentA = find(a);
            int parentB = find(b);
            if (parentA != parentB) {
                parent[parentA] = parentB;
                count[parentB] += count[parentA];
            }
        }
    }

    public int[] hitBricks(int[][] grid, int[][] hits) {
        int m = grid.length;
        int n = grid[0].length;
        UnionFind uf = new UnionFind(m * n + 1);
        for (int[] hit : hits) {
            if (grid[hit[0]][hit[1]] == 1) {
                grid[hit[0]][hit[1]] = 2;
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) unionAround(i, j, grid, uf);
            }
        }

        int count = uf.count[uf.find(0)];
        int[] res = new int[hits.length];
        for (int i = hits.length - 1; i >= 0; i--) {
            int[] hit = hits[i];
            if (grid[hit[0]][hit[1]] == 2) {
                unionAround(hit[0], hit[1], grid, uf);
                grid[hit[0]][hit[1]] = 1;
            }
            int newCount = uf.count[uf.find(0)];
            // -1 for the the brick got hit
            res[i] = (newCount - count > 0) ? newCount - count - 1 : 0;
            count = newCount;
        }
        return res;
    }

    private void unionAround(int x, int y, int[][] grid, UnionFind uf) {
        int m = grid.length;
        int n = grid[0].length;
        int[] dx = new int[] {-1, 1, 0, 0};
        int[] dy = new int[] {0, 0, -1, 1};
        for (int i = 0; i < 4; i++) {
            int nextX = x + dx[i];
            int nextY = y + dy[i];
            if (nextX < 0 || nextX >= m || nextY < 0 || nextY >= n) continue;
            if (grid[nextX][nextY] == 1) {
                // shift all by 1
                uf.union(x * n + y + 1, nextX * n + nextY + 1);
            }
        }
        // use 0 as pivot to connect all elements in row 0
        if (x == 0) uf.union(x *n + y + 1, 0);
    }

}

#DFS: 去掉hit，讲顶点roof的块标记。再加上hit，判断是否连接上
# 7ms 97.61%

class Solution {

    public int[] hitBricks(int[][] grid, int[][] hits) {
        int n = grid[0].length;
		// remove all hit bricks
        for (int i = 0; i < hits.length; i++) {
            grid[hits[i][0]][hits[i][1]] -= 1;
        }

        // dfs from roof, mark visited cells to 2
        for (int c = 0; c < n; c++) {
            if (grid[0][c] == 1) dfs(grid, 0, c);
        }

        int[] ans = new int[hits.length];
		// iterate from last hit to first
        for (int i = hits.length - 1; i >= 0; i--) {
            int r = hits[i][0];
            int c = hits[i][1];
            grid[r][c] += 1; // put brick back
            // if the cell is attathed to the roof (or any cell with value 2)
            ans[i] = grid[r][c] == 1
                && isConnectedTop(grid, r, c) ? dfs(grid, r, c) -1 : 0;
        }
        return ans;
    }

  	private boolean isConnectedTop(int[][] grid, int r, int c) {
        if (r == 0) return true;
        if (r > 0 && grid[r - 1][c] == 2) return true;
        if (r + 1 < grid.length && grid[r + 1][c] == 2) return true;
        if (c > 0 && grid[r][c - 1] == 2) return true;
        if (c + 1 < grid[0].length && grid[r][c + 1] == 2) return true;
        return false;
    }

    private int dfs(int[][] grid, int r, int c) {
        grid[r][c] = 2;
        int size = 1;
        if (r > 0 && grid[r - 1][c] == 1) size += dfs(grid, r - 1, c);
        if (r + 1 < grid.length && grid[r + 1][c] == 1) size += dfs(grid, r + 1, c);
        if (c > 0 && grid[r][c - 1] == 1) size += dfs(grid, r, c - 1);
        if (c + 1 < grid[0].length && grid[r][c + 1] == 1) size += dfs(grid, r, c + 1);
        return size;
    }
}
'''