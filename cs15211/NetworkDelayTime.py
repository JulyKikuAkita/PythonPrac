__source__ = 'https://leetcode.com/problems/network-delay-time/'
# Time:  O(N^2+E)
# Space: O(N+E)  the size of the graph O(E), plus the size of the other objects used O(N).
#
# Description: Leetcode # 743. Network Delay Time
#
# There are N network nodes, labelled 1 to N.
#
# Given times, a list of travel times as directed edges times[i] = (u, v, w),
# where u is the source node, v is the target node,
# and w is the time it takes for a signal to travel from source to target.
#
# Now, we send a signal from a certain node K.
# How long will it take for all nodes to receive the signal? If it is impossible, return -1.
#
# Note:
# N will be in the range [1, 100].
# K will be in the range [1, N].
# The length of times will be in the range [1, 6000].
# All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 1 <= w <= 100.
#
import unittest
import collections

# 100ms 69.56% //Dijkstra's
class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {node: float('inf') for node in xrange(1, N+1)}
        seen = [False] * (N+1)
        dist[K] = 0

        while True:
            cand_node = -1
            cand_dist = float('inf')
            for i in xrange(1, N+1):
                if not seen[i] and dist[i] < cand_dist:
                    cand_dist = dist[i]
                    cand_node = i

            if cand_node < 0: break
            seen[cand_node] = True
            for nei, d in graph[cand_node]:
                dist[nei] = min(dist[nei], dist[cand_node] + d)

        ans = max(dist.values())
        return ans if ans < float('inf') else -1

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/network-delay-time/solution/

Approach #1: Depth-First Search [Accepted]
Complexity Analysis
Time Complexity: O(N^N + ElogE) where E is the length of times.
We can only fully visit each node up to N-1 times, one per each other node.
Plus, we have to explore every edge and sort them.
Sorting each small bucket of outgoing edges is bounded by sorting all of them,
because of repeated use of the inequality xlogx + ylogy <= (x+y)log(x+y).
Space Complexity: O(N + E), the size of the graph O(E),
plus the size of the implicit call stack in our DFS (O(N)

# 113ms 23.29%
class Solution {
    Map<Integer, Integer> dist;
    public int networkDelayTime(int[][] times, int N, int K) {
        Map<Integer, List<int[]>> graph = new HashMap();
        for (int[] edge: times) {
            if (!graph.containsKey(edge[0]))
                graph.put(edge[0], new ArrayList<int[]>());
            graph.get(edge[0]).add(new int[]{edge[2], edge[1]});
        }
        for (int node: graph.keySet()) {
            Collections.sort(graph.get(node), (a, b) -> a[0] - b[0]);
        }
        dist = new HashMap();
        for (int node = 1; node <= N; ++node)
            dist.put(node, Integer.MAX_VALUE);

        dfs(graph, K, 0);
        int ans = 0;
        for (int cand: dist.values()) {
            if (cand == Integer.MAX_VALUE) return -1;
            ans = Math.max(ans, cand);
        }
        return ans;
    }

    public void dfs(Map<Integer, List<int[]>> graph, int node, int elapsed) {
        if (elapsed >= dist.get(node)) return;
        dist.put(node, elapsed);
        if (graph.containsKey(node))
            for (int[] info: graph.get(node))
                dfs(graph, info[1], elapsed + info[0]);
    }
}

Approach #2: Dijkstra's Algorithm [Accepted]
Complexity Analysis
Time Complexity: O(N^2 + E))m where E is the length of times in the basic implementation,
and O(ElogE) in the heap implementation,
as potentially every edge gets added to the heap.
Space Complexity: O(N + E), the size of the graph (O(E), plus the size of the other objects used (O(N)).

# 20ms 91.46%
class Solution {
    Map<Integer, Integer> dist;
    public int networkDelayTime(int[][] times, int N, int K) {
        Map<Integer, List<int[]>> graph = new HashMap();
        for (int[] edge: times) {
            if (!graph.containsKey(edge[0]))
                graph.put(edge[0], new ArrayList<int[]>());
            graph.get(edge[0]).add(new int[]{edge[1], edge[2]});
        }
        dist = new HashMap();
        for (int node = 1; node <= N; ++node)
            dist.put(node, Integer.MAX_VALUE);

        dist.put(K, 0);
        boolean[] seen = new boolean[N+1];

        while (true) {
            int candNode = -1;
            int candDist = Integer.MAX_VALUE;
            for (int i = 1; i <= N; ++i) {
                if (!seen[i] && dist.get(i) < candDist) {
                    candDist = dist.get(i);
                    candNode = i;
                }
            }

            if (candNode < 0) break;
            seen[candNode] = true;
            if (graph.containsKey(candNode))
                for (int[] info: graph.get(candNode))
                    dist.put(info[0],
                             Math.min(dist.get(info[0]), dist.get(candNode) + info[1]));
        }

        int ans = 0;
        for (int cand: dist.values()) {
            if (cand == Integer.MAX_VALUE) return -1;
            ans = Math.max(ans, cand);
        }
        return ans;
    }
}

# Dijkstra's algorithm
# 9ms 98.61%
class Solution {
    public int networkDelayTime(int[][] times, int N, int K) {
        Integer[][] graph = buildGraph(times, N);

        Integer[] minTimes = new Integer[N + 1];
        boolean[] finalized = new boolean[N + 1];
        minTimes[K] = 0;

        // Note: N range from 1 - N
        for (int count = 0; count < N - 1; count++) {
            int minDistanceNode = minDistanceIndex(minTimes, finalized);
            if (minDistanceNode == -1) {
                // Not all nodes clustered
                return -1;
            }
            finalized[minDistanceNode] = true;
            for (int dest = 1; dest < N + 1; dest++) {
                if (!finalized[dest] && graph[minDistanceNode][dest] != null &&
                   (minTimes[dest] == null || minTimes[dest] > minTimes[minDistanceNode] + graph[minDistanceNode][dest])) {
                    minTimes[dest] = minTimes[minDistanceNode] + graph[minDistanceNode][dest];
                }
            }
        }

        int max = 0;
        for (int i = 1; i <= N; i++) {
            if (minTimes[i] == null) {
                return -1;
            }
            max = Math.max(max, minTimes[i]);
        }
        return max;
    }

    private int minDistanceIndex(Integer[] minTimes, boolean[] finalized) {
        int min = Integer.MAX_VALUE;
        int minIndex = -1;
        for (int i = 1; i < minTimes.length; i++) {
            if (!finalized[i] && minTimes[i] != null && minTimes[i] < min) {
                min = minTimes[i];
                minIndex = i;
            }
        }
        return minIndex;
    }

    private Integer[][] buildGraph(int[][] times, int N) {
        Integer[][] graph = new Integer[N + 1][N + 1];
        for (int[] time : times) {
            graph[time[0]][time[1]] = time[2];
        }
        return graph;
    }
}

# https://leetcode.com/problems/network-delay-time/discuss/183873/Java-solutions-using-Dijkstra-FloydWarshall-and-Bellman-Ford-algorithm
# Dijkstra's algorithm + PQ
# Time complexity: O(Nlog(N) + E), Space complexity: O(N + E)
# 56ms 64.93%
class Solution {
    public int networkDelayTime(int[][] times, int N, int K) {
        Map<Integer, List<int[]>> graph = new HashMap<>();
        for (int[] edge : times) {
            graph.computeIfAbsent(edge[0], k -> new ArrayList<>()).add(new int[]{edge[1], edge[2]});
        }
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> (a[0] - b[0]));
        boolean[] visited = new boolean[N + 1];
        int[] minDis = new int[N + 1];
        Arrays.fill(minDis, Integer.MAX_VALUE);
        minDis[K] = 0;
        pq.offer(new int[]{0, K});
        int ans = 0;
        while(!pq.isEmpty()) {
            int[] cur = pq.poll();
            if (visited[cur[1]]) continue;
            visited[cur[1]] = true;
            ans = cur[0];
            N--;
            if (!graph.containsKey(cur[1])) continue;
            for (int[] next : graph.get(cur[1])) {
                if (!visited[next[0]] && cur[0] + next[1] < minDis[next[0]]) {
                    minDis[next[0]] = cur[0] + next[1]; //better performance
                    pq.offer(new int[] {cur[0] + next[1], next[0]});
                }
            }
        }
        return N == 0 ? ans : -1;
    }
}

# Bellman Ford
# Time complexity: O(N*E), Space complexity: O(N)
# 29ms 85.14%
class Solution {
    public int networkDelayTime(int[][] times, int N, int K) {
        int[] dist = new int[N + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[K] = 0;
        for (int i = 0; i < N; i++) {
            for (int[] e : times) {
                int u = e[0], v = e[1], w = e[2];
                if (dist[u] != Integer.MAX_VALUE && dist[v] > dist[u] + w) {
                    dist[v] = dist[u] + w;
                }
            }
        }
        
        int maxWait = 0;
        for (int i = 1; i <= N; i++) {
            maxWait = Math.max(dist[i], maxWait);
        }
        return maxWait == Integer.MAX_VALUE ? -1 : maxWait;
    }
}

# Floyd-Warshall algorithm
# Time complexity: O(N^3), Space complexity: O(N^2)
# 35ms 79.48%
class Solution {
    public int networkDelayTime(int[][] times, int N, int K) {
        double[][] disTo = new double[N + 1][N + 1];
        for (int i = 1; i < N + 1; i++) Arrays.fill(disTo[i], Double.POSITIVE_INFINITY);
        for (int i = 1; i < N + 1; i++) disTo[i][i] = 0;
        for (int[] edge: times) disTo[edge[0]][edge[1]] = edge[2];

        for (int k = 1; k < N + 1; k++) {
            for (int i = 1; i < N + 1; i++) {
                for (int j = 1; j < N + 1; j++) {
                    if (disTo[i][j] > disTo[i][k] + disTo[k][j]) {
                        disTo[i][j] = disTo[i][k] + disTo[k][j];
                    }
                }
            }
        }
        double max = Double.MIN_VALUE;
        for (int i = 1; i < N + 1; i++) {
            if (disTo[K][i] == Double.POSITIVE_INFINITY) return -1;
            max = Math.max(disTo[K][i], max);
        }
        return (int) max;
    }
}
'''
