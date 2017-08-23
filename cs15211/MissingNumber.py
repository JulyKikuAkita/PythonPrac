__source__ = 'https://leetcode.com/problems/missing-number/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/missing-number.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 268. Missing Number
#
# Given an array containing n distinct numbers taken from
# 0, 1, 2, ..., n, find the one that is missing from the array.
#
# For example,
# Given nums = [0, 1, 3] return 2.
#
# Note:
# Your algorithm should run in linear runtime complexity.
# Could you implement it using only constant extra space complexity?
#
# Companies
# Microsoft Bloomberg
# Related Topics
# Array Math Bit Manipulation
# Similar Questions
# First Missing Positive Single Number Find the Duplicate Number
#
import unittest
import operator
class Solution(object):
    def missingNumber(self, nums):
         return reduce(operator.xor, nums, \
                      reduce(operator.xor, xrange(len(nums) + 1)))

class Solution2():
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1

        for n in nums:
            i = n
            if i == len(nums) and nums[len(nums)-1] != len(nums):
                n = nums[len(nums)-1]
                nums[len(nums)-1] = len(nums)
                i = n

            while i < len(nums) and i != nums[i]:
                tmp, nums[i] = nums[i], i,
                i = tmp

        for i in xrange(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#17.78% 4ms
public class Solution {
    public int missingNumber(int[] nums) {
        int index = 0;
        while (index < nums.length) {
            if (nums[index] != index && nums[index] < nums.length) {
                swap(nums, index, nums[index]);
            } else {
                index++;
            }
        }
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != i) {
                return i;
            }
        }
        return nums.length;
    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}

# 1.XOR
#37.54% 1ms
public class Solution {
    public int missingNumber(int[] nums) {
        int xor = 0, i = 0;
        for (i = 0; i < nums.length; i++) {
            xor = xor ^ i ^ nums[i];
        }

        return xor ^ i;
    }
}

2.SUM
#37.54% 1ms
public class Solution {
    public int missingNumber(int[] nums) { //sum
        int len = nums.length;
        int sum = ( 0 + len ) * ( len + 1 ) / 2;
        for(int i = 0; i < len; i++)
            sum -= nums[i];
        return sum;
    }
}

3.Binary Search
#11.58% 12ms
public class Solution {
    public int missingNumber(int[] nums) { //binary search
        Arrays.sort(nums);
        int left = 0, right = nums.length, mid= (left + right) / 2;
        while(left < right){
            mid = left + (right - left) / 2;
            if ( nums[mid] > mid) right = mid;
            else left = mid+1;
        }
        return left;
    }
}
'''