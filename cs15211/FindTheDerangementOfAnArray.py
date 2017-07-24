__source__ = 'https://leetcode.com/problems/find-the-derangement-of-an-array/description/'
# Time:  O(n)
# Space: O(n)
#
# Description: Leetcode # 634. Find the Derangement of An Array
#
# In combinatorial mathematics, a derangement is a permutation of the elements of a set,
# such that no element appears in its original position.
#
# There's originally an array consisting of n integers from 1 to n in ascending order,
# you need to find the number of derangement it can generate.
#
# Also, since the answer may be very large, you should return the output mod 109 + 7.
#
# Example 1:
# Input: 3
# Output: 2
# Explanation: The original array is [1,2,3]. The two derangements are [2,3,1] and [3,1,2].
# Note:
# n is in the range of [1, 106].
#
# Companies
# IXL
# Related Topics
# Math
# Similar to Climbing Stairs
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
#Thought:

For the k th element, it has k-1 positions and there are two possibilities for its position

1.It's not in the first element, so it's going to be the same thing as D(n - 1)

2.It's in the position of the first element,so there are two elements in the deranged position.
So it's going to be the same thing as D(n - 2)

so res = ((i-1)(dn1+dn2))%1000000007;*
why we use long not int:
a(11) = 14684570
a(12) = 176214841
a(13) = 12 * (a(12) + a(11)) = 2290792932 > Integer.MAX_VALUE

The Staggered formula is D(n) = (n-1) [D(n-2) + D(n-1)]:
# DFS using D(n) = (n-1) [D(n-2) + D(n-1)]

Approach #2 Using Recursion [Stack Overflow]

# Line 13: java.lang.StackOverflowError
public class Solution {
    public int findDerangement(int n) {
        Integer[] memo = new Integer[n + 1];
        return find(n, memo);
    }
    public int find(int n, Integer[] memo) {
        if (n == 0)
            return 1;
        if (n == 1)
            return 0;
        if (memo[n] != null)
            return memo[n];
        memo[n] = (int)(((n - 1L) * (find(n - 1, memo) + find(n - 2, memo))) % 1000000007);
        return memo[n];
    }
}

Approach #4 Constant Space Dynamic Programming [Accepted]:
# 72.95% 19ms
public class Solution {
    public int findDerangement(int n) {
        if (n == 0)
            return 1;
        if (n == 1)
            return 0;
        int first = 1, second = 0;
        for (int i = 2; i <= n; i++) {
            int temp = second;
             //    dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2]);
            second = (int)(((i - 1L) * (first + second)) % 1000000007);
            first = temp;
        }
        return second;
    }
}

class Solution {
    public int findDerangement(int n) {
        int one = 1;
        int two = 0;
        int MOD = 1000000007;

    //    dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2]);
        if (n < 2) {
            return (0);
        }

        for (int i = 3; i <= n; i++) {
            int cur = (int)(((i - 1) *((long)(one + two))) % MOD);

            two = one;
            one = cur;
        }

        return (one);
    }
}

Approach #5 Using Formula [Accepted]:

class Solution {
    private static final int M = 1000000007;
        public int findDerangement(int n) {
            long ans = 1;
            for (int i = 1; i <= n; i++)
                ans = (i * ans % M + (i % 2 == 0 ? 1 : -1)) % M;
            return (int) ans;
        }
}
'''