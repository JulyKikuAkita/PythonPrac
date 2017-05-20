__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/burst-balloons.py
# Time:  O(n^3)
# Space: O(n^2)

# Given n balloons, indexed from 0 to n-1.
# Each balloon is painted with a number on it
# represented by array nums.
# You are asked to burst all the balloons.
# If the you burst balloon i you will get
# nums[left] * nums[i] * nums[right] coins.
# Here left and right are adjacent indices of i.
# After the burst, the left and right then
# becomes adjacent.
#
# Find the maximum coins you can collect by
# bursting the balloons wisely.
#
# Note:
# (1) You may imagine nums[-1] = nums[n] = 1.
#     They are not real therefore you can not burst them.
# (2) 0 <= n <= 500, 0 <= nums[i] <= 100
#
# Example:
#
# Given [3, 1, 5, 8]
#
# Return 167
#
#     nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
#
# Google
# dp[l][r] = max(dp[l][r], nums[l] * nums[m] * nums[r] + dp[l][m] + dp[m][r])

# https://leetcode.com/discuss/72216/share-some-analysis-and-explanations
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        coins = [1] + [ i for i in nums if i > 0 ] + [1]
        n = len(coins)
        max_coins = [[ 0 for _ in xrange(n)] for _ in xrange(n)]

        for k in xrange(2, n):
            for left in xrange(n - k):
                right = left + k
                for i in xrange(left + 1, right):
                    max_coins[left][right] = max(max_coins[left][right], \
                                                 coins[left] * coins[i] * coins[right] + \
                                                 max_coins[left][i] + max_coins[i][right])
        return max_coins[0][-1]

#DFS
# https://www.hrwhisper.me/leetcode-burst-balloons/
class Solution2(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[ 0 for j in xrange( n + 2)] for i in xrange(n+2)]
        return self.dfs(1, n, dp, nums)

    def dfs(self, i, j , dp, nums):
        if dp[i][j] > 0:
            return dp[i][j]
        for k in xrange(i, j +1):
            dp[i][j] = max(dp[i][j], nums[i-1] * nums[k] * nums[j+1] + self.dfs(i, k-1, dp, nums) + self.dfs(k+1, j, dp,nums))
        return dp[i][j]

#java
js = '''
public class Solution {
    public int maxCoins(int[] nums) {
        int len = nums.length + 2;
        int[] newNums = new int[len];
        newNums[0] = 1;
        newNums[len - 1] = 1;
        for (int i = 0; i < len - 2; i++) {
            newNums[i + 1] = nums[i];
        }
        int[][] dp = new int[len][len];
        for (int diff = 2; diff < len; diff++) {
            for (int i = 0; i < len - diff; i++) {
                int j = i + diff;
                for (int k = i + 1; k < j; k++) {
                    dp[i][j] = Math.max(dp[i][j], newNums[i] * newNums[k] * newNums[j] + dp[i][k] + dp[k][j]);
                }
            }
        }
        return dp[0][len - 1];
    }
}
'''