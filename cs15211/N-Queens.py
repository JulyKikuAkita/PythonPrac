__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/n-queens.py
# Time:  O(n!)
# Space: O(n)
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
# backtracking
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



if __name__ == "__main__":
    #print Solution().solveNQueens(4)
    #print Solution2().solveNQueens(4)
    print SolutionCC150().solveNQueens(4)


class SolutionOther:
    # @return a list of lists of string
    # http://www.cnblogs.com/zuoyuan/p/3747249.html

    def solveNQueens(self, n):
        self.board = [-1 for i in range(n)]
        self.res = []
        self.dfs( 0, [], n)
        return self.res


    def check(self, k, j): # check if the kth queen can be put in column j!
        for i in range(k):
            # queen's j == current j (same col with queen)
            # or
            # queen's i - i' == queen's j - j'  ( k = depth = ith row of the board, self.board[i] == queen's j position)
            # at level k, every point shares the same i = k
            if self.board[i] == j or abs(k-i) == abs(self.board[i] - j):
                return False
        return True

    def dfs(self, depth, valuelist, n):
        if depth == n:
            self.res.append(valuelist)
            return
        for i in range(n):
            if self.check(depth, i):
                self.board[depth] = i
                s = '.'* n
                #print i, depth, s[:i], valuelist+[s[:i]+'Q'+s[i+1:]]
                self.dfs(depth+1, valuelist+[s[:i]+'Q'+s[i+1:]], n)

    # http://chaoren.is-programmer.com/posts/43589.html
    def solveNQueens_way2(self, n):
        self.res = []
        self.solve(n, 0, [-1 for i in xrange(n)])
        return self.res
    def solve(self, n, currQueenNum, board):
        if currQueenNum == n:
            oneAnswer = [['.' for j in xrange(n)] for i in xrange(n)]
            #print oneAnswer
            for i in xrange(n):
                oneAnswer[i][board[i]] = 'Q'
                oneAnswer[i] = ''.join(oneAnswer[i])
            self.res.append(oneAnswer)
            return
        for i in xrange(n):
            valid = True
            for k in xrange(currQueenNum):
                if board[k] == i:
                    valid = False
                    break
                if abs(board[k] - i) == currQueenNum - k:
                    valid = False
                    break
            if valid:
                board[currQueenNum] = i
                self.solve(n, currQueenNum+1, board)


class SolutionJS:
    # @return an integer
    def solveNQueens(self, n):
        self.solutions = []
        self.solveNQueensRecu([], 0, n)
        return self.solutions

    def solveNQueensRecu(self, solution, row, n):
        if row == n:
            self.solutions.append(map(lambda x: '.' * x + "Q" + '.' * (n - x - 1), solution))

        for i in xrange(n):
            if self.isValid(solution + [i], row):
                self.solveNQueensRecu(solution + [i], row + 1, n)

    def isValid(self, res, row):
        for i in xrange(row):
            if res[i] == res[row]:
                return False
            if abs(i - row) == abs(res[i] - res[row]):
                return False
        return True

#test
test = SolutionOther()
print test.solveNQueens(4)
#print test.solveNQueens_way2(4)

'''
reduce(function, iterable[, initializer])
Apply function of two arguments cumulatively to the items of iterable, from left to right, so as to reduce the iterable to a single value.
For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5). The left argument, x, is the accumulated value and the right argument, y,
is the update value from the iterable. If the optional initializer is present, it is placed before the items of the iterable in the calculation, and serves as
a default when the iterable is empty. If initializer is not given and iterable contains only one item, the first item is returned. Roughly equivalent to:

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

#java
js = '''
public class Solution {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> result = new ArrayList<>();
        solveNQueens(new int[n], 0, result);
        return result;
    }

    private void solveNQueens(int[] board, int index, List<List<String>> result) {
        if (index == board.length) {
            result.add(printResult(board));
            return;
        }
        for (int i = 0; i < board.length; i++) {
            if (isValid(board, index, i)) {
                board[index] = i;
                solveNQueens(board, index + 1, result);
            }
        }
    }

    private boolean isValid(int[] board, int index, int num) {
        for (int i = 0; i < index; i++) {
            if (board[i] == num || Math.abs(index - i) == Math.abs(num - board[i])) {
                return false;
            }
        }
        return true;
    }

    private List<String> printResult(int[] board) {
        List<String> result = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i]; j++) {
                sb.append('.');
            }
            sb.append('Q');
            for (int j = board[i] + 1; j < board.length; j++) {
                sb.append('.');
            }
            result.add(sb.toString());
            sb.setLength(0);
        }
        return result;
    }
}


public class Solution2 {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> res = new ArrayList<>();
        int[] record = new int[n];
        dfs(res, record, 0);
        return res;
    }

    private void dfs(List<List<String>> res, int[] record, int cur){
        if(cur >= record.length){
            res.add(generateResult(record));
            return;
        }

        for(int i = 0; i < record.length ; i++){
            record[cur] = i;
            if(isValid(record, cur)){
                dfs(res, record, cur + 1);
            }
        }
    }

    private boolean isValid(int[] record, int cur){
        for(int i = 0; i < cur; i++){
            if(record[i] == record[cur]) return false;

            if(Math.abs(record[cur] - record[i]) == (cur - i)){
                return false;
            }
        }
        return true;
    }

    private List<String> generateResult(int[] record){
        List<String> res = new ArrayList<>();

        for(int i = 0; i < record.length; i++){
            StringBuilder sb = new StringBuilder();
            for(int j = 0; j < record.length; j++){
                if(record[i] == j){
                    sb.append('Q');
                }else{
                    sb.append('.');
                }
            }
            res.add(sb.toString());
        }
        return res;
    }
}
'''