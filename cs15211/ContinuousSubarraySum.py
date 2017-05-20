__author__ = 'July'
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
explanation = '''
if k == 0
If there are two continuous zeros in nums, return True
Time O(n).

if n >= 2k and k > 0
There will be at least three numbers in sum with the same remainder divided by k. So I can return True without any extra calculation.
Time O(1).

if n < 2k and k > 0
If I can find two numbers in sum with the same remainder divided by k and the distance of them is greater than or equal to 2， return True.
Time O(n) <= O(k).

k < 0
same as k > 0.
'''
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

java = '''
public class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        if (nums == null || nums.length <= 1) return false;
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, -1); //considering [1,1] 2 should return true;
        int runningSum = 0;
        for (int i = 0; i < nums.length; i++) {
            runningSum += nums[i];
            if ( k != 0) {
                runningSum %= k;
                if (map.get(runningSum) != null) {
                    if ((i - map.get(runningSum)) > 1) return true; //considering [5,2,4], 5 should return false
                } else {
                    map.put(runningSum, i);
                }
            }else {
                if ( i >=1 && nums[i] == nums[i-1] && nums[i] == 0)
                    return true;
            }
        }
        return false;
    }
}
'''