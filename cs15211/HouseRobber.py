__source__ = 'https://leetcode.com/problems/house-robber/#/description'
# Time:  O(n)
# Space: O(1)
#
# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security system connected
# and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police.
#
# Companies
# LinkedIn Airbnb
# Related Topics
# Dynamic Programming
# Similar Questions
# Maximum Product Subarray House Robber II Paint House Paint Fence House Robber III Non-negative Integers without Consecutive Ones
#

class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        if len(num) == 0:
            return 0
        if len(num) == 1:
            return num[0]
        num_i, num_i_1 = max(num[1], num[0]), num[0]
        for i in xrange(2, len(num)):
            num_i_1, num_i_2 = num_i, num_i_1
            num_i = max(num[i] + num_i_2, num_i_1)
        return num_i

# http://www.programcreek.com/2014/03/leetcode-house-robber-java/
class SolutionJava:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        if not num or len(num) < 0:
            return 0

        odd, even = 0, 0
        for i in xrange(len(num)):
            if i % 2 == 0:
                even += num[i]
                even = max(even, odd)
            else:
                odd += num[i]
                odd = max(even, odd)
        return max(even, odd)



if __name__ == '__main__':
        #print Solution().rob([8,4,8,5,9,6,5,4,4,10])
        print Solution().rob([10,100,1000,10000])
        print SolutionJava().rob([10,100,1000,10000])

#Java
Java = '''
Thought: https://leetcode.com/problems/house-robber/#/solution
f(k) = max(f(k-2) + Ak, f(k-1))

public class Solution {
    public int rob(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        int[] dp = new int[2];
        dp[0] = nums[0];
        int index = 1;
        for (int i = 1; i < nums.length; i++) {
            dp[index] = Math.max(dp[index] + nums[i], dp[1 - index]);
            index = 1 - index;
        }
        return dp[1 - (nums.length & 1)];
    }
}

37.20%
public class Solution {
    public int rob(int[] nums) {
        int rob = 0; //max monney can get if rob current house
        int notRob = 0; //max money can get if not rob current house
        for(int i = 0; i < nums.length; i++) {
            int curRob = notRob + nums[i];
            notRob = Math.max(notRob, rob); //if not rob ith house, take the max value of robbed (i-1)th house and not rob (i-1)th house
            rob = curRob;
        }
        return Math.max(rob, notRob);
    }
}

40%
public int rob(int[] num) {
    int prevMax = 0;
    int currMax = 0;
    for (int x : num) {
        int temp = currMax;
        currMax = Math.max(prevMax + x, currMax);
        prevMax = temp;
    }
    return currMax;
}

'''