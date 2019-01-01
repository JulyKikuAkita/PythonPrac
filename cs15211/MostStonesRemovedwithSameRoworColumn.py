# coding=utf-8
__source__ = 'https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 947. Most Stones Removed with Same Row or Column
#
# On a 2D plane, we place stones at some integer coordinate points.
# Each coordinate point may have at most one stone.
#
# Now, a move consists of removing a stone that shares a column or row with another stone on the grid.
#
# What is the largest possible number of moves we can make?
#
# Example 1:
#
# Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# Output: 5
#
# Example 2:
#
# Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
# Output: 3
#
# Example 3:
#
# Input: stones = [[0,0]]
# Output: 0
#
# Note:
#
#     1 <= stones.length <= 1000
#     0 <= stones[i][j] < 10000
#
import unittest

# Union find
# 60ms 86.85%
class DSU:
    def __init__(self, N):
        self.p = range(N)

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr

class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        N = len(stones)
        dsu = DSU(20000)
        for x, y in stones:
            dsu.union(x, y + 10000)

        return N - len({dsu.find(x) for x, y in stones})

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/solution/
#
Approach 1: Depth-First Search
Complexity Analysis
Time Complexity: O(N^2), where N is the length of stones.
Space Complexity: O(N^2)

# 35ms 50.91%
class Solution {
    public int removeStones(int[][] stones) {
        int N = stones.length;
        // graph[i][0] = the length of the 'list' graph[i][1:]
        int[][] graph = new int[N][N];
        for (int i = 0; i < N; ++i)
            for (int j = i+1; j < N; ++j)
                if (stones[i][0] == stones[j][0] || stones[i][1] == stones[j][1]) {
                    graph[i][++graph[i][0]] = j;
                    graph[j][++graph[j][0]] = i;
                }
        int ans = 0;
        boolean[] seen = new boolean[N];
        for (int i = 0; i < N; ++i) {
            if (!seen[i]) {
                Stack<Integer> stack = new Stack();
                stack.push(i);
                seen[i] = true;
                ans--;
                while (!stack.isEmpty()) {
                    int node = stack.pop();
                    ans++;
                    for (int k = 1; k <= graph[node][0]; ++k) {
                        int nei = graph[node][k];
                        if (!seen[nei]) {
                            stack.push(nei);
                            seen[nei] = true;
                        }
                    }
                }
            }
        }
        return ans;
    }
}

Approach 2: Union-Find
Complexity Analysis
Time Complexity: O(Nlog⁡N), where N is the length of stones. 
(If we used union-by-rank, this can be O(N * α(N)), where alphaα is the Inverse-Ackermann function.)
Space Complexity: O(N)

# 17ms 83.39%
class Solution {
    public int removeStones(int[][] stones) {
        int N = stones.length;
        DSU dsu = new DSU(20000);
        for (int[] stone: stones)
            dsu.union(stone[0], stone[1] + 10000);

        Set<Integer> seen = new HashSet();
        for (int[] stone: stones)
            seen.add(dsu.find(stone[0]));
        return N - seen.size();
    }
}

class DSU {
    int[] parent;
    
    public DSU(int N) {
        parent = new int[N];
        for (int i = 0; i < N; ++i)
            parent[i] = i;
    }
    
    public int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    
    public void union(int x, int y) {
        parent[find(x)] = find(y);
    }
}

'''
