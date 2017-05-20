__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/sort-transformed-array.py
'''
Given a sorted array of integers nums and integer values a, b and c. Apply a function of the form f(x) = ax2 + bx + c to each element x in the array.

The returned array must be in sorted order.

Expected time complexity: O(n)

Example:
nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,

Result: [3, 9, 15, 33]

nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5

Result: [-23, -5, 1, 7]
Credits:
Special thanks to @elmirap for adding this problem and creating all test cases.

Hide Company Tags Google
Hide Tags Math Two Pointers

'''
# Time:  O(n)
# Space: O(1)

class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        f = lambda x, a, b, c : a * x * x + b * x + c

        result = []
        if not nums:
            return result

        left, right = 0, len(nums) - 1
        d = -1 if a > 0 else 1
        while left <= right:
            if d * f(nums[left], a, b, c) < d * f(nums[right], a, b, c):
                result.append(f(nums[left], a, b, c))
                left += 1
            else:
                result.append(f(nums[right], a, b, c))
                right -= 1

        return result[::d]


#Java
js ='''
public class Solution {
    public int[] sortTransformedArray(int[] nums, int a, int b, int c) {
        if (nums.length == 0) {
            return nums;
        }
        if (a == 0) {
            return transform1DArray(nums, b, c);
        } else {
            return transform2DArray(nums, a, b, c);
        }
    }

    private int[] transform1DArray(int[] nums, int b, int c) {
        int[] result = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            result[i] = calculate(nums[i], 0, b, c);
        }
        if (b < 0) {
            reverse(result);
        }
        return result;
    }

    private int[] transform2DArray(int[] nums, int a, int b, int c) {
        int[] result = new int[nums.length];
        int index = 0;
        double midPoint = -((double) b / a / 2);
        int closestIndex = findClosestIndex(nums, midPoint);
        int left = closestIndex - 1;
        int right = closestIndex + 1;

        result[index++] = calculate(nums[closestIndex], a, b, c);
        while (left >= 0 && right < nums.length) {
            if (Math.abs(nums[left] - midPoint) < Math.abs(nums[right] - midPoint)) {
                result[index++] = calculate(nums[left--], a, b, c);
            } else {
                result[index++] = calculate(nums[right++], a, b, c);
            }
        }
        while (left >= 0) {
            result[index++] = calculate(nums[left--], a, b, c);
        }
        while (right < nums.length) {
            result[index++] = calculate(nums[right++], a, b, c);
        }
        if (a < 0) {
            reverse(result);
        }
        return result;
    }

    private int findClosestIndex(int[] nums, double midPoint) {
        int index = 0;
        int start = 0;
        int end = nums.length - 1;
        while (start <= end) {
            int mid = start + (end - start) / 2;
            if (Math.abs(nums[mid] - midPoint) < Math.abs(nums[index] - midPoint)) {
                index = mid;
            }
            if (nums[mid] < midPoint) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        return index;
    }

    private int calculate(int num, int a, int b, int c) {
        return a * num * num + b * num + c;
    }

    private void reverse(int[] arr) {
        int start = 0;
        int end = arr.length - 1;
        while (start < end) {
            swap(arr, start++, end--);
        }
    }

    private void swap(int[] arr, int a, int b) {
        int tmp = arr[a];
        arr[a] = arr[b];
        arr[b] = tmp;
    }
}
'''