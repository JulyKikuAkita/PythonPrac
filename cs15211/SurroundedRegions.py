__source__ = 'https://leetcode.com/problems/surrounded-regions/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/surrounded-regions.py
# Time:  O(m * n)
# Space: O(m + n)
# BFS (DFS OT)
# Flood fill
#
# Description: Leetcode #  130. Surrounded Regions
#
# Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
# For example,
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:
#
# X X X X
# X X X X
# X X X X
# X O X X
#
# Related Topics
# Breadth-first Search Union Find
# Similar Questions
# Number of Islands Walls and Gates

import unittest
class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if not board:
            return
        current = []

        # list all (x,y) at the outer most side :up and down
        for i in xrange(len(board)):
            current.append((i, 0))
            current.append((i, len(board[0]) - 1))

        # list all (x,y) at the outer most side : left and right
        for i in xrange(len(board[0])):
            current. append((0, i))
            current.append((len(board) - 1, i))

        while current:
            (i, j) = current.pop()
            if board[i][j] in ['O', 'V']:
                board[i][j] = 'V'
                for  x, y in [(i + 1, j) , (i - 1, j), (i, j +1), (i, j - 1)]:
                    if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == 'O':
                        board[x][y] = 'V'
                        current.append((x, y))

        # go through board to make all 'V' to 'X'
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] != 'V':
                    board[i][j] = 'X'
                else:
                    board[i][j] = 'O'

#OT
class SolutionFloodFillDFS:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    dir = (0,1), (0,-1), (1,0), (-1,0)
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        dict = {}
        for i in xrange(len(board)):
            for j in (0, len(board[0]) - 1):
             if board[i][j] == "O":
                 self.dfs(board, i, j, dict)


        for p in xrange(len(board[0])):
            for q in (0, len(board) - 1):
             if board[q][p] == "O":
                 self.dfs(board, q, p, dict)

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == "N":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

    def dfs(self, board, i, j, dict):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == "X" or board[i][j] == "N":
            return
        if board[i][j] == "O":
            board[i][j] = "N"
        for d in self.dir:
            x = i + d[0]
            y = j + d[1]
            self.dfs(board, x, y, dict)
#test
board = [['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        test = SolutionFloodFillDFS()
        #Solution().solve(board)
        #SolutionJavaDFS().solve(board)
        #SolutionJavaBFS().solve(board)
        SolutionFloodFillDFS().solve(board)
        for i in xrange(len(board[0])):
            print board[i]

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/contains-duplicate/solution/

# 43.77% 9ms
public class Solution {
    public static final int[][] DIRECTIONS = new int[][] {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    public void solve(char[][] board) {
        if (board.length == 0 || board[0].length == 0) {
            return;
        }
        int m = board.length;
        int n = board[0].length;
        for (int j = 0; j < n; j++) {
            fillBoarder(board, 0, j);
            fillBoarder(board, m - 1, j);
        }
        for (int i = 1; i < m - 1; i++) {
            fillBoarder(board, i, 0);
            fillBoarder(board, i, n - 1);
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == '#') {
                    board[i][j] = 'O';
                } else {
                    board[i][j] = 'X';
                }
            }
        }
    }
// ArrayDeque > LinkedList
private void fillBoarder(char[][] board, int row, int col){
        if(board[row][col] != 'O'){
            return;
        }
        Queue<Integer> rowQueue = new ArrayDeque<>();
        Queue<Integer> colQueue = new ArrayDeque<>();

        rowQueue.offer(row);
        colQueue.offer(col);
        board[row][col] = '#';
        while(!rowQueue.isEmpty()){
            int curRow = rowQueue.poll();
            int curCol = colQueue.poll();
            for(int[] dir : DIRECTIONS){
                int p = curRow + dir[0];
                int q = curCol + dir[1];
                if( p >= 0 && p < board.length && q >=0 && q< board[0].length && board[p][q] == 'O'){
                    board[p][q] = '#';
                    rowQueue.offer(p);
                    colQueue.offer(q);
                }
            }
        }
    }
}

# Java DFS + boundary cell turning solution
# 58.28% 6MS
public class Solution {
    public void solve(char[][] board) {
        if (board.length == 0 || board[0].length == 0)
            return;
        if (board.length < 2 || board[0].length < 2)
            return;
        int m = board.length, n = board[0].length;
        //Any 'O' connected to a boundary can't be turned to 'X', so ...
        //Start from first and last column, turn 'O' to '*'.
        for (int i = 0; i < m; i++) {
            if (board[i][0] == 'O')
                boundaryDFS(board, i, 0);
            if (board[i][n-1] == 'O')
                boundaryDFS(board, i, n-1);
        }
        //Start from first and last row, turn '0' to '*'
        for (int j = 0; j < n; j++) {
            if (board[0][j] == 'O')
                boundaryDFS(board, 0, j);
            if (board[m-1][j] == 'O')
                boundaryDFS(board, m-1, j);
        }
        //post-prcessing, turn 'O' to 'X', '*' back to 'O', keep 'X' intact.
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O')
                    board[i][j] = 'X';
                else if (board[i][j] == '*')
                    board[i][j] = 'O';
            }
        }
    }
    //Use DFS algo to turn internal however boundary-connected 'O' to '*';
    private void boundaryDFS(char[][] board, int i, int j) {
        if (i < 0 || i > board.length - 1 || j <0 || j > board[0].length - 1)
            return;
        if (board[i][j] == 'O')
            board[i][j] = '*';
        if (i > 1 && board[i-1][j] == 'O')
            boundaryDFS(board, i-1, j);
        if (i < board.length - 2 && board[i+1][j] == 'O')
            boundaryDFS(board, i+1, j);
        if (j > 1 && board[i][j-1] == 'O')
            boundaryDFS(board, i, j-1);
        if (j < board[i].length - 2 && board[i][j+1] == 'O' )
            boundaryDFS(board, i, j+1);
    }
}

#BFS
# 37.72% 10ms
public class Solution {
    private static final int[][] DIRECTIONS = new int[][] {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};

    public void solve(char[][] board) {
        int m = board.length;
        int n = m == 0 ? 0 : board[0].length;
        if (m == 0 || n == 0) {
            return;
        }
        for (int i = 0; i < m; i++) {
            if (board[i][0] == 'O') {
                bfs(board, m, n, i, 0);
            }
            if (board[i][n - 1] == 'O') {
                bfs(board, m, n, i, n - 1);
            }
        }
        for (int j = 1; j < n - 1; j++) {
            if (board[0][j] == 'O') {
                bfs(board, m, n, 0, j);
            }
            if (board[m - 1][j] == 'O') {
                bfs(board, m, n, m - 1, j);
            }
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == '#') {
                    board[i][j] = 'O';
                } else if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                }
            }
        }
    }

    private void bfs(char[][] board, int m, int n, int i, int j) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(i * n + j);
        board[i][j] = '#';
        while (!queue.isEmpty()) {
            int cur = queue.poll();
            int row = cur / n;
            int col = cur % n;
            for (int[] direction : DIRECTIONS) {
                int newRow = row + direction[0];
                int newCol = col + direction[1];
                if (newRow >= 0 && newRow < m && newCol >= 0 && newCol < n && board[newRow][newCol] == 'O') {
                    board[newRow][newCol] = '#';
                    queue.add(newRow * n + newCol);
                }
            }
        }
    }
}
'''