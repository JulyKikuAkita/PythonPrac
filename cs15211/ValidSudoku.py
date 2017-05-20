__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/valid-sudoku.py
# Time:  O(n^2)
# Space: O(n)
# Hashtable
#
# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
#
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
#
#
# A partially filled sudoku which is valid.
#
# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
#
# https://github.com/kamyu104/LeetCode/blob/master/Python/valid-sudoku.py
#
#  Snapchat Uber Apple
# Hide Tags Hash Table

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for i in xrange(9):
            if not self.isValidList(board[i][j] for j in xrange(9)) or not self.isValidList(board[j][i] for j in xrange(9)):
                return False

        for i in xrange(3):
            for j in xrange(3):
                if not self.isValidList([board[m][n] for n in xrange(3 * j, 3 * j + 3) for m in xrange(3 * i, 3 * i + 3)]):
                    return False
        return True

    def isValidList2(self, dataList):
        dup = []
        for data in dataList:
            if data != ".":
                if data not in dup:
                    dup.append(data)
                else:
                    return False
        return True

    def isValidList(self, xs):
        #print "list xs =",xs
        xs = filter(lambda x : x != '.', xs)
        return len(set(xs)) == len(xs) # no duplicate in set

class Solution2:
    # @param board, a 9x9 2D array
    # @return a boolean
    '''
    #rule:
        Each row must have the numbers 1-9 occuring just once.
        Each column must have the numbers 1-9 occuring just once.
        And the numbers 1-9 must occur just once in each of the 9 sub-boxes of the grid.
    '''
    def isValidSudoku(self, board):
       board= board[:]
       def isValid(x, y,tmp):
           for i in range(9):
               if board[i][y] == tmp: return False
           for i in range(9):
               if board[x][i] == tmp: return False
           for i in range(3):
               for j in range(3):
                   if board[(x/3)*3+i][(y/3)*3+j] == tmp: return False
       for i in range(9):
           for j in range(9):
               if board[i][j] == '.' : continue
               tmp = board[i][j]
               board[i][j] = 'D' # ERR: String are immutable, cannot reassign
               if isValid(i, j, tmp) == False: return False
               else:
                    board[i][j] = tmp
       return True


    def isValidSudoku2(self, board):
        #check row
        for row in board:
            dup = []
            for i in row:
                if i != '.':
                    if i not in dup:
                        dup.append(i)
                    else:
                        return False
        #check column
        for i in xrange(9):
            dup = []
            for j in xrange(9):
                k = board[j][i]
                if k != ',':
                    if k not in dup:
                        dup.append(k)
                    else:
                        return False
        #check 3x3 subboard
        for i in [0,3,6]:
            for j in [0,3,6]:
                dup = []
                for m in [0,1,2]:
                    for n in [0,1,2]:
                        k = board[i+m][j+n]
                        if k != '.':
                            if k not in dup:
                                dup.append(k)
                            else:
                                return False
        return True




#test
test = Solution2()
#print test.isValidSudoku(["..4...63.",".........","5......9.","...56....","4.3.....1","...7.....","...5.....",".........","........."])
#print test.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])

if __name__ == '__main__':
    board = [[1, '.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', 2, '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', 3, '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', 4, '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', 5, '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', 6, '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', 7, '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', 8, '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.', 9]]

    print Solution().isValidSudoku(board)
    print Solution2().isValidSudoku(board)


#java
js = '''
public class Solution {
    public boolean isValidSudoku(char[][] board) {

        for(int i = 0; i < 9 ; i++){
            Set<Character> col = new HashSet<>();
            Set<Character> row = new HashSet<>();
            for(int j = 0; j < 9 ; j++){
                if(board[i][j] != '.'){
                    if(col.contains(board[i][j])){
                        return false;
                    }else{
                        col.add(board[i][j]);
                    }
                }
               // Iterator it = col.iterator();
               // while (it.hasNext())
               //   System.out.println(it.next());
                if(board[j][i] != '.'){
                    if(row.contains(board[j][i])){
                        return false;
                    }else{
                        row.add(board[j][i]);
                    }
                }
            if(!isValidGrid(i, j, board)) return false;

            }
        }

        return true;

    }

    private boolean isValidGrid(int x, int y, char[][] board){
        Set<Character> grid = new HashSet<>();
        for(int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++){
                int m = (x/3) * 3 + i;
                int n = (y/3) * 3 + j;
                if(board[m][n] != '.'){
                    if(grid.contains(board[m][n])){
                        return false;
                    }else{
                        grid.add(board[m][n]);
                    }
                }
            }
        }
        return true;
    }
}


js2 =
public class Solution {
    public boolean isValidSudoku(char[][] board) {
        return isRowValid(board) && isColValid(board) && isBlockValid(board);
    }

    private boolean isRowValid(char[][] board) {
        for (int i = 0; i < 9; i++) {
            boolean[] flags = new boolean[9];
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.' && !isValid(board, flags, i, j)) {
                    return false;
                }
            }
        }
        return true;
    }

    private boolean isColValid(char[][] board) {
        for (int j = 0; j < 9; j++) {
            boolean[] flags = new boolean[9];
            for (int i = 0; i < 9; i++) {
                if (board[i][j] != '.' && !isValid(board, flags, i, j)) {
                    return false;
                }
            }
        }
        return true;
    }

    private boolean isBlockValid(char[][] board) {
        for (int i = 0; i < 9; i += 3) {
            for (int j = 0; j < 9; j += 3) {
                boolean[] flags = new boolean[9];
                for (int m = i; m < i + 3; m++) {
                    for (int n = j; n < j + 3; n++) {
                        if (board[m][n] != '.' && !isValid(board, flags, m, n)) {
                            return false;
                        }
                    }
                }
            }
        }
        return true;
    }

    private boolean isValid(char[][] board, boolean[] flags, int i, int j) {
        int cur = board[i][j] - '1';
        if (flags[cur]) {
            return false;
        } else {
            flags[cur] = true;
        }
        return true;
    }
}


public class Solution {
    public boolean isValidSudoku(char[][] board) {
        List<Set<Character>> rowList = new ArrayList<Set<Character>>();
        List<Set<Character>> colList = new ArrayList<Set<Character>>();
        List<Set<Character>> boxList = new ArrayList<Set<Character>>();

        for (int i = 0 ; i < 9 ;i++){
            Set<Character> rowSet = new HashSet<Character>();
            rowList.add(rowSet);

            Set<Character> colSet = new HashSet<Character>();
            colList.add(colSet);

            Set<Character> boxSet = new HashSet<Character>();
            boxList.add(boxSet);

        }

        for ( int row = 0; row < 9; row++){
            for ( int col = 0; col < 9; col++) {
                char cur = board[row][col];
                if (cur == '.')
                    continue;

                //row
                Set<Character> rowSet = rowList.get(row);
                if (rowSet.contains(cur)){
                    return false;
                }else{
                    rowSet.add(cur);
                }

                //column
                Set<Character> colSet = colList.get(col);
                if(colSet.contains(cur)){
                    return false;
                }else{
                    colSet.add(cur);
                }

                //box
                int count = row / 3 * 3 + col /3;
                Set<Character> boxSet = boxList.get(count);
                if (boxSet.contains(cur)){
                    return false;
                }else{
                    boxSet.add(cur);
                }

            }
        }
        return true;
    }
}
'''