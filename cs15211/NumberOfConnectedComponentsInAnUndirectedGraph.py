__source__ = 'https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/number-of-connected-components-in-an-undirected-graph.py
# Time:  O(nlog*n) ~= O(n), n is the length of the positions
# Space: O(n)
#
# Description: Leetcode # 323. Number of Connected Components in an Undirected Graph
#
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
# write a function to find the number of connected components in an undirected graph.
#
# Example 1:
#      0          3
#      |          |
#      1 --- 2    4
# Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.
#
# Example 2:
#      0           4
#      |           |
#      1 --- 2 --- 3
# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.
#
# Note:
# You can assume that no duplicate edges will appear in edges. Since all edges are undirected,
# [0, 1] is the same as [1, 0] and thus will not appear together in edges.
#
# Companies
# Google Twitter
# Related Topics
# Depth-first Search Breadth-first Search Union Find Graph
# Similar Questions
# Number of Islands Graph Valid Tree Friend Circles
#
import unittest
# Time:  O(nlog*n) ~= O(n), n is the length of the positions
# Space: O(n)

class UnionFind(object):
    def __init__(self, n):
        self.set = range(n)
        self.count = n

    def find_set(self, x):
       if self.set[x] != x:
           self.set[x] = self.find_set(self.set[x])  # path compression.
       return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root != y_root:
            self.set[min(x_root, y_root)] = max(x_root, y_root)
            self.count -= 1


class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        union_find = UnionFind(n)
        for i, j in edges:
            union_find.union_set(i, j)
        return union_find.count

#http://blog.csdn.net/bearkino/article/details/50723722
#Graph
# BFS:

class SolutionBFS(object):
    def countComponents(self, n, edges):
        visited = [0] * n
        dict = { x :[] for x in xrange(n)}

        for edge in edges:
            dict[edge[0]].append(edge[1])
            dict[edge[1]].append(edge[0])

        result = 0
        for i in xrange(n):
            if not visited[i]:
                result += 1
                touched = [i]

                while touched:
                    node = touched.pop(0)
                    if not visited[node]:
                        visited[node] = 1
                        for j in dict[node]:
                            touched.append(j)
        return result



class SolutionDFS(object):
    def countComponents(self, n, edges):
        visited = [0] * n
        dict = { x: []  for x in xrange(n)}
        for edge in edges:
            dict[edge[0]].append(edge[1])
            dict[edge[1]].append(edge[0])

        result = 0
        for i in xrange(n):
            if not visited[i]:
                self.dfs(i, dict, visited)
                result += 1
        return result

    def dfs(self, i, dict, visited):
        if visited[i]:
            return
        visited[i] = 1
        for j in dict[i]:
            self.dfs(j, dict, visited)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().containsDuplicate([12344555,12344555])

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
https://discuss.leetcode.com/topic/40685/java-union-find-dfs-bfs-code-very-clean

# 46ms 5.46%
class Solution {
    public int countComponents(int n, int[][] edges) {
        if (n <= 0) {
            return 0;
        }
        Integer[] groups = new Integer[n];
        for (int i = 0; i < n; i++) {
            groups[i] = i;
        }
        for (int[] edge : edges) {
            int group1 = groups[edge[0]];
            int group2 = groups[edge[1]];
            if (group1 != group2) {
                for (int i = 0; i < n; i++) {
                    if (groups[i] == group2) {
                        groups[i] = group1;
                    }
                }
            }
        }
        return new HashSet<Integer>(Arrays.asList(groups)).size();
    }
}

# DFS:
# 7ms 43.65%
class Solution {
    public int countComponents(int n, int[][] edges) {
        if (n <= 1) {
            return n;
        }
        List<List<Integer>> adjList = new ArrayList<List<Integer>>();
        for (int i = 0; i < n; i++) {
            adjList.add(new ArrayList<Integer>());
        }
        for (int[] edge : edges) {
            adjList.get(edge[0]).add(edge[1]);
            adjList.get(edge[1]).add(edge[0]);
        }
        boolean[] visited = new boolean[n];
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                count++;
                dfs(visited, i, adjList);
            }
        }
        return count;
    }

    public void dfs(boolean[] visited, int index, List<List<Integer>> adjList) {
        visited[index] = true;
        for (int i : adjList.get(index)) {
            if (!visited[i]) {
                dfs(visited, i, adjList);
            }
        }
    }
}

# BFS
# 9ms 36.40%
class Solution {
    public int countComponents(int n, int[][] edges) {
        if( n<= 1) return n;
        List<List<Integer>> adjList = new ArrayList<List<Integer>>();
        for (int i = 0; i < n; i++) adjList.add(new ArrayList<Integer>());
        for (int[] edge : edges) {
            adjList.get(edge[0]).add(edge[1]);
            adjList.get(edge[1]).add(edge[0]);
        }
        boolean[] visited = new boolean[n];
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                count++;
                Queue<Integer> q = new LinkedList<>();
                q.offer(i);
                while(!q.isEmpty()) {
                    int idx = q.poll();
                    visited[idx] = true;
                    for (int next : adjList.get(idx)) {
                        if (!visited[next]) q.offer(next);
                    }
                }
            }
        }
        return count;
    }
}


# Union Find:
# 1ms 100%
class Solution {
    public int countComponents(int n, int[][] edges) {
        int[] nodes = new int[n];
        int[] count = new int[n];
        int res = n;
        for (int i = 0; i < n; i++) nodes[i] = i;
        Arrays.fill(count, 1);
        for (int [] edge: edges) {
            if (union(nodes, count, edge[0], edge[1])) res--;
        }
        return res;
    }

    private boolean union(int[] nodes, int [] count, int i, int j) {
        int rootI = root(nodes, i);
        int rootJ = root(nodes, j);
        if (rootI != rootJ) {
            if (count[rootI] < count[rootJ]) {
                nodes[rootI] = rootJ;
                count[rootJ] += count[rootI];
            } else {
                nodes[rootJ] = rootI;
                count[rootI] += count[rootJ];
            }
            return true;
        } else {
            return false;
        }
    }

    private int root(int[] nodes, int i) {
        while (i != nodes[i]) {
            nodes[i] = nodes[nodes[i]];
            i = nodes[i];
        }
        return i;
    }
}

Thought:
This is 1D version of Number of Islands II. For more explanations, check out this 2D Solution.

n points = n islands = n trees = n roots.
With each edge added, check which island is e[0] or e[1] belonging to.
If e[0] and e[1] are in same islands, do nothing.
Otherwise, union two islands, and reduce islands count by 1.
Bonus: path compression can reduce time by 50%.

# 1ms 100%
class Solution {
    public int countComponents(int n, int[][] edges) {
        int[] root = new int[n];
        for (int i = 0; i < n; i++) {
            root[i] = i;
        }

        for (int[] edge: edges) {
            int root1 = findRoot(root, edge[0]);
            int root2 = findRoot(root, edge[1]);
            if (root1 != root2) {
                root[root1] = root2;
                n--;
            }
        }
        return n;
    }

    private int findRoot(int[]root, int id) {
        while (root[id] != id) {
            root[id] = root[root[id]];
            id = root[id];
        }
        return id;
    }
}

# 1ms 100%
class Solution {
    public int countComponents(int n, int[][] edges) {
        if (n <= 1) {
            return n;
        }
        int[] roots = new int[n];
        for (int i = 0; i < n; i++) {
            roots[i] = i;
        }
        for (int[] edge : edges) {
            int x = find(roots, edge[0]);
            int y = find(roots, edge[1]);
            if (x != y) {
                roots[x] = y;
                n--;
            }
        }
        return n;
    }

    public int find(int[] roots, int id) {
        int x = id;
        while (roots[id] != id) {
            id = roots[id];
        }
        while (roots[x] != id) {
            int fa = roots[x];
            roots[x] = id;
            x = fa;
        }
        return id;
    }
}

'''
