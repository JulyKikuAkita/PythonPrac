__source__ = 'https://leetcode.com/problems/random-pick-index/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/random-pick-index.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 398. Random Pick Index
#
# Given an array of integers with possible duplicates,
# randomly output the index of a given target number.
# You can assume that the given target number must exist in the array.
#
# Note:
# The array size can be very large.
# Solution that uses too much extra space will not pass the judge.
#
# Example:
#
# int[] nums = new int[] {1,2,3,3,3};
# Solution solution = new Solution(nums);
#
# // pick(3) should return either index 2, 3, or 4 randomly.
# Each index should have equal probability of returning.
# solution.pick(3);
#
# // pick(1) should return 0. Since in the array only nums[0] is equal to 1.
# solution.pick(1);
#
# Companies
# Facebook
# Related Topics
# Reservoir Sampling
# Similar Questions
# Linked List Random Node
#
from random import randint
import unittest
# 60ms 85.04%
class Solution(object):
    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        """
        self.__nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        reservoir = -1
        n = 0
        for i in xrange(len(self.__nums)):
            if self.__nums[i] != target:
                continue
            reservoir = i if n == 0 or randint(1, n+1) == 1 else reservoir
            n += 1
        return reservoir

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# 175ms 38.31%
class Solution {
    int[] nums;
    Random rand;

    public Solution(int[] nums) {
        this.nums = nums;
        this.rand = new Random();
    }

    public int pick(int target) {
        int res = -1;
        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != target)
                continue;
            // randomly select an int from 0 to the nums of target.
            // If x equals 0, set the res as the current index. The probability is always 1/nums for the latest appeared number.
            // For example, 1 for 1st num, 1/2 for 2nd num, 1/3 for 3nd num (1/2 * 2/3 for each of the first 2 nums).
            int whetherToChange = rand.nextInt(++count);
            res = whetherToChange == 0 ? i : res;
        }
        return res;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int param_1 = obj.pick(target);
 */

# 209ms 17.46%
class Solution {
    int[] nums;
    Random rand;

    public Solution(int[] nums) {
        this.nums = nums;
        this.rand = new Random();
    }

    public int pick(int target) {
        int res = -1;
        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != target)
                continue;
            if (rand.nextInt(++count) == 0)
                res = i;
        }
        return res;
    }
}
'''
