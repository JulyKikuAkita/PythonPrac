__source__ = 'https://leetcode.com/problems/sliding-puzzle/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 773. Sliding Puzzle
#
# On a 2x3 board, there are 5 tiles represented by the integers 1 through 5,
# and an empty square represented by 0.
#
# A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.
#
# The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].
#
# Given a puzzle board, return the least number of moves required so that the state of the board is solved.
# If it is impossible for the state of the board to be solved, return -1.
#
# Examples:
#
# Input: board = [[1,2,3],[4,0,5]]
# Output: 1
# Explanation: Swap the 0 and the 5 in one move.
# Input: board = [[1,2,3],[5,4,0]]
# Output: -1
# Explanation: No number of moves will make the board solved.
# Input: board = [[4,1,2],[5,0,3]]
# Output: 5
# Explanation: 5 is the smallest number of moves that solves the board.
# An example path:
# After move 0: [[4,1,2],[5,0,3]]
# After move 1: [[4,1,2],[0,5,3]]
# After move 2: [[0,1,2],[4,5,3]]
# After move 3: [[1,0,2],[4,5,3]]
# After move 4: [[1,2,0],[4,5,3]]
# After move 5: [[1,2,3],[4,5,0]]
# Input: board = [[3,2,4],[1,5,0]]
# Output: 14
# Note:
#
# board will be a 2 x 3 array as described above.
# board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].
#
import unittest
import collections
import itertools
# 36ms 83.75%
class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        R, C = len(board), len(board[0])
        start = tuple(itertools.chain(*board))
        queue = collections.deque([(start, start.index(0), 0)])
        seen = {start}

        target = tuple(range(1, R*C) + [0])

        while queue:
            board, posn, depth = queue.popleft()
            if board == target: return depth
            for d in (-1, 1, -C, C):
                nei = posn + d
                if abs(nei/C - posn/C) + abs(nei%C - posn%C) != 1:
                    continue
                if 0 <= nei < R*C:
                    newboard = list(board)
                    newboard[posn], newboard[nei] = newboard[nei], newboard[posn]
                    newt = tuple(newboard)
                    if newt not in seen:
                        seen.add(newt)
                        queue.append((newt, nei, depth+1))
        return -1

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/sliding-puzzle/solution/
#
Approach #1: Breadth-First Search [Accepted]
Complexity Analysis
Time Complexity: O(R * C * (R * C)!), where R, C are the number of rows and columns in board.
There are O((R * C)!) possible board states.
Space Complexity: O(R * C * (R * C)!).

# 28ms 23.89%
class Solution {
    public int slidingPuzzle(int[][] board) {
        int R = board.length, C = board[0].length;
        int sr = 0, sc = 0;
        search:
            for (sr = 0; sr < R; sr++)
                for (sc = 0; sc < C; sc++)
                    if (board[sr][sc] == 0)
                        break search;

        int[][] directions = new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        Queue<Node> queue = new ArrayDeque();
        Node start = new Node(board, sr, sc, 0);
        queue.add(start);

        Set<String> seen = new HashSet();
        seen.add(start.boardstring);

        String target = Arrays.deepToString(new int[][]{{1,2,3}, {4,5,0}});

        while (!queue.isEmpty()) {
            Node node = queue.remove();
            if (node.boardstring.equals(target))
                return node.depth;

            for (int[] di: directions) {
                int nei_r = di[0] + node.zero_r;
                int nei_c = di[1] + node.zero_c;

                if ((Math.abs(nei_r - node.zero_r) + Math.abs(nei_c - node.zero_c) != 1) ||
                        nei_r < 0 || nei_r >= R || nei_c < 0 || nei_c >= C)
                    continue;

                int[][] newboard = new int[R][C];
                int t = 0;
                for (int[] row: node.board)
                    newboard[t++] = row.clone();
                newboard[node.zero_r][node.zero_c] = newboard[nei_r][nei_c];
                newboard[nei_r][nei_c] = 0;

                Node nei = new Node(newboard, nei_r, nei_c, node.depth+1);
                if (seen.contains(nei.boardstring))
                    continue;
                queue.add(nei);
                seen.add(nei.boardstring);
            }
        }

        return -1;
    }
}

class Node {
    int[][] board;
    String boardstring;
    int zero_r;
    int zero_c;
    int depth;
    Node(int[][] B, int r, int c, int d) {
        board = B;
        boardstring = Arrays.deepToString(board);
        zero_r = r;
        zero_c = c;
        depth = d;
    }
}


Approach #2: A* Search [Accepted]
Complexity Analysis
Time Complexity: O(R * C * (R * C)!), where R, C are the number of rows and columns in board.
Tighter bounds are possible, but difficult to prove. (In testing with random permutations of a 3x3 board,
 about 50 times less nodes were searched compared to breadth-first-search.)
Space Complexity: O(R * C * (R * C)!).

# 84ms 6.99%
class Solution {
    public int slidingPuzzle(int[][] board) {
        int R = board.length, C = board[0].length;
        int sr = 0, sc = 0;

        //Find sr, sc
        search:
            for (sr = 0; sr < R; sr++)
                for (sc = 0; sc < C; sc++)
                    if (board[sr][sc] == 0)
                        break search;

        int[][] directions = new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        PriorityQueue<Node> heap = new PriorityQueue<Node>((a, b) ->
            (a.heuristic + a.depth) - (b.heuristic + b.depth));
        Node start = new Node(board, sr, sc, 0);
        heap.add(start);

        Map<String, Integer> cost = new HashMap();
        cost.put(start.boardstring, 9999999);

        String target = Arrays.deepToString(new int[][]{{1,2,3}, {4,5,0}});
        String targetWrong = Arrays.deepToString(new int[][]{{1,2,3}, {5,4,0}});

        while (!heap.isEmpty()) {
            Node node = heap.poll();
            if (node.boardstring.equals(target))
                return node.depth;
            if (node.boardstring.equals(targetWrong))
                return -1;
            if (node.depth + node.heuristic > cost.get(node.boardstring))
                continue;

            for (int[] di: directions) {
                int nei_r = di[0] + node.zero_r;
                int nei_c = di[1] + node.zero_c;

                // If the neighbor is not on the board or wraps incorrectly around rows/cols
                if ((Math.abs(nei_r - node.zero_r) + Math.abs(nei_c - node.zero_c) != 1) ||
                        nei_r < 0 || nei_r >= R || nei_c < 0 || nei_c >= C)
                    continue;

                int[][] newboard = new int[R][C];
                int t = 0;
                for (int[] row: node.board)
                    newboard[t++] = row.clone();

                // Swap the elements on the new board
                newboard[node.zero_r][node.zero_c] = newboard[nei_r][nei_c];
                newboard[nei_r][nei_c] = 0;

                Node nei = new Node(newboard, nei_r, nei_c, node.depth+1);
                if (nei.depth + nei.heuristic >= cost.getOrDefault(nei.boardstring, 9999999))
                    continue;
                heap.add(nei);
                cost.put(nei.boardstring, nei.depth + nei.heuristic);
            }
        }

        return -1;
    }
}

class Node {
    int[][] board;
    String boardstring;
    int heuristic;
    int zero_r;
    int zero_c;
    int depth;
    Node(int[][] B, int zr, int zc, int d) {
        board = B;
        boardstring = Arrays.deepToString(board);

        //Calculate heuristic
        heuristic = 0;
        int R = B.length, C = B[0].length;
        for (int r = 0; r < R; ++r)
            for (int c = 0; c < C; ++c) {
                if (board[r][c] == 0) continue;
                int v = (board[r][c] + R*C - 1) % (R*C);
                // v/C, v%C: where board[r][c] should go in a solved puzzle
                heuristic += Math.abs(r - v/C) + Math.abs(c - v%C);
            }
        heuristic /= 2;
        zero_r = zr;
        zero_c = zc;
        depth = d;
    }
}

# 12ms 53.26%
class Solution {
    public int slidingPuzzle(int[][] board) {
        String target = "123450";
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 2; i++)
            for (int j = 0; j < 3; j++)
                sb.append(board[i][j]);
        String s = sb.toString();
        Set<String> seen = new HashSet<>();
        Queue<String> q = new LinkedList<>();
        q.offer(s);
        seen.add(s);
        int ans = 0;
        int[] dirs = new int[] {1, -1, 3, -3};
        while (!q.isEmpty()) {
            for (int size = q.size(); size > 0; size--) {
                String cur = q.poll();
                if (cur.equals(target)) return ans;
                int i = cur.indexOf('0');
                for (int inx = 0; inx < 4; inx++) {
                    int j = i + dirs[inx];
                    if (j < 0 || j > 5 || i == 2 && j == 3 || i == 3 && j == 2) continue;
                    char[] chs = cur.toCharArray();
                    char tmp = chs[i];
                    chs[i] = chs[j];
                    chs[j] = tmp;
                    String str = new String(chs);
                    if (seen.add(str)) q.offer(str);
                }
            }
            ans++;
        }
        return -1;
    }
}

# 9ms 75.03%
class Solution {
    public int slidingPuzzle(int[][] board) {
        String target = "123450";
        String start = "";
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                start += board[i][j];
            }
        }
        int[][] dirs = new int[][]{{1, 3}, {0, 2, 4}, {1, 5}, {0, 4}, {1, 3, 5}, {2, 4}};
        Deque<String> queue = new LinkedList();
        Set<String> visit = new HashSet();
        queue.offerLast(start);
        visit.add(start);
        int res = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0 ; i < size; i++) {
                String cur = queue.pollFirst();
                if (cur.equals(target)) return res;

                int zero = cur.indexOf('0');
                for (int dir : dirs[zero]) {
                    String nei = swap(cur, zero, dir);
                    if (visit.add(nei)) queue.offer(nei);
                }
            }
            res++;
        }
        return -1;
    }

    private String swap(String input, int i, int j) {
        char[] arr = input.toCharArray();
        char tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
        return new String(arr);
    }
}

'''
