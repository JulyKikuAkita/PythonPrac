__source__ = 'https://leetcode.com/problems/n-queens-ii/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/n-queens-ii.py
# Time:  O(n!)
# Space: O(n)
# DFS
#
# Description: Leetcode # 52. N-Queens II
#
# Follow up for N-Queens problem.
#
# Now, instead outputting board configurations, return the total number of distinct solutions.
#
# Companies
# Zenefits
# Related Topics
# Backtracking
# Similar Questions
# N-Queens
#
import unittest
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

#test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        test = SolutionOther()
        #print test.totalNQueens(4)
        #print test.totalNQueens_iterative(4)

        print Solution().totalNQueens(8)
        print Solution2().totalNQueens(8)
        print SolutionCC150().totalNQueens(8)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
This is a classic backtracking problem.

Start row by row, and loop through columns. At each decision point, skip unsafe positions by using three boolean arrays.

Start going back when we reach row n.

Just FYI, if using HashSet, running time will be at least 3 times slower!

# 71.35% 3ms
public class Solution {
    public int totalNQueens(int n) {
        boolean[] cols = new boolean[n];     // columns   |
        boolean[] d1 = new boolean[2 * n];   // diagonals \
        boolean[] d2 = new boolean[2 * n];   // diagonals /
        return backtracking(0, cols, d1, d2, n);
    }

    public int backtracking(int row, boolean[] cols, boolean[] d1, boolean []d2, int n) {
        if (row == n) return 1;
        int count = 0;
        for (int i = 0; i < n ;i++) {
            int id1 = i + row;
            int id2 = i - row + n;
            if( cols[i] || d1[id1] ||d2[id2]) continue;
            cols[i] = d1[id1] = d2[id2] = true;
            count +=  backtracking(row + 1, cols, d1, d2, n);
            cols[i] = d1[id1] = d2[id2] = false;
        }
        return count;
    }
}

#55.74% 4ms
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

#98.30% 1ms
public class Solution {
    public int totalNQueens(int n) {
        if (n < 1) return 0;
        int upLimit = (1 << n) - 1;
        int result = solve(upLimit, 0, 0 ,0);
        return result;
    }

    private int solve(int upLimit, int colLimit, int leftLimit, int rightLimit) {
        if (upLimit == colLimit) return 1;
        int pos = upLimit & (~(colLimit | leftLimit | rightLimit)), count = 0;
        while (pos != 0) {
            int mostRightOne = pos & (~pos + 1);
            pos -= mostRightOne;
            count += solve(upLimit, colLimit | mostRightOne,
                          (leftLimit | mostRightOne) << 1,
                          (rightLimit | mostRightOne) >>> 1);
        }
        return count;
    }
}
'''