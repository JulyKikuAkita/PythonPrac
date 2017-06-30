__source__ = 'https://leetcode.com/problems/house-robber-ii/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/house-robber-ii.py
# Time:  O(n)
# Space: O(1)
#
# Note: This is an extension of House Robber.
#
# After robbing those houses on that street, the thief has found himself a new place
# for his thievery so that he will not get too much attention. This time, all houses
# at this place are arranged in a circle. That means the first house is the neighbor
# of the last one. Meanwhile, the security system for these houses remain the same as
# for those in the previous street.
#
# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police.
#
# Companies
# Microsoft
# Related Topics
# Dynamic Programming
# Similar Questions
# House Robber Paint House Paint Fence House Robber III Non-negative Integers without Consecutive Ones
#
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]
        return max(self.robRange(nums, 0, len(nums) - 1) , self.robRange(nums, 1, len(nums)))

    def robRange(self, nums, start, end):
        num_i, num_i_1 = nums[start], 0
        for i in xrange(start + 1, end):
            num_i_1, num_i_2 = num_i, num_i_1
            num_i = max(nums[i] + num_i_2, num_i_1)
        return num_i

if __name__ == '__main__':
        print Solution().rob([8,4,8,5,9,6,5,4,4,10])

#java
ans='''
public class Solution {
    public int rob(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        } else if (nums.length == 1) {
            return nums[0];
        }
        return Math.max(rob(nums, 0, nums.length - 2), rob(nums, 1, nums.length - 1));
    }

    private int rob(int[] nums, int start, int end) {
        int odd = 0;
        int even = 0;
        for (int i = start; i <= end; i++) {
            if (i % 2 == 0) {
                even = Math.max(even + nums[i], odd);
            } else {
                odd = Math.max(odd + nums[i], even);
            }
        }
        return Math.max(odd, even);
    }
}

60%
public class Solution {
    public int rob(int[] nums) {
        if(nums == null || nums.length == 0) return 0;
        if(nums.length == 1) return nums[0];

        return Math.max(rob1(nums, 0, nums.length - 2) , rob1(nums, 1, nums.length -1));
    }

    public int rob1(int[] nums, int start, int end) {
        if (end - start <= 1) return nums[start];  //for case: [0,0]
        int[] dp = new int[nums.length];
        dp[start] = nums[start];
        dp[start + 1] = Math.max(nums[start], nums[start+1]); //same as nums.length = 2

        for (int i = start + 2; i <= end ; i++){
            dp[i] = Math.max(dp[i-2] + nums[i], dp[i-1]);
        }
        return dp[end];

    }
}
'''