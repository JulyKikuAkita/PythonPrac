__source__ = 'https://leetcode.com/problems/n-queens/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/n-queens.py
# Time:  O(n!)
# Space: O(n)
#
# Description: Leetcode # 217. Contains Duplicate
#
# The n-queens puzzle is the problem of placing n queens on
# an nxn chess board such that no two queens attack each other.
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens' placement,
# where 'Q' and '.' both indicate a queen and an empty space respectively.
#
# For example,
# There exist two distinct solutions to the 4-queens puzzle:
#
# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
#
#
# Related Topics
# Backtracking
# Similar Questions
# N-Queens II
import unittest
# quick solution for checking if it is diagonally legal
class Solution:
    # @return an integer
    def solveNQueens(self, n):
        self.cols = [False] * n
        self.main_diag = [False] * (2 * n)
        self.anti_diag = [False] * (2 * n)
        self.solutions = []
        #print self.main_diag
        self.solveNQueensRecu([], 0, n)
        return self.solutions

    def solveNQueensRecu(self, solution, row, n):
        if row == n:
            self.solutions.append(map(lambda x: '.' * x + "Q" + '.' * (n - x - 1), solution))
        else:
            for i in xrange(n):
                if not self.cols[i] and not self.main_diag[row + i] and not self.anti_diag[row - i + n ]:
                    self.cols[i] = self.main_diag[row + i] = self.anti_diag[row - i + n] = True

                    self.solveNQueensRecu(solution + [i], row + 1, n)
                    self.cols[i] = self.main_diag[row + i] = self.anti_diag[row - i + n ] = False

# slower solution
class Solution2:
    # @return an integer
    def solveNQueens(self, n):
        self.solutions = []
        self.solveNQueensRecu([], 0, n)
        return self.solutions

    def solveNQueensRecu(self, solution, row, n):
        if row == n:
            #print solution
            self.solutions.append(map(lambda x: '.' * x + 'Q' + '.' * (n - x - 1), solution))
        else:
            for i in xrange(n):
                # reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5)
                # def reduce(function, iterable, initializer=None):
                if i not in solution and reduce(lambda acc, j: abs(row - j) != abs(i - solution[j]) and acc, xrange(len(solution)), True ):
                    #print row, solution
                    self.solveNQueensRecu(solution + [i], row + 1, n)

class SolutionCC150:
    def solveNQueens(self, n):
        cur, result = [], []
        colForRow = [ -1 for i in xrange(n)]
        self.placeQueens(0, n, colForRow, cur, result)
        print colForRow
        return result

    def placeQueens(self, row, n, colForRow, cur, result):
        if row == n:
            result.append(cur)
            return
        for i in xrange(n):
            colForRow[row] = i
            if self.foundQueenPosition(row, n, colForRow):
                s = '.' * n
                self.placeQueens(row + 1, n ,colForRow, cur + [s[:i] + "Q" + s[i+1:]], result)

    def foundQueenPosition(self, row, n, colForRow):
        for i in xrange(row):
            diff = abs(colForRow[i] - colForRow[row])
            if diff == 0 or diff == row - i:
                return False
        return True

# Thought:
# ideas:
#
# Use the DFS helper function to find solutions recursively.
# A solution will be found when the length of queens is equal to n ( queens is a list of the indices of the queens).
#
#
# In this problem, whenever a location (x, y) is occupied, any other locations (p, q )
# where p + q == x + y or p - q == x - y would be invalid. We can use this information to keep track of the indicators
# (xy_dif and xy_sum ) of the invalid positions and then call DFS recursively with valid positions only.
#
#
# At the end, we convert the result (a list of lists; each sublist is the indices of the queens) into the desire format.

class SolutionOther:
    # @return a list of lists of string
    def solveNQueens(self, n):
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p==n:
                result.append(queens)
                return None
            for q in range(n):
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum:
                    DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])
        result = []
        DFS([],[],[])
        return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]

# Thought:
redeuce = '''
reduce(function, iterable[, initializer])
Apply function of two arguments cumulatively to the items of iterable, from left to right,
so as to reduce the iterable to a single value.
For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5).
The left argument, x, is the accumulated value and the right argument, y,
is the update value from the iterable. If the optional initializer is present,
it is placed before the items of the iterable in the calculation, and serves as
a default when the iterable is empty. If initializer is not given and iterable contains only one item,
the first item is returned. Roughly equivalent to:

def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        try:
            initializer = next(it)
        except StopIteration:
            raise TypeError('reduce() of empty sequence with no initial value')
    accum_value = initializer
    for x in it:
        accum_value = function(accum_value, x)
    return accum_value

    Map:
    def fahrenheit(T):
    return ((float(9)/5)*T + 32)
def celsius(T):
    return (float(5)/9)*(T-32)
temp = (36.5, 37, 37.5,39)

F = map(fahrenheit, temp)
C = map(celsius, F)

'''
# test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        test = SolutionOther()
        print test.solveNQueens(4)
        #print test.solveNQueens_way2(4)

        #print Solution().solveNQueens(4)
        #print Solution2().solveNQueens(4)
        print SolutionCC150().solveNQueens(4)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:

#75.29% 7ms
public class Solution {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> result = new ArrayList<>();
        solveNQueens(new int[n], 0, result);
        return result;
    }

    private void solveNQueens(int[] board, int index, List<List<String>> result) {
        if (index == board.length) {
            result.add(generateResult(board));
            return;
        }
        for (int i = 0; i < board.length; i++) {
            if (isValid(board, index, i)) {
                board[index] = i;
                solveNQueens(board, index + 1, result);
            }
        }
    }

    private boolean isValid(int[] board, int index, int pos) {
        for (int i = 0; i < index; i++) {
            if (board[i] == pos || index - i == Math.abs(board[i] - pos)) {
                return false;
            }
        }
        return true;
    }

    private List<String> generateResult(int[] board) {
        List<String> result = new ArrayList<>();
        for (int i = 0; i < board.length; i++) {
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < board[i]; j++) {
                sb.append('.');
            }
            sb.append('Q');
            for (int j = board[i] + 1; j < board.length; j++) {
                sb.append('.');
            }
            result.add(sb.toString());
        }
        return result;
    }
}

#96.87% 4ms
public class Solution {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> res=new ArrayList();
        if(n == 0) return res;
        char[][] board=new char[n][n];
        boolean[] col=new boolean[n];
        boolean[] dia=new boolean[ 2 * n - 1];
        boolean[] antidia=new boolean[ 2 * n - 1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <n; j++) {
                board[i][j]= '.';
            }
        }
        dfs(board, n, col, dia, antidia, 0, res);
        return res;
    }

    public void dfs(char[][] board, int n, boolean[] col, boolean[] dia, boolean[] antidia, int row, List<List<String>> res){
        if (row == n) {
            List<String> cur = new ArrayList<>();
            for(int i = 0; i < n; i++) {
                cur.add(new String(board[i]));
            }
            res.add(cur);
            return;
        }
        for (int i  = 0; i < n; i++) {
            if (col[i] || dia[row + i] || antidia[row - i + n - 1]) continue;
            col[i] = dia[row + i] = antidia[row - i + n - 1 ] = true;
            board[row][i] = 'Q';
            dfs(board, n, col, dia, antidia, row + 1, res);
            board[row][i] = '.';
            col[i] = dia[row + i] = antidia[row - i + n - 1 ] = false;
        }
    }
}
'''