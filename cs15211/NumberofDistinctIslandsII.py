__source__ = 'https://leetcode.com/problems/number-of-distinct-islands-ii/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 711. Number of Distinct Islands II
#
# https://en.wikipedia.org/wiki/Dihedral_group
# similar question: Starry Night
# http://olympiads.win.tue.nl/ioi/ioi98/contest/day1/starry/starry.html
#
# Given a non-empty 2D array grid of 0's and 1's,
# an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)
# You may assume all four edges of the grid are surrounded by water.
#
# Count the number of distinct islands.
# An island is considered to be the same as another if they have the same shape,
# or have the same shape after rotation (90, 180, or 270 degrees only)
# or reflection (left/right direction or up/down direction).
#
# Example 1:
# 11000
# 10000
# 00001
# 00011
# Given the above grid map, return 1.
#
# Notice that:
# 11
# 1
# and
#  1
# 11
# are considered same island shapes.
# Because if we make a 180 degrees clockwise rotation on the first island,
# then two islands will have the same shapes.
# Example 2:
# 11100
# 10001
# 01001
# 01110
# Given the above grid map, return 2.
#
# Here are the two distinct islands:
# 111
# 1
# and
# 1
# 1
#
# Notice that:
# 111
# 1
# and
# 1
# 111
# are considered same island shapes.
# Because if we flip the first array in the up/down direction, then they have the same shapes.
# Note: The length of each dimension in the given grid does not exceed 50.
#

import unittest

# https://leetcode.com/problems/number-of-distinct-islands-ii/discuss/108798/Detailed-Explanation-Python-beat-100-(~350ms)
# First of all, please look at my solution to another problem (#694 Number of Distinct Islands)
#
# Similar to its sister problem, the basic idea is simple:
#
# Scan the matrix, each time when 1 is found, search the nearby 1, push them inside a queue and mark them as -1.
#
# It is important to use the information inside the queue. As we know, the queue stands for a specific shape of an island.
#
# i. Push the island to the left upper corner by subtracting the original data with its minimum axis value.
# ii. Sort the queue and tuple it to avoid redundancy.
# iii. Find its x-axis mirror: (x,y) --> (-x,y)
# iv. Find its y-axis mirror: (x,y) --> (x,-y)
# v. Find its origin mirror: (x,y) --> (-x,-y)
# vi. Find its diagonal mirror: (x,y) --> (y,x)
# vii. Repeat 2.3, 2.4, and 2.5 on the diagonal mirror island.
# viii. Add all these 8 islands into the pool
#
# There are several tricks are used here:
#
# Augment the original matrix (grid) with a row of zeros and a column of zeros.
# This is to avoid the check of index every single time
#
# Instead of using another matrix to store the visited element,
# I directly change the value in place. -1 indicates visited.
# You can use a deep copy if you do not like change value in place.
#
# The element in the queue is centered by subtracting the minimum x and minimum y and then sorted,
# so that this shape of island will be unique.
#
#216ms 100%
class Solution(object):
    def __init__(self):
        self.shapes = set()
        self.rst = 0

    def numDistinctIslands2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # each shape, we add its other same shapes (mirror and reflection)
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        # add one more along row and col of grid to avoid boundary check
        grid.append([0] * n)
        for row in grid:
            row.append(0)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j)
        return self.rst

    def bfs(self, grid, i0, j0):
        grid[i0][j0] = -1
        shape = []
        q = []
        q.append((i0, j0))
        while q:
            curr = q.pop(0)
            shape.append(curr)
            for direction in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                nextI = curr[0] + direction[0]
                nextJ = curr[1] + direction[1]
                if grid[nextI][nextJ] == 1:
                    grid[nextI][nextJ] = -1
                    q.append((nextI, nextJ))

        self.addIsland(shape)

    def addIsland(self, shape):
        i_min = min(i for i, j in shape)
        j_min = min(j for i, j in shape)
        # org shape - relative
        island1 = tuple(sorted((i - i_min, j - j_min) for i, j in shape))
        if island1 in self.shapes:
            return
        # new shape
        self.rst += 1
        # find its all same shapes
        i_max=max(i for i,j in island1)
        j_max=max(j for i,j in island1)

        island2=tuple(sorted((-i+i_max,j) for i,j in island1)) # i axis mirror
        island3=tuple(sorted((i,-j+j_max) for i,j in island1)) # j axis mirror
        island4=tuple(sorted((-i+i_max,-j+j_max) for i,j in island1)) # origin mirror - rotate 180 degree clockwise

        island5=tuple(sorted((j,i) for i,j in island1)) # diagonal mirror
        # i axis mirror but use j_max since i and j is flip in diagonal mirror
        island6=tuple(sorted((-i+j_max,j) for i,j in island5))
        # j axis mirror but use i_max since i and j is flip in diagonal mirror
        island7=tuple(sorted((i,-j+i_max) for i,j in island5))
        # origin mirror - rotate 180 degree clockwise
        island8=tuple(sorted((-i+j_max,-j+i_max) for i,j in island5))

        # off diagonal mirror is same as diagonal mirror plus origin mirror - (-j+j_max, -i+i_max)

        self.shapes |= set([island1,island2,island3,island4,island5,island6,island7,island8])

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/number-of-distinct-islands-ii/solution/

Approach #1: Canonical Hash [Accepted]
Complexity Analysis
# Time Complexity: O(R * Clog(R*C)), where R is the number of rows in the given grid,
# and C is the number of columns.
# We visit every square once, and each square belongs to at most one shape.
# The log factor comes from sorting the shapes.
# Space complexity: O(R*C), the space used to keep track of the shapes.

# 69ms 96.52%
class Solution {
    int[][] grid;
    boolean[][] seen;
    ArrayList<Integer> shape;

    private void explore(int r, int c) {
        if (0 <= r && r < grid.length && 0 <= c && c < grid[0].length && grid[r][c] == 1 && !seen[r][c]) {
            seen[r][c] = true;
            shape.add(r * grid[0].length + c);
            explore(r+1, c);
            explore(r-1, c);
            explore(r, c+1);
            explore(r, c-1);
        }
    }

    private String canonical(ArrayList<Integer> shape) {
        String ans = "";
        int lift = grid.length + grid[0].length;
        int[] out = new int[shape.size()];
        int[] xs = new int[shape.size()];
        int[] ys = new int[shape.size()];

        for (int c = 0; c < 8; ++c) {
            int t = 0;
            for (int z : shape) {
                int x = z / grid[0].length;
                int y = z % grid[0].length;
                //x y, x -y, -x y, -x -y
                //y x, y -x, -y x, -y -x
                xs[t] = c <= 1 ? x : c <= 3 ? -x : c <= 5? y : -y;
                ys[t++] = c <= 3 ? (c %2 == 0 ? y : -y) : (c % 2 == 0 ? x : -x);
            }

            int mx = xs[0], my =ys[0];
            for (int x : xs) mx = Math.min(mx, x);
            for (int y : ys) my = Math.min(my, y);

            for (int j = 0; j < shape.size(); ++j) {
                out[j] = (xs[j] - mx) * lift + (ys[j] - my);
            }
            Arrays.sort(out);
            String candidate = Arrays.toString(out);
            if (ans.compareTo(candidate) < 0) ans = candidate;
        }
        return ans;
    }

    public int numDistinctIslands2(int[][] grid) {
        this.grid = grid;
        seen = new boolean[grid.length][grid[0].length];
        Set shapes = new HashSet<String>();

        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[0].length; c++) {
                shape = new ArrayList();
                explore(r, c);
                if (!shape.isEmpty()) shapes.add(canonical(shape));
            }
        }
        return shapes.size();
    }
}
####################################################################################################################
# 46ms 100%  # add all rotate result to list

class Solution {
    private class Island {
        public int imin, imax, jmin, jmax, size;
        private HashSet<Integer> points = new HashSet<>();

        public Island() {
            imin = jmin = Integer.MAX_VALUE;
            imax = jmax = Integer.MIN_VALUE;
            size = 0;
        }

        public int w() {
            return jmax - jmin + 1;
        }

        public int h() {
            return imax - imin + 1;
        }

        public void add(int i, int j) { //Note: The length of each dimension in the given grid does not exceed 50.
            points.add(i * 50 + j);
            size++;
            imin = Math.min(imin, i);
            imax = Math.max(imax, i);
            jmin = Math.min(jmin, j);
            jmax = Math.max(jmax, j);
        }

        public boolean contains(int k, int l) {
            return points.contains(k * 50 + l);
        }

        @Override
        public boolean equals(Object obj) {
            if(obj == null || obj.getClass() != this.getClass()) return false;
            Island other = (Island)obj;
            return imin == other.imin && imax == other.imax &&
                   jmin == other.jmin && jmax == other.jmax &&
                   size == other.size;
        }

        @Override
        public int hashCode() {
            int hash = imin;
            hash = (hash << 4) ^ imax;
            hash = (hash << 4) ^ jmin;
            hash = (hash << 4) ^ jmax;
            hash = (hash << 4) ^ size;
            return hash;
        }
    }

    private boolean areSameIslands(Island isl1, Island isl2) {
        int w = isl1.w(), h = isl1.h();
        if( w == isl2.w() && h == isl2.h()) {
            boolean notSame = false;
            boolean same = true, same_rotate180 = true,
                    same_reflectY = true, same_reflectY_rotate180 = true;
            for(int i = 0; i < h && !notSame; i++){
                for(int j = 0; j < w && !notSame; j++) {
                    same = same && areSameInPoint(isl1, isl2, i, j, i, j);
                    same_rotate180 = same_rotate180 && areSameInPoint(isl1, isl2, i, j, h - i - 1, w - j - 1);
                    same_reflectY =  same_reflectY  && areSameInPoint(isl1, isl2, i, j, h - i - 1, j);
                    same_reflectY_rotate180 = same_reflectY_rotate180 && areSameInPoint(isl1, isl2, i, j, i, w - j - 1);
                    notSame = !same && !same_rotate180 && !same_reflectY && !same_reflectY_rotate180;
                }
            }
            if(!notSame) return true;
        }
        if(h == isl2.w() && w == isl2.h()) {
            boolean notSame = false;
            boolean same_rotate90 = true, same_rotate270 = true,
                    same_rotate90_reflectY = true, same_rotate270_reflectY = true;
            for(int i = 0; i < h && !notSame; i++)
                for(int j = 0; j < w && !notSame; j++) {
                    same_rotate90           = same_rotate90           && areSameInPoint(isl1, isl2, i, j, w - j - 1, i);
                    same_rotate270          = same_rotate270          && areSameInPoint(isl1, isl2, i, j, j, h - i - 1);
                    same_rotate90_reflectY  = same_rotate90_reflectY  && areSameInPoint(isl1, isl2, i, j, w - j - 1, h - i - 1);
                    same_rotate270_reflectY = same_rotate270_reflectY && areSameInPoint(isl1, isl2, i, j, j, i);
                    notSame = !same_rotate90 && !same_rotate270 && !same_rotate90_reflectY && !same_rotate270_reflectY;
                }
            if(!notSame) return true;
        }
        return false;
    }


    private boolean areSameInPoint(Island isl1, Island isl2, int i1, int j1, int i2, int j2) {
        int k1 = i1 + isl1.imin;
        int l1 = j1 + isl1.jmin;
        int k2 = i2 + isl2.imin;
        int l2 = j2 + isl2.jmin;
        boolean contains1 = isl1.contains(k1, l1), contains2 = isl2.contains(k2, l2);
        return contains1 == contains2;
    }

    private void dfs(Island island, int i, int j, int[][] grid, HashSet<Integer> marked) {
        if(marked.contains(i * 50 + j) || grid[i][j] == 0) return;
        marked.add(i * 50 + j);
        island.add(i, j);
        int[][] dirs = new int[][] { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
        for (int[] dir : dirs) {
            int k = i + dir[0];
            int l = j + dir[1];
            if(k < 0 || k >= grid.length || l < 0 || l >= grid[0].length || grid[k][l] == 0) continue;
            dfs(island, k, l, grid, marked);
        }
    }

    public int numDistinctIslands2(int[][] grid) {
        if(grid == null || grid.length == 0 || grid[0].length == 0) return 0;
        HashMap<Integer, List<Island>> islands = new HashMap<>();
        HashSet<Integer> marked = new HashSet<>();
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++) {
                if(marked.contains(i * 50 + j) || grid[i][j] == 0) continue;
                Island island = new Island();
                dfs(island, i, j, grid, marked);
                if(!islands.containsKey(island.size))
                    islands.put(island.size, new ArrayList<>(Arrays.asList(island)));
                else {
                    List<Island> sameSize = islands.get(island.size);
                    boolean found = false;
                    for(Island other : sameSize) {
                        if(areSameIslands(island, other)) {
                            found = true;
                            break;
                        }
                    }
                    if (!found) sameSize.add(island);
                }
            }
        }
        int count = 0;
        for(List<Island> x : islands.values()) count += x.size();
        return count;
    }
}
#####################################################################################################################
https://leetcode.com/problems/number-of-distinct-islands-ii/discuss/108794/Consise-C%2B%2B-solution-using-DFS-%2Bsorting-to-find-canonical-representation-for-each-island
# 206ms 26.92%
class Solution {
    int[][] r90  = {{0,-1}, {1,0}};//rotate 90 degrees
    int[][] r180 = {{-1,0}, {0,-1}};
    int[][] r270 = {{0,1}, {-1,0}};
    int[][] updownR = {{1,0},{0,-1}};//up-down mirror
    int[][] leftRightR = {{-1,0},{0,1}};//left right mirror

    //i doubt following two transforms, from the problem description
    //there are only 5 transforms, but if i dont put following two, then 
    //there are one case it will fail.
    int[][] mirror45 ={{0,1},{1,0}};
    int[][] mirror135 ={{0,-1},{-1,0}};
    int[][][] transforms = {r90,r180,r270, updownR, leftRightR,mirror45,mirror135};
    int[][] dir = {{0,-1},{0,1},{-1, 0},{1, 0}};
    int m =0, n =0;
    
    public int numDistinctIslands2(int[][] grid) {
        if (grid == null || grid.length == 0 || grid[0] == null || grid[0].length == 0) return 0;
        
        m = grid.length;
        n = grid[0].length;
        Set<String> allIslands = new HashSet<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    List<int[]> island = new ArrayList<>();
                    buildIsland(grid, i, j, island);
                    String normalString = normalizeIsland(island);
                    allIslands.add(normalString);
                }
            }
        }
        return allIslands.size();
    }
    
    private void buildIsland(int[][] grid, int i, int j, List<int[]> island){
        island.add(new int[]{i,j});
        grid[i][j] = 0;
        for (int k = 0; k < 4; k++) {
            int ni = i + dir[k][0];
            int nj = j + dir[k][1];
            if (ni < 0 || ni >= m || nj < 0 || nj >= n || grid[ni][nj] == 0) continue;
            buildIsland(grid, ni, nj, island);
        }
    }
    
    private String normalizeIsland(List<int[]> island){
        List<String> codedIsland = new ArrayList<>();
        codedIsland.add(encodeIsland(island));
        for(int[][] transform: transforms){
            List<int[]> newIsland = new ArrayList<>();
            for(int[] cell : island) {
                newIsland.add(transform(transform, cell));
            }
            codedIsland.add(encodeIsland(newIsland));
        }
        Collections.sort(codedIsland);
        return codedIsland.get(0);
    }
    
    private int[] transform(int[][] matrix, int[] point){
        int[] res = new int[matrix.length];
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                res[i] += (matrix[i][j] * point[j]);
            }
        }
        return res;
    }
    
    private String encodeIsland(List<int[]> island){
        Collections.sort(island, (a,b)->{//sort the cells from up->down and left->right
            if (a[0] == b[0]) return a[1] - b[1];
            else return a[0] - b[0];
        });
        StringBuilder sb = new StringBuilder();
        int anchorX = island.get(0)[0];
        int anchorY = island.get(0)[1];
        
        for(int[] cell: island){
            sb.append(cell[0] - anchorX).append(":").append(cell[1] - anchorY).append("_"); //"x:y_"
        }
        return sb.toString();   
    }
}

#####################################################################################################################
# With TreeSet 
# 160ms 38.46%
class Solution {
    public int numDistinctIslands2(int[][] a) {
        Set<String> islands = new HashSet<>();
        for (int i = 0; i < a.length; i++)
            for (int j = 0; j < a[0].length; j++)
                if (a[i][j] == 1) {
                    List<int[]> cells = new LinkedList<>();
                    dfs(i, j, a, cells);
                    islands.add(norm(cells));
                }
        return islands.size();
    }

    String norm(List<int[]> cells) {
        TreeSet<String> normShapes = new TreeSet<>();
        for (int i = -1; i <= 1; i += 2)
            for (int j = -1; j <= 1; j += 2) {
                List<int[]> s1 = new ArrayList<>(), s2 = new ArrayList<>();
                for (int[] cell : cells) {
                    int x = cell[0], y = cell[1];
                    s1.add(new int[]{i * x, j * y});
                    s2.add(new int[]{i * y, j * x});
                }
                for (List<int[]> s : Arrays.asList(s1, s2)) {
                    s.sort(new Comparator<int[]>() {
                        @Override public int compare(int[] o1, int[] o2) {
                            return o1[0] != o2[0] ? o1[0] - o2[0] : o1[1] - o2[1];
                        }
                    });
                    int x = s.get(0)[0], y = s.get(0)[1];
                    StringBuilder b = new StringBuilder();
                    for (int[] p : s)
                        b.append(p[0] - x).append(":").append(p[1] - y).append(":");
                    normShapes.add(b.toString());
                }
            }
        return normShapes.first();
    }

    void dfs(int i, int j, int[][] a, List<int[]> cells) {
        if (i < 0 || i >= a.length || j < 0 || j >= a[0].length || a[i][j] != 1) return;
        cells.add(new int[]{i, j});
        a[i][j] = -1;
        dfs(i + 1, j, a, cells); dfs(i - 1, j, a, cells);
        dfs(i, j + 1, a, cells); dfs(i, j - 1, a, cells);
    }
}
#####################################################################################################################
# solution for Starry Night: http://olympiads.win.tue.nl/ioi/ioi98/contest/day1/starry/starry.html

# 77ms 82.61%
import java.util.*;

class Solution {
    private static final int dr[] = {1, -1, 0, 0};
    private static final int dc[] = {0, 0, 1, -1};
    private static final int INF = 10000;

    private int left = INF;
    private int right = 0;
    private int top = INF;
    private int bottom = 0;

    private void markIsland(int[][] grid, int row, int col, int id) {
        left = Math.min(left, col);
        right = Math.max(right, col);
        top = Math.min(top, row);
        bottom = Math.max(bottom, row);

        grid[row][col] = id;
        for (int i = 0; i < 4; ++i) {
            int nr = row + dr[i];
            int nc = col + dc[i];
            if (nr >= 0 && nr < grid.length && nc >= 0 && nc < grid[0].length && grid[nr][nc] == 1) {
                markIsland(grid, nr, nc, id);
            }
        }
    }

    private int[][] cutIsland(int[][] grid, int r1, int c1, int r2, int c2, int id) {
        int[][] res = new int[r2 - r1 + 1][c2 - c1 + 1];
        for (int i = r1; i <= r2; ++i) {
            for (int j = c1; j <= c2; ++j) {
                if (grid[i][j] == id) {
                    res[i - r1][j - c1] = 1;
                }
            }
        }
        return res;
    }

    private int[][] rotate90(int[][] grid) {
        int row = grid.length;
        int col = grid[0].length;

        int[][] res = new int[col][row];
        for (int i = 0; i < row; ++i) {
            for (int j = 0; j < col; ++j) {
                res[j][row - i - 1] = grid[i][j];
            }
        }
        return res;
    }

    private int[][] upDown(int[][] grid) {
        int row = grid.length;
        int col = grid[0].length;

        int[][] res = new int[row][col];
        for (int i = 0; i < row; ++i) {
            for (int j = 0; j < col; ++j) {
                res[row - i - 1][j] = grid[i][j];
            }
        }
        return res;
    }

    private int[][] leftRight(int[][] grid) {
        int row = grid.length;
        int col = grid[0].length;

        int[][] res = new int[row][col];
        for (int i = 0; i < row; ++i) {
            for (int j = 0; j < col; ++j) {
                res[i][col - j - 1] = grid[i][j];
            }
        }
        return res;
    }

    boolean same(int[][] g1, int[][] g2) {
        if (g1.length != g2.length || g1[0].length != g2[0].length) {
            return false;
        }

        for (int i = 0; i < g1.length; ++i) {
            for (int j = 0; j < g1[0].length; ++j) {
                if (g1[i][j] != g2[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }

    List<int[][]> transform(int[][] orig) {
        List<int[][]> trans = new ArrayList<>();
        trans.add(orig);
        trans.add(rotate90(trans.get(trans.size() - 1)));
        trans.add(rotate90(trans.get(trans.size() - 1)));
        trans.add(rotate90(trans.get(trans.size() - 1)));
        trans.add(upDown(orig));
        trans.add(rotate90(trans.get(trans.size() - 1)));
        trans.add(rotate90(trans.get(trans.size() - 1)));
        trans.add(rotate90(trans.get(trans.size() - 1)));
        trans.add(leftRight(orig));
        trans.add(rotate90(trans.get(trans.size() - 1)));
        trans.add(rotate90(trans.get(trans.size() - 1)));
        trans.add(rotate90(trans.get(trans.size() - 1)));
        return trans;
    }

    public int numDistinctIslands2(int[][] grid) {
        int id = 2;

        int row = grid.length;
        int col = grid[0].length;

        List<int[][]> islands = new ArrayList<>();
        for (int i = 0; i < row; ++i) {
            for (int j = 0; j < col; ++j) {
                if (grid[i][j] == 1) {
                    left = INF; right = 0; top = INF; bottom = 0;
                    markIsland(grid, i, j, id);
                    islands.add(cutIsland(grid, top, left, bottom, right, id));
                    ++id;
                }
            }
        }

        int sz = islands.size();
        boolean[] vis = new boolean[sz];

        int res = 0;
        for (int i = 0; i < sz; ++i) {
            if (vis[i] == false) {
                ++res;

                List<int[][]> trans = transform(islands.get(i));
                int num = trans.size();
                for (int j = i + 1; j < sz; ++j) {
                    for (int k = 0; k < num; ++k) {
                        if (same(islands.get(j), trans.get(k))) {
                            vis[j] = true;
                            break;
                        }
                    }
                }
            }
        }

        return res;
    }
}

'''
