__source__ = 'https://leetcode.com/problems/image-overlap/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 835. Image Overlap
#
# Two images A and B are given, represented as binary,
# square matrices of the same size.
# (A binary matrix has only 0s and 1s as values.)
#
# We translate one image however we choose
# (sliding it left, right, up, or down any number of units),
# and place it on top of the other image.
# After, the overlap of this translation is the number of positions that have a 1 in both images.
#
# (Note also that a translation does not include any kind of rotation.)
#
# What is the largest possible overlap?
#
# Example 1:
#
# Input: A = [[1,1,0],
#             [0,1,0],
#             [0,1,0]]
#        B = [[0,0,0],
#             [0,1,1],
#             [0,0,1]]
# Output: 3
# Explanation: We slide A to right by 1 unit and down by 1 unit.
# Notes:
#
# 1 <= A.length = A[0].length = B.length = B[0].length <= 30
# 0 <= A[i][j], B[i][j] <= 1
#
import unittest
# 1008ms 23.45%
class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        N = len(A)
        A2 = [complex(r, c) for r, row in enumerate(A)
              for c, v in enumerate(row) if v]
        B2 = [complex(r, c) for r, row in enumerate(B)
              for c, v in enumerate(row) if v]
        Bset = set(B2)
        seen = set()
        ans = 0
        for a in A2:
            for b in B2:
                d = b-a
                if d not in seen:
                    seen.add(d)
                    ans = max(ans, sum(x+d in Bset for x in A2))
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/image-overlap/solution/
Approach #1: Translate by Delta [Accepted]
Complexity Analysis
Time Complexity: O(N^6), where N is the length of A or B.
Space Complexity: O(N^2)

# 241ms 9.93%
import java.awt.Point;
class Solution {
    public int largestOverlap(int[][] A, int[][] B) {
        int N = A.length;
        List<Point> A2 = new ArrayList(), B2 = new ArrayList();
        for (int i = 0; i < N*N; ++i) {
            if (A[i/N][i%N] == 1) A2.add(new Point(i/N, i%N));
            if (B[i/N][i%N] == 1) B2.add(new Point(i/N, i%N));
        }

        Set<Point> Bset = new HashSet(B2);

        int ans = 0;
        Set<Point> seen = new HashSet();
        for (Point a: A2) for (Point b: B2) {
            Point delta = new Point(b.x - a.x, b.y - a.y);
            if (!seen.contains(delta)) {
                seen.add(delta);
                int cand = 0;
                for (Point p: A2)
                    if (Bset.contains(new Point(p.x + delta.x, p.y + delta.y)))
                        cand++;
                ans = Math.max(ans, cand);
            }
        }

        return ans;
    }
}

Approach #2: Count by Delta [Accepted]
Complexity Analysis
Time Complexity: O(N^4), where N is the length of A or B.
Space Complexity: O(N^2)

# 7ms 98.53%
class Solution {
    public int largestOverlap(int[][] A, int[][] B) {
        int N = A.length;
        int[][] count = new int[2 * N + 1][2 * N + 1];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (A[i][j] == 1) {
                    for (int i2 = 0; i2 < N; i2++) {
                        for (int j2 = 0; j2 < N; j2++) {
                            if (B[i2][j2] == 1)
                                count[i - i2 + N][j - j2 + N] += 1;
                        }
                    }
                }
            }
        }
        int ans = 0;
        for (int[] row: count)
            for (int v: row)
                ans = Math.max(ans, v);
        return ans;
    }
}

# 7ms 98.53%
class Solution {
    public int largestOverlap(int[][] A, int[][] B) {
        int n = A.length;
        int res = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                res = Math.max(res, Math.max(helper(A, B, i, j), helper(B, A, i, j)));
            }
        }
        return res;
    }

    public int helper(int[][] A, int[][] B, int offseti, int offsetj) {
        int n = A.length;
        int res = 0;
        for (int i = offseti; i < n; i++) {
            for (int j = offsetj; j < n; j++) {
                res += A[i][j] * B[i - offseti][j - offsetj];
            }
        }
        return res;
    }
}
'''