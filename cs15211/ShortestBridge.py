__source__ = 'https://leetcode.com/problems/shortest-bridge/'
# Time:  O(N)
# Space: O(N)
#
# Description: Leetcode # 934. Shortest Bridge
#
# In a given 2D binary array A, there are two islands.
# (An island is a 4-directionally connected group of 1s not connected to any other 1s.)
#
# Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.
#
# Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)
#
# Example 1:
#
# Input: [[0,1],[1,0]]
# Output: 1
#
# Example 2:
#
# Input: [[0,1,0],[0,0,0],[0,0,1]]
# Output: 2
#
# Example 3:
#
# Input: [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Output: 1
#
# Note:
#
#     1 <= A.length = A[0].length <= 100
#     A[i][j] == 0 or A[i][j] == 1
#
import unittest
import collections

# 980ms 8.29%
class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        R, C = len(A), len(A[0])

        def neighbors(r, c):
            for nr, nc in ((r-1,c),(r,c-1),(r+1,c),(r,c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        def get_components():
            done = set()
            components = []
            for r, row in enumerate(A):
                for c, val in enumerate(row):
                    if val and (r, c) not in done:
                        # Start dfs
                        stack = [(r, c)]
                        seen = {(r, c)}
                        while stack:
                            node = stack.pop()
                            for nei in neighbors(*node):
                                if A[nei[0]][nei[1]] and nei not in seen:
                                    stack.append(nei)
                                    seen.add(nei)
                        done |= seen
                        components.append(seen)
            return components

        source, target = get_components()
        print source, target
        queue = collections.deque([(node, 0) for node in source])
        done = set(source)
        while queue:
            node, d = queue.popleft()
            if node in target: return d-1
            for nei in neighbors(*node):
                if nei not in done:
                    queue.append((nei, d+1))
                    done.add(nei)
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/shortest-bridge/solution/
#
Approach 1: Find and Grow
Complexity Analysis
Time Complexity: O(A), where A is the content of A[][] metrix.
Space Complexity: O(A)

# 69ms 24.84%
class Solution {
    class Node {
        int r, c, depth;
        Node(int r, int c, int d) {
            this.r = r;
            this.c = c;
            depth = d;
        }
    }
    
    private int[][] getComponents(int[][] A) {
        int R = A.length, C = A[0].length;
        int[][] colors = new int[R][C];
        int t = 0;

        for (int r0 = 0; r0 < R; ++r0) {
            for (int c0 = 0; c0 < C; ++c0) {
                if (colors[r0][c0] == 0 && A[r0][c0] == 1) {
                    // Start dfs
                    Stack<Integer> stack = new Stack();
                    stack.push(r0 * C + c0);
                    colors[r0][c0] = ++t;
                    
                    while (!stack.isEmpty()) {
                        int node = stack.pop();
                        int r = node / C, c = node % C;
                        for (int nei : neighbors(A, r, c)) {
                            int nr = nei / C, nc = nei % C;
                            if (A[nr][nc] == 1 && colors[nr][nc] == 0) {
                                colors[nr][nc] = t;
                                stack.push(nr * C + nc);
                            }
                        }
                    }
                }
            }
        }
        return colors;
    }
    
    private List<Integer> neighbors(int[][] A, int r, int c) {
        int R = A.length, C = A[0].length;
        List<Integer> ans = new ArrayList();
        if (r - 1 >= 0) ans.add((r - 1) * R + c);
        if (c - 1 >= 0) ans.add(r * R + (c - 1));
        if (r + 1 < R) ans.add((r + 1) * R + c);
        if (c + 1 < C) ans.add(r * R + (c + 1));
        return ans;
    }

    public int shortestBridge(int[][] A) {
        int R = A.length, C = A[0].length;
        int[][] colors = getComponents(A);

        Queue<Node> queue = new LinkedList();
        Set<Integer> target = new HashSet();
        
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (colors[r][c] == 1) {
                    queue.add(new Node(r, c, 0));
                } else if(colors[r][c] == 2) {
                    target.add(r * C + c);
                }
            }
        }
        
        while (!queue.isEmpty()) {
            Node node = queue.poll();
            if (target.contains(node.r * C + node.c)) {
                return node.depth - 1;
            }
            for (int nei : neighbors(A, node.r, node.c)) {
                int nr = nei / C, nc = nei % C;
                if (colors[nr][nc] != 1) {
                    queue.add(new Node(nr, nc, node.depth + 1));
                    colors[nr][nc] = 1;
                }
            }
        }
        throw null;
    }
}

# 26ms 83.69%
class Solution {
    private static int[][] dirs = new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public int shortestBridge(int[][] A) {
        int m = A.length, n = A[0].length;
        boolean[][] visited = new boolean[m][n];
        Queue<int[]> q = new LinkedList<>();
        boolean found = false;
        // 1. dfs to find an island, mark it in visited
        for (int i = 0; i < m; i++) {
            if (found) break;
            for (int j = 0; j < n; j++) {
                if (A[i][j] == 1) {
                    dfs(A, visited, q, i, j);
                    found = true;
                    break;
                }
            }
        }
        // 2. bfs to expand this island
        int step = 0;
        while (!q.isEmpty()) {
            int size = q.size();
            while (size-- > 0) {
                int[] cur = q.poll();
                for (int[] dir : dirs) {
                    int i = cur[0] + dir[0];
                    int j = cur[1] + dir[1];
                    if (i >= 0 && j >= 0 && i < m && j < n && !visited[i][j]) {
                        if (A[i][j] == 1) return step;
                        q.offer(new int[]{i, j});
                        visited[i][j] = true;
                    }
                }
            }
            step++;
        }
        return - 1;
    }
    
    private void dfs(int[][] A, boolean[][] visited, Queue<int[]> q, int i, int j) {
        if (i < 0 || j < 0 || i >= A.length || j >= A[0].length || visited[i][j] || A[i][j] == 0) return;
        visited[i][j] = true;
        q.offer(new int[]{i, j});
        for (int[] dir : dirs) {
            dfs(A, visited, q, i + dir[0], j + dir[1]);
        }
    }
}

# https://leetcode.com/problems/shortest-bridge/discuss/189293/C%2B%2B-BFS-Island-Expansion-%2B-UF-Bonus
# Same idea but pain one island to 2
# 26ms 83.69%
class Solution {
    public int shortestBridge(int[][] A) {
        paint(A); //paint one island with int 2
        Queue<int[]> q = new LinkedList<>(); //queue contains coordinates to do bfs
        boolean[][] visited = new boolean[A.length][A[0].length];
        
        for(int i = 0; i < A.length; i ++){//initialize queue with all coordinates with number 2
            for(int j = 0; j < A[0].length; j ++){
                if (A[i][j] == 2) {
                    q.add(new int[]{i, j});
                    visited[i][j] = true;
                }
            }
        }
        
        int level = 0;
        while(!q.isEmpty()) { //level order bfs
            int size = q.size();
            for (int i = 0; i < size; i++) {
                int[] cur = q.poll();
                int x = cur[0], y = cur[1];
                if (A[x][y] == 1) { //found, then return
                    return level - 1;
                }
                if (x > 0 && !visited[x - 1][y]) {
                    q.add(new int[]{x-1, y});
                    visited[x-1][y] = true;
                }
                if(x + 1 < A.length && !visited[x + 1][y]){
                    q.add(new int[]{x + 1, y});
                    visited[x + 1][y] = true;
                }
                if(y > 0 && !visited[x][y - 1]){
                    q.add(new int[]{x, y - 1});
                    visited[x][y - 1] = true;
                }
                if(y + 1 < A[0].length && !visited[x][y + 1]){
                    q.add(new int[]{x, y + 1});
                    visited[x][y + 1] = true;
                }
            }
            level++;
        }
        return -1;
    }
    
    private void paint(int[][] A){//paint one island with int 2
        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < A[0].length; j++) {
                if (A[i][j] == 1) {
                    dfs(i, j, A);
                    return;
                }
            }
        }
    }
    
    private void dfs(int x, int y, int[][] A){ //helper function for paint function
        if(x < 0 || x > A.length - 1 || y < 0 || y > A[0].length - 1 || A[x][y] != 1) return;
        A[x][y] = 2;
        dfs(x - 1, y, A);
        dfs(x + 1, y, A);
        dfs(x, y - 1, A);
        dfs(x, y + 1, A);
    }
}
'''
