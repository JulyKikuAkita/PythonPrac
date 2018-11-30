import collections

__source__ = 'https://leetcode.com/problems/snakes-and-ladders/'
# Time:  O(N^2)
# Space: O(N^2)
#
# Description: Leetcode # 909. Snakes and Ladders
#
# # On an N x N board,
# the numbers from 1 to N*N are written boustrophedonically starting from the bottom left of the board,
# and alternating direction each row.  For example, for a 6 x 6 board, the numbers are written as follows:
#
# You start on square 1 of the board (which is always in the last row and first column).
# Each move, starting from square x, consists of the following:
#
# You choose a destination square S with number x+1, x+2, x+3, x+4, x+5, or x+6, provided this number is <= N*N.
# (This choice simulates the result of a standard 6-sided die roll: ie., there are always at most 6 destinations.)
# If S has a snake or ladder, you move to the destination of that snake or ladder.  Otherwise, you move to S.
# A board square on row r and column c has a "snake or ladder" if board[r][c] != -1.
# The destination of that snake or ladder is board[r][c].
#
# Note that you only take a snake or ladder at most once per move:
# if the destination to a snake or ladder is the start of another snake or ladder,
# you do not continue moving.  (For example, if the board is `[[4,-1],[-1,3]]`,
# and on the first move your destination square is `2`,
# then you finish your first move at `3`, because you do not continue moving to `4`.)
#
# Return the least number of moves required to reach square N*N.  If it is not possible, return -1.
#
# Example 1:
#
# Input: [
# [-1,-1,-1,-1,-1,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,35,-1,-1,13,-1],
# [-1,-1,-1,-1,-1,-1],
# [-1,15,-1,-1,-1,-1]]
# Output: 4
# Explanation:
# At the beginning, you start at square 1 [at row 5, column 0].
# You decide to move to square 2, and must take the ladder to square 15.
# You then decide to move to square 17 (row 3, column 5), and must take the snake to square 13.
# You then decide to move to square 14, and must take the ladder to square 35.
# You then decide to move to square 36, ending the game.
# It can be shown that you need at least 4 moves to reach the N*N-th square, so the answer is 4.
# Note:
#
# 2 <= board.length = board[0].length <= 20
# board[i][j] is between 1 and N*N or is equal to -1.
# The board square with number 1 has no snake or ladder.
# The board square with number N*N has no snake or ladder.
#
import unittest

# 44ms 97.37%
class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        m, n = len(board), len(board[0])
        line, flip = [0], 0
        for i in xrange(m-1, -1, -1):
            if flip:
                temp = board[i][::-1]
            else:
                temp = board[i]

            line += temp
            flip = flip ^ 1


        q = collections.deque([(1, 0)])
        visited = set([1])
        target = m*n
        while q:
            node, hop = q.popleft()

            for move in xrange(1, 7):
                nextloc = node + move

                if nextloc < len(line) and line[nextloc] != -1:
                    nextloc = line[nextloc]

                if nextloc < len(line) and nextloc not in visited:
                    visited.add(nextloc)
                    q.append((nextloc, hop+1))
                    if nextloc == target: return hop+1

        return -1

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/snakes-and-ladders/solution/
# Approach 1: Breadth-First Search
# Complexity Analysis
# Time Complexity: O(N^2), where N is the length of the board.
# Space Complexity: O(N^2)
#

#24ms 56.68%
class Solution {
    public int snakesAndLadders(int[][] board) {
        int N = board.length;
        Map<Integer, Integer> dist = new HashMap();
        dist.put(1, 0);
        Queue<Integer> queue = new LinkedList();
        queue.add(1);

        while (!queue.isEmpty()) {
            int s = queue.remove();
            if (s == N * N) return dist.get(s);

            for (int s2 = s + 1; s2 <= Math.min(s + 6, N * N); ++s2) {
                int rc = get(s2, N);
                int r = rc / N, c = rc % N;
                int s2Final = board[r][c] == -1 ? s2 : board[r][c];
                if (!dist.containsKey(s2Final)) {
                    dist.put(s2Final, dist.get(s) + 1);
                    queue.add(s2Final);
                }
            }
        }
        return -1;
    }

    public int get(int s, int N) {
        // Given a square num s, return board coordinates (r, c) as r*N + c
        int quot = (s - 1) / N;
        int rem = (s - 1) % N;
        int row = N - 1 - quot;
        int col = row % 2 != N % 2 ? rem : N - 1 - rem;
        return row * N + col;
    }
}


# 10ms 100%  # not quite understand tho...
class Solution {
    public int snakesAndLadders(int[][] board) {
        int N = board.length;
        int target = N * N ;
        int res = 1;
        int[] bd = new int[target+1];
        boolean[] visited = new boolean[target+1];
        //mapping value at board to a tmp array
        for( int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                bd[getIndex(N, i, j)] = board[i][j];
            }
        }

        LinkedList<Integer> queue = new LinkedList<>();
        queue.add(1);
        while(!queue.isEmpty()){
            int n = queue.size();
            for (int i = 0 ; i < n; i++) {
                int x = queue.removeFirst();
                visited[x] = true;
                for (int k = 1; k < 7; k++) { //move 1- 6 steps
                    if (x + k == target || bd[x + k] == target) return res;
                    if (bd[x + k] > 0 && !visited[bd[x + k]]) queue.add(bd[x + k]);
                }
                int m = 6;
                while (m > 0 && bd[x + m] > 0) m--;
                if (m > 0 && !visited[x + m]) queue.add(x + m);
            }
            res++;
            if (res >= target) return -1;
        }

        return -1;
    }

    private int getIndex(int n, int i, int j) {
        if ((n - 1 - i) % 2 == 0) return ((n - 1 - i) * n + 1 + j);
        else
            return ((n - 1 - i) * n + n - j);
    }
}
'''