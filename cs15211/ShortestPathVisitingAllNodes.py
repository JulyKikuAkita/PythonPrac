__source__ = 'https://leetcode.com/problems/shortest-path-visiting-all-nodes/'
# Time:  O(2^N * N)
# Space: O(2^N * N)
#
# Description: Leetcode # 847. Shortest Path Visiting All Nodes
#
# An undirected, connected graph of N nodes (labeled 0, 1, 2, ..., N-1) is given as graph.
#
# graph.length = N, and j != i is in the list graph[i] exactly once,
# if and only if nodes i and j are connected.
#
# Return the length of the shortest path that visits every node.
# You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.
#
# Example 1:
#
# Input: [[1,2,3],[0],[0],[0]]
# Output: 4
# Explanation: One possible path is [1,0,2,0,3]
# Example 2:
# Note: Graph: index 0 connect to [1],  [2],  [3]
#      / - [1]
# [0] - - [2]
#      \ - [3]
#
# Input: [[1],[0,2,4],[1,3,4],[2],[1,2]]
# Output: 4
# Explanation: One possible path is [0,1,4,2,3]
#
# Note: Graph: index 0 connect to [1]; index 1 connect to [0], [2], [4], same for the rest
#
# [0] - - [1] - [2] -[3]
#          |     |
#          --[4]--

# Note:
#
# 1 <= graph.length <= 12
# 0 <= graph[i].length < graph.length
#
import unittest
import collections

# 108ms 68.09%
class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        N = len(graph)
        queue = collections.deque((1 << x, x) for x in xrange(N))
        dist = collections.defaultdict(lambda: N*N)
        for x in xrange(N): dist[1 << x, x] = 0

        while queue:
            cover, head = queue.popleft()
            d = dist[cover, head]
            if cover == 2**N - 1: return d
            for child in graph[head]:
                cover2 = cover | (1 << child)
                if d + 1 < dist[cover2, child]:
                    dist[cover2, child] = d + 1
                    queue.append((cover2, child))

# 228ms 23.40%
class Solution_Bellman_Ford(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        N = len(graph)
        dist = [[float('inf')] * N for i in xrange(1 << N)]
        for x in xrange(N):
            dist[1<<x][x] = 0

        for cover in xrange(1 << N):
            repeat = True
            while repeat:
                repeat = False
                for head, d in enumerate(dist[cover]):
                    for nei in graph[head]:
                        cover2 = cover | (1 << nei)
                        if d + 1 < dist[cover2][nei]:
                            dist[cover2][nei] = d + 1
                            if cover == cover2:
                                repeat = True

        return min(dist[2**N - 1])
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/shortest-path-visiting-all-nodes/solution/
video: http://zxi.mytechroad.com/blog/graph/leetcode-847-shortest-path-visiting-all-nodes/

Approach #1: Breadth First Search [Accepted]
NOte: The neighbors are (cover | (1 << child), child) for each child in graph[head].

Complexity Analysis
Time Complexity: O(2^N * N)
Space Complexity: O(2^N * N)

# 108ms 68.09%
class Solution {

    class State {
        int cover, head;
        State(int c, int h) {
            cover = c;
            head = h;
        }
    }

    public int shortestPathLength(int[][] graph) {
        int N = graph.length;
        Queue<State> queue = new LinkedList();
        int[][] dist = new int[1<<N][N];
        for (int[] row : dist) Arrays.fill(row, N * N);

        for (int x = 0; x < N; x++) {
            queue.offer(new State(1<<x, x));
            dist[1<<x][x] = 0;
        }

        while (!queue.isEmpty()) {
            State node = queue.poll();
            int d = dist[node.cover][node.head];
            if (node.cover == (1 << N) - 1) return d;
            for (int child : graph[node.head]) {
                //The neighbors are (cover | (1 << child), child) for each child in graph[head].
                int cover2 = node.cover | (1 << child);
                if (d + 1 < dist[cover2][child]) {
                    dist[cover2][child] = d + 1;
                    queue.offer(new State(cover2, child));
                }
            }
        }
        throw null;
    }
}

Approach #2: Dynamic Programming [Accepted]  Bellman-Ford algorithm
NOte: https://www.programiz.com/dsa/bellman-ford-algorithm can apply to negative edge
Complexity Analysis
Time Complexity: O(2^N * N) ?O( n^3 2^N), since the inner loop essentially runs Bellman-ford which is o(|v||E|),
in this case O(n^3) since there can be n^2 edges
Space Complexity: O(2^N * N)

#12ms 80.89%
class Solution {
    public int shortestPathLength(int[][] graph) {
        int N = graph.length;
        int dist[][] = new int[1 << N][N];
        for (int[] row : dist) Arrays.fill(row, N * N);
        for (int x = 0; x < N; x++) dist[1 << x][x] = 0;

        for (int cover = 0; cover < 1 << N; cover++) {
            boolean repeat = true;
            while (repeat) {
                repeat  = false;
                for (int head = 0; head < N; head++) {
                    int d = dist[cover][head];
                    for (int next : graph[head]) {
                        int cover2 = cover | (1 << next);
                        if (d + 1 < dist[cover2][next]) {
                            dist[cover2][next] = d + 1;
                            if (cover == cover2) repeat = true;
                        }
                    }
                }
            }
        }

        int ans = N * N;
        for (int cand : dist[(1 << N) - 1]) ans = Math.min(ans, cand);
        return ans;
    }
}

# 8ms 99.45%
class Solution {
    public int shortestPathLength(int[][] graph) {
        if (graph == null || graph.length == 0) return 0;
        int target = (1 << graph.length) - 1; //target state
        boolean[][] visited = new boolean[graph.length][target + 1];
        Queue<int[]> queue = new ArrayDeque(); //{pathHeadNode, pathMask}

        for (int i = 0; i < graph.length; i++) {
            queue.offer(new int[]{i, 1 << i});
            visited[i][1 << i] = true;
        }

        int step = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] cur = queue.poll();
                if (cur[1] == target) { //cur[1] is current path mask
                    return step;
                }
                for (int nei : graph[cur[0]]) {
                    int nextVisit = ( 1 << nei) | cur[1];
                    if (!visited[nei][nextVisit]) {
                        visited[nei][nextVisit] = true;
                        queue.offer(new int[]{nei, nextVisit});
                    }
                }
            }
            step++;
        }
        return -1;
    }
}
'''