__source__ = 'https://leetcode.com/problems/search-in-rotated-sorted-array/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/search-in-rotated-sorted-array.py
# Time:  O(logn)
# Space: O(1)
# Binary Search
#
# Description: Leetcode # 33. Search in Rotated Sorted Array
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
# Companies
# LinkedIn Bloomberg Uber Facebook Microsoft
# Related Topics
# Binary Search Array
# Similar Questions
# Search in Rotated Sorted Array II Find Minimum in Rotated Sorted Array
#
import unittest
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        low, high = 0, len(A)

        while low < high:
            mid = low + (high - low) / 2
            if A[mid] == target:
                return mid

            if A[low] <= A[mid]:
                if A[low] <= target and target < A[mid]:
                    high = mid
                else:
                    low= mid + 1
            else:
                if A[mid] < target and target <= A[high - 1]:
                    low = mid + 1
                else:
                    high = mid
        return -1

class SolutionCC150:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        low, high = 0, len(A) - 1

        while low <= high:
            mid = (low + high) / 2
            if A[mid] == target:
                return mid
            elif A[low] <= A[mid]:
                if target > A[mid]:
                    low = mid + 1
                elif target >= A[low]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif target < A[mid]:
                high = mid - 1
            elif target <= A[high]:
                low = mid + 1
            else:
                high = mid -1
        return -1

class SolutionOther:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        begin, end = 0, len(A)-1
        while begin <= end:
            mid = begin + ((end - begin) >> 1)

            if A[mid] == target:
                return mid
            elif (A[mid] > A[begin] and target >= A[begin] and target < A[mid]) or \
                 (A[mid] < A[begin] and not (target <= A[end] and target > A[mid])):
                end = mid - 1
            else:
                begin = mid + 1
        return -1


class Solution3(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) < 1 :
            return -1

        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[start]:  # no =, fail
                if target >= nums[start] and target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if target >= nums[mid] and target <= nums[end]: # no =, fail
                    start = mid
                else:
                    end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().search([3, 5, 1], 3)
        print Solution().search([1], 1)
        print Solution().search([4, 5, 6, 7, 0, 1, 2], 5)
        print
        print SolutionCC150().search([3, 5, 1], 3)
        print SolutionCC150().search([1], 1)
        print SolutionCC150().search([4, 5, 6, 7, 0, 1, 2], 5)
        print SolutionCC150().search([1, 3, 5], 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
Explanation

Let's say nums looks like this: [12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

Because it's not fully sorted, we can't do normal binary search. But here comes the trick:

If target is let's say 14, then we adjust nums to this, where "inf" means infinity:
[12, 13, 14, 15, 16, 17, 18, 19, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]

If target is let's say 7, then we adjust nums to this:
[-inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

And then we can simply do ordinary binary search.
# 87.20% 13ms
public class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return mid;
            }
            if (nums[left] <= nums[mid]) { //need to have equal here, otherwise fail,
            dunno why cannot at else part ex: [3,1] and target = 1
                if (nums[left] < target && target <= nums[mid]) { //here all equal also pass
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {
                if (nums[mid] < target && target <= nums[right]) { //here all equal also pass
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        return -1;
    }
}


Note: unable to use Collections.binarySearch
public class Solution {
    public int search(int[] nums, int target) {
        List<Integer> res = new LinkedList<>();
        for (int n: nums) res.add(n);
        int idx = Collections.binarySearch(res, target);
        return  idx < 0 ? -1 : idx;
    }
}

'''