__source__ = 'https://leetcode.com/problems/shuffle-an-array/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/shuffle-an-array.py
# Time:  O(n)
# Space: O(n)
#
# Description: 384. Shuffle an Array
#
# Shuffle a set of numbers without duplicates.
#
# Example:
#
# // Init an array with set 1, 2, and 3.
# int[] nums = {1,2,3};
# Solution solution = new Solution(nums);
#
# // Shuffle the array [1,2,3] and return its result.
# Any permutation of [1,2,3] must equally likely to be returned.
# solution.shuffle();
#
# // Resets the array back to its original configuration [1,2,3].
# solution.reset();
#
# // Returns the random shuffling of array [1,2,3].
# solution.shuffle();

import unittest
from random import random
# 676ms 24.17%
class Solution(object):

    def __init__(self, nums):
        """

        :type nums: List[int]
        :type size: int
        """
        self.__nums = nums


    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.__nums


    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        nums = list(self.__nums)
        for i in xrange(len(nums)):
            j = random.randint(i, len(nums)-1)
            nums[i], nums[j] = nums[j], nums[i]
        return nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/shuffle-an-array/solution/

# 141ms 96.72%
import java.util.Random;
public class Solution {
    private Random mRandom;
    private int[] mNums;

    public Solution(int[] nums) {
        mNums =nums;
        mRandom = new Random();
    }

    /** Resets the array to its original configuration and return it. */
    public int[] reset() {
        return mNums;
    }

    /** Returns a random shuffling of the array. */
    public int[] shuffle() {
        if (mNums == null) return null;
        int[] a = mNums.clone();
        for (int i = 1; i < a.length; i++) {
            int j = mRandom.nextInt(i + 1);
            swap(a, i, j);
        }
        return a;
    }

    private void swap(int[] a, int i, int j) {
        int tmp = a[i];
        a[i] = a[j];
        a[j] = tmp;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int[] param_1 = obj.reset();
 * int[] param_2 = obj.shuffle();
 */

'''
