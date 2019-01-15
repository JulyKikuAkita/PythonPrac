__source__ = 'https://leetcode.com/problems/longest-continuous-increasing-subsequence/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 674. Longest Continuous Increasing Subsequence
#
# Given an unsorted array of integers, find the length of longest continuous increasing subsequence.
#
# Example 1:
# Input: [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
# Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.
# Example 2:
# Input: [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2], its length is 1.
# Note: Length of the array will not exceed 10,000.
#
# Related Topics
# Array Facebook
# Similar Questions
# Number of Longest Increasing Subsequence
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
# Thought: https://leetcode.com/problems/longest-continuous-increasing-subsequence/solution/

# 4ms 35.26%
class Solution {
    public int findLengthOfLCIS(int[] nums) {
        int res = 0, cnt = 0;
        for(int i = 0; i < nums.length; i++){
            if(i == 0 || nums[i-1] < nums[i]) res = Math.max(res, ++cnt);
            else cnt = 1;
        }
        return res;
    }
}

# 4ms 35.26%
class Solution {
    public int findLengthOfLCIS(int[] nums) {
        if(nums == null || nums.length == 0)
            return  0;
        int res = 1;
        int count = 1;
        for(int i = 1; i < nums.length; i++) {
            if(nums[i] > nums[i - 1]) {
                count++;
                if(count > res)
                    res = count;
            } else
                count = 1;
        }
        return res++;
    }
}
'''
