__source__ = 'https://leetcode.com/problems/increasing-triplet-subsequence/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/increasing-triplet-subsequence.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 334. Increasing Triplet Subsequence
#
# Given an unsorted array return whether an increasing
# subsequence of length 3 exists or not in the array.
#
# Formally the function should:
# Return true if there exists i, j, k
# such that arr[i] < arr[j] < arr[k]
# given 0 <= i < j < k <= n-1 else return false.
# Your algorithm should run in O(n) time complexity and O(1) space complexity.
#
# Examples:
# Given [1, 2, 3, 4, 5],
# return true.
#
# Given [5, 4, 3, 2, 1],
# return false.
#
# Companies
# Facebook
# Similar Questions
# Longest Increasing Subsequence
#
import bisect
import unittest
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        min_num, a, b = float("inf"), float("inf"), float("inf")
        for c in nums:
            if min_num >= c:
                min_num = c
            elif b >= c:
                a, b = min_num, c
            else:  # a < b < c
                return True
        return False

# Time:  O(n * logk)
# Space: O(k)
# Generalization of k-uplet.
class Solution_Generalization(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def increasingKUplet(nums, k):
            inc = [float('inf')] * (k - 1)
            for num in nums:
                i = bisect.bisect_left(inc, num)
                if i >= k - 1:
                    return True
                inc[i] = num
            return k == 0

        return increasingKUplet(nums, 3)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# 4ms 50.74%
class Solution {
    public boolean increasingTriplet(int[] nums) {
        int index = 1;
        while (index < nums.length) {
            if (nums[index] > nums[index - 1]) {
                break;
            }
            index++;
        }
        if (index == nums.length) {
            return false;
        }
        int index1 = index - 1;
        int index2 = index;
        for (int i = index + 1; i < nums.length; i++) {
            if (nums[i] > nums[index2]) {
                return true;
            } else if (nums[i] > nums[index1]) {
                index2 = i;
            } else {
                index1 = i;
            }
        }
        return false;
    }
}

# 3ms 92.22%
class Solution {
    public boolean increasingTriplet(int[] nums) {
        if(nums == null){
            return false;
        }

        int min = Integer.MAX_VALUE; int secondMin = Integer.MAX_VALUE;

        for(int i : nums){
            if(i <= min){
                min = i;
            }
            else if(i < secondMin){
                secondMin = i;
            }
            else if(i > secondMin){
                return true;
            }
        }
        return false;
    }
}
'''