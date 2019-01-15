# coding=utf-8
__source__ = 'https://leetcode.com/problems/tallest-billboard/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 956. Tallest Billboard
#
# You are installing a billboard and want it to have the largest height.
# The billboard will have two steel supports, one on each side.
# Each steel support must be an equal height.
#
# You have a collection of rods which can be welded together.
# For example, if you have rods of lengths 1, 2, and 3,
# you can weld them together to make a support of length 6.
#
# Return the largest possible height of your billboard installation.
# If you cannot support the billboard, return 0.
#
# Example 1:
#
# Input: [1,2,3,6]
# Output: 6
# Explanation: We have two disjoint subsets {1,2,3} and {6}, which have the same sum = 6.
#
# Example 2:
#
# Input: [1,2,3,4,5,6]
# Output: 10
# Explanation: We have two disjoint subsets {2,3,5} and {4,6}, which have the same sum = 10.
#
# Example 3:
#
# Input: [1,2]
# Output: 0
# Explanation: The billboard cannot be supported, so we return 0.
#
# Note:
#
#     0 <= rods.length <= 20
#     1 <= rods[i] <= 1000
#     The sum of rods is at most 5000.
#

import unittest
# 1424ms 50%
class Solution(object):
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        def make(A):
            states = {(0, 0)}
            for x in A:
                states |= ({(a+x, b) for a, b in states} |
                           {(a, b+x) for a, b in states})

            delta = {}
            for a, b in states:
                delta[a-b] = max(delta.get(a-b, 0), a)
            return delta

        N = len(rods)
        Ldelta = make(rods[:N/2])
        Rdelta = make(rods[N/2:])

        ans = 0
        for d in Ldelta:
            if -d in Rdelta:
                ans = max(ans, Ldelta[d] + Rdelta[-d])
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/tallest-billboard/solution/
Approach 1: Dynamic Programming
Complexity Analysis
Time Complexity: O(NS), where N is the length of rods, and S is the maximum of ∑rods[i].
Space Complexity: O(NS)
The recursion is dp[i][s] = max(dp[i+1][s], dp[i+1][s-rods[i]], rods[i] + dp[i+1][s+rods[i]]).

# 55ms 100%
class Solution {
    int NINF = Integer.MIN_VALUE / 3;
    Integer[][] memo;

    public int tallestBillboard(int[] rods) {
        int N = rods.length;
        // "memo[n][x]" will be stored at memo[n][5000+x]
        // Using Integer for default value null
        memo = new Integer[N][10001];
        return (int) dp(rods, 0, 5000);
    }

    private int dp(int[] rods, int i, int s) {
        if (i == rods.length) {
            return s == 5000 ? 0 : NINF;
        } else if (memo[i][s] != null) {
            return memo[i][s];
        } else {
            int ans = dp(rods, i + 1, s);
            ans = Math.max(ans, dp(rods, i + 1, s - rods[i]));
            ans = Math.max(ans, rods[i] + dp(rods, i + 1, s + rods[i]));
            memo[i][s] = ans;
            return ans;
        }
    }
}

# This is a knapsack problem.
# dp[i][j] represents whether the sum of first i numbers can be j - 5000. dp[0][5000] = true.
# Then dp[i + 1][j] = dp[i][j - rods[i]] | dp[i][j + rods[i]] | dp[i][j].
# max[i][j] represents the largest sum of all positive numbers when the sum of first i numbers is j - 5000.
#
# Time complexity: O(N*sum)
# P.S. This solution can be optimized to O(sum) space and use max array only.


# 79ms 66.67%
class Solution {
    public int tallestBillboard(int[] rods) {
        int n = rods.length;
        boolean[][] dp = new boolean[n + 1][10001];
        int[][] max = new int[n + 1][10001];
        dp[0][5000] = true;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= 10000; j++) {
                if (j - rods[i] >= 0 && dp[i][j - rods[i]]) {
                    dp[i + 1][j] = true;
                    max[i + 1][j] = Math.max(max[i + 1][j], max[i][j - rods[i]] + rods[i]);
                }
                if (j + rods[i] <= 10000 && dp[i][j + rods[i]]) {
                    dp[i + 1][j] = true;
                    max[i + 1][j] = Math.max(max[i + 1][j], max[i][j + rods[i]]);
                }
                if (dp[i][j]) {
                    dp[i + 1][j] = true;
                    max[i + 1][j] = Math.max(max[i + 1][j], max[i][j]);
                }
            }
        }
        return max[n][5000];
    }
}

Approach 2: Meet in the Middle
Complexity Analysis
Time Complexity: O(3^N/2), where N is the length of rods.
Space Complexity: O(3^N/2).

# 209ms 0%
import java.awt.Point;
class Solution {
    public int tallestBillboard(int[] rods) {
        int N = rods.length;
        Map<Integer, Integer> Ldelta = make(Arrays.copyOfRange(rods, 0, N/2));
        Map<Integer, Integer> Rdelta = make(Arrays.copyOfRange(rods, N/2, N));
        int ans = 0;
        for (int d: Ldelta.keySet()) {
            if (Rdelta.containsKey(-d))
                ans = Math.max(ans, Ldelta.get(d) + Rdelta.get(-d));
        }
        return ans;
    }

    private Map<Integer, Integer> make(int[] A) {
        Point[] dp = new Point[60000];
        int t = 0;
        dp[t++] = new Point(0, 0);
        for (int v : A) {
            int stop = t;
            for (int i = 0; i < stop; ++i) {
                Point p = dp[i];
                dp[t++] = new Point(p.x + v, p.y);
                dp[t++] = new Point(p.x, p.y + v);
            }
        }

        Map<Integer, Integer> ans = new HashMap();
        for (int i = 0; i < t; i++) {
            int a = dp[i].x;
            int b = dp[i].y;
            ans.put(a - b, Math.max(ans.getOrDefault(a - b, 0), a));
        }
        return ans;
    }
}

'''