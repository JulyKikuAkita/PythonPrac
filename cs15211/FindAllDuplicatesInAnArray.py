__source__ = 'https://github.com/kamyu104/LeetCode/blob/master/Python/find-all-duplicates-in-an-array.py'
# Time:  O(n)
# Space: O(1)
#
# Description:
# Given an array of integers, 1 <= a[i] <= n (n = size of array),
# some elements appear twice and others appear once.
# Find all the elements that appear twice in this array.
# Could you do it without extra space and in O(n) runtime?
#
# Example:
# Input
#
# [4,3,2,7,8,2,3,1]
#
# Output
#
# [2,3]
# Pocket Gems
# Hide Tags Array
# Hide Similar Problems (E) Find All Numbers Disappeared in an Array

import unittest

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        i = 0
        while i < len(nums):
            if nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            else:
                i += 1

        for i in xrange(len(nums)):
            if i != nums[i]-1:
                result.append(nums[i])
        return result

# your function here

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
// when find a number i, flip the number at position i-1 to negative.
// if the number at position i-1 is already negative, i is the number that occurs twice.
public class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < nums.length; ++i) {
            int index = Math.abs(nums[i])-1;
            if (nums[index] < 0)
                res.add(Math.abs(index+1));
            nums[index] = -nums[index];
        }
        return res;
    }
}

public class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> res = new ArrayList<>();
        int[] arr = new int[nums.length];
        for(int i = 0; i < nums.length; i++) {
            if( arr[nums[i] - 1] != 0) res.add(nums[i]);
            else arr[nums[i] - 1] = nums[i];
        }
        return res;
    }
}
'''