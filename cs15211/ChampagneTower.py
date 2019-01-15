__source__ = 'https://leetcode.com/problems/champagne-tower/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 799. Champagne Tower
#
# We stack glasses in a pyramid, where the first row has 1 glass,
# the second row has 2 glasses, and so on until the 100th row.
# Each glass holds one cup (250ml) of champagne.
#
# Then, some champagne is poured in the first glass at the top.
# When the top most glass is full, any excess liquid poured will fall equally
# to the glass immediately to the left and right of it.
# When those glasses become full, any excess champagne will fall equally
# to the left and right of those glasses, and so on.
# (A glass at the bottom row has it's excess champagne fall on the floor.)
#
# For example, after one cup of champagne is poured, the top most glass is full.
# After two cups of champagne are poured, the two glasses on the second row are half full.
# After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.
# After four cups of champagne are poured, the third row has the middle glass half full,
# and the two outside glasses are a quarter full, as pictured below.
#
# Now after pouring some non-negative integer cups of champagne,
# return how full the j-th glass in the i-th row is (both i and j are 0 indexed.)
#
# Example 1:
# Input: poured = 1, query_glass = 1, query_row = 1
# Output: 0.0
# Explanation: We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)).
# There will be no excess liquid so all the glasses under the top glass will remain empty.
#
# Example 2:
# Input: poured = 2, query_glass = 1, query_row = 1
# Output: 0.5
# Explanation: We poured 2 cups of champange to the top glass of the tower (which is indexed as (0, 0)).
# There is one cup of excess liquid. The glass indexed as (1, 0) and the glass indexed as (1, 1)
# will share the excess liquid equally, and each will get half cup of champange.
#
#
# Note:
#
# poured will be in the range of [0, 10 ^ 9].
# query_glass and query_row will be in the range of [0, 99].

import unittest

# 88ms 89.08%
class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        A = [[0] * k for k in xrange(1, 102)]
        A[0][0] = poured
        for r in xrange(query_row + 1):
            for c in xrange(r+1):
                q = (A[r][c] - 1.0) / 2.0
                if q > 0:
                    A[r+1][c] += q
                    A[r+1][c+1] += q

        return min(1, A[query_row][query_glass])

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/champagne-tower/solution/
Approach #1: Simulation [Accepted]
Complexity Analysis
Time Complexity: O(R^2), where R is the number of rows. As this is fixed, we can consider this complexity to be O(1).
Space Complexity: O(R^2), or O(1) by the reasoning above.
Note: if a glass has flow-through X, then Q = (X - 1.0) / 2.0 quantity of champagne will equally flow left and right.

# 13ms 81.04%
class Solution {
    public double champagneTower(int poured, int query_row, int query_glass) {
        double[][] A = new double[102][102];
        A[0][0] = (double) poured;
        for (int r = 0; r <= query_row; r++) {
            for (int c = 0; c <= r; c++) {
                 double q = (A[r][c] - 1.0) / 2.0;
                 if (q > 0) {
                    A[r + 1][c] += q;
                    A[r + 1][c + 1] += q;

                 }
            }
        }
        return Math.min(1, A[query_row][query_glass]);
    }
}

# 14ms 72.91%
class Solution {
    public double champagneTower(int poured, int query_row, int query_glass) {
        double[] res = new double[101];
        res[0] = poured;
        for (int row = 1; row <= query_row; row++) {
            for (int i = row; i >= 0; i--) {
                res[i + 1] += res[i] = Math.max(0.0, (res[i] - 1) / 2);
            }
        }
        return Math.min(res[query_glass], 1.0);
    }
}

'''