__source__ = 'https://leetcode.com/problems/graph-valid-tree/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/graph-valid-tree.py
# Time:  O(|V| + |E|)
# Space: O(|V| + |E|)
#
# Description: Leetcode # 261. Graph Valid Tree
#
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges
# (each edge is a pair of nodes),
# write a function to check whether these edges make up a valid tree.
#
# For example:
#
# Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
#
# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.
#
# Note: you can assume that no duplicate edges will appear in edges.
# Since all edges are undirected, [0, 1] is the same as [1, 0] and thus
# will not appear together in edges.
#
# Companies
# Google Facebook Zenefits
# Related Topics
# Depth-first Search Breadth-first Search Graph Union Find
# Similar Questions
# Course Schedule Number of Connected Components in an Undirected Graph
#
# Thought: https://discuss.leetcode.com/topic/21737/8-10-lines-union-find-dfs-and-bfs
import unittest
import collections
# Time:  O(|V| + |E|)
# Space: O(|V| + |E|)

#45ms
class SolutionUnionFind(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        parent = range(n)
        def find(x):
            return x if parent[x] == x else find(parent[x])
        def union(xy):
            x, y = map(find, xy)
            parent[x] = y
            return x != y
        return len(edges) == n-1 and all(map(union, edges))

    def validTree2(self, n, edges):
        parent = range(n)
        def find(x):
            return x if parent[x] == x else find(parent[x])
        for e in edges:
            x, y = map(find, e)
            if x == y:
                return False
            parent[x] = y
        return len(edges) == n - 1

    def validTree3(self, n, edges):
        if len(edges) != n - 1:
            return False
        parent = range(n)
        def find(x):
            return x if parent[x] == x else find(parent[x])
        def union(xy):
            x, y = map(find, xy)
            parent[x] = y
            return x != y
        return all(map(union, edges))

    # DFS
    def validTreeDFS1(self, n, edges):
        neighbors = {i: [] for i in range(n)}
        for v, w in edges:
            neighbors[v] += w,
            neighbors[w] += v,
        def visit(v):
            map(visit, neighbors.pop(v, []))
        visit(0)
        return len(edges) == n-1 and not neighbors

    def validTreeDFS2(self, n, edges):
        if len(edges) != n - 1:
            return False
        neighbors = {i: [] for i in range(n)}
        for v, w in edges:
            neighbors[v] += w,
            neighbors[w] += v,
        def visit(v):
            map(visit, neighbors.pop(v, []))
        visit(0)
        return not neighbors
# BFS solution. Same complexity but faster version.
class Solution:
    # @param {integer} n
    # @param {integer[][]} edges
    # @return {boolean}
    def validTree(self, n, edges):
        if len(edges) != n - 1:  # Check number of edges.
            return False
        elif n == 1:
            return True

        # A structure to track each node's [visited_from, neighbors]
        visited_from = [-1] * n
        neighbors = collections.defaultdict(list)
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)

        if len(neighbors) != n:  # Check number of nodes.
            return False

        # BFS to check whether the graph is valid tree.
        visited = {}
        q = collections.deque([0])
        while q:
            i = q.popleft()
            visited[i] = True
            for node in neighbors[i]:
                if node != visited_from[i]:
                    if node in visited:
                        return False
                    else:
                        visited[node] = True
                        visited_from[node] = i
                        q.append(node)
        return len(visited) == n

# Time:  O(|V| + |E|)
# Space: O(|V| + |E|)
# BFS solution.
class Solution2:
    # @param {integer} n
    # @param {integer[][]} edges
    # @return {boolean}
    def validTree(self, n, edges):
        # A structure to track each node's [visited_from, neighbors]
        visited_from = [-1] * n
        neighbors = collections.defaultdict(list)
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)

        # BFS to check whether the graph is valid tree.
        visited = {}
        q = collections.deque([0])
        while q:
            i = q.popleft()
            visited[i] = True
            for node in neighbors[i]:
                if node != visited_from[i]:
                    if node in visited:
                        return False
                    else:
                        visited[node] = True
                        visited_from[node] = i
                        q.append(node)
        return len(visited) == n

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
# union find
# 0ms 100%
class Solution {
    public boolean validTree(int n, int[][] edges) {
        int[] array = new int[n];
        Arrays.fill(array, -1);

        for (int i = 0; i < edges.length; i++) {
            int x = findRoot(array, edges[i][0]);
            int y = findRoot(array, edges[i][1]);
            if (x == y) return false;
            array[x] = y;
        }
        return n - 1 == edges.length;
    }

    public int findRoot(int[] arr, int i) {
        if (arr[i] == -1) return i;
        return findRoot(arr, arr[i]);
    }
}

# union find
# 0ms 100%
class Solution {
    public boolean validTree(int n, int[][] edges) {
        if (n < 1 || edges.length < n - 1) return false; //eg. n = 4, [[0,1],[2,3]]
        int[] nodes = new int[n];
        for (int i = 0; i < n; i++) nodes[i] = i;
        for (int[] edge: edges) {
            int x = find(nodes, edge[0]);
            int y = find(nodes, edge[1]);
            if (x == y) return false;
            nodes[x] = y;
        }
        return true;
    }
    
    public int find(int[] nodes, int x) {
        if (x != nodes[x]) {
            nodes[x] = find(nodes, nodes[x]);
        }
        return nodes[x];
    }
}

# DFS
# 11ms 8.22% 
class Solution {
    public boolean validTree(int n, int[][] edges) {
        if (n < 1 || edges.length < n - 1) return false;
        // build the graph using adjacent list
        List<Set<Integer>> graph = new ArrayList<Set<Integer>>();
        for (int i = 0; i < n; i++) graph.add(new HashSet());
        
        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }
        
        boolean[] visited = new boolean[n];
        Stack<Integer> s = new Stack<>();
        s.push(0);
        while (!s.isEmpty()) {
            int node = s.pop();
            if (visited[node]) return false;
            visited[node] = true;
            for (int nei : graph.get(node)) {
                s.push(nei);
                graph.get(nei).remove(node);
            }
        }
        
        for (boolean v : visited) {
            if (!v) return false;
        }
        return true;
    }
}

# BFS
# 8ms 12.33%
class Solution {
    public boolean validTree(int n, int[][] edges) {
        if (n < 1 || edges.length < n - 1) return false;
        // build the graph using adjacent list
        List<Set<Integer>> graph = new ArrayList<Set<Integer>>();
        for (int i = 0; i < n; i++) graph.add(new HashSet());
        
        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }
        
        boolean[] visited = new boolean[n];
        Queue<Integer> q = new LinkedList<>();
        q.add(0);
        while (!q.isEmpty()) {
            int node = q.poll();
            if (visited[node]) return false;
            visited[node] = true;
            for (int nei : graph.get(node)) {
                q.offer(nei);
                graph.get(nei).remove(node);
            }
        }
        
        for (boolean v : visited) {
            if (!v) return false;
        }
        return true;
    }
}

'''
