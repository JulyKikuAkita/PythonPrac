__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/n-queens-ii.py
# Time:  O(n!)
# Space: O(n)
# DFS
#
# Follow up for N-Queens problem.
#
# Now, instead outputting board configurations, return the total number of distinct solutions.
#
# Zenefits
# quick solution for checking if it is diagonally legal
class Solution:
    # @return an integer
    def totalNQueens(self, n):
        self.cols = [False] * n
        self.main_diag = [False] * (2 * n)
        self.anti_diag = [False] * (2 * n)
        return self.totalNQueensRecu([], 0, n)

    def totalNQueensRecu(self, solution, row, n):
        if row == n:
            return 1
        result = 0
        for i in xrange(n):
            if not self.cols[i] and not self.main_diag[row + i] and not self.anti_diag[row - i + n]:
                self.cols[i] = self.main_diag[row + i] = self.anti_diag[row - i + n ] = True
                result += self.totalNQueensRecu(solution + [i], row + 1 ,n)
                self.cols[i] = self.main_diag[row + i] = self.anti_diag[row - i + n] = False
        return result

# slower solution
class Solution2:
    # @return an integer
    def totalNQueens(self, n):
        return self.totalNQueensRecu([], 0, n)

    def totalNQueensRecu(self, solution, row, n):
        if row == n:
            return 1
        result = 0
        for i in xrange(n):
            # reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5)
            # def reduce(function, iterable, initializer=None):
            if i not in solution and reduce(lambda acc, j : abs(row - j) != abs(i - solution[j]) and acc , xrange(len(solution)),True):
                result += self.totalNQueensRecu(solution + [i], row + 1, n)
        return result

class SolutionCC150:
    # @return an integer
    def totalNQueens(self, n):
        board = [-1 for i in xrange(n)]
        return self.dfs( 0, board, n)

    def dfs(self,  depth, board, n):
        if depth == n :
            return 1
        result = 0
        for i in xrange(n):
            if self.check(depth, i, board):
                board[depth] = i
                result += self.dfs( depth+1, board, n)
        return result

    def check(self, depth, candidate, board):
        for j in xrange(depth):
            if candidate == board[j] or abs(depth - j) == abs( candidate - board[j]):
                return False
        return True


class SolutionOther:
    # @return an integer
    # http://chaoren.is-programmer.com/posts/43590.html
    def totalNQueens(self, n):
        self.res = 0
        self.solve(n, 0, [-1 for i in xrange(n)])
        return self.res

    def solve(self, n, currQueenNum, board):
        if currQueenNum == n:
            self.res += 1
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
                self.solve(n, currQueenNum + 1, board)

    #solve it not using recursion
    # http://www.cnblogs.com/zuoyuan/p/3747658.html
    def totalNQueens_iterative(self, n):
        self.board = [ -1 for i in range(n)]
        row = 0 ; col = 0 ;  sum = 0
        while row < n :
            while col < n:
                if self.check(row, col):
                    self.board[row] = col
                    col = 0
                    break
                else:
                    col += 1
            if self.board[row] == -1:
                if row == 0 :
                    break
                else:
                    row -= 1
                    col = self.board[row]+1
                    self.board[row] = -1
                    continue
            if row == n-1:
                sum += 1
                col = self.board[row]+1
                self.board[row] = -1
                continue
            row += 1
        return sum


    def check(self, k, j):  # check if the kth queen can be put in column j!
        for i in range(k):
            if self.board[i] == j or abs(k - i) == abs(self.board[i] - j):
                return False
        return True


class SolutionJS:
    # @return an integer
    def totalNQueens(self, n):

        return self.totalNQueensRecu([], 0, n)

    def totalNQueensRecu(self, solution, row, n):
        if row == n:
            return 1
        result = 0
        for i in xrange(n):
            if self.isValid(solution + [i], row):
                result += self.totalNQueensRecu(solution + [i], row + 1 ,n)
        return result

    def isValid(self, res, row):
        for i in xrange(row):
            if res[i] == res[row]:
                return False
            if abs(res[i] - res[row]) == abs( i - row):
                return False
        return True
#test
test = SolutionOther()
#print test.totalNQueens(4)
#print test.totalNQueens_iterative(4)

if __name__ == "__main__":
    print Solution().totalNQueens(8)
    print Solution2().totalNQueens(8)
    print SolutionCC150().totalNQueens(8)

#java
js = '''
public class Solution {
    public int totalNQueens(int n) {
        return totalNQueens(new int[n], 0);
    }

    private int totalNQueens(int[] board, int index) {
        if (index == board.length) {
            return 1;
        }
        int result = 0;
        for (int i = 0; i < board.length; i++) {
            if (isValid(board, index, i)) {
                board[index] = i;
                result += totalNQueens(board, index + 1);
            }
        }
        return result;
    }

    private boolean isValid(int[] board, int index, int num) {
        for (int i = 0; i < index; i++) {
            if (board[i] == num || Math.abs(index - i) == Math.abs(num - board[i])) {
                return false;
            }
        }
        return true;
    }
}
'''