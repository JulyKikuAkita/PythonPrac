__source__ = 'https://leetcode.com/problems/loud-and-rich/'
# Time:  O(N)
# Space: O(N)
#
# Description: Leetcode # 851. Loud and Rich
#
# In a group of N people (labelled 0, 1, 2, ..., N-1),
# each person has different amounts of money, and different levels of quietness.
#
# For convenience, we'll call the person with label x, simply "person x".
#
# We'll say that richer[i] = [x, y] if person x definitely has more money than person y.
# Note that richer may only be a subset of valid observations.
#
# Also, we'll say quiet[x] = q if person x has quietness q.
#
# Now, return answer, where answer[x] = y if y is the least quiet person
# (that is, the person y with the smallest value of quiet[y]),
# among all people who definitely have equal to or more money than person x.
#
# Example 1:
#
# Input: richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]
# Output: [5,5,2,5,4,5,6,7]
# Explanation:
# answer[0] = 5.
# Person 5 has more money than 3, which has more money than 1, which has more money than 0.
# The only person who is quieter (has lower quiet[x]) is person 7, but
# it isn't clear if they have more money than person 0.
#
# answer[7] = 7.
# Among all people that definitely have equal to or more money than person 7
# (which could be persons 3, 4, 5, 6, or 7), the person who is the quietest (has lower quiet[x])
# is person 7.
#
# The other answers can be filled out with similar reasoning.
# Note:
#
# 1 <= quiet.length = N <= 500
# 0 <= quiet[i] < N, all quiet[i] are different.
# 0 <= richer.length <= N * (N-1) / 2
# 0 <= richer[i][j] < N
# richer[i][0] != richer[i][1]
# richer[i]'s are all different.
# The observations in richer are all logically consistent.
#
import unittest
# 84ms 90.79%
class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        N = len(quiet)
        graph = [[] for _ in xrange(N)]
        for u, v in richer:
            graph[v].append(u)

        answer = [None] * N
        def dfs(node):
            #Want least quiet person in this subtree
            if answer[node] is None:
                answer[node] = node
                for child in graph[node]:
                    cand = dfs(child)
                    if quiet[cand] < quiet[answer[node]]:
                        answer[node] = cand
            return answer[node]

        return map(dfs, range(N))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/loud-and-rich/solution/
#
Approach #1: Cached Depth-First Search [Accepted]
Complexity Analysis
Time Complexity: O(N), where N is the number of people.
Space Complexity: O(N), the space used by the answer, and the implicit call stack of dfs.

# Consider the directed graph with edge x -> y if y is richer than x.
# For each person x, we want the quietest person in the subtree at x.
# 17ms 73.38%
class Solution {
    ArrayList<Integer>[] graph;
    int[] answer;
    int[] quiet;

    public int[] loudAndRich(int[][] richer, int[] quiet) {
        int N = quiet.length;
        graph = new ArrayList[N];
        answer = new int[N];
        this.quiet = quiet;
        
        for (int node = 0; node < N; node++) {
            graph[node] = new ArrayList<Integer>();
        }
        
        for (int[] edge : richer) {
            graph[edge[1]].add(edge[0]);
        }
        
        Arrays.fill(answer, -1);

        for (int node = 0; node < N; ++node)
            dfs(node);
        return answer;
    }
    
    private int dfs(int node) {
        if (answer[node] == -1) {
            answer[node] = node;
            for (int child : graph[node]) {
                int cand = dfs(child);
                if (quiet[cand] < quiet[answer[node]])
                    answer[node] = cand;
            }
        }
        return answer[node];
    }
}

# 7ms 99.62%
class Solution {
    public int[] loudAndRich(int[][] richer, int[] quiet) {
        int[] res = new int[quiet.length];
        for (int i = 0; i < res.length; i++) res[i] = i;
        while (true) {
            boolean changed = false;
            for (int[] r : richer) {
                if (quiet[res[r[0]]] < quiet[res[r[1]]]) {
                    res[r[1]] = res[r[0]];
                    changed = true;
                }
            }
            if (!changed) break;
        }
        return res;
    }
}
'''
