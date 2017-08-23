__source__ = 'https://leetcode.com/problems/minimum-height-trees/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/minimum-height-trees.py
# Time:  O(n)
# Space: O(n)
#
# Description: Leetcode # 310. Minimum Height Trees
#
# For a undirected graph with tree characteristics, we can
# choose any node as the root. The result graph is then a
# rooted tree. Among all possible rooted trees, those with
# minimum height are called minimum height trees (MHTs).
# Given such a graph, write a function to find all the
# MHTs and return a list of their root labels.
#
# Format
# The graph contains n nodes which are labeled from 0 to n - 1.
# You will be given the number n and a list of undirected
# edges (each edge is a pair of labels).
#
# You can assume that no duplicate edges will appear in edges.
# Since all edges are undirected, [0, 1] is the same as [1, 0]
# and thus will not appear together in edges.
#
# Example 1:
#
# Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]
#
#         0
#         |
#         1
#        / \
#       2   3
# return [1]
#
# Example 2:
#
# Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
#
#      0  1  2
#       \ | /
#         3
#         |
#         4
#         |
#         5
# return [3, 4]
#
# Hint:
#
# How many MHTs can a graph have at most?
# Note:
#
# (1) According to the definition of tree on Wikipedia:
#     "a tree is an undirected graph in which any two vertices
#     are connected by exactly one path. In other words,
#     any connected graph without simple cycles is a tree."
#
# (2) The height of a rooted tree is the number of edges on the
#     longest downward path between the root and a leaf.
#
# Companies
# Google
# Related Topics
# Breadth-first Search Graph
# Similar Questions
# Course Schedule Course Schedule II
#
import collections
import unittest
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]

        neighbors = collections.defaultdict(set)

        for u,v in edges:
            neighbors[u].add(v)
            neighbors[v].add(u)

        pre_level, unvisited = [], set()
        for i in xrange(n):
            if len(neighbors[i]) == 1: # A leaf
                pre_level.append(i)
            unvisited.add(i)

        # A graph can have 2 MHTs at most.
        # BFS from the leaves until the number
        # of the unvisited nodes is less than 3.

        while len(unvisited) > 2:
            cur_level = []
            for u in pre_level:
                unvisited.remove(u)
                for v in neighbors[u]:
                    if v in unvisited:
                        neighbors[v].remove(u)
                        if len(neighbors[v]) == 1:
                            cur_level.append(v)
            pre_level = cur_level

        return list(unvisited)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: Our problem want us to find the minimum height trees and return their root labels.
First we can think about a simple case -- a path graph.

For a path graph of n nodes, find the minimum height trees is trivial.
Just designate the middle point(s) as roots.

Despite its triviality, let design a algorithm to find them.

Suppose we don't know n, nor do we have random access of the nodes.
We have to traversal. It is very easy to get the idea of two pointers.
One from each end and move at the same speed. When they meet or they are one step away,
(depends on the parity of n), we have the roots we want.

This gives us a lot of useful ideas to crack our real problem.

For a tree we can do some thing similar. We start from every end,
by end we mean vertex of degree 1 (aka leaves). We let the pointers move the same speed.
When two pointers meet, we keep only one of them, until the last two pointers meet or one step away we then find the roots.

It is easy to see that the last two pointers are from the two ends of the longest path in the graph.

The actual implementation is similar to the BFS topological sort.
Remove the leaves, update the degrees of inner vertexes.
Then remove the new leaves. Doing so level by level until there are 2 or 1 nodes left. What's left is our answer!

The time complexity and space complexity are both O(n).

Note that for a tree we always have V = n, E = n-1.

# 74.12% 49ms  # easy to understand
public class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        if (n == 1) return Collections.singletonList(0);

        List<Set<Integer>> adj = new ArrayList<>(n);
        for (int i = 0; i < n; ++i) adj.add(new HashSet<>());
        for (int[] edge : edges) {
            adj.get(edge[0]).add(edge[1]);
            adj.get(edge[1]).add(edge[0]);
        }

        List<Integer> leaves = new ArrayList<>();
        for (int i = 0; i < n; ++i)
            if (adj.get(i).size() == 1) leaves.add(i);

        while (n > 2) {
            n -= leaves.size();
            List<Integer> newLeaves = new ArrayList<>();
            for (int i : leaves) {
                int j = adj.get(i).iterator().next();
                adj.get(j).remove(i);
                if (adj.get(j).size() == 1) newLeaves.add(j);
            }
            leaves = newLeaves;
        }
        return leaves;
    }
}

#88.71% 30ms
public class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        List<Integer> result = new ArrayList<>();
        List<List<Integer>> graph = new ArrayList<>();
        int[] degrees = new int[n];
        int count = n;
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            degrees[edge[0]]++;
            degrees[edge[1]]++;
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }
        for (int i = 0; i < n; i++) {
            if (degrees[i] <= 1) { //cannot use ==, TLE
                queue.add(i);
                count--;
            }
        }
        while (count > 0) {
            int size = queue.size();
            while (size-- > 0) {
                int cur = queue.poll();
                for (int neighbor : graph.get(cur)) {
                    degrees[neighbor]--;
                    if (degrees[neighbor] == 1) {
                        queue.add(neighbor);
                        count--;
                    }
                }
            }
        }
        while (!queue.isEmpty()) {
            result.add(queue.poll());
        }
        return result;
    }
}
'''