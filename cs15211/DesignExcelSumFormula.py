__source__ = 'https://leetcode.com/problems/design-excel-sum-formula/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 631. Design Excel Sum Formula
#
#Your task is to design the basic function of Excel and implement the function of sum formula.
# Specifically, you need to implement the following functions:
#
# Excel(int H, char W): This is the constructor. The inputs represents the height and width of the Excel form.
# H is a positive integer, range from 1 to 26. It represents the height. W is a character range from 'A' to 'Z'.
# It represents that the width is the number of characters from 'A' to W.
# The Excel form content is represented by a height * width 2D integer array C,
# it should be initialized to zero. You should assume that the first row of C starts from 1,
# and the first column of C starts from 'A'.
#
#
# void Set(int row, char column, int val): Change the value at C(row, column) to be val.
#
#
# int Get(int row, char column): Return the value at C(row, column).
#
#
# int Sum(int row, char column, List of Strings : numbers):
# This function calculate and set the value at C(row, column),
# where the value should be the sum of cells represented by numbers.
# This function return the sum result at C(row, column).
# This sum formula should exist until this cell is overlapped by another value or another sum formula.
#
# numbers is a list of strings that each string represent a cell or a range of cells.
# If the string represent a single cell, then it has the following format : ColRow.
# For example, "F7" represents the cell at (7, F).
#
# If the string represent a range of cells, then it has the following format : ColRow1:ColRow2.
# The range will always be a rectangle, and ColRow1 represent the position of the top-left cell,
# and ColRow2 represents the position of the bottom-right cell.
#
#
# Example 1:
# Excel(3,"C");
# // construct a 3*3 2D array with all zero.
# //   A B C
# // 1 0 0 0
# // 2 0 0 0
# // 3 0 0 0
#
# Set(1, "A", 2);
# // set C(1,"A") to be 2.
# //   A B C
# // 1 2 0 0
# // 2 0 0 0
# // 3 0 0 0
#
# Sum(3, "C", ["A1", "A1:B2"]);
# // set C(3,"C") to be the sum of value at C(1,"A") and the values sum of the rectangle range
# whose top-left cell is C(1,"A") and bottom-right cell is C(2,"B"). Return 4.
# //   A B C
# // 1 2 0 0
# // 2 0 0 0
# // 3 0 0 4
#
# Set(2, "B", 2);
# // set C(2,"B") to be 2. Note C(3, "C") should also be changed.
# //   A B C
# // 1 2 0 0
# // 2 0 2 0
# // 3 0 0 6
# Note:
# You could assume that there won't be any circular sum reference. For example, A1 = sum(B1) and B1 = sum(A1).
# The test cases are using double-quotes to represent a character.
# Please remember to RESET your class variables declared in class Excel,
# as static/class variables are persisted across multiple test cases. Please see here for more details.
#
#
# Companies
# Microsoft
# Related Topics
# Design

import unittest

class Solution(object):
    pass  # your function here


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/design-excel-sum-formula/solution/

# 91ms 14.06%
class Excel {
    int[][] matrix;
    Map<Integer, String[]> map;
    public Excel(int H, char W) {
       matrix=new int[H][W-'A'+1];
       map=new HashMap<>();
    }

    public void set(int r, char c, int v) {
       int k=(r-1)*26+c-'A';
       if(map.containsKey(k)) map.remove(k);
       matrix[r-1][c-'A']=v;
    }

    public int get(int r, char c) {
        int k=(r-1)*26+c-'A';
       if(map.containsKey(k)) return sum(r,c, map.get(k));
        return matrix[r-1][c-'A'];
    }

    public int sum(int r, char c, String[] strs) {
       int res=0;
       for(String s:strs){
           int index=s.indexOf(":");
           if(index==-1){
              char col=s.charAt(0);
              int row=Integer.parseInt(s.substring(1));
              res+=get(row,col);
           }else{
               int y1=s.charAt(0)-'A';
               int x1=Integer.parseInt(s.substring(1,index));
               int y2=s.charAt(index+1)-'A';
               int x2=Integer.parseInt(s.substring(index+2));
               for(int i=x1;i<=x2;i++){
                   for(int j=y1;j<=y2;j++){
                       res+=get(i,(char)(j+'A'));
                   }
               }
           }
       }
        map.put((r-1)*26+c-'A',strs);
        return res;
    }
}
/**
 * Your Excel object will be instantiated and called as such:
 * Excel obj = new Excel(H, W);
 * obj.set(r,c,v);
 * int param_2 = obj.get(r,c);
 * int param_3 = obj.sum(r,c,strs);
 */


# 98ms 9.38%
class Excel {
    Formula[][] Formulas;
    class Formula {
        Formula(HashMap < String, Integer > c, int v) {
            val = v;
            cells = c;
        }
        HashMap < String, Integer > cells;
        int val;
    }
    Stack < int[] > stack = new Stack < > ();
    public Excel(int H, char W) {
        Formulas = new Formula[H][(W - 'A') + 1];
    }

    public int get(int r, char c) {
        if (Formulas[r - 1][c - 'A'] == null)
            return 0;
        return Formulas[r - 1][c - 'A'].val;
    }
    public void set(int r, char c, int v) {
        Formulas[r - 1][c - 'A'] = new Formula(new HashMap < String, Integer > (), v);
        topologicalSort(r - 1, c - 'A');
        execute_stack();
    }

    public int sum(int r, char c, String[] strs) {
        HashMap < String, Integer > cells = convert(strs);
        int summ = calculate_sum(r - 1, c - 'A', cells);
        set(r, c, summ);
        Formulas[r - 1][c - 'A'] = new Formula(cells, summ);
        return summ;
    }

    public void topologicalSort(int r, int c) {
        for (int i = 0; i < Formulas.length; i++)
            for (int j = 0; j < Formulas[0].length; j++)
                if (Formulas[i][j] != null && Formulas[i][j].cells.containsKey("" + (char)('A' + c) + (r + 1))) {
                    topologicalSort(i, j);
                }
        stack.push(new int[] {r,c});
    }

    public void execute_stack() {
        while (!stack.isEmpty()) {
            int[] top = stack.pop();
            if (Formulas[top[0]][top[1]].cells.size() > 0)
                calculate_sum(top[0], top[1], Formulas[top[0]][top[1]].cells);
        }
    }

    public HashMap < String, Integer > convert(String[] strs) {
        HashMap < String, Integer > res = new HashMap < > ();
        for (String st: strs) {
            if (st.indexOf(":") < 0)
                res.put(st, res.getOrDefault(st, 0) + 1);
            else {
                String[] cells = st.split(":");
                int si = Integer.parseInt(cells[0].substring(1)), ei = Integer.parseInt(cells[1].substring(1));
                char sj = cells[0].charAt(0), ej = cells[1].charAt(0);
                for (int i = si; i <= ei; i++) {
                    for (char j = sj; j <= ej; j++) {
                        res.put("" + j + i, res.getOrDefault("" + j + i, 0) + 1);
                    }
                }
            }
        }
        return res;
    }

    public int calculate_sum(int r, int c, HashMap < String, Integer > cells) {
        int sum = 0;
        for (String s: cells.keySet()) {
            int x = Integer.parseInt(s.substring(1)) - 1, y = s.charAt(0) - 'A';
            sum += (Formulas[x][y] != null ? Formulas[x][y].val : 0) * cells.get(s);
        }
        Formulas[r][c] = new Formula(cells, sum);
        return sum;
    }
}

/**
 * Your Excel object will be instantiated and called as such:
 * Excel obj = new Excel(H, W);
 * obj.set(r,c,v);
 * int param_2 = obj.get(r,c);
 * int param_3 = obj.sum(r,c,strs);
 */


# 61ms 95.31%
class Excel {

    int[][] grid;
    String[][][] formula;
    public Excel(int H, char W) {
        grid = new int[H][W-'A'+1];
        formula = new String[H][W-'A'+1][];
    }

    public void set(int r, char c, int v) {
        grid[r-1][c-'A'] = v;
        formula[r-1][c-'A'] = null;
    }

    public int get(int r, char c) {
        if (formula[r-1][c-'A'] == null)
            return grid[r-1][c-'A'];
        else
            return sum(r, c, formula[r-1][c-'A']);
    }

    public int sum(int r, char c, String[] strs) {
        formula[r-1][c-'A'] = strs;
        int res = 0;
        for (String str : strs) {
            int index = -1;
            if ((index = str.indexOf(':')) == -1) {
                int[] pos = helper(str);
                res += get(pos[0]+1, (char)('A'+pos[1]));
            } else {
                int[] pos1 = helper(str.substring(0, index));
                int[] pos2 = helper(str.substring(index+1));
                res += rangeSum(pos1[0], pos1[1], pos2[0], pos2[1]);
            }
        }
        return grid[r-1][c-'A'] = res;
    }

    public int rangeSum(int row1, int col1, int row2, int col2) {
        int res = 0;
        for (int i = row1; i <= row2; i++) {
            for (int j = col1; j <= col2; j++)
                res += get(i+1, (char)('A'+j));
        }
        return res;
    }

    public int[] helper(String str) {
        int col = str.charAt(0) - 'A';
        int row = 0;
        for (int i = 1; i < str.length(); i++)
            row = row * 10 + str.charAt(i) - '0';
        row--;
        return new int[]{row, col};
    }
}

'''