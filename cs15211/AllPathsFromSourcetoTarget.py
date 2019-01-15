__source__ = 'https://leetcode.com/problems/all-paths-from-source-to-target/'
# Time:  O(2^N * N^2) //Because for each path, there exists two possibilities for each node
# (except for the first and the last): appearing or not appearing in the path.
# Therefore, we have 1*2*...*2*1 = 2^(N-2) possibilities for paths.
# Space: O(2^N * N)
#
# Description: Leetcode # 797. All Paths From Source to Target
#
# Given a directed, acyclic graph of N nodes.
# Find all possible paths from node 0 to node N-1, and return them in any order.
#
# The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.
# graph[i] is a list of all nodes j for which the edge (i, j) exists.
#
# Example:
# Input: [[1,2], [3], [3], []]
# Output: [[0,1,3],[0,2,3]]
# Explanation: The graph looks like this:
# 0--->1
# |    |
# v    v
# 2--->3
# There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
# Note:
#
# The number of nodes in the graph will be in the range [2, 15].
# You can print different paths in any order, but you should keep the order of nodes inside one path.
#
import unittest

#164ms 76.44%
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(graph)
        self.path = [None for _ in range(n)]
        self.path[n-1] = [[n-1]]
        return self.dfs(0, graph)

    def dfs(self, n, graph):
        if self.path[n]:
            return self.path[n]
        ret = []
        for i in graph[n]:
            lst = self.dfs(i, graph)
            for l in lst:
                ret.append([n] + l)
        self.path[n] = ret
        return ret

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/all-paths-from-source-to-target/solution/
Approach #1: Recursion [Accepted]
Complexity Analysis
Time Complexity: O(2^N N^2). We can have exponentially many paths, and for each such path,
our prepending operation path.add(0, node) will be O(N^2)
Space Complexity: O(2^N N), the size of the output dominating the final space complexity.

#3ms 100%
class Solution {
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        int goal = graph.length - 1;
        List<List<Integer>> paths = new ArrayList<>();
        ArrayList<Integer> path = new ArrayList<Integer>();
        path.add(0);

        dfs(0, goal, paths, path, graph);

        return paths;
    }

    private void dfs(int origin, int goal, List<List<Integer>> ans, List<Integer> path, int[][] graph) {
        if (origin == goal) {
            ans.add(new ArrayList<Integer>(path));
            return;
        }

        int[] edges = graph[origin];
        for (int i : edges) {
            path.add(i);
            dfs(i, goal, ans, path, graph);
            path.remove(path.size() - 1);
        }
    }
}

#3ms 100%
class Solution {
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        List<List<Integer>> out = new ArrayList<>();
        List<Integer> tempList = new ArrayList<>();
        int[] visited = new int[graph.length];  // 0 -> unvisited, 1 -> visited
        dfs(graph, 0, visited, tempList, out);
        return out;
    }

    //If a DAG needs to mark visited?
    public void dfs(int[][] graph, int vtx, int[] visited, List<Integer> tempList, List<List<Integer>> out) {
        tempList.add(vtx);
        if (vtx == graph.length-1) {
            out.add(new ArrayList<>(tempList));
        } else {
            visited[vtx] = 1;
            for (int nei : graph[vtx]) {
                if (visited[nei] == 0) {
                    dfs(graph, nei, visited, tempList, out);
                    tempList.remove(tempList.size()-1);
                    visited[nei] = 0;
                }
            }
        }
    }
}
'''