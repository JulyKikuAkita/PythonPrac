__source__ = 'https://leetcode.com/problems/sum-of-distances-in-tree/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 834. Sum of Distances in Tree
#
# An undirected, connected tree with N nodes labelled 0...N-1 and N-1 edges are given.
#
# The ith edge connects nodes edges[i][0] and edges[i][1] together.
#
# Return a list ans, where ans[i] is the sum of the distances between node i and all other nodes.
#
# Example 1:
#
# Input: N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
# Output: [8,12,6,10,10,10]
# Explanation:
# Here is a diagram of the given tree:
#   0
#  / \
# 1   2
#    /|\
#   3 4 5
# We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
# equals 1 + 1 + 2 + 2 + 2 = 8.  Hence, answer[0] = 8, and so on.
#
# Note: 1 <= N <= 10000
#
import unittest
import collections

# 176ms 96.19%
class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        count = [1] * N
        ans = [0] * N
        def dfs(node = 0, parent = None):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]

        def dfs2(node = 0, parent = None):
            for child in graph[node]:
                if child != parent:
                    ans[child] = ans[node] - count[child] + N - count[child]
                    dfs2(child, node)
        dfs()
        dfs2()
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/sum-of-distances-in-tree/solution/
#
Approach #1: Subtree Sum and Count [Accepted]
Complexity Analysis
Time Complexity: O(N), where N is the number of nodes in the graph.
Space Complexity: O(N)

ans[child] = ans[parent] - count[child] + (N - count[child]). 
This is because there are count[child] nodes that are 1 easier to get to from child than parent, 
and N-count[child] nodes that are 1 harder to get to from child than parent.

# 38ms 82.17%
class Solution {
    int[] ans, count;
    List<Set<Integer>> graph;
    int N;
    
    public int[] sumOfDistancesInTree(int N, int[][] edges) {
        this.N = N;
        graph = new ArrayList<Set<Integer>>();
        ans = new int[N];
        count = new int[N];
        Arrays.fill(count, 1);
        
        for (int i = 0; i < N; i++) 
            graph.add(new HashSet<Integer>());
        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }
        dfs(0, -1);
        dfs2(0, -1);
        return ans;
    }
    
    private void dfs(int node, int parent) {
        for (int child :graph.get(node)) {
            if (child != parent) {
                dfs(child, node);
                count[node] += count[child];
                ans[node] += ans[child] + count[child];
            }
        }
    }
    
    private void dfs2(int node, int parent) {
        for (int child : graph.get(node)) {
            if (child != parent) {
                ans[child] = ans[node] - count[child] + N - count[child];
                dfs2(child, node);
            }
        }
    }
}


# 20ms 99.16%
class Solution {
    public int[] sumOfDistancesInTree(int N, int[][] edges) {
        List<Integer>[] graph = new List[N];
        for (int i = 0; i < N; i++) graph[i] = new ArrayList();
        for (int[] edge: edges) {
            graph[edge[0]].add(edge[1]);
            graph[edge[1]].add(edge[0]);
        }
        int[] count = new int[N], sum = new int[N];
        boolean[] visited = new boolean[N];
        
        int center = 0;
        visited[center] = true;
        dfs(center, count, sum, visited, graph);
        
        // dfs2
        Arrays.fill(visited, false);
        visited[center] = true;
        int[] sumOfDist = new int[N]; 
        sumOfDist[center] = sum[center];
        for(int ne: graph[center]) {
            visited[ne] = true;
            dfs2(ne, sum[center], count[center], sumOfDist, count, sum, visited, graph);
        }
        return sumOfDist;    
    }
    
    private int[] dfs(int st, int[] count, int[] sums, boolean[] visited, List<Integer>[] graph) {
        int cnt = 0, sum = 0;
        for (int ne : graph[st]) {
            if (!visited[ne]) {
                visited[ne] = true;
                int[] res = dfs(ne, count, sums, visited, graph);
                cnt += res[0];
                sum += res[1];
            }
        }
        count[st] = cnt + 1;
        sums[st] = sum + cnt;
        return new int[]{count[st], sums[st]};
    }
    
    private void dfs2(int node, int csum, int ccnt, int[] sumOfDist, int[] count, int[] sum, boolean[] visited, List<Integer>[] graph) {
        sumOfDist[node] = csum + ccnt - 2 * count[node];
        for (int ne : graph[node]) {
            if (!visited[ne]) {
                visited[ne] = true;
                dfs2(ne, sumOfDist[node], ccnt, sumOfDist, count, sum, visited, graph);
            }
        }
    }
}

'''
