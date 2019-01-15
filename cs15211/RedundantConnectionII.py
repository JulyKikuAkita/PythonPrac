__source__ = 'https://leetcode.com/problems/redundant-connection-ii/description/'
# Time:  O(V) numbert of vertices
# Space: O(V)
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
Approach #1: Depth-First Search [Accepted]
Complexity Analysis
Time Complexity: O(N) where N is the number of vertices (and also the number of edges) in the graph. 
We perform a depth-first search.
Space Complexity: O(N), the size of the graph.
# 23ms 6.62%
class Solution {
    public int[] findRedundantDirectedConnection(int[][] edges) {
        int N = edges.length;
        Map<Integer, Integer> parent = new HashMap();
        List<int[]> candidates = new ArrayList();
        for (int[] edge: edges) {
            if (parent.containsKey(edge[1])) {
                candidates.add(new int[]{parent.get(edge[1]), edge[1]});
                candidates.add(edge);
            } else {
                parent.put(edge[1], edge[0]);
            }
        }

        int root = orbit(1, parent).node;
        if (candidates.isEmpty()) {
            Set<Integer> cycle = orbit(root, parent).seen;
            int[] ans = new int[]{0, 0};
            for (int[] edge: edges) {
                if (cycle.contains(edge[0]) && cycle.contains(edge[1])) {
                    ans = edge;
                }
            }
            return ans;
        }

        Map<Integer, List<Integer>> children = new HashMap();
        for (int v: parent.keySet()) {
            int pv = parent.get(v);
            if (!children.containsKey(pv))
                children.put(pv, new ArrayList<Integer>());
            children.get(pv).add(v);
        }

        boolean[] seen = new boolean[N+1];
        seen[0] = true;
        Stack<Integer> stack = new Stack();
        stack.add(root);
        while (!stack.isEmpty()) {
            int node = stack.pop();
            if (!seen[node]) {
                seen[node] = true;
                if (children.containsKey(node)) {
                    for (int c: children.get(node))
                        stack.push(c);
                }
            }
        }
        for (boolean b: seen) if (!b)
            return candidates.get(0);
        return candidates.get(1);
    }

    public OrbitResult orbit(int node, Map<Integer, Integer> parent) {
        Set<Integer> seen = new HashSet();
        while (parent.containsKey(node) && !seen.contains(node)) {
            seen.add(node);
            node = parent.get(node);
        }
        return new OrbitResult(node, seen);
    }

}
class OrbitResult {
    int node;
    Set<Integer> seen;
    OrbitResult(int n, Set<Integer> s) {
        node = n;
        seen = s;
    }
}

This problem is limited to a graph with N nodes and N edges.
No node is singled out if a edge is removed.
For example, [[1,2],[2,4],[3,4]], 4 nodes 3 edges, is not applicable to this problem.
You cannot remove [3,4] to single out node 3.

There are 3 cases:

Case 1) No loop, but there is one node who has 2 parents.
Case 2) A loop, and there is one node who has 2 parents, that node must be inside the loop.
Case 3) A loop, and every node has only 1 parent.
Case 1: e.g. [[1,2],[1,3],[2,3]] ,node 3 has 2 parents ([1,3] and [2,3]). 
Return the edge that occurs last that is, return [2,3].
Case 2: e.g. [[1,2],[2,3],[3,1],[4,1]] , {1->2->3->1} is a loop, node 1 has 2 parents ([4,1] and [3,1]).
Return the edge that is inside the loop, that is, return [3,1].
Case 3: e.g. [[1,2],[2,3],[3,1],[1,4]] , {1->2->3->1} is a loop, you can remove any edge in a loop,
the graph is still valid. Thus, return the one that occurs last, that is, return [3,1].
Also, [[2,1],[3,1],[4,2],[1,4]] is a good example

# Union Find
# 5ms 95.59%%
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
# Union Find
# 5ms 95.59%%
class Solution {
    public int[] findRedundantDirectedConnection(int[][] edges) {
        int[] parent = new int[edges.length+1];
        for (int i = 0; i < parent.length; i++) {
            parent[i] = i;
        }
        int[] cycleEdge = null;
        int[] mParent = null;

        for (int[] edge : edges) {
            int x = find(parent, edge[0]);
            int y = find(parent, edge[1]);
            
            if (x == y)
                cycleEdge = edge;
            else {
                if (y != edge[1])
                    mParent = edge;
                else
                    parent[y] = x;
            }
        }
        // means we only got the multiparent problem, and the edges we recorded using parent so far are good, so juse return this one.
        if (cycleEdge == null)
            return mParent;

        // means we only got the cycle problem, in this case we can remove any edge in the cycle, so just remove this one.
        if (mParent == null)
            return cycleEdge;

        // now, it means we have both cycle and multi-parent problem.
        // In my code, i didn't record an edge into parent if we think it's involved into the multi-parent problem,
        // but we are still getting the cycle problem. Since in this problem we can only have edges point to the same
        // node, so, current mParent edge is the wrong one, we need to remove the other one pointint to the same
        // dest as mParent ex: [[2,1],[3,1],[4,2],[1,4]]
        for (int[] edge : edges) {
            if (edge[1] == mParent[1])
                return edge;
        }

        return new int[2];
    }
    
    public int find(int[] parent, int x) {
        if (parent[x] == x)
            return x;
        return find(parent, parent[x]);
    }
}
'''
