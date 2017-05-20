__author__ = 'July'
'''
A 2d grid map of m rows and n columns is initially filled with water.
We may perform an addLand operation which turns the water at position (row, col) into a land.
Given a list of positions to operate, count the number of islands after each addLand operation.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example:

Given m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]].
Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
We return the result as an array: [1, 1, 2, 3]

Challenge:

Can you do it in time complexity O(k log mn), where k is the length of the positions?

# Google
# Union Find
'''
# Time:  O(klog*k) ~= O(k), k is the length of the positions
# Space: O(k)

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


# http://algobox.org/number-of-islands-ii/
#java
js = '''
public class Solution {
    private int[][] dir = {{0,1}, {0,-1}, {-1,0},{1,0}};

    public List<Integer> numIslands2(int m, int n, int[][] positions) {
        UnionFind2D islands = new UnionFind2D(m,n);
        List<Integer> res = new ArrayList<>();

        for(int[] position : positions){
            int x = position[0], y = position[1];
            int p = islands.add(x, y);
            for(int[] d : dir){
                int q = islands.getID(x+d[0], y+d[1]);
                if(q > 0 && !islands.find(p,q)){
                    islands.unite(p,q);
                }
            }
            res.add(islands.size());
        }
        return res;
    }
}

class UnionFind2D{
    private int[] id;
    private int[] sz;
    private int m,n,count;

    public UnionFind2D(int m, int n){
        this.count = 0;
        this.n = n;
        this.m = m;
        this.id = new int[m*n + 1];
        this.sz = new int[m*n + 1];
    }

    public int index(int x, int y){return x*n + y + 1;}

    public int size(){return this.count;}

    public int getID(int x, int y){
        if(0<= x && x< m && 0<= y && y<n){
            return id[index(x,y)];
        }
        return 0;
    }

    public int add(int x, int y){
        int i = index(x, y);
        id[i] = i;
        sz[i] = 1;
        ++count;
        return i;
    }

    public boolean find(int p, int q){
        return root(p) == root(q);
    }

    public void unite(int p, int q){
        int i = root(p), j = root(q);
        if(sz[i] < sz[j]){ //weighted quick union
            id[i] =j; sz[j] += sz[i];
        }else{
            id[j] = i; sz[i] += sz[j];
        }
        --count;
    }

    private int root(int i){
        for(; i != id[i]; i = id[i]){
            id[i] = id[id[i]]; //path compression
        }
        return i;
    }

}

public class Solution {
    public List<Integer> numIslands2(int m, int n, int[][] positions) {
        int len = positions.length;
        int[] lands = new int[len];
        for (int i = 0; i < len; i++) {
            lands[i] = i;
        }
        int[][] grid = new int[m][n];
        List<Integer> result = new ArrayList<>();
        int cur = 0;
        for (int i = 0; i < len; i++) {
            int x = positions[i][0];
            int y = positions[i][1];
            if (grid[x][y] > 0) {
                result.add(cur);
                continue;
            }
            cur++;
            grid[x][y] = i + 1;
            if (x > 0 && grid[x - 1][y] > 0 && union(lands, grid[x - 1][y] - 1, i)) {
                cur--;
            }
            if (x < m - 1 && grid[x + 1][y] > 0 && union(lands, grid[x + 1][y] - 1, i)) {
                cur--;
            }
            if (y > 0 && grid[x][y - 1] > 0 && union(lands, grid[x][y - 1] - 1, i)) {
                cur--;
            }
            if (y < n - 1 && grid[x][y + 1] > 0 && union(lands, grid[x][y + 1] - 1, i)) {
                cur--;
            }
            result.add(cur);
        }
        return result;
    }

    private boolean union(int[] lands, int i, int j) {
        int iRoot = root(lands, i);
        int jRoot = root(lands, j);
        boolean ret = iRoot != jRoot;
        lands[jRoot] = iRoot;
        return ret;
    }

    private int root(int[] lands, int i) {
        while (i != lands[i]) {
            lands[i] = lands[lands[i]];
            i = lands[i];
        }
        return i;
    }
}
'''