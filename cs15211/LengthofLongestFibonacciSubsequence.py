__source__ = 'https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/'
# Time:  O(N^2)
# Space: O(NlogM), where M is the largest element of A.
#
# Description: Leetcode # 873. Length of Longest Fibonacci Subsequence
#
# A sequence X_1, X_2, ..., X_n is fibonacci-like if:
#
# n >= 3
# X_i + X_{i+1} = X_{i+2} for all i + 2 <= n
# Given a strictly increasing array A of positive integers forming a sequence,
# find the length of the longest fibonacci-like subsequence of A.
# If one does not exist, return 0.
#
# (Recall that a subsequence is derived from another sequence A by deleting any number of elements
# (including none) from A, without changing the order of the remaining elements.
# For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].)
#
# Example 1:
#
# Input: [1,2,3,4,5,6,7,8]
# Output: 5
# Explanation:
# The longest subsequence that is fibonacci-like: [1,2,3,5,8].
# Example 2:
#
# Input: [1,3,7,11,12,14,18]
# Output: 3
# Explanation:
# The longest subsequence that is fibonacci-like:
# [1,11,12], [3,11,14] or [7,11,18].
#
#
# Note:
#
# 3 <= A.length <= 1000
# 1 <= A[0] < A[1] < ... < A[A.length - 1] <= 10^9
# (The time limit has been reduced by 50% for submissions in Java, C, and C++.)
#
import unittest
# 992ms 34.19%
class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        S = set(A)
        ans = 0
        for i in xrange(len(A)):
            for j in xrange(i+1, len(A)):
                """
                With the starting pair (A[i], A[j]),
                y represents the future expected value in
                the fibonacci subsequence, and x represents
                the most current value found.
                """
                x, y = A[j], A[i] + A[j]
                length = 2
                while y in S:
                    x, y = y, x + y
                    length += 1
                ans = max(ans, length)
        return ans if ans >= 3 else 0

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/solution/
#
Approach 1: Brute Force with Set
Complexity Analysis
Time Complexity: O(N^2logM), where N is the length of A, and M is the maximum value of A.
Space Complexity: O(N), the space used by the set S. 

# 110ms 28.72%
class Solution {
    public int lenLongestFibSubseq(int[] A) {
        int N = A.length;
        Set<Integer> S = new HashSet();
        for (int x: A) S.add(x);

        int ans = 0;
        for (int i = 0; i < N; ++i)
            for (int j = i+1; j < N; ++j) {
                /* With the starting pair (A[i], A[j]),
                 * y represents the future expected value in
                 * the fibonacci subsequence, and x represents
                 * the most current value found. */
                int x = A[j], y = A[i] + A[j];
                int length = 2;
                while (S.contains(y)) {
                    // x, y -> y, x+y
                    int tmp = y;
                    y += x;
                    x = tmp;
                    ans = Math.max(ans, ++length);
                }
            }

        return ans >= 3 ? ans : 0;
    }
}

Approach 2: Dynamic Programming
Complexity Analysis
Time Complexity: O(N^2), where N is the length of A.
Space Complexity: O(NlogM), where M is the largest element of A. 
We can show that the number of elements in a subsequence is bounded by O(logaM) 
where a is the minimum element in the subsequence. 

Let longest[i, j] be the longest path ending in [i, j]. 
Then longest[j, k] = longest[i, j] + 1 if (i, j) and (j, k) are connected. 
Since i is uniquely determined as A.index(A[k] - A[j]), 
this is efficient: we check for each j < k what i is potentially, 
and update longest[j, k] accordingly.

# 31ms 94.14%
class Solution {
    public int lenLongestFibSubseq(int[] A) {
        int n = A.length;
        int[][] dp = new int[n][n];
        int max = 0;
        for (int i = 2; i < n; i++) {
            int l = 0, r = i - 1;
            while (l < r) {
                int sum = A[l] + A[r];
                if (sum < A[i]) l++;
                else if (sum > A[i]) r--;
                else {
                    dp[r][i] = dp[l][r] + 1;
                    max = Math.max(max, dp[r][i]);
                    l++;
                    r--;
                }
                    
            }
        }
        return max == 0? 0 : max + 2;
    }
}

# 115ms 25.56%
class Solution {
    public int lenLongestFibSubseq(int[] A) {
        int N = A.length;
        Map<Integer, Integer> index = new HashMap();
        for (int i = 0; i < N; ++i)
            index.put(A[i], i);

        Map<Integer, Integer> longest = new HashMap();
        int ans = 0;

        for (int k = 0; k < N; ++k)
            for (int j = 0; j < k; ++j) {
                int i = index.getOrDefault(A[k] - A[j], -1);
                if (i >= 0 && i < j) {
                    // Encoding tuple (i, j) as integer (i * N + j)
                    int cand = longest.getOrDefault(i * N + j, 2) + 1;
                    longest.put(j * N + k, cand);
                    ans = Math.max(ans, cand);
                }
            }

        return ans >= 3 ? ans : 0;
    }
}

# 10ms 99.70%
class Solution {
    public int lenLongestFibSubseq(int[] A) {
        int n = A.length, ans = 0;
        for (int i = 0; i < n - 2 ; i++) {
            int pos = i + 2;
            for (int j = i + 1; j < n - 1; j++) {
                int sum = A[i] + A[j];
                while (pos < n && A[pos] < sum) pos++;
                if (pos == n) return ans;
                if (A[pos] != sum) continue;
                int b = sum, c = sum + A[j], len = 3, k = pos;
                while (true) {
                    while (k < n && A[k] < c) k++;
                    if (k == n) break;
                    if (A[k] != c) break;
                    len++;
                    c = c + b;
                    b = c - b;
                }
                ans = Math.max(ans, len);    
            }
            if (pos == n) break;
        }
        return ans;
    }
}
'''
