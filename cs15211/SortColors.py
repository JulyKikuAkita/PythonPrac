__source__ = 'https://leetcode.com/problems/sort-colors/'
# Time:  O(n)
# Space: O(1)
# Sort
#
# Description: Leetcode # 75. Sort Colors
#
# Given an array with n objects colored red, white or blue,
# sort them so that objects of the same color are adjacent,
# with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note:
# You are not suppose to use the library's sort function for this problem.
#
# click to show follow up.
#
# Follow up:
# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's,
# then overwrite array with total number of 0's, then 1's and followed by 2's.
#
# Could you come up with an one-pass algorithm using only constant space?
#
# Companies
# Pocket Gems Microsoft Facebook
# Related Topics
# Array Two Pointers Sort
# Similar Questions
# Sort List Wiggle Sort Wiggle Sort II
#
import unittest
class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        i, last_zero, first_two = 0, -1, len(A)
        while i < first_two:
            if A[i] == 0:
                last_zero += 1
                A[i], A[last_zero] = A[last_zero], A[i]
            elif A[i] == 2:
                first_two -= 1
                A[i], A[first_two] = A[first_two], A[i]
                i -= 1  # i need to be at the same position as element switch from end of arr is not sorted yet
            i += 1

class SolutionOther:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        if A == []:
            return
        length = len(A)
        i, p0, p2= 0, 0, length - 1

        while i <= p2:
            if A[i] == 2:
                A[p2], A[i] = A[i], A[p2]
                p2 -= 1
            elif A[i] == 0:
                A[p0], A[i] = A[i], A[p0]
                p0 += 1
                i += 1
            else:
                i+= 1

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        #test
        test = SolutionOther()
        arr = [2,1,0,0,2,2,2,1,0]
        arr1 = [1,0]
        test.sortColors(arr1)
        print arr1

        A = [2, 1, 1, 0, 0, 2]
        Solution().sortColors(A)
        print A

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# 0ms 100%
class Solution {
    public void sortColors(int[] nums) {
        int red = 0;
        int blue = nums.length - 1;
        int cur = 0;
        while (cur <= blue) {
            if (nums[cur] == 0) {
                swap(nums, red++, cur++);
            } else if (nums[cur] == 2) {
                swap(nums, blue--, cur);
            } else {
                cur++;
            }
        }
    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}

# Two pass: count each color and then swap
# 0ms 100%
class Solution {
    public void sortColors(int[] nums) {
        int num0 = 0, num1 = 0, num2 = 0;

        for(int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) ++num0;
            else if (nums[i] == 1) ++num1;
            else if (nums[i] == 2) ++num2;
        }

        for(int i = 0; i < num0; ++i) nums[i] = 0;
        for(int i = 0; i < num1; ++i) nums[num0+i] = 1;
        for(int i = 0; i < num2; ++i) nums[num0+num1+i] = 2;
    }
}
'''
