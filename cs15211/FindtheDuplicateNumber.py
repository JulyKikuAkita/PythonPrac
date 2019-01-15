__source__ = 'https://leetcode.com/problems/find-the-duplicate-number/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/find-the-duplicate-number.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 287. Find the Duplicate Number
#
# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
# prove that at least one duplicate number must exist. Assume that there is only one duplicate number,
# find the duplicate one.
#
# Note:
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated more than once.
#
# Companies
# Bloomberg
# Related Topics
# Array Two Pointers Binary Search
# Similar Questions
# First Missing Positive Single Number Linked List Cycle II Missing Number Set Mismatch
#
import unittest
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Treat each (key, value) pair of the array as the (pointer, next) node of the linked list,
        # thus the duplicated number will be the begin of the cycle in the linked list.
        # Besides, there is always a cycle in the linked list which
        # starts from the first element of the array.
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

# Time:  O(nlogn)
# Space: O(1)
# Binary search method.
class Solution2(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left, right = 1, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            # Get count of num <= mid.
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                right = mid - 1
            else:
                left = mid + 1
        return left

# Time:  O(n)
# Space: O(n)
class Solution3(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        duplicate = 0
        # Mark the value as visited by negative.
        for num in nums:
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1
            else:
                duplicate = abs(num)
                break
        # Rollback the value.

        for num in nums:
            if nums[abs(num) - 1] < 0:
                nums[abs(num) - 1] *= -1
            else:
                break
        return duplicate

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/find-the-duplicate-number/solution/

# 0ms 100%
class Solution {
    public int findDuplicate(int[] nums) {
        int slow = 0;
        int fast = 0;
        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);
        int result = 0;
        while (result != slow) {
            result = nums[result];
            slow = nums[slow];
        }
        return result;
    }
}

suppose the array is

index: 0 1 2 3 4 5

value: 2 5 1 1 4 3
first subtract 1 from each element in the array, so it is much easy to understand.
use the value as pointer. the array becomes:

index: 0 1 2 3 4 5

value: 1 4 0 0 3 2
enter image description here

Second if the array is

index: 0 1 2 3 4 5

value: 0 1 2 4 2 3
we must choose the last element as the head of the linked list. If we choose 0, we can not detect the cycle.

Let the distance from the first node to the the node where cycle begins be A,
and let say the slow pointer travels travels A+B. The fast pointer must travel 2A+2B to catch up.
The cycle size is N. Full cycle is also how much more fast pointer has traveled than slow pointer at meeting point.

A+B+N = 2A+2B
N=A+B

# 0ms 100%
class Solution {
    public int findDuplicate(int[] nums) {
        int length = nums.length;
        int slow = length;
        int fast = length;
        do {
            slow = nums[slow - 1];
            fast = nums[nums[fast - 1] - 1];
        } while (slow != fast);
        slow = length;
        while (slow != fast) {
            slow = nums[slow - 1];
            fast = nums[fast - 1];
        }
        return slow;
    }
}
'''