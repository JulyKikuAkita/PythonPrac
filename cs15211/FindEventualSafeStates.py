__source__ = 'https://leetcode.com/problems/find-eventual-safe-states/'
# Time:  O(N + E)
# Space: O(N)
#
# Description: Leetcode # 802. Find Eventual Safe States
#
# In a directed graph, we start at some node and every turn,
# walk along a directed edge of the graph.
# If we reach a node that is terminal (that is, it has no outgoing directed edges), we stop.
#
# Now, say our starting node is eventually safe if and only if we must eventually walk to a terminal node.
# More specifically, there exists a natural number K so that for any choice of where to walk,
# we must have stopped at a terminal node in less than K steps.
#
# Which nodes are eventually safe?  Return them as an array in sorted order.
#
# The directed graph has N nodes with labels 0, 1, ..., N-1, where N is the length of graph.
# The graph is given in the following form: graph[i] is a list of labels j
# such that (i, j) is a directed edge of the graph.
#
# Example:
# Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# Output: [2,4,5,6]
# Here is a diagram of the above graph.
#
# Illustration of graph
#
# Note:
#
# graph will have length at most 10000.
# The number of edges in the graph will not exceed 32000.
# Each graph[i] will be a sorted list of different integers,
# chosen within the range [0, graph.length - 1].
#
import collections
import unittest
# 512ms 18.54%
class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        N = len(graph)
        safe = [False] * N

        graph = map(set, graph)
        rgraph = [set() for _ in xrange(N)]
        q = collections.deque()

        for i, js in enumerate(graph):
            if not js:
                q.append(i)
            for j in js:
                rgraph[j].add(i)

        while q:
            j = q.popleft()
            safe[j] = True
            for i in rgraph[j]:
                graph[i].remove(j)
                if len(graph[i]) == 0:
                    q.append(i)
        return [i for i, v in enumerate(safe) if v]

# 304ms 35.35%
class Solution2(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        WHITE, GRAY, BLACK = 0, 1, 2
        color = collections.defaultdict(int)

        def dfs(node):
            if color[node] != WHITE:
                return color[node] == BLACK

            color[node] = GRAY
            for nei in graph[node]:
                if color[nei] == BLACK:
                    continue
                if color[nei] == GRAY or not dfs(nei):
                    return False
            color[node] = BLACK
            return True
        return filter(dfs, range(len(graph)))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/find-eventual-safe-states/solution/
Approach #1: Reverse Edges [Accepted]
Complexity Analysis
Time Complexity: O(N + E), where N is the number of nodes in the given graph, and E is the total number of edges.
Space Complexity: O(N) in additional space complexity.

# 114ms 22.56%
class Solution {
    public List<Integer> eventualSafeNodes(int[][] graph) {
        int N = graph.length;
        boolean[] safe = new boolean[N];

        List<Set<Integer>> tmp = new ArrayList();
        List<Set<Integer>> rgraph = new ArrayList();
        for (int i = 0; i < N; ++i) {
            tmp.add(new HashSet());
            rgraph.add(new HashSet());
        }

        Queue<Integer> queue = new LinkedList();
        for (int i = 0; i < N; i++) {
            if (graph[i].length == 0) queue.offer(i);
            for (int j : graph[i]) {
                tmp.get(i).add(j);
                rgraph.get(j).add(i);
            }
        }

        while (!queue.isEmpty()) {
            int j = queue.poll();
            safe[j] = true;
            for (int i : rgraph.get(j)) {
                tmp.get(i).remove(j);
                if (tmp.get(i).isEmpty()) queue.offer(i);
            }
        }

        List<Integer> ans = new ArrayList();
        for (int i = 0; i < N; i++) {
            if (safe[i]) ans.add(i);
        }
        return ans;
    }
}

Approach #2: Depth-First Search [Accepted]
Complexity Analysis
Time Complexity: O(N + E), where N is the number of nodes in the given graph, and E is the total number of edges.
Space Complexity: O(N) in additional space complexity.

# 11ms 97.36%
class Solution {
    public List<Integer> eventualSafeNodes(int[][] graph) {
        int N = graph.length;
        int[] color = new int[N];
        List<Integer> ans = new ArrayList();

        for (int i = 0; i < N; i++) {
            if (dfs(i, color, graph)) ans.add(i);
        }
        return ans;
    }

    // colors: WHITE 0, GRAY 1, BLACK 2;
    private boolean dfs(int node, int[] color, int[][] graph) {
        if (color[node] > 0) return color[node] == 2;
        color[node] = 1;
        for (int nei: graph[node]) {
            if (color[node] == 2) continue;
            if (color[nei] == 1 || !dfs(nei, color, graph)) return false;
        }
        color[node] = 2;
        return true;
    }
}

# https://leetcode.com/problems/find-eventual-safe-states/discuss/120633/Java-Solution-(DFS-andand-Topological-Sort)
# topological sort
# 62ms 36.36%
class Solution {
    public List<Integer> eventualSafeNodes(int[][] graph) {
        int n = graph.length;
        int[] degree = new int [n];
        Set<Integer>[] map = new HashSet[n];
        for (int i = 0; i < n; i++) map[i] = new HashSet();
        for (int i = 0; i < n; i++) {
            for (int node : graph[i]) {
                map[node].add(i);
                degree[i]++;
            }
        }
        Queue<Integer> queue = new LinkedList();
        Set<Integer> set = new HashSet();
        for (int i = 0; i < n; i++) {
            if (degree[i] == 0) {
                set.add(i);
                queue.add(i);
            }
        }

        while (!queue.isEmpty()) {
            int node = queue.poll();
            set.add(node);
            for (int nei : map[node]) {
                degree[nei]--;
                if (degree[nei] == 0) {
                    queue.add(nei);
                }
            }
        }
        
        List<Integer> ans = new ArrayList(set);
        Collections.sort(ans);
        return ans;
    }
}

# https://leetcode.com/problems/find-eventual-safe-states/discuss/119871/Straightforward-Java-solution-easy-to-understand!
# 14ms 60.33%
class Solution {
    // value of color represents three states:
    static int NOT_V = 0; // 0:have not been visited
    static int SAFE = 1; // 1:safe
    static int LOOP = 2; // 2:unsafe
    public List<Integer> eventualSafeNodes(int[][] graph) {
        List<Integer> res = new ArrayList();
        int[] color = new int[graph.length];
        for (int i = 0; i < graph.length; i++) {
            if (dfs(graph, color, i)) res.add(i);
        }
        return res;
            
    }
    
    private boolean dfs(int[][] graph, int[] color, int start) {
        if (color[start] == LOOP) return false;
        if (color[start] == SAFE) return true;
        color[start] = LOOP;
        for (int nei : graph[start]) {
            if (!dfs(graph, color, nei)) return false;
        }
        color[start] = SAFE;
        return true;
    }
}
'''
