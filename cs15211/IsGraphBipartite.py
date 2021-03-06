__source__ = 'https://leetcode.com/problems/is-graph-bipartite/'
# Time:  O(N + E)
# Space: O(N)
#
# Description: Leetcode # 785. Is Graph Bipartite?
#
# Given an undirected graph, return true if and only if it is bipartite.
#
# Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B
# such that every edge in the graph has one node in A and another node in B.
#
# The graph is given in the following form: graph[i] is a list of indexes j for which
# the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.
# There are no self edges or parallel edges: graph[i] does not contain i,
# and it doesn't contain any element twice.
#
# Example 1:
# Input: [[1,3], [0,2], [1,3], [0,2]]
# Output: true
# Explanation:
# The graph looks like this:
# 0----1
# |    |
# |    |
# 3----2
# We can divide the vertices into two groups: {0, 2} and {1, 3}.
# Example 2:
# Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
# Output: false
# Explanation:
# The graph looks like this:
# 0----1
# | \  |
# |  \ |
# 3----2
# We cannot find a way to divide the set of nodes into two independent subsets.
#
#
# Note:
#
# graph will have length in range [1, 100].
# graph[i] will contain integers in range [0, graph.length - 1].
# graph[i] will not contain i or duplicate values.
# The graph is undirected: if any element j is in graph[i], then i will be in graph[j].
#
import unittest
import collections

# 44ms 27.94%
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        color = {}
        for node in xrange(len(graph)):
            if node not in color:
                stack = [node]
                color[node] = 0
                while stack:
                    node = stack.pop()
                    for nei in graph[node]:
                        if nei not in color:
                            stack.append(nei)
                            color[nei] = color[node] ^ 1
                        elif color[nei] == color[node]:
                            return False
        return True

# use deque
# 32ms 77.45%
class Solution2(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        if n < 2: return True

        map = {}
        for i in xrange(n):
            if i not in map:
                map[i] = 1
                queue = collections.deque([i])
                while queue:
                    x = queue.popleft()
                    for y in graph[x]:
                        if y not in map:
                            map[y] = - map[x]
                            queue.append(y)
                        elif map[y] == map[x]:
                            return False
        return True


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/is-graph-bipartite/solution/
#
# Hungarian Algorithm
#
# Time Complexity: O(N+E), where N is the number of nodes in the graph, and E is the number of edges.
# We explore each node once when we transform it from uncolored to colored,
# traversing all its edges in the process.
#
# Space Complexity: O(N), the space used to store the color.
#
# We should be careful to consider disconnected components of the graph,
# by searching each node. For each uncolored node,
# we'll start the coloring process by doing a depth-first-search on that node.
# Every neighbor gets colored the opposite color from the current node.
# If we find a neighbor colored the same color as the current node,
# then our coloring was impossible.
#

# 7ms 34.26%
class Solution {
    public boolean isBipartite(int[][] graph) {
        int n = graph.length;
        if (n < 2) return true;
        int[] color = new int[n];
        Arrays.fill(color, -1);

        for  (int start = 0; start < n; start++) {
            if (color[start] == -1) {
                Stack<Integer> stack = new Stack();
                stack.push(start);
                color[start] = 0;

                while(!stack.isEmpty()) {
                    Integer node = stack.pop();
                    for (int nei : graph[node]) {
                        if (color[nei] == -1) {
                            stack.push(nei);
                            color[nei] = color[node] ^ 1;
                        } else if (color[nei] == color[node]) {
                            return false;
                        }
                    }

                }
            }
        }
        return true;
    }
}

# DFS
# 5ms 73.41%
class Solution {
    public boolean isBipartite(int[][] graph) {
        int n = graph.length;
        int[] colors = new int[n];

        for (int i = 0; i < n; i++) { //might be a disconnected graph -> check each unvisited node.
            if (colors[i] == 0 && !validColor(graph, colors, 1, i)) return false;
        }
        return true;
    }

    public boolean validColor(int[][] graph, int[] colors, int color, int node) {
        if (colors[node] != 0) return colors[node] == color;
        colors[node] = color;
        for (int next: graph[node]) {
            if (!validColor(graph, colors, -color, next)) return false;
        }
        return true;
    }
}

# BFS
# 8ms 34.72%
class Solution {
    public boolean isBipartite(int[][] graph) {
        int RED = 1, BLUE = -1, n = graph.length;
        int[] color = new int[n];
        Queue<Integer> queue = new LinkedList<Integer>();
        for (int i = 0; i < n; i++) {
            if (color[i] != 0) continue;
            color[i] = RED;
            queue.add(i);
            while (!queue.isEmpty()) {
                int node = queue.poll();
                for (int nei : graph[node]) {
                    if (color[nei] == color[node]) return false;
                    if (color[nei] != 0) continue;
                    color[nei] = -color[node];
                    queue.add(nei);
                }
            }
        }
        return true;
    }
}

# Use 2 sets
# For every connected component in the graph, arbitrarily assign one vertex in set A. 
# Then do a depth first search starting from that arbitrary vertex, 
# assign the neighbors of every vertex into a different set from itself. 
# If no vertex appears in both sets, then the graph is bipartite, otherwise it's not.
# 26ms 5.54%
class Solution {
    public boolean isBipartite(int[][] graph) {
        Set<Integer> A = new HashSet<>();
        Set<Integer> B = new HashSet<>();
        Set<Integer> visited = new HashSet<>();
        
        for (int i = 0; i < graph.length; i++) {
            if (!visited.contains(i)) {
                visited.add(i);
                A.add(i);
                dfs(graph, i, A, B, visited);
            }
        }
        
        for (int i = 0; i < graph.length; i++) {
            if (A.contains(i) && B.contains(i)) return false;
        }
        return true;
    }
    
    private void dfs(int[][] graph, int cur, Set<Integer> A, Set<Integer> B, Set<Integer> visited) {
        visited.add(cur);
        if (A.contains(cur)) {
            for (int nei : graph[cur]) {
                B.add(nei);
                if (!visited.contains(nei)) dfs(graph, nei, A, B, visited);
            }
        } else {
            for (int nei : graph[cur]) {
                A.add(nei);
                if (!visited.contains(nei)) dfs(graph, nei, A, B, visited);
            }
        }
    }
}

# Union Find
# considering if need more than 2 colors
# 10ms 21.99%
class Solution {
    public boolean isBipartite(int[][] graph) {
        int n = graph.length;
        int[] p = new int[n];
        for (int i = 0 ; i < n; i++) p[i] = i;
        for (int i = 0 ; i < n; i++) {
            for (int j = 0; j < graph[i].length; j++) {
                int node = graph[i][j];
                if (find(p, i) == find(p, node)) return false; //i, node can't be in the same set
                int n1 = find(p, graph[i][0]);
                int n2 = find(p, graph[i][j]);
                if (n1 != n2) p[n1] = n2;
            }
        }
        return true;
    }
    
    public int find(int[] p, int x) {
        while (x != p[x]) {
            p[x] = p[p[x]];
            x = p[x];
        }
        return x;
    }
} 
'''
