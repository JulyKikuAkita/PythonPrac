__source__ = 'https://leetcode.com/problems/spiral-matrix-iii/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 885. Spiral Matrix III
#
# On a 2 dimensional grid with R rows and C columns, we start at (r0, c0) facing east.
#
# Here, the north-west corner of the grid is at the first row and column,
# and the south-east corner of the grid is at the last row and column.
#
# Now, we walk in a clockwise spiral shape to visit every position in this grid.
#
# Whenever we would move outside the boundary of the grid,
# we continue our walk outside the grid (but may return to the grid boundary later.)
#
# Eventually, we reach all R * C spaces of the grid.
#
# Return a list of coordinates representing the positions of the grid in the order they were visited.
#
# Example 1:
#
# Input: R = 1, C = 4, r0 = 0, c0 = 0
# Output: [[0,0],[0,1],[0,2],[0,3]]
#
# Example 2:
#
# Input: R = 5, C = 6, r0 = 1, c0 = 4
# Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],
# [4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
#
# Note:
#
#     1 <= R <= 100
#     1 <= C <= 100
#     0 <= r0 < R
#     0 <= c0 < C
#
import unittest
# 180ms 92.16%
class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        ans = [(r0, c0)]
        if R * C == 1: return ans

        # For walk length k = 1, 3, 5 ...
        for k in xrange(1, 2*(R+C), 2):

            # For direction (dr, dc) = east, south, west, north;
            # and walk length dk...
            for dr, dc, dk in ((0, 1, k), (1, 0, k), (0, -1, k+1), (-1, 0, k+1)):

                # For each of dk units in the current direction ...
                for _ in xrange(dk):

                    # Step in that direction
                    r0 += dr
                    c0 += dc

                    # If on the grid ...
                    if 0 <= r0 < R and 0 <= c0 < C:
                        ans.append((r0, c0))
                        if len(ans) == R * C:
                            return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/spiral-matrix-iii/solution/
#
Approach 1: Walk in a Spiral
Complexity Analysis
Time Complexity: O((max(R, C))^2) Potentially,
our walk needs to spiral until we move R in one direction, 
and C in another direction, so as to reach every cell of the grid.
Space Complexity: O(R * C), the space used by the answer.

# 6ms 97.59%
class Solution {
    public int[][] spiralMatrixIII(int R, int C, int r0, int c0) {
        int[] dr = new int[]{0, 1, 0, -1};
        int[] dc = new int[]{1, 0, -1, 0};

        int[][] ans = new int[R*C][2];
        int t = 0;

        ans[t++] = new int[]{r0, c0};
        if (R * C == 1) return ans;
        for (int k = 1; k < 2*(R+C); k += 2)
            for (int i = 0; i < 4; ++i) {  // i: direction index
                int dk = k + (i / 2);  // number of steps in this direction
                for (int j = 0; j < dk; ++j) {  // for each step in this direction...
                    // step in the i-th direction
                    r0 += dr[i];
                    c0 += dc[i];
                    if (0 <= r0 && r0 < R && 0 <= c0 && c0 < C) {
                        ans[t++] = new int[]{r0, c0};
                        if (t == R * C) return ans;
                    }
                }
            }
        throw null;
    }
}

# 4ms 100%
class Solution {
    // the pattern is right step 1 down step 1,
    // then left step 2 up step 2,
    // then right step 3 down step 3,
    // then left step 4 up step 4,
    // ....
    // need to skip printing the last element each time.
    public int[][] spiralMatrixIII(int R, int C, int r0, int c0) {
        int n = R * C;
        int[][] result = new int[n][2];
        for(int i = 0, x = r0, y = c0, step = 1, rightAndDown = 1; i < n; ++step, rightAndDown ^= 1) {
            if (rightAndDown == 1) {
                // right: [[x,y], [x,y+step])
                if (x >= 0 && x < R) {
                    for(int j = Math.max(0, y), k = Math.min(C, y+step); j < k; ++j) {
                        result[i][0] = x;
                        result[i][1] = j;
                        ++i;
                    }
                }
                y += step;
                // down: [[x,y], [x+step,y])
                if (y >= 0 && y < C) {
                    for(int j = Math.max(0, x), k = Math.min(R, x+step); j < k; ++j) {
                        result[i][0] = j;
                        result[i][1] = y;
                        ++i;
                    }
                }
                x += step;
            } else {
                // left: [[x,y], [x,y-step])
                if (x >= 0 && x < R) {
                    for(int j = Math.min(C-1, y), k = Math.max(0, y-step+1); j >= k; --j) {
                        result[i][0] = x;
                        result[i][1] = j;
                        ++i;
                    }
                }
                y -= step;
                // up: [[x,y], [x-step,y])
                if (y >= 0 && y < C) {
                    for(int j = Math.min(R-1, x), k = Math.max(0, x-step+1); j >= k; --j) {
                        result[i][0] = j;
                        result[i][1] = y;
                        ++i;
                    }
                }
                x -= step;
            }
        }
        return result;
    }
}
'''
