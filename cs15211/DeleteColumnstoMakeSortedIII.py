__source__ = 'https://leetcode.com/problems/delete-columns-to-make-sorted-iii/'
# Time:  O(N * W^2)
# Space: O(W)
#
# Description: Leetcode # 960. Delete Columns to Make Sorted III
#
# We are given an array A of N lowercase letter strings, all of the same length.
#
# Now, we may choose any set of deletion indices, and for each string,
# we delete all the characters in those indices.
#
# For example, if we have an array A = ["babca","bbazb"] and deletion indices {0, 1, 4},
# then the final array after deletions is ["bc","az"].
#
# Suppose we chose a set of deletion indices D such that after deletions,
# the final array has every element (row) in lexicographic order.
#
# For clarity, A[0] is in lexicographic order (ie. A[0][0] <= A[0][1] <= ... <= A[0][A[0].length - 1]),
# A[1] is in lexicographic order (ie. A[1][0] <= A[1][1] <= ... <= A[1][A[1].length - 1]), and so on.
#
# Return the minimum possible value of D.length.
#
# Example 1:
#
# Input: ["babca","bbazb"]
# Output: 3
# Explanation: After deleting columns 0, 1, and 4, the final array is A = ["bc", "az"].
# Both these rows are individually in lexicographic order (ie. A[0][0] <= A[0][1] and A[1][0] <= A[1][1]).
# Note that A[0] > A[1] - the array A isn't necessarily in lexicographic order.
#
# Example 2:
#
# Input: ["edcba"]
# Output: 4
# Explanation: If we delete less than 4 columns, the only row won't be lexicographically sorted.
#
# Example 3:
#
# Input: ["ghi","def","abc"]
# Output: 0
# Explanation: All rows are already lexicographically sorted.
#
# Note:
#
#     1 <= A.length <= 100
#     1 <= A[i].length <= 100
#
import unittest
# 288ms 49.08%
class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        W = len(A[0])
        dp = [1] * W
        for i in xrange(W-2, -1, -1):
            for j in xrange(i+1, W):
                if all(row[i] <= row[j] for row in A):
                    dp[i] = max(dp[i], 1 + dp[j])

        return W - max(dp)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/delete-columns-to-make-sorted-iii/solution/
#
Approach 1: Dynamic Programming
Complexity Analysis
Time Complexity: O(N * W^2), where N is the length of A, and W is the length of each word in A.
Space Complexity: O(W)
# 22ms 22.78%
class Solution {
    public int minDeletionSize(String[] A) {
        int W = A[0].length();
        int[] dp = new int[W];
        Arrays.fill(dp, 1);
        for (int i = W-2; i >= 0; --i)
            search: for (int j = i+1; j < W; ++j) {
                for (String row: A)
                    if (row.charAt(i) > row.charAt(j))
                        continue search;

                dp[i] = Math.max(dp[i], 1 + dp[j]);
            }

        int kept = 0;
        for (int x: dp)
            kept = Math.max(kept, x);
        return W - kept;
    }
}

# 25ms 16.38%
class Solution {
    public int minDeletionSize(String[] A) {
        if (A == null || A.length <= 0) return -1;
        int n = A.length;
        int m = A[0].length();
        int[] dp = new int[m];
        dp[0] = 1;
        int res = 0;
        for (int i = 1; i < m; i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++) {
                int tmp = dp[j] + 1;
                for (int k = 0; k < n; k++) {
                    if (A[k].charAt(i) < A[k].charAt(j)) {
                        tmp = 1;
                        break;
                    }
                }
                dp[i] = Math.max(dp[i], tmp);
            }
            res = Math.max(res, dp[i]);
        }
        return m - res;
    }
}
'''
