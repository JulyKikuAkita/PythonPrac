# coding=utf-8
__source__ = 'https://leetcode.com/problems/redundant-connection/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 684. Redundant Connection
#
# In this problem, a tree is an undirected graph that is connected and has no cycles.
#
# The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N),
# with one additional edge added. The added edge has two different vertices chosen from 1 to N,
# and was not an edge that already existed.
#
# The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v,
# that represents an undirected edge connecting nodes u and v.
#
# Return an edge that can be removed so that the resulting graph is a tree of N nodes.
# If there are multiple answers, return the answer that occurs last in the given 2D-array.
# The answer edge [u, v] should be in the same format, with u < v.
#
# Example 1:
# Input: [[1,2], [1,3], [2,3]]
# Output: [2,3]
# Explanation: The given undirected graph will be like this:
#   1
#  / \
# 2 - 3
# Example 2:
# Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
# Output: [1,4]
# Explanation: The given undirected graph will be like this:
# 5 - 1 - 2
#     |   |
#     4 - 3
# Note:
# The size of the input 2D-array will be between 3 and 1000.
# Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.
#
# Update (2017-09-26):
# We have overhauled the problem description + test cases and specified clearly the graph is an undirected graph.
# For the directed graph follow up please see Redundant Connection II). We apologize for any inconvenience caused.
#
# Companies
# Google
# Related Topics
# Tree
# Similar Questions
# Redundant Connection II
#
import unittest
import collections
# 80ms 7,30%
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(set)

        def dfs(source, target):
            if source not in seen:
                seen.add(source)
                if source == target: return True
                return any(dfs(nei, target) for nei in graph[source])

        for u, v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u, v):
                return u, v
            graph[u].add(v)
            graph[v].add(u)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/redundant-connection/solution/

# union find
# 3ms 80.49%
class Solution {
    public int[] findRedundantConnection(int[][] edges) {
        int[] parent = new int[2001];
        for (int i = 0; i < parent.length; i++) parent[i] = i;

        for (int[] edge: edges){
            int f = edge[0], t = edge[1];
            if (find(parent, f) == find(parent, t)) return edge;
            else parent[find(parent, f)] = find(parent, t);
        }
        return new int[2];
    }

    private int find(int[] parent, int f) {
        if (f != parent[f]) {
          parent[f] = find(parent, parent[f]);
        }
        return parent[f];
    }
}

# 3ms 80.49%
class Solution {
    public int[] findRedundantConnection(int[][] edges) {
        int[] root = new int[1001];
        for (int[] edge : edges) {
            int x = findParent(root, edge[0]);
            int y = findParent(root, edge[1]);
            if (x == y)  return edge;
            root[x] = y;
        }
        return new int[2];
    }

    private int findParent(int[] root, int i) {
        int id = i;
        while (root[id] != 0) {
            id = root[id];
        }
        return id;
    }
}

# Approach #1: DFS [Accepted]
# DFS
# Complexity Analysis
# Time Complexity: O(N^2) where N is the number of vertices (and also the number of edges) in the graph. 
# In the worst case, for every edge we include, we have to search every previously-occurring edge of the graph.
# Space Complexity: O(N). The current construction of the graph has at most NN nodes.
class Solution {
    Set<Integer> seen = new HashSet();
    int MAX_EDGE_VAL = 1000;
    public int[] findRedundantConnection(int[][] edges) {
        ArrayList<Integer>[] graph = new ArrayList[MAX_EDGE_VAL + 1];
        for (int i = 0; i<= MAX_EDGE_VAL; i++) {
            graph[i] = new ArrayList();
        }
        
        for (int[] edge : edges) {
            seen.clear();
            if (!graph[edge[0]].isEmpty() && !graph[edge[1]].isEmpty() && dfs(graph, edge[0], edge[1])) return edge;
            graph[edge[0]].add(edge[1]);
            graph[edge[1]].add(edge[0]);
        }
        throw new AssertionError();
    }
    
    public boolean dfs(ArrayList<Integer>[] graph, int source, int target) {
        if (!seen.contains(source)) {
            seen.add(source);
            if (source == target) return true;
            for (int nei: graph[source]) {
                if (dfs(graph, nei, target)) return true;
            }
        } 
        return false;
    }
}

# Approach #2: Union-Find [Accepted]
# Complexity Analysis
# Time Complexity: O(Nα(N))≈O(N), where N is the number of vertices (and also the number of edges) in the graph, 
# α is the Inverse-Ackermann function. 
# We make up to N queries of dsu.union, which takes (amortized) O(α(N)) time. 
# Outside the scope of this article, it can be shown why dsu.union has O(α(N)) complexity, 
# what the Inverse-Ackermann function is, and why O(α(N)) is approximately O(1).
# Space Complexity: O(N). The current construction of the graph (embedded in our dsu structure) has at most N nodes.
# 6ms 39.17%
class Solution {
    int MAX_EDGE_VAL = 1000;
    public int[] findRedundantConnection(int[][] edges) {
        DSU dsu = new DSU(MAX_EDGE_VAL + 1);
        for (int[] edge: edges) {
            if (!dsu.union(edge[0], edge[1])) return edge;
        }
        throw new AssertionError();
    }
    
    class DSU {
        int[] parent;
        int[] rank;
        
        public DSU(int size) {
            parent = new int[size];
            rank = new int[size];
            for (int i = 0; i < size; i++) parent[i] = i;
        }
        
        public int find(int x) {
            if (x != parent[x]) parent[x] = find(parent[x]);
            return parent[x];
        }
        
        public boolean union(int x, int y) {
            int xr = find(x), yr = find(y);
            if (xr == yr) {
                return false;
            } else if (rank[xr] < rank[yr]) {
                parent[xr] = yr;
            } else if (rank[xr] > rank[yr]) {
                parent[yr] = xr;
            } else {
                parent[yr] = xr;
                rank[xr]++;
            }
            return true;
        }
    }
}
'''
