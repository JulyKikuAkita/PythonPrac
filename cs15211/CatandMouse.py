__source__ = 'https://leetcode.com/problems/cat-and-mouse/'
# Time:  O(N^3)
# Space: O(N^2)
#
# Description: Leetcode # 913. Cat and Mouse
#
# A game on an undirected graph is played by two players, Mouse and Cat, who alternate turns.
#
# The graph is given as follows: graph[a] is a list of all nodes b such that ab is an edge of the graph.
#
# Mouse starts at node 1 and goes first, Cat starts at node 2 and goes second, and there is a Hole at node 0.
#
# During each player's turn, they must travel along one edge of the graph that meets where they are.
# For example, if the Mouse is at node 1, it must travel to any node in graph[1].
#
# Additionally, it is not allowed for the Cat to travel to the Hole (node 0.)
#
# Then, the game can end in 3 ways:
#
# If ever the Cat occupies the same node as the Mouse, the Cat wins.
# If ever the Mouse reaches the Hole, the Mouse wins.
# If ever a position is repeated (ie. the players are in the same position as a previous turn,
# and it is the same player's turn to move), the game is a draw.
# Given a graph, and assuming both players play optimally, return 1 if the game is won by Mouse,
# 2 if the game is won by Cat, and 0 if the game is a draw.
#
#
#
# Example 1:
#
# Input: [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
# Output: 0
# Explanation:
# 4---3---1
# |   |
# 2---5
#  \ /
#   0
#
#
# Note:
#
# 3 <= graph.length <= 50
# It is guaranteed that graph[1] is non-empty.
# It is guaranteed that graph[2] contains a non-zero element.
#
import unittest
import collections
# 484ms 11.11%
class Solution(object):
    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        N = len(graph)

        # What nodes could play their turn to
        # arrive at node (m, c, t) ?
        def parents(m, c, t):
            if t == 2:
                for m2 in graph[m]:
                    yield m2, c, 3-t
            else:
                for c2 in graph[c]:
                    if c2:
                        yield m, c2, 3-t

        DRAW, MOUSE, CAT = 0, 1, 2
        color = collections.defaultdict(int)

        # degree[node] : the number of neutral children of this node
        degree = {}
        for m in xrange(N):
            for c in xrange(N):
                degree[m,c,1] = len(graph[m])
                degree[m,c,2] = len(graph[c]) - (0 in graph[c])

        # enqueued : all nodes that are colored
        queue = collections.deque([])
        for i in xrange(N):
            for t in xrange(1, 3):
                color[0, i, t] = MOUSE
                queue.append((0, i, t, MOUSE))
                if i > 0:
                    color[i, i, t] = CAT
                    queue.append((i, i, t, CAT))

        # percolate
        while queue:
            # for nodes that are colored :
            i, j, t, c = queue.popleft()
            # for every parent of this node i, j, t :
            for i2, j2, t2 in parents(i, j, t):
                # if this parent is not colored :
                if color[i2, j2, t2] is DRAW:
                    # if the parent can make a winning move (ie. mouse to MOUSE), do so
                    if t2 == c: # winning move
                        color[i2, j2, t2] = c
                        queue.append((i2, j2, t2, c))
                    # else, this parent has degree[parent]--, and enqueue if all children
                    # of this parent are colored as losing moves
                    else:
                        degree[i2, j2, t2] -= 1
                        if degree[i2, j2, t2] == 0:
                            color[i2, j2, t2] = 3 - t2
                            queue.append((i2, j2, t2, 3 - t2))

        return color[1, 2, 1]
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/cat-and-mouse/solution/
Approach 1: Minimax / Percolate from Resolved States
Complexity Analysis
Time Complexity: O(N^3), where N is the number of nodes in the graph. There are O(N^2) states,
and each state has an outdegree of N, as there are at most N different moves.
Space Complexity: O(N^2)

# 45ms 34.14%
class Solution {
    public int catMouseGame(int[][] graph) {
        int N = graph.length;
        final int DRAW = 0, MOUSE = 1, CAT = 2;

        int[][][] color = new int[50][50][3];
        int[][][] degree = new int[50][50][3];

        // degree[node] : the number of neutral children of this node
        for (int m = 0; m < N; ++m)
            for (int c = 0; c < N; ++c) {
                degree[m][c][1] = graph[m].length;
                degree[m][c][2] = graph[c].length;
                for (int x: graph[c]) if (x == 0) {
                    degree[m][c][2]--;
                    break;
                }
            }

        // enqueued : all nodes that are colored
        Queue<int[]> queue = new LinkedList();
        for (int i = 0; i < N; ++i)
            for (int t = 1; t <= 2; ++t) {
                color[0][i][t] = MOUSE;
                queue.add(new int[]{0, i, t, MOUSE});
                if (i > 0) {
                    color[i][i][t] = CAT;
                    queue.add(new int[]{i, i, t, CAT});
                }
            }

        // percolate
        while (!queue.isEmpty()) {
            // for nodes that are colored :
            int[] node = queue.remove();
            int i = node[0], j = node[1], t = node[2], c = node[3];
            // for every parent of this node i, j, t :
            for (int[] parent: parents(graph, i, j, t)) {
                int i2 = parent[0], j2 = parent[1], t2 = parent[2];
                // if this parent is not colored :
                if (color[i2][j2][t2] == DRAW) {
                    // if the parent can make a winning move (ie. mouse to MOUSE), do so
                    if (t2 == c) {
                        color[i2][j2][t2] = c;
                        queue.add(new int[]{i2, j2, t2, c});
                    } else {
                        // else, this parent has degree[parent]--, and enqueue
                        // if all children of this parent are colored as losing moves
                        degree[i2][j2][t2]--;
                        if (degree[i2][j2][t2] == 0) {
                            color[i2][j2][t2] = 3 - t2;
                            queue.add(new int[]{i2, j2, t2, 3 - t2});
                        }
                    }
                }
            }
        }

        return color[1][2][1];
    }

    // What nodes could play their turn to
    // arrive at node (m, c, t) ?
    public List<int[]> parents(int[][] graph, int m, int c, int t) {
        List<int[]> ans = new ArrayList();
        if (t == 2) {
            for (int m2: graph[m])
                ans.add(new int[]{m2, c, 3-t});
        } else {
            for (int c2: graph[c]) if (c2 > 0)
                ans.add(new int[]{m, c2, 3-t});
        }
        return ans;
    }
}

# 5ms 92.77%
class Solution {
    public int catMouseGame(int[][] graph) {
        int size = graph.length;
        int dp[][] = new int[size][size];
        for (int i = 0; i < size; i++) Arrays.fill(dp[i], -1);

        for (int i = 0; i < size; ++i) {
            dp[i][i] = 2;
            dp[0][i] = 1;   // mouse reached home, m win
             // cat met mouse, cat win
        }

        return helper(graph, 1, 2, dp);
    }

    public int helper(int[][] graph, int mouse, int cat, int dp[][]) {

        if (dp[mouse][cat] != -1) return dp[mouse][cat];  // use cached value

        dp[mouse][cat] = 0;  // if there is a cycle, draw
        int mouseDefault = 2;  //  default cat win, try to update this number to 1 or 0
        int[] mouseGoList = graph[mouse], catGoList = graph[cat];

        for (int mouseGo : mouseGoList) {
            if (mouseGo == cat) continue;   // I'm a mouse, why go for a cat?

            int catDefault = 1;  //  default mouse win, try to update this number to 2 or 0
            for (int catGo : catGoList) {
                if (catGo == 0) continue;  // cannot go to hole
                int next = helper(graph, mouseGo, catGo, dp);
                if (next == 2) {   // if cat win in this path, no need to continue
                    catDefault = 2;
                    break;
                }
                if (next == 0) {   // at least it's a draw
                    catDefault = 0;
                }
            }
            if (catDefault == 1) {  // if mouse can win in this path, no need to continue
                mouseDefault = 1;
                break;
            }
            if (catDefault == 0) {  // at least it's a draw
                mouseDefault = 0;
            }
        }
        dp[mouse][cat] = mouseDefault;
        return dp[mouse][cat];
    }
}
'''