__author__ = 'July'
#https://github.com/kamyu104/LeetCode/blob/master/Python/number-of-connected-components-in-an-undirected-graph.py
'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:
     0          3
     |          |
     1 --- 2    4
Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

Example 2:
     0           4
     |           |
     1 --- 2 --- 3
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.

Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Hide Company Tags Google
Show Tags
Show Similar Problems

'''
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


#java
js = '''
public class Solution {
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
'''