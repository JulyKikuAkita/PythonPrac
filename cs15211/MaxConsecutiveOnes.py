__source__ = 'https://leetcode.com/problems/max-consecutive-ones/'
# Time:  O(n)
# Space: O(1)
#
# Description: 485. Max Consecutive Ones
#
# Given a binary array, find the maximum number of consecutive 1s in this array.
#
# Example 1:
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.
# Note:
#
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000
# Hide Company Tags Google
# Hide Tags Array
# Hide Similar Problems (M) Max Consecutive Ones II
#
import unittest
# 60ms 57.78%
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        ans = 0
        for num in nums:
            if num == 1:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 0
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
#
# 8ms 22.64%
class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int cnt = 0;
        int res = 0;
        for (int n : nums) {
            if (n == 1) {
                cnt++;
                res = Math.max(res, cnt);
            }else {
                cnt = 0;
            }
        }
        return res;
    }
}

'''
