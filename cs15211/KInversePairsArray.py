__source__ = 'https://leetcode.com/problems/k-inverse-pairs-array/'
# Approach #7 1-D dynamic Programmming [Accepted]:
# Time O(n * k) dp array of size k+1k+1 is filled n+1n+1 times
# Space O(n) dpdp array of size (k+1)(k+1) is used.
#
# Description: Leetcode # 629. K Inverse Pairs Array
#
# Given two integers n and k, find how many different arrays consist of numbers from 1 to n
# such that there are exactly k inverse pairs.
#
# We define an inverse pair as following: For ith and jth element in the array,
# if i < j and a[i] > a[j] then it's an inverse pair; Otherwise, it's not.
#
# Since the answer may be very large, the answer should be modulo 109 + 7.
#
# Example 1:
# Input: n = 3, k = 0
# Output: 1
# Explanation:
# Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pair.
# Example 2:
# Input: n = 3, k = 1
# Output: 2
# Explanation:
# The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
# Note:
# The integer n is in the range [1, 1000] and k is in the range [0, 1000].
#
# Companies
# Works Applications
# Related Topics
# Dynamic Programming
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
# Thought: https://leetcode.com/problems/k-inverse-pairs-array/solution/

This rule of displacements holds true because,
whenever a number is shifted y times towards the left starting from the array a0,
after the shift, y numbers smaller than it lie towards its right, giving a total of y inverse pairs.

# 27ms 64.95%
class Solution {
     public static int kInversePairs(int n, int k) {
            int mod = 1000000007;
            if (k > n*(n-1)/2 || k < 0) return 0;
            if (k == 0 || k == n*(n-1)/2) return 1;
            long[][] dp = new long[n+1][k+1];
            dp[2][0] = 1;
            dp[2][1] = 1;
            for (int i = 3; i <= n; i++) {
                dp[i][0] = 1;
                for (int j = 1; j <= Math.min(k, i*(i-1)/2); j++) {
                    dp[i][j] = dp[i][j-1] + dp[i-1][j];
                    if (j >= i) dp[i][j] -= dp[i-1][j-i];
                    dp[i][j] = (dp[i][j]+mod) % mod;
                }
            }
            return (int) dp[n][k];
        }
}

Approach #7 1-D dynamic Programmming [Accepted]:
Time O(n * k) dp array of size k+1k+1 is filled n+1n+1 times
Space O(n) dpdp array of size (k+1)(k+1) is used.

# 11ms 100%
class Solution {
    public int kInversePairs(int n, int k) {
        int[] d = new int[k+1];
        d[0] = 1;
        for(int i = 2;i <= n;i++){
           for(int j = 1;j <= k;j++){
                d[j] = (d[j] + d[j-1]) % 1000000007;
           }
           for(int j = k;j >= i;j--){
                d[j] = (d[j] - d[j-i] + 1000000007) % 1000000007;
           }
        }
        return d[k];
    }
}

Approach #2 Using Recursion with memoization [Time Limit Exceeded]
Time O(n^2 * k)
Space O(n)
# TLE
class Solution {
    Integer[][] memo = new Integer[1001][1001];
    public int kInversePairs(int n, int k) {
        if (n == 0)
            return 0;
        if (k == 0)
            return 1;
        if (memo[n][k] != null)
            return memo[n][k];
        int inv = 0;
        for (int i = 0; i <= Math.min(k, n - 1); i++)
            inv = (inv + kInversePairs(n - 1, k - i)) % 1000000007;
        memo[n][k] = inv;
        return inv;
    }
}



'''