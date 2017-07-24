__source__ = 'https://leetcode.com/problems/number-of-islands-ii/description/'
# https://leetcode.com/problems/number-of-islands-ii/#/description
# Time:  O(klog*k) ~= O(k), k is the length of the positions
# Space: O(k)
#
# Description: Leetcode # 305. Number of Islands II
#
# A 2d grid map of m rows and n columns is initially filled with water.
# We may perform an addLand operation which turns the water at position (row, col) into a land.
# Given a list of positions to operate, count the number of islands after each addLand operation.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.
#
# Example:
#
# Given m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]].
# Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).
#
# 0 0 0
# 0 0 0
# 0 0 0
# Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.
#
# 1 0 0
# 0 0 0   Number of islands = 1
# 0 0 0
# Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.
#
# 1 1 0
# 0 0 0   Number of islands = 1
# 0 0 0
# Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.
#
# 1 1 0
# 0 0 1   Number of islands = 2
# 0 0 0
# Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.
#
# 1 1 0
# 0 0 1   Number of islands = 3
# 0 1 0
# We return the result as an array: [1, 1, 2, 3]
#
# Challenge:
#
# Can you do it in time complexity O(k log mn), where k is the length of the positions?
#
# Companies
# Google
# Related Topics
# Union Find
# Similar Questions
# Number of Islands

# Time:  O(klog*k) ~= O(k), k is the length of the positions
# Space: O(k)
import unittest
class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        def node_id(node, n):
            return node[0] * n + node[1]

        def find_set(x):
           if set[x] != x:
               set[x] = find_set(set[x])  # path compression.
           return set[x]

        def union_set(x, y):
            x_root, y_root = find_set(x), find_set(y)
            set[min(x_root, y_root)] = max(x_root, y_root)

        numbers = []
        number = 0
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        set = {}
        for position in positions:
            node = (position[0], position[1])
            set[node_id(node, n)] = node_id(node, n)
            number += 1

            for d in directions:
                neighbor = (position[0] + d[0], position[1] + d[1])
                if 0 <= neighbor[0] < m and 0 <= neighbor[1] < n and \
                   node_id(neighbor, n) in set:
                   if find_set(node_id(node, n)) != find_set(node_id(neighbor, n)):
                       # Merge different islands, amortised time: O(log*k) ~= O(1)
                       union_set(node_id(node, n), node_id(neighbor, n))
                       number -= 1
            numbers.append(number)

        return numbers

class Solution2(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        islands = Union()
        for p in map(tuple, positions):
            islands.add(p)
            for dp in (0,1), (0,-1), (1,0), (-1,0):
                q = (p[0] + dp[0], p[1] + dp[1])
                if q in islands.id:
                    islands.unite(p,q)
            ans += [islands.count]
        return ans

class Union(object):
    def __init__(self):
        self.id = {}
        self.sz = {}
        self.count = 0
    def add(self, p):
        self.id[p] = p
        self.sz[p] = 1
        self.count += 1
    def root(self, i):
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i

    def unite(self, p, q):
        i, j = self.root(p), self.root(q)
        if i ==j:
            return
        if self.sz[i] >self.sz[j]:
            i, j = j, i
        self.id[i] = j
        self.sz[j] += self.sz[i]
        self.count -= 1

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://discuss.leetcode.com/topic/29613/easiest-java-solution-with-explanations
# 81.60% 18ms
public class Solution {
    int[][] dirs = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};

    public List<Integer> numIslands2(int m, int n, int[][] positions) {
        List<Integer> result = new ArrayList<>();
        if(m <= 0 || n <= 0) return result;

        int count = 0;                      // number of islands
        int[] roots = new int[m * n];       // one island = one tree
        Arrays.fill(roots, -1);

        for(int[] p : positions) {
            int root = n * p[0] + p[1];     // assume new point is isolated island
            roots[root] = root;             // add new island
            count++;

            for(int[] dir : dirs) {
                int x = p[0] + dir[0];
                int y = p[1] + dir[1];
                int nb = n * x + y;
                if(x < 0 || x >= m || y < 0 || y >= n || roots[nb] == -1) continue;

                int rootNb = findIsland(roots, nb);
                if(root != rootNb) {        // if neighbor is in another island
                    roots[root] = rootNb;   // union two islands
                    root = rootNb;          // current tree root = joined tree root
                    count--;
                }
            }

            result.add(count);
        }
        return result;
    }

    public int findIsland(int[] roots, int id) {
        while(id != roots[id]) {
            roots[id] = roots[roots[id]];   // only one line added
            id = roots[id];
        }
        return id;
    }
}

#95.94% 16ms
public class Solution {
    private static final int[][] DIRECTIONS = new int[][] {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};

    public List<Integer> numIslands2(int m, int n, int[][] positions) {
        List<Integer> result = new ArrayList<>();
        int[][] matrix = new int[m][n];
        int[] islands = new int[positions.length];
        int[] count = new int[positions.length];
        int numIslands = 0;

        for (int i = 0; i < islands.length; i++) {
            islands[i] = i;
        }
        Arrays.fill(count, 1);
        for (int i = 0; i < positions.length; i++) {
            int x = positions[i][0];
            int y = positions[i][1];
            if (matrix[x][y] > 0) {
                result.add(numIslands);
                continue;
            }
            matrix[x][y] = i + 1;
            numIslands++;
            for (int[] direction : DIRECTIONS) {
                int newX = x + direction[0];
                int newY = y + direction[1];
                if (newX >= 0 && newX < m && newY >= 0 && newY < n && matrix[newX][newY] > 0 && union(islands, count, i, matrix[newX][newY] - 1)) {
                    numIslands--;
                }
            }
            result.add(numIslands);
        }
        return result;
    }

    private boolean union(int[] arr, int[] count, int i, int j) {
        int iRoot = root(arr, i);
        int jRoot = root(arr, j);
        if (iRoot != jRoot) {
            if (count[iRoot] <= count[jRoot]) {
                arr[iRoot] = jRoot;
                count[jRoot] += count[iRoot];
                count[iRoot] = 0;
            } else {
                arr[jRoot] = iRoot;
                count[iRoot] += count[jRoot];
                count[jRoot] = 0;
            }
            return true;
        } else {
            return false;
        }
    }

    private int root(int[] arr, int i) {
        while (arr[i] != i) {
            arr[i] = arr[arr[i]];
            i = arr[i];
        }
        return i;
    }
}
#https://discuss.leetcode.com/topic/29518/java-python-clear-solution-with-unionfind-class-weighting-and-path-compression
Java/Python clear solution with UnionFind Class (Weighting and Path compression)
Union Find
is an abstract data structure supporting find and unite on disjointed sets of objects,
typically used to solve the network connectivity problem.

The two operations are defined like this:

find(a,b) : are a and b belong to the same set?

unite(a,b) : if a and b are not in the same set, unite the sets they belong to.

With this data structure, it is very fast for solving our problem. Every position is an new land,
if the new land connect two islands a and b, we combine them to form a whole.
The answer is then the number of the disjointed sets.

The following algorithm is derived from Princeton's lecture note on Union Find in Algorithms and Data Structures
It is a well organized note with clear illustration describing from the naive QuickFind to the one with Weighting
and Path compression.
With Weighting and Path compression, The algorithm runs in O((M+N) log* N) where M is the number of operations
( unite and find ), N is the number of objects, log* is iterated logarithm while the naive runs in O(MN).

For our problem, If there are N positions, then there are O(N) operations and N objects then total is O(N log*N),
when we don't consider the O(mn) for array initialization.

Note that log*N is almost constant (for N = 265536, log*N = 5) in this universe, so the algorithm is almost linear
with N.

However, if the map is very big, then the initialization of the arrays can cost a lot of time when mn is much larger
than N. In this case we should consider using a hashmap/dictionary for the underlying data structure to avoid this
overhead.

Of course, we can put all the functionality into the Solution class which will make the code a lot shorter.
But from a design point of view a separate class dedicated to the data sturcture is more readable and reusable.

I implemented the idea with 2D interface to better fit the problem.

#81.60% 18ms
public class Solution {

    private int[][] dir = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}};

    public List<Integer> numIslands2(int m, int n, int[][] positions) {
        UnionFind2D islands = new UnionFind2D(m, n);
        List<Integer> ans = new ArrayList<>();
        for (int[] position : positions) {
            int x = position[0], y = position[1];
            int p = islands.add(x, y);
            for (int[] d : dir) {
                int q = islands.getID(x + d[0], y + d[1]);
                if (q > 0 && !islands.find(p, q))
                    islands.unite(p, q);
            }
            ans.add(islands.size());
        }
        return ans;
    }
}

class UnionFind2D {
    private int[] id;
    private int[] sz;
    private int m, n, count;

    public UnionFind2D(int m, int n) {
        this.count = 0;
        this.n = n;
        this.m = m;
        this.id = new int[m * n + 1];
        this.sz = new int[m * n + 1];
    }

    public int index(int x, int y) { return x * n + y + 1; }

    public int size() { return this.count; }

    public int getID(int x, int y) {
        if (0 <= x && x < m && 0<= y && y < n)
            return id[index(x, y)];
        return 0;
    }

    public int add(int x, int y) {
        int i = index(x, y);
        id[i] = i; sz[i] = 1;
        ++count;
        return i;
    }

    public boolean find(int p, int q) {
        return root(p) == root(q);
    }

    public void unite(int p, int q) {
        int i = root(p), j = root(q);
        if (sz[i] < sz[j]) { //weighted quick union
            id[i] = j; sz[j] += sz[i];
        } else {
            id[j] = i; sz[i] += sz[j];
        }
        --count;
    }

    private int root(int i) {
        for (;i != id[i]; i = id[i])
            id[i] = id[id[i]]; //path compression
        return i;
    }
}
//Runtime: 20 ms
'''