__source__ = 'https://leetcode.com/problems/continuous-subarray-sum/'
# Time:  O(n^2)
# Space: O(n)
#
# Description: Leetcode # 523. Continuous Subarray Sum
#
# Given a list of non-negative numbers and a target integer k, write a function to check if
# the array has a continuous subarray of size at least 2 that sums up to the multiple of k,
# that is, sums up to n*k where n is also an integer.

# Example 1:
# Input: [23, 2, 4, 6, 7],  k=6
# Output: True
# Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
# Example 2:
# Input: [23, 2, 6, 4, 7],  k=6
# Output: True
# Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
# Note:
# The length of the array won't exceed 10,000.
# You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
# Hide Company Tags Facebook
# Hide Tags Dynamic Programming Math
# Hide Similar Problems (M) Subarray Sum Equals K
#
# explanation =
# if k == 0
# If there are two continuous zeros in nums, return True
# Time O(n).
#
# if n >= 2k and k > 0
# There will be at least three numbers in sum with the same remainder divided by k. So I can return True without any extra calculation.
# Time O(1).
#
# if n < 2k and k > 0
# If I can find two numbers in sum with the same remainder divided by k
# and the distance of them is greater than or equal to 2, return True.
# Time O(n) <= O(k).
#
# k < 0
# same as k > 0.
#
class Solution(object):
    def checkSubarraySum(self, nums, k):


        if k == 0:
            # if two continuous zeros in nums, return True
            # time O(n)
            for i in range(0, len(nums) - 1):
                if nums[i] == 0 and nums[i+1] == 0:
                    return True
            return False

        k = abs(k)
        if len(nums) >= k * 2:
            return True

        #if n >= 2k: return True
        #if n < 2k:  time O(n) is O(k)

        sum = [0]
        for x in nums:
            sum.append((sum[-1] + x) % k)

        Dict = {}
        for i in range(0, len(sum)):
            if Dict.has_key(sum[i]):
                if i - Dict[sum[i]] > 1:
                    return True
            else:
                Dict[sum[i]] = i

        return False

Java = '''
# Thought: https://leetcode.com/problems/continuous-subarray-sum/solution/

# Approach #2 Better Brute Force [Accepted]
# Time complexity : O(n^2). Two for loops are used for considering every subarray possible.
# Space complexity : O(n). sumsum array of size nn is used.
# 50ms 22.98%
class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        int[] sums = new int[nums.length];
        sums[0] = nums[0];
        for (int i = 1; i < nums.length; i++) sums[i] = sums[i - 1] + nums[i];
        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                int ttl = sums[j] - sums[i] + nums[i];
                if ( ttl == k || (k != 0 && ttl % k == 0)) return true;
            }
        }
        return false;
    }
}

# Approach #3 Using HashMap [Accepted]
# Time complexity : O(n). Only one traversal of the array numsnums is done.
# Space complexity : O(min(n,k)). The HashMap can contain upto min(n,k)min(n,k) different pairings.

# whenever the same sum % k sum value is obtained corresponding to two indices i and j, 
# it implies that sum of elements between those indices is an integer multiple of k.
# subArray sum i = k * m + (remainder); 1)
# subArray sum j = k * n + (remainder); 2) 
# let 1 - 2)   =   k * (m - n)
# 9ms 44.20%
class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap();
        int sum = 0;
        map.put(0, -1);
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            if (k != 0) sum = sum % k;
            if (map.get(sum) == null) map.put(sum, i);
            else {
                if (i - map.get(sum) > 1) { //considering [0, 0, 0] 0, at index 0, continue;
                    return true;
                }
            }
        }
        return false;
    }
}
'''
