__source__ = 'https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/description/'
# Time:  O(N)
# Space: O(1)
#
# DP
#
# 1) if a1 < a2 and b1 < b2, then it is allowed to have both of these columns natural (unswapped),
# or both of these columns swapped. This possibility leads to n2 = min(n2, n1) and s2 = min(s2, s1 + 1).
#
# 2) Another, (not exclusive) possibility is that a1 < b2 and b1 < a2.
# This means that it is allowed to have exactly one of these columns swapped.
# This possibility leads to n2 = min(n2, s1) or s2 = min(s2, n1 + 1).
#
# Description: Leetcode # 801. Minimum Swaps To Make Sequences Increasing
#
# We have two integer sequences A and B of the same non-zero length.
#
# We are allowed to swap elements A[i] and B[i].
# Note that both elements are in the same index position in their respective sequences.
#
# At the end of some number of swaps, A and B are both strictly increasing.
# (A sequence is strictly increasing if and only if A[0] < A[1] < A[2] < ... < A[A.length - 1].)
#
# Given A and B, return the minimum number of swaps to make both sequences strictly increasing.
# It is guaranteed that the given input always makes it possible.
#
# Example:
# Input: A = [1,3,5,4], B = [1,2,3,7]
# Output: 1
# Explanation:
# Swap A[3] and B[3].  Then the sequences are:
# A = [1, 3, 5, 7] and B = [1, 2, 3, 4]
# which are both strictly increasing.
# Note:
#
# A, B are arrays with the same length, and that length will be in the range [1, 1000].
# A[i], B[i] are integer values in the range [0, 2000].
#
import unittest

#81.92% 32ms
class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n1, s1 = 0 ,1
        for i in xrange(1, len(A)):
            n2 = s2 = float("inf")
            if A[i-1] < A[i] and B[i-1] < B[i]:
                n2 = min(n2, n1)
                s2 = min(s2, s1 + 1)
            if A[i-1] < B[i] and B[i-1] < A[i]:
                n2 = min(n2, s1)
                s2 = min(s2, n1 + 1)
            n1, s1 = n2, s2
        return min(n1, s1)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/solution/
# 100% 4ms
#
class Solution {
    public int minSwap(int[] A, int[] B) {
        int swap = 1;
        int noswap = 0;
        for(int i = 1; i < A.length; i++) {
            if(A[i-1] >= B[i] || B[i-1] >= A[i]) {
                swap++;
            } else if(A[i-1] >= A[i] || B[i-1] >= B[i]) {
                int temp = swap;
                swap = noswap + 1;
                noswap = temp;
            } else {
                int min = Math.min(swap, noswap);
                swap = min+1;
                noswap = min;
            }
        }
        return Math.min(swap, noswap);
    }
}

#118ms 65.67%
class Solution {
    public int orderOfLargestPlusSign(int N, int[][] mines) {
        int[][] grid = new int[N][N], dp = new int[N][N];
        for (int i = 0; i < mines.length; i++) {
            grid[mines[i][0]][mines[i][1]] = 1;
        }

        // left
        for (int i = 0; i < N; i++) {
            int count = 0;
            for (int j = 0; j < N; j++) {
                if (grid[i][j] == 1) count = 0;
                else count++;
                dp[i][j] = count;
            }
        }
        // right
        for (int i = 0; i < N; i++) {
            int count = 0;
            for (int j = N - 1; j >= 0; j--) {
                if (grid[i][j] == 1) count = 0;
                else count++;
                dp[i][j] = Math.min(count, dp[i][j]);
            }
        }

        //up
        for (int i = 0; i < N; i++) {
            int count = 0;
            for (int j = 0; j < N; j++) {
                if (grid[j][i] == 1) count = 0;
                else count++;
                dp[j][i] = Math.min(count, dp[j][i]);
            }
        }

        //down
        for (int i = 0; i < N; i++) {
            int count = 0;
            for (int j = N -1; j >= 0; j--) {
                if (grid[j][i] == 1) count = 0;
                else count++;
                dp[j][i] = Math.min(count, dp[j][i]);
            }
        }

        int ans = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                ans = Math.max(ans, dp[i][j]);
            }
        }
        return ans;
    }
}
'''