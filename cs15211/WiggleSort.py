__source__ = 'https://leetcode.com/problems/wiggle-sort/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/wiggle-sort.py
# Time:  O(n)
# Space: O(1)
# Description: Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
# For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].
# Companies
# Google
# Related Topics
# Array Sort
# Similar Questions
# Sort Colors Wiggle Sort II
#
import unittest
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in xrange(1, len(nums)):
            if ((i % 2) and nums[i - 1] > nums[i]) or \
                (not (i % 2) and nums[i - 1] < nums[i]):
                # Swap unordered elements.
                nums[i - 1], nums[i] = nums[i], nums[i - 1]


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

#Java
# http://blog.csdn.net/xudli/article/details/48749155
Java = '''
Thought: https://leetcode.com/articles/wiggle-sort/
The final sorted nums needs to satisfy two conditions:

If i is odd, then nums[i] >= nums[i - 1];
If i is even, then nums[i] <= nums[i - 1].

why is this greedy solution can ensure previous sequences and coming sequences W.R.T position i wiggled?
My explanation is recursive,
suppose nums[0 .. i - 1] is wiggled, for position i:
if i is odd, we already have, nums[i - 2] >= nums[i - 1],
if nums[i - 1] <= nums[i], then we does not need to do anything, its already wiggled.
if nums[i - 1] > nums[i], then we swap element at i -1 and i.
Due to previous wiggled elements (nums[i - 2] >= nums[i - 1]),
we know after swap the sequence is ensured to be nums[i - 2] > nums[i - 1] < nums[i], which is wiggled.

similarly,
if i is even, we already have, nums[i - 2] <= nums[i - 1],
if nums[i - 1] >= nums[i], pass
if nums[i - 1] < nums[i], after swap, we are sure to have wiggled nums[i - 2] < nums[i - 1] > nums[i].
The same recursive solution applies to all the elements in the sequence, ensuring the algo success.

# 63.16%, 1 ms
public class Solution {
    public void wiggleSort(int[] nums) {
        if(nums == null || nums.length <2 ) return;

        for(int i = 1; i < nums.length; i++){
            if( (i % 2 == 0 && nums[i-1] < nums[i] ) || (i % 2 != 0 && nums[i-1] > nums[i])){
                int tmp = nums[i];
                nums[i] = nums[i-1];
                nums[i-1] = tmp;
            }
        }

    }
}

#25.26%, 2ms
public class Solution {
    public void wiggleSort(int[] nums) {
        for (int i = 0; i < nums.length - 1; i++) {
            if ((i % 2 == 0) == (nums[i] > nums[i + 1])) {
                swap(nums, i, i + 1);
            }
        }
    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}


#25.26%, 2ms
public class Solution {
    public void wiggleSort(int[] nums) {
        for (int i = 0; i < nums.length - 1; i++) {
            if ((i & 1) == 0) {
                if (nums[i] > nums[i + 1]) {
                    swap(nums, i, i + 1);
                }
            } else {
                if (nums[i] < nums[i + 1]) {
                    swap(nums, i, i + 1);
                }
            }
        }
    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}
'''