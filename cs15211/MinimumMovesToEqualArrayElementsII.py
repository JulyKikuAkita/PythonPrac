__source__ = 'https://github.com/kamyu104/LeetCode/blob/master/Python/minimum-moves-to-equal-array-elements-ii.py'
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/#/solutions
# Time:  O(n) on average
# Space: O(1)
#
# Description:
# Given a non-empty integer array, find the minimum number of moves required to make all array elements equal,
# where a move is incrementing a selected element by 1 or decrementing a selected element by 1.
#
# You may assume the array's length is at most 10,000.
#
# Example:
#
# Input:
# [1,2,3]
#
# Output:
# 2
#
# Explanation:
# Only two moves are needed (remember each move increments or decrements one element):
#
# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]
# Hide Tags Math
# Hide Similar Problems (H) Best Meeting Point (E) Minimum Moves to Equal Array Elements
#
#
import unittest
from random import randint
# Quick select solution.
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def kthElement(nums, k):
            def PartitionAroundPivot(left, right, pivot_idx, nums):
                pivot_value = nums[pivot_idx]
                new_pivot_idx = left
                nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
                for i in xrange(left, right):
                    if nums[i] > pivot_value:
                        nums[i], nums[new_pivot_idx] = nums[new_pivot_idx], nums[i]
                        new_pivot_idx += 1

                nums[right], nums[new_pivot_idx] = nums[new_pivot_idx], nums[right]
                return new_pivot_idx

            left, right = 0, len(nums) - 1
            while left <= right:
                pivot_idx = randint(left, right)
                new_pivot_idx = PartitionAroundPivot(left, right, pivot_idx, nums)
                if new_pivot_idx == k - 1:
                    return nums[new_pivot_idx]
                elif new_pivot_idx > k - 1:
                    right = new_pivot_idx - 1
                else:  # new_pivot_idx < k - 1.
                    left = new_pivot_idx + 1

        median = kthElement(nums, len(nums)/2 + 1)
        return sum(abs(num - median) for num in nums)

    def minMoves22(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        median = sorted(nums)[len(nums) / 2]
        return sum(abs(num - median) for num in nums)

    def minMoves23(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(nums[~i] - nums[i] for i in xrange(len(nums) / 2))


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()


Java = '''
#Thought: https://leetcode.com/articles/minimum-moves-to-equal-array-elements-ii/#approach-7-using-median-of-medians-accepted
Java O(n) Time using QuickSelect
This solution relies on the fact that if we increment/decrement each element to the median of all the elements,
the optimal number of moves is necessary.
The median of all elements can be found in expected O(n) time using QuickSelect
(or deterministic O(n) time using Median of Medians).

public class Solution {
    public int minMoves2(int[] nums) {
        int sum = 0;
        int median = quickSelect(nums, nums.length / 2 + 1, 0, nums.length - 1);

        for (int i = 0; i < nums.length; i++) {
            sum += Math.abs(nums[i] - median);
        }
        return sum;
    }

    public int quickSelect(int[] arr, int k, int start, int end) {
        int l = start, r = end, pivot = arr[(l + r) / 2];
        while (l <= r) {
            while (arr[l] < pivot) l++;
            while (arr[r] > pivot) r--;
            if ( l >= r) break;
            swap(arr, l++, r--);
        }

        if (l - start + 1 > k) return quickSelect(arr, k, start, l - 1);
        if (l - start + 1 == k && l == r) return arr[l];
        return quickSelect(arr, k - r + start - 1, r + 1, end);
    }

    public void swap(int[] arr, int i, int j) {
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }
}

# count the difference between median
public class Solution2 {
    public int minMoves2(int[] nums) {
        Arrays.sort(nums);
        int i = 0, j = nums.length - 1;
        int count = 0;
        while (i < j) {
            count += nums[j] - nums[i];
            i++;
            j--;
        }
        return count;
    }
}
'''