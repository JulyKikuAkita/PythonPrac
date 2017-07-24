__source__ = 'https://leetcode.com/problems/set-mismatch/description/'
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 645. Set Mismatch
# The set S originally contains numbers from 1 to n. But unfortunately, due to the data error,
# one of the numbers in the set got duplicated to another number in the set,
# which results in repetition of one number and loss of another number.
#
# Given an array nums representing the data status of this set after the error.
# Your task is to firstly find the number occurs twice and then find the number that is missing.
# Return them in the form of an array.
#
# Example 1:
# Input: nums = [1,2,2,4]
# Output: [2,3]
# Note:
# The given array size will in the range [2, 10000].
# The given array's numbers won't have any order.
# # Companies
# Amazon
# Related Topics
# Hash Table Math
# Similar Questions
# Find the Duplicate Number
#
#
import unittest
# 82ms
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        count = [0] * (N+1)
        for x in nums:
          count[x] += 1
        for x in xrange(1, len(nums)+1):
            if count[x] == 2:
                twice = x
            if count[x] == 0:
                never = x
        return twice, never

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/set-mismatch/solution/

#91.20%  8ms # iterate twice to get count for each num
public class Solution {
    public int[] findErrorNums(int[] nums) {
        int duplicate = 0;
        int[] hash = new int[nums.length + 1];

        for(int i = 0; i < nums.length; i++) {
            if(++hash[nums[i]] > 1)
                duplicate = nums[i];
        }

        for(int i = 1; i < hash.length; i++) {
            if(hash[i] == 0)
                return new int[] {duplicate, i};
        }

        return new int[nums.length];
    }
}

XOR: https://leetcode.com/problems/set-mismatch/solution/
# 65.67% 11ms
public class Solution {
    public int[] findErrorNums(int[] nums) {
        int xor = 0, xor0 = 0, xor1 = 0;
        for (int n: nums)
            xor ^= n;
        for (int i = 1; i <= nums.length; i++)
            xor ^= i;
        int rightmostbit = xor & ~(xor - 1);
        for (int n: nums) {
            if ((n & rightmostbit) != 0)
                xor1 ^= n;
            else
                xor0 ^= n;
        }
        for (int i = 1; i <= nums.length; i++) {
            if ((i & rightmostbit) != 0)
                xor1 ^= i;
            else
                xor0 ^= i;
        }
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == xor0)
                return new int[]{xor0, xor1};
        }
        return new int[]{xor1, xor0};
    }
}

# Hashset
# 16.03% 45ms
public class Solution {
    public int[] findErrorNums(int[] nums) {
        Set<Integer> set = new HashSet<>();
        int duplicate = 0, n = nums.length;
        long sum = (n * (n+1)) / 2;
        for(int i : nums) {
            if(set.contains(i)) duplicate = i;
            sum -= i;
            set.add(i);
        }
        return new int[] {duplicate, (int)sum + duplicate};
    }
}
'''