__source__ = 'https://leetcode.com/problems/rotate-array/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/rotate-array.py
# Time:  O(n)
# Space: O(1)
# Array
#
# Description: Leetcode # 189. Rotate Array
#
# Rotate an array of n elements to the right by k steps.
#
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
#
# Note:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
#
# [show hint]
#
# Related problem: Reverse Words in a String II# Companies
# Microsoft Bloomberg
# Related Topics
# Array
# Similar Questions
# Rotate List Reverse Words in a String II
#
# Note:
# Assuming we are given {1,2,3,4,5,6} and order 2. The basic idea is:
# 1. Divide the array two parts: 1,2,3,4 and 5, 6
# 2. Rotate first part: 4,3,2,1,5,6
# 3. Rotate second part: 4,3,2,1,6,5
# 4. Rotate the whole array: 5,6,1,2,3,4
#
import unittest
class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        k %= len(nums)
        self.reverse(nums, 0, len(nums))
        self.reverse(nums, 0, k)
        self.reverse(nums, k, len(nums))

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end - 1] = nums[end - 1], nums[start]
            start += 1
            end -= 1

from fractions import gcd
class Solution2:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        k %= len(nums)
        num_cycle = gcd(len(nums), k)
        cycle_len = len(nums) / num_cycle
        #print k, num_cycle, cycle_len
        for i in xrange(num_cycle):
            self.apply_cycle_permutation(k , i , cycle_len, nums)

    def apply_cycle_permutation(self, k, offset, cycle_len, nums):
        tmp = nums[offset]
        for i in xrange(1, cycle_len):
            print ((offset + i * k) % len(nums)), offset, nums[(offset + i * k) % len(nums)], nums
            nums[(offset + i * k) % len(nums)], tmp = tmp , nums[(offset + i * k) % len(nums)]
        nums[offset] = tmp

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        nums = [1,2,3,4,5,6,7]
        nums1 = [-1]
        nums2 = [1,2,3,4,5]
        Solution2().rotate(nums2, 2)
        print nums2

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/rotate-array/solution/

Approach #2 Using Extra Array [Accepted]
# 0ms 100%
class Solution {
    public void rotate(int[] nums, int k) {
        k = k % nums.length;
        int res[] = new int[nums.length];
        System.arraycopy(nums, 0, res, k, nums.length - k);
        System.arraycopy(nums, nums.length - k, res, 0, k);
        System.arraycopy(res, 0, nums, 0, nums.length);
    }
}

Approach #3 Using Cyclic Replacements [Accepted]
# 0ms 100%
class Solution {
    public void rotate(int[] nums, int k) {
        k = k % nums.length;
        int count = 0;
        for (int start = 0; count < nums.length; start++) {
            int current = start;
            int prev = nums[start];
            do {
                int next = (current + k) % nums.length;
                int temp = nums[next];
                nums[next] = prev;
                prev = temp;
                current = next;
                count++;
            } while (start != current);
        }
    }
}

Approach #4 Using Reverse [Accepted]
The basic idea is that, for example, nums = [1,2,3,4,5,6,7] and k = 3,
first we reverse [1,2,3,4], it becomes[4,3,2,1]; then we reverse[5,6,7], it becomes[7,6,5],
finally we reverse the array as a whole, it becomes[4,3,2,1,7,6,5] ---> [5,6,7,1,2,3,4].

Reverse is done by using two pointers, one point at the head and the other point at the tail,
after switch these two, these two pointers move one position towards the middle.


# 0ms 100%
class Solution {
    public void rotate(int[] nums, int k) {
        k %= nums.length;
        reverse(nums, 0, nums.length - k - 1);
        reverse(nums, nums.length - k, nums.length - 1);
        reverse(nums, 0, nums.length - 1);
    }

    private void reverse(int[] nums, int start, int end) {
        while (start < end) {
            int tmp = nums[start];
            nums[start++] = nums[end];
            nums[end--] = tmp;
        }
    }
}
'''
