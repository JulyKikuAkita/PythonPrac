__source__ = 'https://leetcode.com/problems/valid-triangle-number/#/description'
# Time:  O(n^2)
# Space: O(1)
#
# Description:
# Given an array consists of non-negative integers,
# your task is to count the number of triplets chosen from the array
# that can make triangles if we take them as side lengths of a triangle.
#
# Example 1:
# Input: [2,2,3,4]
# Output: 3
# Explanation:
# Valid combinations are:
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
# Note:
# The length of the given array won't exceed 1000.
# The integers in the given array are in the range of [0, 1000].
# Hide Company Tags Expedia
# Hide Tags Array
# Hide Similar Problems (M) 3Sum Smaller
#
import unittest


class Solution(object):
    pass  # your function here


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/articles/valid-triangle-number/

public class Solution {
    public int triangleNumber(int[] nums) {
        Arrays.sort(nums);
        int count = 0, n = nums.length;
        for (int i = n -1; i >= 0; i--) {
            int l = 0, r = i-1;
            while (l < r) {
                if (nums[l] + nums[r] > nums[i]) {
                    count += r - l;
                    r--;
                }else {
                    l++;
                }
            }
        }
        return count;
    }
}

'''