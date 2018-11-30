import collections
import itertools

__source__ = 'https://leetcode.com/problems/number-of-corner-rectangles/description/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 750. Number Of Corner Rectangles
#
# Given a grid where each entry is only 0 or 1, find the number of corner rectangles.
#
# A corner rectangle is 4 distinct 1s on the grid that form an axis-aligned rectangle.
# Note that only the corners need to have the value 1. Also, all four 1s used must be distinct.
#
# Example 1:
#
# Input: grid =
# [[1, 0, 0, 1, 0],
#  [0, 0, 1, 0, 1],
#  [0, 0, 0, 1, 0],
#  [1, 0, 1, 0, 1]]
# Output: 1
# Explanation: There is only one corner rectangle,
# with corners grid[1][2], grid[1][4], grid[3][2], grid[3][4].
#
# Example 2:
#
# Input: grid =
# [[1, 1, 1],
#  [1, 1, 1],
#  [1, 1, 1]]
# Output: 9
# Explanation: There are four 2x2 rectangles, four 2x3 and 3x2 rectangles,
# and one 3x3 rectangle.
#
# Example 3:
#
# Input: grid =
# [[1, 1, 1, 1]]
# Output: 0
# Explanation: Rectangles must have four distinct corners.
#
# Note:
#
# The number of rows and columns of grid will each be in the range [1, 200].
# Each grid[i][j] will be either 0 or 1.
# The number of 1s in the grid will be at most 6000.
#
import unittest

class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = collections.Counter()
        ans = 0
        for row in grid:
            for c1, v1 in enumerate(row):
              if v1:
                for c2 in xrange(c1 + 1, len(row)):
                    if row[c2]:
                        ans += count[c1, c2]
                        count[c1,c2] += 1
        return ans

#54.19% 856ms
class Solution2(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = [[c for c , val in enumerate(row) if val] for row in grid]
        N = sum(len(row) for row in grid)
        SQRTN = int(N**.5)

        ans = 0
        count = collections.Counter()
        for r, row in enumerate(rows):
            if len(row) >= SQRTN:
                target = set (row)
                for r2, row2 in enumerate(rows):
                    if r2 <= r and len(row2) >= SQRTN:
                        continue;
                    found = sum(1 for c2 in row2 if c2 in target)
                    ans += found * (found - 1) / 2
            else:
                for pair in itertools.combinations(row, 2):
                    ans += count[pair]
                    count[pair] += 1
        return ans

class Solution3(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid)<2 or len(grid[0])<2:
            return 0
        n = len(grid[0])
        count = [[0]*n for _ in range(n)]
        for row in grid:
            ones = [i for i in range(n) if row[i]]
            for i, j in itertools.combinations(ones, 2):
                count[i][j] += 1
        ans = 0
        for row in count:
            for m in row:
                if m>1:
                    ans += m * (m-1)/2
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/number-of-corner-rectangles/solution/

Approach #1: Count Corners [Accepted]

Complexity Analysis
Time Complexity: O(R*C^2) where R,C is the number of rows and columns.
Space Complexity: O(C^2) in additional space.

#78.50 % 70ms
class Solution {
    public int countCornerRectangles(int[][] grid) {
        Map<Integer, Integer> count = new HashMap();
        int ans = 0;
        for (int[] row: grid) {
            for (int c1 = 0; c1 < row.length; ++c1) if (row[c1] == 1) {
                for (int c2 = c1+1; c2 < row.length; ++c2) if (row[c2] == 1) {
                    int pos = c1 * 200 + c2;
                    int c = count.getOrDefault(pos, 0);
                    ans += c;
                    count.put(pos, c+1);
                }
            }
        }
        return ans;
    }
}

# https://leetcode.com/problems/number-of-corner-rectangles/discuss/110200/Summary-of-three-solutions-based-on-three-different-ideas
Idea I -- Check each candidate rectangle one by one to see if it is a corner rectangle
# Assuming we enumerate any two rows i and j (for i < j),
# a corner rectangle can be edged at the column k as long as grid[i][k] == 1 && grid[j][k] == 1.
# If we could all columns mentioned above as numPairs,
# any two of them can form a unique corner rectangle,
# i.e. numPairs * (numPairs - 1) in total.
#
# Time complexity: O(m^2 * n^2)
# Space complexity: O(1)
# 59.25% 114ms
class Solution {
    public int countCornerRectangles(int[][] grid) {
        int m = grid.length, n = grid[0].length, res = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0) continue;

                for (int p = i + 1; p < m; p++) {
                    if (grid[p][j] == 0) continue;

                    for (int q = j + 1; q < n; q++) {
                        res += grid[i][q] & grid[p][q];
                    }
                }
            }
        }

        return res;
    }
}

Idea II -- Divide the candidate rectangles into groups and then count the number of corner rectangles for each group
Time complexity: O(m^2 * n)
Space complexity: O(1)

class Solution {
    public int countCornerRectangles(int[][] grid) {

        int rows = grid.length, cols = grid[0].length, numRectangles = 0;

        for (int i = 0; i + 1 < rows; i++) {
            for (int j = i + 1; j < rows; j++) {
                int numPairs = 0; // Number of pair such that grid[i][k] == 1 && grid[j][k] == 1
                for (int k = 0; k < cols; k++) {
                    if (grid[i][k] == 1 && grid[j][k] == 1) {
                        numPairs++;
                    }
                }
                if (numPairs > 1)
                    numRectangles += numPairs * (numPairs - 1) / 2;
            }
        }

        return numRectangles;
    }

}

# Idea III -- Build the grid matrix row by row and then count the number of new corner rectangles
resulting from the added row

# DP:
Time complexity: O(m * n^2)
Space complexity: O(n^2)
# T(i, j, q) = T(i-1, j, q) + cnt where cnt = 1 if grid[i][j] == 1 && grid[i][q] == 1, otherwise cnt = 0
class Solution {
    public int countCornerRectangles(int[][] grid) {
        int m = grid.length, n = grid[0].length, res = 0;
        int[][] dp = new int[n][n];
        for (int r = 0; r < m; r++) {
            for(int i = 0; i <n; i++) {
                if (grid[r][i] == 0) continue;
                for (int j = i + 1; j < n; j++) {
                    if (grid[r][j] == 1) res += dp[i][j]++;
                }
            }
        }
        return res;
    }
}
'''