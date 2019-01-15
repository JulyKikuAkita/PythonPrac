__source__ = 'https://leetcode.com/problems/combination-sum-iv/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/combination-sum-iv.py
# Time:  O(nlon + n * t), t is the value of target.
# Space: O(t)
#
# Description: Leetcode # 377. Combination Sum IV
#
# Given an integer array with all positive numbers and no duplicates,
# find the number of possible combinations that add up to a positive integer target.
#
# Example:
#
# nums = [1, 2, 3]
# target = 4
#
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
#
# Note that different sequences are counted as different combinations.
#
# Therefore the output is 7.
# Follow up:
# What if negative numbers are allowed in the given array?
# How does it change the problem?
#
# What limitation we need to add to the question to allow negative numbers?
#
# Companies
# Google Snapchat Facebook
# Related Topics
# Dynamic Programming
# Similar Questions
# Combination Sum
#
# DP:  comb[target] = sum(comb[target - nums[i]]),
import unittest
# bottom-up approach
# 28ms 95.28%
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target+1)
        dp[0] = 1
        nums.sort()

        for i in xrange(1, target+1):
            for j in xrange(len(nums)):
                if nums[j] <= i:
                    dp[i] += dp[i - nums[j]]
                else:
                    break

        return dp[target]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
# DP:  comb[target] = sum(comb[target - nums[i]]),
Think about the recurrence relation first.
How does the # of combinations of the target related to the # of combinations of numbers that are smaller than the target?

So we know that target is the sum of numbers in the array.
Imagine we only need one more number to reach target, this number can be any one in the array, right?
So the # of combinations of target, comb[target] = sum(comb[target - nums[i]]),
where 0 <= i < nums.length, and target >= nums[i].

In the example given, we can actually find the # of combinations of 4
with the # of combinations of 3(4 - 1), 2(4- 2) and 1(4 - 3).
As a result, comb[4] = comb[4-1] + comb[4-2] + comb[4-3] = comb[3] + comb[2] + comb[1].

Then think about the base case. Since if the target is 0, there is only one way to get zero,
which is using 0, we can set comb[0] = 1.

EDIT: The problem says that target is a positive integer that makes me feel it's unclear to put it in the above way.
Since target == 0 only happens when in the previous call, target = nums[i],
we know that this is the only combination in this case, so we return 1.

1. bruce force: # TLE
public class Solution {
    public int combinationSum4(int[] nums, int target) {
        if (target == 0) {
            return 1;
        }
        int res = 0;
        for (int i = 0; i < nums.length; i++) {
            if (target >= nums[i]) {
                res += combinationSum4(nums, target - nums[i]);
            }
        }
        return res;
    }
}

//Submission Result: Memory Limit Exceeded
//Last executed input:
//[4,2,1]
//32
# TLE
public class Solution {
    public int combinationSum4(int[] nums, int target) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(result, new ArrayList<Integer>(), nums, target, 0);
        return result.size();
    }

    private void backtrack(List<List<Integer>> list, List<Integer> tempList, int[] nums, int remain, int start) {
        if (start >= nums.length || remain < 0) return;
        if (remain == 0) {
            list.add(new ArrayList<>(tempList));
            return;
        }
        for (int i = 0; i < nums.length; i++) { // i always start with 0 to reuse same arr element
            tempList.add(nums[i]);
            backtrack(list, tempList, nums, remain - nums[i], i);
            tempList.remove(tempList.size() - 1);
        }
    }
}

2. recursion with memorization
JAVA recursion solution using HashMap as memory.
The DP solution goes through every possible sum from 1 to target one by one.
Using recursion can skip those sums that are not the combinations of the numbers in the given array.
Also, there is no need to sort the array first.

# 4ms 18.12%
class Solution {
    Map<Integer, Integer> map = new HashMap<>();
    public int combinationSum4(int[] nums, int target) {
        int count = 0;
        if (nums == null || nums.length == 0 || target < 0 ) return 0;
        if ( target == 0  ) return 1;
        if (map.containsKey(target)) return map.get(target);
        for (int num: nums){
            count += combinationSum4(nums, target-num);
        }
        map.put(target, count);
        return count;
    }
}

# https://discuss.leetcode.com/topic/52302/1ms-java-dp-solution-with-detailed-explanation
3. DP
# 0ms 100%
public class Solution {
    private int[] dp;
    public int combinationSum4(int[] nums, int target) {
        dp = new int[target +1];
        Arrays.fill(dp, -1);
        dp[0] = 1;
        return helper(nums, target);
    }
    private int helper(int[] nums, int target) {
        if(dp[target] != -1) {
            return dp[target];
        }
        int res = 0;
        for( int i = 0; i < nums.length; i++) {
            if (target >= nums[i]) {
                res += helper(nums, target - nums[i]);
            }
        }
        dp[target] = res;
        return res;
    }
}

EDIT: The above solution is top-down. How about a bottom-up one?
# 2ms 47.99%
class Solution {
    public int combinationSum4(int[] nums, int target) {
        int[] comb = new int[target + 1];
        comb[0] = 1;
        for (int i = 1; i < comb.length; i++) {
            for (int j = 0; j < nums.length; j++) {
                if (i - nums[j] >= 0) {
                    comb[i] += comb[i - nums[j]];
                }
            }
        }
        return comb[target];
    }
}

# DP:
# 2ms 47.99%
Then think about the base case.
Since if the target is 0, there is only one way to get zero, which is using 0, we can set comb[0] = 1.

class Solution {
    public int combinationSum4(int[] nums, int target) {
        Arrays.sort(nums);
        int[] dp = new int[target + 1]; //base case dp[0]
        for (int i = 1; i < dp.length; i++) {
            for (int num : nums) {
                if ( num > i) break;
                else if (num == i) dp[i] += 1;
                else dp[i] += dp[i - num];
            }
        }
        return dp[target];
    }
}
'''
