__source__ = 'https://leetcode.com/problems/remove-element/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/remove-element.py
# Time:  O(n)
# Space: O(1)
# Array
#
# Description: Leetcode # 27. Remove Element
#
# Given an array and a value, remove all instances of that value in place and return the new length.
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
#
# Example:
# Given input array nums = [3,2,2,3], val = 3
#
# Your function should return length = 2, with the first two elements of nums being 2.
# Related Topics
# Array Two Pointers
# Similar Questions
# Remove Duplicates from Sorted Array Remove Linked List Elements Move Zeroes
#
import unittest
class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        i, last = 0, len(A) - 1
        while i <= last:
            if A[i] == elem:
                A[i], A[last] = A[last], A[i]
                last -= 1
            else:
                i += 1
        return last + 1

class SolutionOther:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        answer =0
        for i in range(len(A)):
            if A[i] != elem:
                A[answer]=A[i]
                answer += 1
        return answer

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        t1 = SolutionOther()
        print t1.removeElement([1,1,1],1)
        print t1.removeElement([1, 2, 3, 4, 5, 2, 2], 2)
        A = [1, 2, 3, 4, 5, 2, 2]
        print Solution().removeElement(A, 2) , A

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/remove-element/solution/

# Two pointers
# 27.72% 10ms
class Solution {
    public int removeElement(int[] nums, int val) {
        int end = -1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[++end] = nums[i];
            }
        }
        return end + 1;
    }
}

# Two pointers
# 4ms 98.55%
class Solution {
    public int removeElement(int[] nums, int val) {
        int j = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[j++] = nums[i];
            }
        }
        return j;
    }
}

# 6ms 45.82%
class Solution {
    public int removeElement(int[] nums, int val) {
        int i = 0;
        int n = nums.length;
        while (i < n) {
            if (nums[i] == val) {
                nums[i] = nums[n - 1];
                // reduce array size by one
                n--;
            } else {
                i++;
            }
        }
        return n;
    }
}


# 4ms 98.55%
class Solution {
    public int removeElement(int[] nums, int val) {
        int end = nums.length;
        for (int i = 0; i < end; i++) {
            if (nums[i] == val) {
                swap(nums, i--, --end);
            }
        }
        return end;
    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}

'''
