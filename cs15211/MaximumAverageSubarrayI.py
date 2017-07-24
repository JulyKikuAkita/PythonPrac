__source__ = 'https://leetcode.com/problems/maximum-average-subarray-i/tabs/description'
# Time:  O(n)
# Space: O(1)
#
# Description:
# Given an array consisting of n integers, find the contiguous subarray of given length k
# that has the maximum average value. And you need to output the maximum average value.
#
# Example 1:
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
# Note:
# 1 <= k <= n <= 30,000.
# Elements of the given array will be in the range [-10,000, 10,000].
# Companies
# Google
# Related Topics
# Array
# Similar Questions
# Maximum Average Subarray II

import unittest
import itertools
import operator
import numpy as np
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sums = np.cumsum([0] + nums)
        return float(max(sums[k:] - sums[:-k])) / k

    def findMaxAverage2(self, nums, k):
        sums = [0] + list(itertools.accumulate(nums))
        return max(map(operator.sub, sums[k:], sums)) / k
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/articles/maximum-average-subarray/

Approach #3 Sliding Window [Accepted]
# 77.58%  20ms
public class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int sum = 0;
        for(int i = 0; i < k; i++) {
            sum += nums[i];
        }
        int maxi = sum;
       for(int i = k; i < nums.length; i++) {
           sum += nums[i];
           sum -= nums[i - k];
           if (sum > maxi) maxi = sum;
       }
       return (double)maxi / k;
    }
}
'''