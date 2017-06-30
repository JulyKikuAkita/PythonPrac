__author__ = 'July'
#Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
#
# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
# Note:
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
# Hide Company Tags Google
# Hide Tags Array Map
# Hide Similar Problems (E) Two Sum (M) Continuous Subarray Sum
#
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = collections.Counter()
        count[0] = 1
        ans = su = 0
        for x in nums:
            su += x
            ans += count[su-k]
            count[su] += 1
        return ans


java = '''
O(n)
public class Solution {
    public int subarraySum(int[] a, int k) {
        int sum = 0;
		HashMap<Integer, Integer> map = new HashMap<>();
		map.put(0, 1);
		int count = 0;
		for (int i = 0; i < a.length; i++) {
			sum += a[i];
			if (map.containsKey(sum - k)) {
				count += map.get(sum-k);
			}
			map.put(sum, map.getOrDefault(sum, 0) + 1);
		}
		return count;
    }
}
'''