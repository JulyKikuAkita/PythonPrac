__author__ = 'July'
# not understanding 02.23.2015
# https://github.com/kamyu104/LeetCode/blob/master/Python/sudoku-solver.py
# Time:  ((9!)^9)
# Space: (1)
# DFS
#
# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# Empty cells are indicated by the character '.'.
#
# You may assume that there will be only one unique solution.
# Uber
# Hide Tags Backtracking Hash Table

class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if(board[i][j] == '.'):
                    for k in xrange(9):
                        #print chr(ord('1') + k), "i, j =", i, j, board[i][j]
                        board[i][j] = chr(ord('1') + k) # turn (1 + k ) into str # ord('1') = int 49 ; chr(49) = str 1
                        #board[i][j] = str(1 + k) the same as use chr(ord())
                        if self.isValid(board, i, j) and self.solveSudoku(board):
                            return True
                        board[i][j] = '.'
                    return False
        return True


    def isValid(self, board, x, y):
        for i in xrange(9):
            if i != x and board[i][y] == board[x][y]:
                return False
        for j in xrange(9):
            if j != y and board[x][j] == board[x][y]:
                return False

        i = 3 * (x / 3)
        while i < 3 * (x / 3 + 1):
            j = 3 * (y / 3)
            while j < 3 * (y / 3 + 1):
                if (i != x or j != y) and board[i][j] == board[x][y]:
                    return False
                j += 1
            i += 1
        return True

# http://www.cnblogs.com/zuoyuan/p/3770271.html
class Solution2:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    # dfs
    def solveSudoku(self, board):
        def isValid(x,y):
            tmp = board[x][y]
            board[x][y] = 'D'
            for i in range(9):
                if board[i][y] == tmp: return False
            for i in range(9):
                if board[x][i] == tmp: return False
            for i in range(3):
                for j in range(3):
                    if board[(x/3)*3+i][(y/3)*3+j] == tmp: return False
            board[x][y] = tmp
            return True

        def dfs(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for k in '123456789':
                            board[i][j] = k
                            if isValid(i,j) and dfs(board):
                                return True
                            board[i][j] = '.'
                        return False
            return True

        dfs(board)


#test
test = Solution2()
board1 = [["..9748..."],["7........"],[".2.1.9..."],["..7...24."],[".64.1.59."],[".98...3.."],["...8.3.2."],["........6"],["...2759.."]]
# ans = ["519748632","783652419","426139875","357986241","264317598","198524367","975863124","832491756","641275983"]

#print test.solveSudoku(board1)

if __name__ == "__main__":
    board = [['5', '3', '.', '.', '7', '.', '.', '.', '.'],
             ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
             ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
             ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
             ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
             ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
             ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
             ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
             ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
    Solution().solveSudoku(board)
    for i in xrange(9):
        print board[i]

#java
js = '''
public class Solution {
    public void solveSudoku(char[][] board) {
        dfs(board);
    }

    private boolean dfs(char[][] board){
        for(int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if ( board[i][j] == '.') {
                    for (char c = '1' ; c <= '9' ; c++) {
                        if (isValid(board, i, j ,c)) {
                            board[i][j] = c;

                            if (dfs(board)){
                                return true;
                            }
                            board[i][j] = '.';
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }

    private boolean isValid(char[][] board, int x, int y, char c) {
        for (int i = 0; i < 9 ; i++) {
            if (board[x][i] == c) return false;
        }

        for (int i = 0; i < 9; i++) {
            if (board[i][y] == c){
                return false;
            }
        }

        for (int i = x /3 * 3; i < x/3 * 3 + 3 ; i++ ) {
            for (int j = y /3 *3; j < y /3 * 3 + 3; j++) {
                if (board[i][j] == c )
                    return false;
            }
        }
        return true;
    }
}

#sol 2

public class Solution {
    public void solveSudoku(char[][] board) {
        solveSudoku(board, findEmptyCells(board), 0);
    }

    private List<Integer> findEmptyCells(char[][] board) {
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') {
                    result.add(i * 9 + j);
                }
            }
        }
        return result;
    }

    private boolean solveSudoku(char[][] board, List<Integer> emptyCells, int index) {
        if (index == emptyCells.size()) {
            return true;
        }
        int cur = emptyCells.get(index);
        int row = cur / 9;
        int col = cur % 9;
        for (char c = '1'; c <= '9'; c++) {
            if (isValid(board, row, col, c)) {
                board[row][col] = c;
                if (solveSudoku(board, emptyCells, index + 1)) {
                    return true;
                }
                board[row][col] = '.';
            }
        }
        return false;
    }

    private boolean isValid(char[][] board, int row, int col, char c) {
        for (int i = 0; i < 9; i++) {
            if (board[i][col] == c) {
                return false;
            }
        }
        for (int j = 0; j < 9; j++) {
            if (board[row][j] == c) {
                return false;
            }
        }
        for (int i = row - (row % 3); i < row - (row % 3) + 3; i++) {
            for (int j = col - (col % 3); j < col - (col % 3) + 3; j++) {
                if (board[i][j] == c) {
                    return false;
                }
            }
        }
        return true;
    }
}
'''