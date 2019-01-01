__source__ = 'https://leetcode.com/problems/valid-permutations-for-di-sequence/'
# Time:  O(N^2)
# Space: O(N^2)
#
# Description: Leetcode # 903. Valid Permutations for DI Sequence
#
# We are given S, a length n string of characters from the set {'D', 'I'}.
# (These letters stand for "decreasing" and "increasing".)
#
# A valid permutation is a permutation P[0], P[1], ..., P[n] of integers {0, 1, ..., n}, such that for all i:
#
# If S[i] == 'D', then P[i] > P[i+1], and;
# If S[i] == 'I', then P[i] < P[i+1].
# How many valid permutations are there?  Since the answer may be large, return your answer modulo 10^9 + 7.
#
# Example 1:
#
# Input: "DID"
# Output: 5
# Explanation:
# The 5 valid permutations of (0, 1, 2, 3) are:
# (1, 0, 3, 2)
# (2, 0, 3, 1)
# (2, 1, 3, 0)
# (3, 0, 2, 1)
# (3, 1, 2, 0)
#
# Note:
#
# 1 <= S.length <= 200
# S consists only of characters from the set {'D', 'I'}.
#
import unittest


class Solution(object):
    pass  # your function here


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/valid-permutations-for-di-sequence/solution/
Approach 1: Dynamic Programming
Complexity Analysis
Time Complexity: O(N^3), where N is the length of S, or O(N^2) with the optimized version.
Space Complexity: O(N^2)
# https://leetcode.com/problems/valid-permutations-for-di-sequence/discuss/196939/Easy-to-understand-solution-with-detailed-explanation
# Before diving into the state transition function, let us first start with a simple example.
# 
# 1. a simple example
# In the following discussion, for simplification, I will use both notation DI-seq and DI-rule instead of DI sequence.
# 
# Consider a permutation 1032, which is based on a DI-seq "DID", 
# how to use it to construct a new instance ending at 2 and based on DI-seq "DIDD"?
# 
# Method:
# step 1.
# for the original permutation 1032, we add 1 to the digits that are larger than or equal to 2.
# 
# 1032->1043
#   ^^
# step 2.
# then directly append 2 to 1043, i.e., 1043 -> 10432
# 
# Remark on step 1:
# (1) By performing add operation, 2 in the original permutation now becomes 3, 
# and thus there is no duplicate element for the new arrival 2.
# (2) More importantly, such operation on the digits will not break the original DI-rule. 
# e.g., 1043 still keeps its old DI-rule, i.e., "DID". The proof is straight-forward, you can validate yourself.
# 
# Now a new permutation with DI-rule "DIDD" and ending at 2 has been constructed from 1032, namely 10432.
# 
# With the same spirit, using 1032("DID"), we can construct instances with DI-rule "DIDD": 
# 20431(ending with 1), 21430(ending with 0).
# (Note that the instance(based on "DIDD") which ends with 3 can not be constructed.)
# 
# Similarly, from 1032("DID"), 
# we can construct instances with DI-rule "DIDI": 10423(ending with 3), 10324(ending with 4).
# (Note that the instance(based on "DIDI") which ends with 1 or 2 can not be constructed.)
# 
# 2. state transition function
# With the example above in mind, the transition function seems to be clear.
# 
# Given a string DI-seq S, let dp[i][j] represents the number of permutation of number 
# 0, 1, ... , i, satisfying DI-rule S.substr(0, i), and ending with digit j.
# 
# if(S[i-1] == 'D')
#    dp[i][j] = dp[i-1][j] + dp[i-1][j+1] + ... + dp[i-1][i-1]
# 
# if(S[i-1] == 'I') 
#    dp[i][j] = dp[i-1][0] + dp[i-1][1] + ... + dp[i-1][j-1]
# 
# 48ms 38.85%
class Solution {
    public int numPermsDISequence(String S) {
        int MOD = 1_000_000_007;
        int N = S.length();

        // dp[i][j] : Num ways to place P_i with relative rank j
        int[][] dp = new int[N+1][N+1];
        Arrays.fill(dp[0], 1);

        for (int i = 1; i <= N; i++) {
            for (int j = 0; j <= i; j++) {
                if (S.charAt(i - 1) == 'D') {
                    for (int k = j; k < i; k++) {
                        dp[i][j] += dp[i - 1][k];
                        dp[i][j] %= MOD;
                    }
                } else {
                    for (int k = 0; k < j; k++) {
                        dp[i][j] += dp [i - 1][k];
                        dp[i][j] %= MOD;
                    }
                }
            }
        }
        int ans = 0;
        for (int x : dp[N]) {
            ans += x;
            ans %= MOD;
        }
        return ans;
    }
}


Approach 2: Divide and Conquer
Complexity Analysis
Time Complexity: O(N^2), where N is the length of S.
Space Complexity: O(N^2)

# Improved 2-D DP
# https://leetcode.com/problems/valid-permutations-for-di-sequence/discuss/168278/C%2B%2BJavaPython-DP-Solution-O(N2)
# dp[i][j] means the number of possible permutations of first i + 1 digits,
# where the i + 1th digit is j + 1th smallest in the rest of digits.
# Explanation:
# As shown in the diagram,
# for "I", we calculate prefix sum of the array,
# for "D", we calculate sufixsum of the array.
# 9ms 68.15%
class Solution {
    public int numPermsDISequence(String S) {
        int n = S.length(), mod = (int) 1e9 + 7;
        int[][] dp = new int[n + 1][n  +1];
        for (int j = 0; j <= n; j++) dp[0][j] = 1;
        for (int i = 0; i < n; i++) {
            if (S.charAt(i) == 'I') {
                for (int j = 0, cur = 0; j < n - i; j++) {
                    dp[i + 1][j] = cur = (cur + dp[i][j]) % mod;
                }
            } else {
                for (int j = n - i - 1, cur = 0; j >= 0; j--) {
                    dp[i + 1][j] = cur = (cur + dp[i][j + 1]) % mod;
                }
            }
        }
        return dp[n][0];
    }
}

# https://leetcode.com/problems/valid-permutations-for-di-sequence/discuss/168612/Top-down-with-Memo-greater-Bottom-up-DP-greater-N3-DP-greater-N2-DP-greater-O(N)-space
# Intuition: Insert the largest number into appropriate postion.
# eg. s='IIDD', we can only insert 4 between I and D. 
# We break the remained numbers 0, 1, 2, 3 into two groups both with the size of 2. 
# We have C(4, 2) possible combinations. Then helper("IIDD") = helper("I") * helper("D") * C(4, 2).
#
# C(n, r) = C(n - 1, r - 1) + C(n - 1, r)
# C(n, 0) = C(n, n) = 1
# Working of Above formula and Pascal Triangle:
# Let us see how above formula works for C(4,3)
# 
# 1==========>> n = 0, C(0,0) = 1
# 1-1========>> n = 1, C(1,0) = 1, C(1,1) = 1
# 1-2-1======>> n = 2, C(2,0) = 1, C(2,1) = 2, C(2,2) = 1
# 1-3-3-1====>> n = 3, C(3,0) = 1, C(3,1) = 3, C(3,2) = 3, C(3,3)=1
# 1-4-6-4-1==>> n = 4, C(4,0) = 1, C(4,1) = 4, C(4,2) = 6, C(4,3)=4, C(4,4)=1
# So here every loop on i, builds i'th row of pascal triangle, using (i-1)th row
# 
# Extension of above formula for modular arithmetic:
# We can use distributive property of modulor operator to find nCr % p using above formula.
# 
#    C(n, r) % p = [ C(n-1, r-1)% p + C(n-1, r)% p ] % p
#    C(n, 0) = C(n, n) = 1
#
# DFS + Memo
# Time complexity: O(n^4)
# 308ms 6.58%
class Solution {
    private int M = (int)1e9 + 7;
    private int[][] nCkMemo;
    public int numPermsDISequence(String S) {
        int n = S.length();
        nCkMemo = new int[n + 1][n + 1];
        return (int)helper(S, new HashMap<>());
    }
    private long helper(String s, Map<String, Long> map) {
        if (s.equals("")) {
            return 1;
        }
        if (map.containsKey(s)) {
            return map.get(s);
        }
        long result = 0;
        int n = s.length();
        if (s.charAt(0) == 'D') {
            result += helper(s.substring(1), map);
            result %= M;
        }
        if (s.charAt(n - 1) == 'I') {
            result += helper(s.substring(0, n - 1), map);
            result %= M;
        }
        for (int i = 1; i < n; i++) {
            if (s.charAt(i - 1) == 'I' && s.charAt(i) == 'D') {
                long left = helper(s.substring(0, i - 1), map);
                long right = helper(s.substring(i + 1), map);
                result += (((left * right) % M) * nCk(n, i)) % M;
                result %= M;
            }
        }
        map.put(s, result);
        return result;
    }
    private int nCk(int n, int k) {
        if (k == 0 || k == n) {
            return 1;
        }
        if (nCkMemo[n][k] == 0) {
            nCkMemo[n][k] = (nCk(n - 1, k) + nCk(n - 1, k - 1)) % M;
        }
        return nCkMemo[n][k];
    }
}
'''
