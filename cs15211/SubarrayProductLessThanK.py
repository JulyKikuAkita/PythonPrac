__source__ = 'https://leetcode.com/problems/subarray-product-less-than-k/'
# Time:  O(N)
# Space: O(1)
#
# Description: Leetcode # 713. Subarray Product Less Than K
#
# Your are given an array of positive integers nums.
#
# Count and print the number of (contiguous) subarrays
# where the product of all the elements in the subarray is less than k.
#
# Example 1:
# Input: nums = [10, 5, 2, 6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
# Note:
#
# 0 < nums.length <= 50000.
# 0 < nums[i] < 1000.
# 0 <= k < 10^6.
#
import unittest

# 284ms 29.27%
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            if prod < k:
                ans += right - left + 1
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/subarray-product-less-than-k/solution/

Approach #2: Sliding Window [Accepted]
Time Complexity: O(N), where N is the length of nums. left can only be incremented at most N times.
Space Complexity: O(1), the space used by prod, left, and ans.

# 18ms 38.88%
class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        if ( k <= 1) return 0;
        int prod = 1, ans = 0, left = 0;
        for (int right = 0; right < nums.length; right++) {
            prod *= nums[right];
            while (prod >= k) prod /= nums[left++];
            ans += right - left + 1;
        }
        return ans;
    }
}

# only for reference
Because \log(\prod_i x_i) = \sum_i \log x_i, we can reduce the problem to subarray sums instead of subarray products.

Algorithm
After this transformation where every value x becomes log(x),
let us take prefix sums prefix[i+1] = nums[0] + nums[1] + ... + nums[i].
Now we are left with the problem of finding, for each i,
the largest j so that nums[i] + ... + nums[j] = prefix[j] - prefix[i] < k.
Because prefix is a monotone increasing array, this can be solved with binary search.
We add the width of the interval [i, j] to our answer, which counts all subarrays [i, k] with k <= j.

Complexity Analysis
Time Complexity: O(NlogN), where N is the length of nums.
Inside our for loop, each binary search operation takes O(logN) time.
Space Complexity: O(N), the space used by prefix.

# 89ms 0.98%
class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        if (k == 0) return 0;
        double logk = Math.log(k);
        double[] prefix = new double[nums.length + 1];
        for (int i = 0; i < nums.length; i++) {
            prefix[i+1] = prefix[i] + Math.log(nums[i]);
        }

        int ans = 0;
        for (int i = 0; i < prefix.length; i++) {
            int lo = i + 1, hi = prefix.length;
            while (lo < hi) {
                int mi = lo + (hi - lo) / 2;
                if (prefix[mi] < prefix[i] + logk - 1e-9) lo = mi + 1;
                else hi = mi;
            }
            ans += lo - i - 1;
        }
        return ans;
    }
}
'''
