__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/largest-divisible-subset.py
# Time:  O(n^2)
# Space: O(n)

# Given a set of distinct positive integers,
# find the largest subset such that every pair (Si, Sj) of
# elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.
#
# If there are multiple solutions, return any subset is fine.
#
# Example 1:
#
# nums: [1,2,3]
#
# Result: [1,2] (of course, [1,3] will also be ok)
# Example 2:
#
# nums: [1,2,4,8]
#
# Result: [1,2,4,8]
#  Google
# Hide Tags Dynamic Programming Math


class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        nums.sort()
        dp = [1] * len(nums)
        prev = [-1] * len(nums)
        largest_idx = 0
        for i in xrange(len(nums)):
            for j in xrange(i):
                if nums[i] % nums[j] == 0:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            if dp[largest_idx] < dp[i]:
                largest_idx = i

        result = []
        i = largest_idx
        while i != -1:
            result.append(nums[i])
            i = prev[i]
        return result[::-1]

#java
js = '''
public class Solution {
    public List<Integer> largestDivisibleSubset(int[] nums) {
        List<Integer> result = new ArrayList<>();
        int[] dp = new int[nums.length];
        int max = 1;

        if (nums.length == 0) {
            return result;
        }
        dp[0] = 1;
        Arrays.sort(nums);
        for (int i = 1; i < nums.length; i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++) {
                if (nums[i] % nums[j] == 0) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                    max = Math.max(max, dp[i]);
                }
            }
        }
        int index = nums.length - 1;
        Integer prev = null;
        while (max > 0) {
            while (dp[index] < max || (prev != null && prev % nums[index] != 0)) {
                index--;
            }
            result.add(nums[index]);
            prev = nums[index];
            max--;
            index--;
        }
        Collections.reverse(result);
        return result;
    }
}
'''