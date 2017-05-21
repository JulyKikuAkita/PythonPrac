__author__ = 'July'
# Time:  O(n)
# Space: O(1)
#
# Given an array of n positive integers and a positive integer s,
# find the minimal length of a subarray of which the sum >=s. IF there isn't one, return 0 instead.
#
# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.
#
# More practice:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
#  Facebook
# Array Two Pointers Binary Search


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

# java solution
# http://www.programcreek.com/2014/05/leetcode-minimum-size-subarray-sum-java/
# 2 points to mark the left and right boundaries of the sliding window.
# When the sum is greater than the target, shift the left pointer;
# when the sum is less than the target, shift the right pointer.

if __name__ == "__main__":
    nums = [2,3,1,2,4,3]
    print Solution().minSubArrayLen(7, nums)
    print Solution2().minSubArrayLen(7, nums)
#java
js = '''
public class Solution {
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
'''