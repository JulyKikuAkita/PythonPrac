__source__ = 'https://leetcode.com/problems/minimum-size-subarray-sum/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/minimum-size-subarray-sum.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 209. Minimum Size Subarray Sum
#
# Given an array of n positive integers and a positive integer s,
# find the minimal length of a subarray of which the sum >=s.
# IF there isn't one, return 0 instead.
#
# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.
#
# More practice:
# If you have figured out the O(n) solution,
# try coding another solution of which the time complexity is O(n log n).
#
# Companies
# Facebook
# Related Topics
# Array Two Pointers Binary Search
# Similar Questions
# Minimum Window Substring Maximum Size Subarray Sum Equals k
#
import unittest
# Sliding window solution.
class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        start = 0
        sum = 0
        min_len = float("inf")
        for i in xrange(len(nums)):
            sum += nums[i]
            while sum >= s:
                min_len = min(min_len, i - start + 1)
                sum -= nums[start]
                start += 1
        if min_len == float("inf"):
            return 0
        return min_len

# Time:  O(nlogn)
# Space: O(n)
# Binary search solution.
class Solution2:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        min_size = float("inf")
        sum_from_start = [n for n in nums]
        for i in xrange(len(sum_from_start) - 1):
            sum_from_start[i + 1] += sum_from_start[i]
        for i in xrange(len(sum_from_start)):
            end = self.binarySearch(lambda x, y : x <= y, sum_from_start, i, len(sum_from_start), sum_from_start[i] - nums[i] + s)
            if end < len(sum_from_start):
                min_size = min(min_size, end - i + 1)
        if min_size == float("inf"):
            return 0
        return min_size

    def binarySearch(self, compare, A, start, end, target):
        while start < end:
            mid = ( start + end ) / 2
            if compare(target, A[mid]):
                end = mid
            else:
                start = mid+1
        return start
# Test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        nums = [2,3,1,2,4,3]
        print Solution().minSubArrayLen(7, nums)
        print Solution2().minSubArrayLen(7, nums)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/minimum-size-subarray-sum/solution/

# 3ms 51.78%
class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        if(s == 0 || nums == null || nums.length == 0) return 0;
        int sum = 0;
        int res = Integer.MAX_VALUE;
        int idx = 0;
        for(int i = 0; i < nums.length ; i++){
            sum += nums[i];
            while(sum >= s){
                res = Math.min(res, i - idx + 1);
                sum -= nums[idx];
                idx += 1;
            }
        }
        return res == Integer.MAX_VALUE ? 0 : res;
    }
}

# Thought:
Since the given array contains only positive integers,
the subarray sum can only increase by including more elements.
Therefore, you don't have to include more elements once the current subarray already has a sum large enough.
This gives the linear time complexity solution by maintaining a minimum window with a two indices.

As to NLogN solution, logN immediately reminds you of binary search.
In this case, you cannot sort as the current order actually matters.
How does one get an ordered array then? Since all elements are positive,
the cumulative sum must be strictly increasing.
Then, a subarray sum can expressed as the difference between two cumulative sum.
Hence, given a start index for the cumulative sum array, the other end index can be searched using binary search.

# Use binary search for end index
# 8ms 13.72%
class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        return solveNLogN(s, nums);
    }

    private int solveN(int s, int[] nums) {
        int start = 0, end = 0, sum = 0, minLen = Integer.MAX_VALUE;
        while (end < nums.length) {
            while (end < nums.length && sum < s) sum += nums[end++];
            if (sum < s) break;
            while (start < end && sum >= s) sum -= nums[start++];
            if (end - start + 1 < minLen) minLen = end - start + 1;
        }
        return minLen == Integer.MAX_VALUE ? 0 : minLen;
    }

    private int solveNLogN(int s, int[] nums) {
        int[] sums = new int[nums.length + 1];
        for (int i = 1; i < sums.length; i++) sums[i] = sums[i - 1] + nums[i - 1];
        int minLen = Integer.MAX_VALUE;
        for (int i = 0; i < sums.length; i++) {
            int end = binarySearch(i + 1, sums.length - 1, sums[i] + s, sums);
            if (end == sums.length) break;
            if (end - i < minLen) minLen = end - i;
        }
        return minLen == Integer.MAX_VALUE ? 0 : minLen;
    }

    private int binarySearch(int lo, int hi, int key, int[] sums) {
        while (lo <= hi) {
           int mid = (lo + hi) / 2;
           if (sums[mid] >= key){
               hi = mid - 1;
           } else {
               lo = mid + 1;
           }
        }
        return lo;
    }
}

# 2ms 99.91%
class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        int start = 0;
        int curr = 0;
        int length = 0;
        for (int i = 0; i < nums.length; i++) {
            curr += nums[i];
            if (curr >= s) {
                while (start < i && curr - nums[start] >= s) {
                    curr -= nums[start];
                    start++;
                }
                length = length == 0 ? i - start + 1 : Math.min(length, i - start + 1);
            }
        }
        return length;
    }
}
'''
