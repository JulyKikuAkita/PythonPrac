__source__ = 'https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/'
# Time:  O(ElogN)
# Space: O(N)
#
# Description: Leetcode # 882. Reachable Nodes In Subdivided Graph
#
# Starting with an undirected graph (the "original graph") with nodes from 0 to N-1,
# subdivisions are made to some of the edges.
#
# The graph is given as follows: edges[k] is a list of integer pairs (i, j, n) such that (i, j)
# is an edge of the original graph,
#
# and n is the total number of new nodes on that edge.
#
# Then, the edge (i, j) is deleted from the original graph,
# n new nodes (x_1, x_2, ..., x_n) are added to the original graph,
#
# and n+1 new edges (i, x_1), (x_1, x_2), (x_2, x_3), ..., (x_{n-1}, x_n), (x_n, j) are added to the original graph.
#
# Now, you start at node 0 from the original graph,
# and in each move, you travel along one edge.
#
# Return how many nodes you can reach in at most M moves.
#
# Example 1:
#
# Input: edges = [[0,1,10],[0,2,1],[1,2,2]], M = 6, N = 3
# Output: 13
# Explanation:
# The nodes that are reachable in the final graph after M = 6 moves are indicated below.
#
# Example 2:
#
# Input: edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], M = 10, N = 4
# Output: 23
#
# Note:
#
#     0 <= edges.length <= 10000
#     0 <= edges[i][0] < edges[i][1] < N
#     There does not exist any i != j for which edges[i][0] == edges[j][0] and edges[i][1] == edges[j][1].
#     The original graph has no parallel edges.
#     0 <= edges[i][2] <= 10000
#     0 <= M <= 10^9
#     1 <= N <= 3000
#     A reachable node is a node that can be travelled to using at most M moves starting from node 0.
#
import unittest
import collections
import heapq
# 196ms 92.31%
class Solution(object):
    def reachableNodes(self, edges, M, N):
        """
        :type edges: List[List[int]]
        :type M: int
        :type N: int
        :rtype: int
        """
        graph = collections.defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = graph[v][u] = w

        pq = [(0, 0)]
        dist = {0: 0}
        used = {}
        ans = 0

        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]: continue
            # Each node is only visited once.  We've reached
            # a node in our original graph.
            ans += 1

            for nei, weight in graph[node].iteritems():
                # M - d is how much further we can walk from this node;
                # weight is how many new nodes there are on this edge.
                # v is the maximum utilization of this edge.
                v = min(weight, M - d)
                used[node, nei] = v

                # d2 is the total distance to reach 'nei' (neighbor) node
                # in the original graph.
                d2 = d + weight + 1
                if d2 < dist.get(nei, M+1):
                    heapq.heappush(pq, (d2, nei))
                    dist[nei] = d2

        # At the end, each edge (u, v, w) can be used with a maximum
        # of w new nodes: a max of used[u, v] nodes from one side,
        # and used[v, u] nodes from the other.
        for u, v, w in edges:
            ans += min(w, used.get((u, v), 0) + used.get((v, u), 0))

        return ans
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/solution/
#
Approach 1: Dijkstra's
Complexity Analysis
Time Complexity: O(ElogN), where E is the length of edges.
Space Complexity: O(N)

# 210ms 58.23%
class Solution {
    public int reachableNodes(int[][] edges, int M, int N) {
        Map<Integer, Map<Integer, Integer>> graph = new HashMap();
        for (int[] edge: edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            graph.computeIfAbsent(u, x->new HashMap()).put(v, w);
            graph.computeIfAbsent(v, x->new HashMap()).put(u, w);
        }

        PriorityQueue<ANode> pq = new PriorityQueue<ANode>(
            (a, b) -> Integer.compare(a.dist, b.dist));
        pq.offer(new ANode(0, 0));

        Map<Integer, Integer> dist = new HashMap();
        dist.put(0, 0);
        Map<Integer, Integer> used = new HashMap();
        int ans = 0;

        while (!pq.isEmpty()) {
            ANode anode = pq.poll();
            int node = anode.node;
            int d = anode.dist;

            if (d > dist.getOrDefault(node, 0)) continue;
            // Each node is only visited once.  We've reached
            // a node in our original graph.
            ans++;

            if (!graph.containsKey(node)) continue;
            for (int nei: graph.get(node).keySet()) {
                // M - d is how much further we can walk from this node;
                // weight is how many new nodes there are on this edge.
                // v is the maximum utilization of this edge.
                int weight = graph.get(node).get(nei);
                int v = Math.min(weight, M - d);
                used.put(N * node + nei, v);

                // d2 is the total distance to reach 'nei' (neighbor) node
                // in the original graph.
                int d2 = d + weight + 1;
                if (d2 < dist.getOrDefault(nei, M+1)) {
                    pq.offer(new ANode(nei, d2));
                    dist.put(nei, d2);
                }
            }
        }

        // At the end, each edge (u, v, w) can be used with a maximum
        // of w new nodes: a max of used[u, v] nodes from one side,
        // and used[v, u] nodes from the other.
        // [We use the encoding (u, v) = u * N + v.]
        for (int[] edge: edges) {
            ans += Math.min(edge[2], used.getOrDefault(edge[0] * N + edge[1], 0) +
                                     used.getOrDefault(edge[1] * N + edge[0], 0) );
        }

        return ans;
    }
}

class ANode {
    int node, dist;
    ANode(int n, int d) {
        node = n;
        dist = d;
    }
}

# 19ms 97.47%
class Solution {
    public int reachableNodes(int[][] edges, int M, int N) {
        boolean flag = true;
        int[] steps = new int[N];
        Arrays.fill(steps, -1);
        steps[0] = M;
        while(flag){
            flag = false;
            for (int[] edge : edges) {
                if (steps[edge[0]] > 0) {
                    int na = steps[edge[0]] - edge[2] - 1;
                    if (na > steps[edge[1]]) {
                        steps[edge[1]] = na;
                        flag = true;
                    }
                }
                if (steps[edge[1]] > 0) {
                    int na = steps[edge[1]] - edge[2] - 1;
                    if (na > steps[edge[0]]) {
                        steps[edge[0]] = na;
                        flag = true;
                    }
                }
            }
        }
        int res = 0;
        for (int i = 0; i < N; i++) 
            if(steps[i] != -1) res++;
        for (int[] edge : edges) {
            int tmp = 0;
            if(steps[edge[0]] > 0) tmp += steps[edge[0]];
            if(steps[edge[1]] > 0) tmp += steps[edge[1]];
            res += tmp > edge[2] ? edge[2] : tmp;
        }
        return res;
    }
}
'''
