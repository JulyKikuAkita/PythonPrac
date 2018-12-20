__source__ = 'https://leetcode.com/problems/magic-squares-in-grid/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 840. Magic Squares In Grid
#
# A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9
# such that each row, column, and both diagonals all have the same sum.
#
# Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?
# (Each subgrid is contiguous).
#
# Example 1:
#
# Input: [[4,3,8,4],
#         [9,5,1,9],
#         [2,7,6,2]]
# Output: 1
# Explanation:
# The following subgrid is a 3 x 3 magic square:
# 438
# 951
# 276
#
# while this one is not:
# 384
# 519
# 762
#
# In total, there is only one magic square inside the given grid.
#
# Note:
#
#     1 <= grid.length <= 10
#     1 <= grid[0].length <= 10
#     0 <= grid[i][j] <= 15
#
import unittest

# 28ms 39.85%
class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R, C = len(grid), len(grid[0])

        def magic(a,b,c,d,e,f,g,h,i):
            return (sorted([a,b,c,d,e,f,g,h,i]) == range(1, 10) and
                (a+b+c == d+e+f == g+h+i == a+d+g ==
                 b+e+h == c+f+i == a+e+i == c+e+g == 15))

        ans = 0
        for r in xrange(R-2):
            for c in xrange(C-2):
                if grid[r+1][c+1] != 5: continue  # optional skip
                if magic(grid[r][c], grid[r][c+1], grid[r][c+2],
                         grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2],
                         grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]):
                    ans += 1
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/magic-squares-in-grid/solution/
#
Approach #1: Brute Force [Accepted]
Complexity Analysis
Time Complexity: O(R * C), where R,C are the number of rows and columns in the given grid.
Space Complexity: O(1)

# 3ms 100%
class Solution {
    public int numMagicSquaresInside(int[][] grid) {
        int R = grid.length, C = grid[0].length;
        int ans = 0;
        for (int r = 0; r < R-2; ++r)
            for (int c = 0; c < C-2; ++c) {
                if (grid[r+1][c+1] != 5) continue;  // optional skip
                if (magic(grid[r][c], grid[r][c+1], grid[r][c+2],
                          grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2],
                          grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]))
                    ans++;
            }

        return ans;
    }

    public boolean magic(int... vals) {
        int[] count = new int[16];
        for (int v: vals) count[v]++;
        for (int v = 1; v <= 9; ++v)
            if (count[v] != 1)
                return false;

        return (vals[0] + vals[1] + vals[2] == 15 &&
                vals[3] + vals[4] + vals[5] == 15 &&
                vals[6] + vals[7] + vals[8] == 15 &&
                vals[0] + vals[3] + vals[6] == 15 &&
                vals[1] + vals[4] + vals[7] == 15 &&
                vals[2] + vals[5] + vals[8] == 15 &&
                vals[0] + vals[4] + vals[8] == 15 &&
                vals[2] + vals[4] + vals[6] == 15);
    }
}

# 3ms 100%
class Solution {
    public int numMagicSquaresInside(int[][] grid) {
        if(grid == null || grid.length < 3 || grid[0] == null || grid[0].length < 3) return 0;
        int m = grid.length;
        int n = grid[0].length;
        int cnt = 0;
        for (int i = 0; i < m - 2; i++) {
            for (int j = 0; j < n - 2; j++) {
                if (isMagicSquare(grid, i, j)) cnt++;
            }
        }
        return cnt;     
    }
    
    private boolean isMagicSquare(int[][] grid, int i, int j) {
        if (grid[i + 1][j + 1] != 5) return false;
        if (grid[i][j] + grid[i + 2][j + 2] != 10) return false;
        if (grid[i][j + 2] + grid[i + 2][j] != 10) return false;
        for (int m = 0; m < 3; m++) {
            int sum1 = 0;
            int sum2 = 0;
            for (int n = 0; n < 3; n++) {
                if (grid[i + m][j + n] > 9 || grid[i + n][j + m] > 9 || grid[i + n][j + m] == 0 || grid[i + m][j + n]  == 0) return false;
                sum1 += grid[i + m][j + n];
                sum2 += grid[i + n][j + m];
            }
            if (sum1 != 15) return false;
            if (sum2 != 15) return false;
        }
        return true;
    }
}
'''
