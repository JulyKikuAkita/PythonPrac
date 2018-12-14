__source__ = 'https://leetcode.com/problems/possible-bipartition/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 886. Possible Bipartition
#
# Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.
#
# Each person may dislike some other people, and they should not go into the same group.
#
# Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.
#
# Return true if and only if it is possible to split everyone into two groups in this way.
#
#
#
# Example 1:
#
# Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: group1 [1,4], group2 [2,3]
# Example 2:
#
# Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
# Output: false
# Example 3:
#
# Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# Output: false
#
#
# Note:
#
# 1 <= N <= 2000
# 0 <= dislikes.length <= 10000
# 1 <= dislikes[i][j] <= N
# dislikes[i][0] < dislikes[i][1]
# There does not exist i != j for which dislikes[i] == dislikes[j].
#
#
#
import unittest

# 168ms 50.76%
class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        color = {}

        def dfs(node, c = 0):
            if node in color:
                return color[node] == c
            color[node] = c
            return all(dfs(nei, c ^ 1) for nei in graph[node])

        return all(dfs(node) for node in xrange(1, N+1) if node not in color)
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/possible-bipartition/solution/
# Algorithm
#
# Consider the graph on N people formed by the given "dislike" edges.
# We want to check that each connected component of this graph is bipartite.
#
# For each connected component, we can check whether it is bipartite by just trying to coloring it with two colors.
# How to do this is as follows: color any node red, then all of it's neighbors blue, then all of those neighbors red,
# and so on. If we ever color a red node blue (or a blue node red), then we've reached a conflict.
#
# Time Complexity:O(N+E), where E is the length of dislikes.
# Space Complexity: O(N+E).
#

# 50ms 60.66%
class Solution {
    ArrayList<Integer>[] graph;
    Map<Integer, Integer> color;

    public boolean possibleBipartition(int N, int[][] dislikes) {
        graph = new ArrayList[N + 1];
        for (int i = 1; i <= N; i++) graph[i] = new ArrayList<>();
        for (int[] edge: dislikes) {
            graph[edge[0]].add(edge[1]);
            graph[edge[1]].add(edge[0]);
        }

        color = new HashMap();
        for (int node = 1; node <= N; node++) {
            if (!color.containsKey(node) && !dfs(node, 0)) return false;
        }
        return true;
    }

    public boolean dfs(int node, int c) {
        if (color.containsKey(node)) return color.get(node) == c;
        color.put(node, c);

        for (int neighbor : graph[node]) {
            if (!dfs(neighbor, c ^ 1)) return false;
        }
        return true;
    }
}
'''