__author__ = 'July'
'''
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Example 1:
Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:
Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

Follow Up:
Can you do it in O(n) time?
# Palantir
# Hash Table

'''

# OT
# O(n^2)
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        ans =0
        for i in xrange(len(nums)):
            for j in xrange(i+1, len(nums)):
                if i != j and sum(nums[i:j])== k:
                    ans = max(ans, j - i )

        return ans

# O(n)
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        result, acc = 0, 0
        dic = { 0: -1} # so that when i - dict[acc-k] have correct len of subarr

        for i in xrange(len(nums)):
            acc += nums[i]
            if acc not in dict:  # need to have this for (key, val) not being update
                dict[acc] = i
            if acc - k in dict:
                result = max(result, i - dict[acc-k])
        return result


#java
jav= '''
public class Solution {
    public int maxSubArrayLen(int[] nums, int k) {
        int len = nums.length;
        int[] sums = new int[len + 1];
        for (int i = 0; i < len; i++) {
            sums[i + 1] = sums[i] + nums[i];
        }
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 1; i < len + 1; i++) {
            map.put(sums[i], i);
        }
        int result = 0;
        for (int i = 0; i < len + 1; i++) {
            int curr = sums[i] + k;
            if (map.containsKey(curr)) {
                result = Math.max(result, map.get(curr) - i);
            }
        }
        return result;
    }
}

public class Solution {
    public int maxSubArrayLen(int[] nums, int k) {
        if(nums.length == 0) return 0;

        int len = nums.length;
        int sums = 0;
        int res = 0;
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, -1);
        for(int i = 0; i < len; i++){
            sums += nums[i];
            if(!map.containsKey(sums)){
                map.put(sums, i);
            }
            if(map.containsKey(sums - k)){
                res = Math.max(res, i - map.get(sums - k));
            }
        }
        return res;
    }
}
'''