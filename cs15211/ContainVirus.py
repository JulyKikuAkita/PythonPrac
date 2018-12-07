# coding=utf-8
__source__ = 'https://leetcode.com/problems/contain-virus/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 749. Contain Virus
#
# A virus is spreading rapidly,
# and your task is to quarantine the infected area by installing walls.
#
# The world is modeled as a 2-D array of cells,
# where 0 represents uninfected cells,
# and 1 represents cells contaminated with the virus.
# A wall (and only one wall) can be installed between any two 4-directionally adjacent cells, on the shared boundary.
#
# Every night, the virus spreads to all neighboring cells in all four directions unless blocked by a wall.
# Resources are limited. Each day, you can install walls around only one region --
# the affected area (continuous block of infected cells) that threatens the most uninfected cells the following night.
# There will never be a tie.
#
# Can you save the day? If so, what is the number of walls required?
# If not, and the world becomes fully infected, return the number of walls used.
#
# Example 1:
# Input: grid =
# [[0,1,0,0,0,0,0,1],
#  [0,1,0,0,0,0,0,1],
#  [0,0,0,0,0,0,0,1],
#  [0,0,0,0,0,0,0,0]]
# Output: 10
# Explanation:
# There are 2 contaminated regions.
# On the first day, add 5 walls to quarantine the viral region on the left. The board after the virus spreads is:
#
# [[0,1,0,0,0,0,1,1],
#  [0,1,0,0,0,0,1,1],
#  [0,0,0,0,0,0,1,1],
#  [0,0,0,0,0,0,0,1]]
#
# On the second day, add 5 walls to quarantine the viral region on the right. The virus is fully contained.
# Example 2:
# Input: grid =
# [[1,1,1],
#  [1,0,1],
#  [1,1,1]]
# Output: 4
# Explanation: Even though there is only one cell saved, there are 4 walls built.
# Notice that walls are only built on the shared boundary of two different cells.
# Example 3:
# Input: grid =
# [[1,1,1,0,0,0,0,0,0],
#  [1,0,1,0,1,1,1,1,1],
#  [1,1,1,0,0,0,0,0,0]]
# Output: 13
# Explanation: The region on the left only builds two new walls.
# Note:
# The number of rows and columns of grid will each be in the range [1, 50].
# Each grid[i][j] will be either 0 or 1.
# Throughout the described process,
# there is always a contiguous viral region that will infect strictly more uncontaminated squares in the next round.
#
import unittest

#100ms 78.95%
class Solution(object):
    def containVirus(self, grid):
        R, C = len(grid), len(grid[0])
        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        def dfs(r, c):
            if (r, c) not in seen:
                seen.add((r, c))
                regions[-1].add((r, c))
                for nr, nc in neighbors(r, c):
                    if grid[nr][nc] == 1:
                        dfs(nr, nc)
                    elif grid[nr][nc] == 0:
                        frontiers[-1].add((nr, nc))
                        perimeters[-1] += 1

        ans = 0
        while True:
            #Find all regions, with associated frontiers and perimeters.
            seen = set()
            regions = []
            frontiers = []
            perimeters = []
            for r, row in enumerate(grid):
                for c, val in enumerate(row):
                    if val == 1 and (r, c) not in seen:
                        regions.append(set())
                        frontiers.append(set())
                        perimeters.append(0)
                        dfs(r, c)

            #If there are no regions left, break.
            if not regions: break

            #Add the perimeter of the region which will infect the most squares.
            triage_index = frontiers.index(max(frontiers, key = len))
            ans += perimeters[triage_index]

            #Triage the most infectious region, and spread the rest of the regions.
            for i, reg in enumerate(regions):
                if i == triage_index:
                    for r, c in reg:
                        grid[r][c] = -1
                else:
                    for r, c in frontiers[i]: grid[r][c] = 1
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/contain-virus/solution/

Approach #1: Simulation [Accepted]
Complexity Analysis
Time Complexity: O((R*C)^(1.3)) where R,C is the number of rows and columns.
After time t, viral regions that are alive must have size at least t^2 + (t-1)^2,
so the total number removed across all time is Omega(t^3) ≤ R*C.
Space Complexity: O(R*C) in additional space.
# 19ms 75.61%

class Solution {
    Set<Integer> seen;
    List<Set<Integer>> regions;
    List<Set<Integer>> frontiers;
    List<Integer> perimeters;
    int[][] grid;
    int R, C;
    int[] dr = new int[]{-1, 1, 0, 0};
    int[] dc = new int[]{0, 0, -1, 1};

    public int containVirus(int[][] grid) {
        this.grid = grid;
        R = grid.length;
        C = grid[0].length;

        int ans = 0;
        while(true) {
            seen = new HashSet();
            regions = new ArrayList();
            frontiers = new ArrayList();
            perimeters = new ArrayList();

            for (int r = 0; r < R; ++r) {
                for (int c = 0; c < C; ++c) {
                    if (grid[r][c] == 1 && !seen.contains(r *C + c)) {
                        regions.add(new HashSet());
                        frontiers.add(new HashSet());
                        perimeters.add(0);
                        dfs(r, c);
                    }
                }
            }
            if (regions.isEmpty()) break;
            int triageIndex = 0;
            for (int i = 0; i < frontiers.size(); ++i) {
                if (frontiers.get(triageIndex).size() < frontiers.get(i).size()) triageIndex = i;
            }
            ans += perimeters.get(triageIndex);

            for (int i = 0; i < regions.size(); ++i) {
                if (i == triageIndex) {
                    for(int code: regions.get(i)){
                        grid[code / C][code % C] = -1;
                    }
                } else {
                    for (int code : regions.get(i)) {
                        int r = code / C, c = code % C;
                        for (int k = 0; k < 4; k++) {
                            int nr = r + dr[k], nc = c + dc[k];
                            if (nr >= 0 && nr < R && nc >= 0 && nc < C && grid[nr][nc] == 0) grid[nr][nc] = 1;
                        }
                    }
                }
            }
        }
        return ans;
    }

    public void dfs(int r, int c) {
        if (!seen.contains(r*C + c)) {
            seen.add(r * C + c);
            int N = regions.size();
            regions.get(N - 1).add(r*C + c);
            for (int k = 0; k < 4; ++k) {
                int nr = r + dr[k], nc = c + dc[k];
                if (nr >= 0 && nr < R && nc >= 0 && nc < C) {
                    if (grid[nr][nc] == 1) dfs(nr, nc);
                    else if (grid[nr][nc] == 0) {
                        frontiers.get(N - 1).add(nr*C + nc);
                        perimeters.set(N - 1, perimeters.get(N - 1) + 1);
                    }
                }
            }

        }
    }
}


#12ms 100%
class Solution {
    int[][] dir = {{0,1},{0,-1},{-1,0},{1,0}};
    int m, n;

    public int containVirus(int[][] grid) {
        m = grid.length; n = grid[0].length;
    	int res = 0;
    	while (true) {
            boolean [][] visited = new boolean[m][n];
	    	int[] cur = new int[4];		// cur[0] represents how many cell will be infected by this group tomorrow,
                                        // cur[1] represents how many walls will be built if this group is chosen.
                                        // cur[2] and cur[3] represents the start of the selected group
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (grid[i][j] == 1 && !visited[i][j]) {
                        boolean[][] checked = new boolean[m][n];  // checked[i][j] represents if the cell is checked.
                                                                // if it's checked, cur[0] won't be counted,
                                                                // but cur[1] still need to increase 1;
                        int[] rt = new int[2];
                        dfs(grid, visited, checked, rt, i , j);
                        if (rt[0] > cur[0]) {
                            cur[0] = rt[0];
                            cur[1] = rt[1];
                            cur[2] = i;
                            cur[3] = j;
                        }
                    }
                }
            }

            if (cur[0] == 0) return res;
            res += cur[1];
            dfs1(grid, cur[2], cur[3]);
            for (int i = 0; i< m; i++) {
                for (int j = 0; j < n; j++) {
                    if (grid[i][j] == 0) {
                        for (int k = 0; k < 4; k++) {
                            int x = i + dir[k][0], y = j + dir[k][1];
                            if ( x >= 0 && x< m && y >= 0 && y < n) {
                                if(grid[x][y] == 1) {
                                    grid[i][j] = 3;
                                    break;
                                }
                            }
                        }
                    }
                }
            }

            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (grid[i][j] == 3) grid[i][j] = 1;
                }
            }
        }
    }

    // change the selected cells from 1 to 2.
    //these cells will be fixed and we won't touch them anymore.
    void dfs1(int[][]grid, int i, int j) {
         grid[i][j] = 2;
         for (int k = 0; k < 4; k++) {
            int x = i + dir[k][0], y = j + dir[k][1];
            if (x >= 0 && x < m && y >= 0 && y < n) {
                if (grid[x][y] == 1) dfs1(grid, x, y);
            }
         }
    }

    void dfs(int[][] grid, boolean[][] visited, boolean[][] checked, int[] rt, int i, int j) {
        int[] res = new int[2];
        visited[i][j] = true;
        for (int k = 0; k < 4; k++) {
            int x = i + dir[k][0], y = j + dir[k][1];
            if (x >= 0 && x < m && y >= 0 && y < n) {
                if (grid[x][y] == 0) {
                    rt[1]++;
                    if (!checked[x][y]) {
                        checked[x][y] = true;
                        rt[0]++;
                    }
                }
                if (grid[x][y] == 1 && !visited[x][y]) {
                    dfs(grid, visited, checked, rt, x, y);
                }
            }
        }
    }
}
'''