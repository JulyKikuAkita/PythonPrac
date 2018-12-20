__source__ = 'https://leetcode.com/problems/redundant-connection-ii/description/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 685. Redundant Connection II
#
# In this problem, a rooted tree is a directed graph such that,
# there is exactly one node (the root) for which all other nodes are descendants of this node,
# plus every node has exactly one parent, except for the root node which has no parents.
#
# The given input is a directed graph that started as a rooted tree with N nodes (with distinct values 1, 2, ..., N),
# with one additional directed edge added. The added edge has two different vertices chosen from 1 to N,
# and was not an edge that already existed.
#
# The resulting graph is given as a 2D-array of edges.
# Each element of edges is a pair [u, v] that represents a directed edge connecting nodes u and v,
# where u is a parent of child v.
#
# Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes.
# If there are multiple answers, return the answer that occurs last in the given 2D-array.
#
# Example 1:
# Input: [[1,2], [1,3], [2,3]]
# Output: [2,3]
# Explanation: The given directed graph will be like this:
#   1
#  / \
# v   v
# 2-->3
#
# Example 2:
# Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
# Output: [4,1]
# Explanation: The given directed graph will be like this:
# 5 <- 1 -> 2
#      ^    |
#      |    v
#      4 <- 3
# Note:
# The size of the input 2D-array will be between 3 and 1000.
# Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.
#
# Companies
# Google
# Related Topics
# Graph
# Similar Questions
# Redundant Connection
#
import collections
import unittest
# 40ms 24.16%
class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        N = len(edges)
        parent = {}
        candidates = []
        for u, v in edges:
            if v in parent:
                candidates.append((parent[v], v))
                candidates.append((u, v))
            else:
                parent[v] = u

        def orbit(node):
            seen = set()
            while node in parent and node not in seen:
                seen.add(node)
                node = parent[node]
            return node, seen

        root = orbit(1)[0]

        if not candidates:
            cycle = orbit(root)[1]
            for u, v in edges:
                if u in cycle and v in cycle:
                    ans = u, v
            return ans

        children = collections.defaultdict(list)
        for v in parent:
            children[parent[v]].append(v)

        seen = [True] + [False] * N
        stack = [root]
        while stack:
            node = stack.pop()
            if not seen[node]:
                seen[node] = True
                stack.extend(children[node])

        return candidates[all(seen)]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/redundant-connection-ii/solution/
#
This problem is limited to a graph with N nodes and N edges.
No node is singled out if a edge is removed.
For example, [[1,2],[2,4],[3,4]], 4 nodes 3 edges, is not applicable to this problem.
You cannot remove [3,4] to single out node 3.

There are 3 cases:

No loop, but there is one node who has 2 parents.
A loop, and there is one node who has 2 parents, that node must be inside the loop.
A loop, and every node has only 1 parent.
Case 1: e.g. [[1,2],[1,3],[2,3]] ,node 3 has 2 parents ([1,3] and [2,3]). 
Return the edge that occurs last that is, return [2,3].
Case 2: e.g. [[1,2],[2,3],[3,1],[4,1]] , {1->2->3->1} is a loop, node 1 has 2 parents ([4,1] and [3,1]).
Return the edge that is inside the loop, that is, return [3,1].
Case 3: e.g. [[1,2],[2,3],[3,1],[1,4]] , {1->2->3->1} is a loop, you can remove any edge in a loop,
the graph is still valid. Thus, return the one that occurs last, that is, return [3,1].

# 4ms 55.39%
class Solution {
    public int[] findRedundantDirectedConnection(int[][] edges) {
        int[] ancestor = new int[edges.length + 1];
        int[][] res = new int[2][2];
        for(int[]node : edges) {
            if(node[1] != getAncestor(ancestor, node[1]))
                res[0] = node;
            else if(getAncestor(ancestor, node[0]) == getAncestor(ancestor, node[1]))
                res[1] = node;
            else
                ancestor[node[1]] = ancestor[node[0]];
            if(res[0][0] != 0 && res[1][0] != 0)
                return find(edges, ancestor, res[0], res[1]);
        }
        return res[0][0] == 0 ? res[1] : res[0];
    }

    public int getAncestor(int[] ancestor, int node) {
        if(node != ancestor[node])
            ancestor[node] = ancestor[node] == 0 ? node : getAncestor(ancestor, ancestor[node]);
        return ancestor[node];
    }

    public int[] find(int[][] edges, int[] ancestor, int[] removed0, int[] removed1) {
        for(int[] res : edges)
            if(res[1] == removed0[1] && getAncestor(ancestor, res[1])  == getAncestor(ancestor, removed1[1]))
                return res;
        return new int[2];
    }
}
'''
