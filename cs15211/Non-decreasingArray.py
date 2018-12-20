__source__ = 'https://leetcode.com/problems/non-decreasing-array/'
# Time:  O(N)
# Space: O(1)
#
# Description: Leetcode # 665. Non-decreasing Array
#
# Given an array with n integers,
# your task is to check if it could become non-decreasing by modifying at most 1 element.
#
# We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
#
# Example 1:
# Input: [4,2,3]
# Output: True
# Explanation: You could modify the first
# 4
#  to
# 1
#  to get a non-decreasing array.
# Example 2:
# Input: [4,2,1]
# Output: False
# Explanation: You can't get a non-decreasing array by modify at most one element.
# Note: The n belongs to [1, 10,000].
# Companies
# Google
# Related Topics
# Array
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
# Thought: https://leetcode.com/problems/non-decreasing-array/solution/

# 9ms 99.39%
class Solution {
    public boolean checkPossibility(int[] nums) {
        int cnt = 0;   //the number of changes
        for(int i = 1; i < nums.length && cnt<=1 ; i++){
            if(nums[i-1] > nums[i]){
                cnt++;
                if(i-2<0 || nums[i-2] <= nums[i])nums[i-1] = nums[i];  //modify nums[i-1] of a priority
                else nums[i] = nums[i-1];  //have to modify nums[i]
            }
        }
        return cnt<=1;
    }
}

# 10ms 89.96%
class Solution {
    public boolean checkPossibility(int[] nums) {
        if(nums == null || nums.length < 2)
            return true;
        boolean change = true;
        int start = 0;
        int last = nums[start];
        start = 1;
        while(start < nums.length){
            int current = nums[start];
            if (last <= current){
                last = current;
                start++;
                continue;
            }
            if(change){
                if(start-2 < 0 || current > nums[start - 2])
                    last = current;
                change = false;
                start++;
            }
            else
                return false;
        }
        return true;
    }
}
'''
