# coding=utf-8
__source__ = 'https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/'
# Time:  O(log(n))
# Space: O(1)
#
# Description: Leetcode # 34. Find First and Last Position of Element in Sorted Array
#
# Given an array of integers nums sorted in ascending order,
# find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example 1:
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
#
# Example 2:
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
#

import unittest


class Solution(object):
    pass  # your function here


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/
Approach 1: Linear Scan
Complexity Analysis
Time complexity : O(n)
This brute-force approach examines each of the n elements of nums exactly twice,
so the overall runtime is linear.
Space complexity : O(1)
The linear scan method allocates a fixed-size array and a few integers,
so it has a constant-size memory footprint.

# 6ms 27.95%
class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] targetRange = {-1, -1};

        // find the index of the leftmost appearance of `target`.
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target) {
                targetRange[0] = i;
                break;
            }
        }

        // if the last loop did not find any index, then there is no valid range
        // and we return [-1, -1].
        if (targetRange[0] == -1) {
            return targetRange;
        }

        // find the index of the rightmost appearance of `target` (by reverse
        // iteration). it is guaranteed to appear.
        for (int j = nums.length-1; j >= 0; j--) {
            if (nums[j] == target) {
                targetRange[1] = j;
                break;
            }
        }

        return targetRange;
    }
}

Approach 2: Binary Search
Complexity Analysis
Time complexity : O(log(n))
Because binary search cuts the search space roughly in half on each iteration,
there can be at most ceil⌈log10(n)⌉ iterations.
Binary search is invoked twice, so the overall complexity is logarithmic.
Space complexity : O(1)
All work is done in place, so the overall memory usage is constant.

# 3ms 100%
class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] res = new int[]{-1, -1};
        if( nums == null || nums.length == 0) return res;
        int left = 0;
        int right = nums.length;

        while (left < right){
            int mid = (left + right) / 2;
            if(nums[mid] < target){
                left = mid + 1;
            }else if(nums[mid] > target){
                right = mid;
            }else{
                int i = mid;
                int j = mid;
                while(i > 0 && nums[i-1] == target){i--;};
                while(j < nums.length - 1 && nums[j+1] == target){j++;};
                res[0] = i;
                res[1] = j;
                return res;
            }
        }

        return res;
    }
}

# 3ms 100%
class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] result = {-1, -1};
        if (nums == null || nums.length == 0 || nums[0] > target || nums[nums.length - 1] < target) {
            return result;
        }
        helper(nums, target, 0, nums.length - 1, result);
        return result;
    }

    private void helper(int[] nums, int target, int start, int end, int[] result) {
        if (start > end) {
            return;
        }
        int mid = (start + end) / 2;
        if (nums[mid] == target) {
            if (result[0] == -1) {
                result[0] = mid;
                result[1] = mid;
            } else {
                result[0] = Math.min(result[0], mid);
                result[1] = Math.max(result[1], mid);
            }
            helper(nums, target, start, mid - 1, result);
            helper(nums, target, mid + 1, end, result);
        } else if (nums[mid] < target) {
            helper(nums, target, mid + 1, end, result);
        } else {
            helper(nums, target, start, mid - 1, result);
        }
    }
}

# 3ms 100%
class Solution {
    // returns leftmost (or rightmost) index at which `target` should be
    // inserted in sorted array `nums` via binary search.
    private int extremeInsertionIndex(int[] nums, int target, boolean left) {
        int lo = 0;
        int hi = nums.length;

        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (nums[mid] > target || (left && target == nums[mid])) {
                hi = mid;
            }
            else {
                lo = mid+1;
            }
        }

        return lo;
    }

    public int[] searchRange(int[] nums, int target) {
        int[] targetRange = {-1, -1};

        int leftIdx = extremeInsertionIndex(nums, target, true);

        // assert that `leftIdx` is within the array bounds and that `target`
        // is actually in `nums`.
        if (leftIdx == nums.length || nums[leftIdx] != target) {
            return targetRange;
        }

        targetRange[0] = leftIdx;
        targetRange[1] = extremeInsertionIndex(nums, target, false)-1;

        return targetRange;
    }
}

'''