__source__ = 'https://leetcode.com/problems/different-ways-to-add-parentheses/#/description'
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
# dp[l][r] = max(dp[l][r], nums[l] * nums[m] * nums[r] + dp[l][m] + dp[m][r])
#
#  Google Snapchat
#Hide Tags Dynamic Programming Divide and Conquer
#

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
java = '''
https://discuss.leetcode.com/topic/30746/share-some-analysis-and-explanations/6
Side notes: In case you are curious, for the problem "leetcode 312. Burst Balloons",
the external information to subarray nums[i, j] is the two numbers (denoted as left and right)
adjacent to nums[i] and nums[j], respectively. If we absorb this extra piece of information
into the definition of T(i, j), we have T(i, j, left, right) which represents the maximum coins obtained
by bursting balloons of subarray nums[i, j] whose two adjacent numbers are left and right.

The original problem will be T(0, n - 1, 1, 1) and
the termination condition is T(i, i, left, right) = left * right * nums[i].
The recurrence relations will be:
T(i, j, left, right) = max(left * nums[k] * right + T(i, k - 1, left, nums[k])
+ T(k + 1, j, nums[k], right)) where i <= k <= j
(here we interpret it as that the balloon at index k is the last to be burst.

Since all balloons can be the last one so we try each case and choose one that yields the maximum coins).
For more details, refer to dietpepsi 's post.

Be Naive First

When I first get this problem, it is far from dynamic programming to me.
I started with the most naive idea the backtracking.

We have n balloons to burst, which mean we have n steps in the game.
In the i th step we have n-i balloons to burst, i = 0~n-1.
Therefore we are looking at an algorithm of O(n!). Well, it is slow, probably works for n < 12 only.

Of course this is not the point to implement it.
We need to identify the redundant works we did in it and try to optimize.

Well, we can find that for any balloons left the maxCoins does not depends on the balloons already bursted.
This indicate that we can use memorization (top down) or dynamic programming (bottom up)
for all the cases from small numbers of balloon until n balloons. How many cases are there?
For k balloons there are C(n, k) cases and for each case it need to scan the k balloons to compare.
The sum is quite big still. It is better than O(n!) but worse than O(2^n).

Better idea

We then think can we apply the divide and conquer technique?
After all there seems to be many self similar sub problems from the previous analysis.

Well, the nature way to divide the problem is burst one balloon
and separate the balloons into 2 sub sections one on the left and one one the right.
However,
in this problem the left and right become adjacent and have effects on the maxCoins in the future.

Then another interesting idea come up. Which is quite often seen in dp problem analysis.
That is reverse thinking. Like I said the coins you get for a balloon does not depend
on the balloons already burst. Therefore
instead of divide the problem by the first balloon to burst, we divide the problem by the last balloon to burst.

Why is that? Because only the first and last balloons we are sure of their adjacent balloons before hand!

For the first we have nums[i-1]*nums[i]*nums[i+1] for the last we have nums[-1]*nums[i]*nums[n].

OK. Think about n balloons if i is the last one to burst, what now?

We can see that the balloons is again separated into 2 sections. But this time
since the balloon i is the last balloon of all to burst, the left and right section
now has well defined boundary and do not affect each other!
Therefore we can do either recursive method with memoization or dp.

Final

Here comes the final solutions. Note that we put 2 balloons with 1 as boundaries
and also burst all the zero balloons in the first round since they won't give any coins.
The algorithm runs in O(n^3) which can be easily seen from the 3 loops in dp solution.

#DP 41%
public class Solution {
    public int maxCoins(int[] nums) {
        int[] newNums = new int[nums.length + 2];
	    int n = 1;
	    // do not keep ballon value == 0
	    for (int x : nums) if (x > 0) newNums[n++] = x;
	    newNums[0] = newNums[n++] = 1;

	    int[][] dp = new int[n][n];
	    for (int k = 2; k < n; k++) {
	        for (int left = 0; left < n - k; left++ ) {
	            int right = left + k;
	            for (int i = left + 1; i < right; i++) {
	                dp[left][right] = Math.max( dp[left][right],
	                    newNums[left]*newNums[i]*newNums[right] + dp[left][i] + dp[i][right]);
	            }
	        }
	    }
	    /*
	    for (int[] row : dp) {
	        for (int each : row) {
	            System.out.print(each + " ");
	        }
	        System.out.println(" ");
	    }
	    */
	    return dp[0][n-1];
    }
}
DP table: if use [3,1,5,8]
0 0 3 30 159 167
0 0 0 15 135 159
0 0 0  0  40  48
0 0 0  0   0  40
0 0 0  0   0   0
0 0 0  0   0   0


# 64%  Java D&C with Memoization
public class Solution {
    public int maxCoins(int[] nums) {
        int[] newNums = new int[nums.length + 2];
	    int n = 1;
	    // do not keep ballon value == 0
	    for (int x : nums) if (x > 0) newNums[n++] = x;
	    newNums[0] = newNums[n++] = 1;
	    int[][] memo = new int[n][n];
        return burst(memo, newNums, 0, n-1);
    }

    public int burst(int[][] memo,int[] nums,int left, int right){
        if (left + 1 == right) return 0; //left -> i -> right
        if (memo[left][right] > 0) return memo[left][right];
        int res = 0;
        for (int i = left + 1; i < right; i++) {
            res = Math.max(res, nums[left] * nums[i] * nums[right]
                                + burst(memo, nums, left, i)
                                + burst(memo, nums, i, right));
        }
        memo[left][right] = res;
        return res;
    }
}
'''
