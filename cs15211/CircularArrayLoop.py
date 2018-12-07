__source__ = 'https://leetcode.com/problems/circular-array-loop/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 457. Circular Array Loop
#
# You are given an array of positive and negative integers.
# If a number n at an index is positive, then move forward n steps.
# Conversely, if it's negative (-n), move backward n steps.
# Assume the first element of the array is forward next to the last element,
# and the last element is backward next to the first element.
# Determine if there is a loop in this array.
# A loop starts and ends at a particular index with more than 1 element along the loop.
# The loop must be "forward" or "backward'.
#
# Example 1: Given the array [2, -1, 1, 2, 2], there is a loop, from index 0 -> 2 -> 3 -> 0.
#
# Example 2: Given the array [-1, 2], there is no loop. (not the same direction so not an loop)
#
# Note: The given array is guaranteed to contain no element "0".
#
# Can you do it in O(n) time complexity and O(1) space complexity?
#

import unittest

# O(n) time O(1) space
# 20 ms 91.03%
class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) < 2:
            return False
        n = len(nums)
        for i in xrange(n) :
            if type(nums[i]) != int: # visited element
                continue
            if nums[i] % n == 0: #self-loop
                continue

            direction = (nums[i] > 0) # loop direction, cannot be changed midway
            mark = str(i)
            while (type(nums[i]) == int and (direction ^ (nums[i] < 0)) and (nums[i] % n != 0)):
                jump = nums[i]
                nums[i] = mark
                i = (i + jump) % n

            if nums[i] == mark:
                return True
        return False
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# https://leetcode.com/problems/circular-array-loop/discuss/94148/Java-SlowFast-Pointer-Solution
# slow/fast pointer :
# If there is a loop (fast == slow), we return true,
else if we meet element with different directions,
then the search fail, we set all elements along the way to 0.
Because 0 is fail for sure so when later search meet 0 we know the search will fail.

#100% 0ms
class Solution {
    public boolean circularArrayLoop(int[] nums) {
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) continue;
            // slow/fast pointer
            int j = i, k = getIndex(i, nums);
            while (nums[k] * nums[i] > 0 && nums[getIndex(k, nums)] * nums[i] > 0) {
                if (j == k) { // check for loop with only one element
                    if (j == getIndex(j, nums)) break;
                    return true;
                }
                j = getIndex(j, nums);
                k = getIndex(getIndex(k, nums), nums);
            }
            // loop not found, set all element along the way to 0
            j = i;
            int val = nums[i];
            while (nums[j] * val > 0) {
                int next = getIndex(j, nums);
                nums[j] = 0;
                j = next;
            }
        }
        return false;
    }

    public int getIndex(int i, int[] nums) {
        int n = nums.length;
        return i + nums[i] >= 0 ? (i + nums[i]) % n : n + ((i + nums[i]) % n);
    }
}

#100% 0ms
class Solution {
    // environment
    private int[] localNums;
    private int size;
    private boolean isForward;

    public boolean circularArrayLoop(int[] nums) {
        if (nums == null || nums.length == 0) { return false; }
        localNums = nums;
        size = nums.length;
        isForward = (nums[0] > 0);
        int slow = 0, fast = 0;
        do {
            for (int i = 0; i < 2; i++) {
                if (isCrossward(fast)) return false;
                fast = skip(fast); //fast move twice
            }
            slow = skip(slow);
        } while(slow != fast);
        return fast == 0; // something they called loop here must go back to the first element
    }

    private int skip(int index) {
        index += localNums[index];
        if (isForward && index >= size) index %= size;
        else if (!isForward && index < 0) index = index % size + size;
        return index;
    }

    private boolean isCrossward(int index) {
        return (isForward && localNums[index] < 0) || (!isForward && localNums[index] > 0);
    }
}
'''