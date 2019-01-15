__source__ = 'https://leetcode.com/problems/maximum-length-of-pair-chain/'
# Time:  O(nlogn)
# Space: O(1)
#
# Description: Leetcode # 646. Maximum Length of Pair Chain
#
# You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.
#
# Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c.
# Chain of pairs can be formed in this fashion.
#
# Given a set of pairs, find the length longest chain which can be formed.
# You needn't use up all the given pairs. You can select pairs in any order.
#
# Example 1:
# Input: [[1,2], [2,3], [3,4]]
# Output: 2
# Explanation: The longest chain is [1,2] -> [3,4]
# Note:
# The number of given pairs will be in the range [1, 1000].
# Companies
# Amazon
# Related Topics
# Dynamic Programming
# Similar Questions
# Longest Increasing Subsequence Increasing Subsequences
#

import unittest
# 44ms 98.46%
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        cur, res = float('-inf'), 0
        for p in sorted(pairs, key=lambda x: x[1]):
            if cur < p[0]: cur, res = p[1], res + 1
        return res

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/maximum-length-of-pair-chain/solution/

This is equivalent to interval scheduling problem.
# 123ms 23.24%
class Solution {
    public int findLongestChain(int[][] pairs) {
        Arrays.sort(pairs, (a,b) -> a[1] - b[1]);
        int sum = 0, n = pairs.length, i = -1;
        while (++i < n) {
            sum++;
            int curEnd = pairs[i][1];
            while (i+1 < n && pairs[i+1][0] <= curEnd) i++;
        }
        return sum;
    }
}

# 31ms 89.86%
class Solution {
    public int findLongestChain(int[][] pairs) {
        if(pairs == null || pairs.length == 0 || pairs[0].length == 0){
            return 0;
        }

        Arrays.sort(pairs, new Comparator<int[]>(){
           public int compare(int[] pair1, int[] pair2){
               return Integer.compare(pair1[1], pair2[1]);
           }
        });

        int res = 1;
        int[] cur = pairs[0];
        for(int i = 1 ; i < pairs.length; i++){
            if(pairs[i][0] > cur[1]){
                res++;
                cur = pairs[i];
            }
        }
        return res;
    }
}

# DP
# 115ms 27.75%
class Solution {
    public int findLongestChain(int[][] pairs) {
        Arrays.sort(pairs, (a, b) -> (a[0] - b[0]));

        int i, j, max = 0, n = pairs.length;
        int dp[] = new int[n];

        for (i = 0; i < n; i++) dp[i] = 1;
        for (i = 1; i < n; i++)
            for (j = 0; j < i; j++)
                if (pairs[i][0] > pairs[j][1] && dp[i] < dp[j] + 1)
                    dp[i] = dp[j] + 1;
        for (i = 0; i < n; i++) if (max < dp[i]) max = dp[i];
        return max;
    }
}
'''
