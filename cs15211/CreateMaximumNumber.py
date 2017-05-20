__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/create-maximum-number.py
# Time:  O(k * (m + n + k)) ~ O(k * (m + n + k^2))
# Space: O(m + n + k^2)
#
# Given two arrays of length m and n with digits 0-9 representing two numbers.
# Create the maximum number of length k <= m + n from digits of the two.
# The relative order of the digits from the same array must be preserved.
# Return an array of the k digits. You should try to optimize your time
# and space complexity.
#
# Example 1:
# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
# return [9, 8, 6, 5, 3]
#
# Example 2:
# nums1 = [6, 7]
# nums2 = [6, 0, 4]
# k = 5
# return [6, 7, 6, 0, 4]
#
# Example 3:
# nums1 = [3, 9]
# nums2 = [8, 9]
# k = 3
# return [9, 8, 9]
#  Google
# Dynamic Programming Greedy


# DP + Greedy solution. (280ms)
class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def get_max_digits(nums, start, end, max_digits):
            max_digits[end] = max_digit(nums, end)
            for i in reversed(xrange(start, end)):
                max_digits[i] = delete_digit(max_digits[i + 1])

        def max_digit(nums, k):
            drop = len(nums) - k
            res = []
            for num in nums:
                while drop and res and res[-1] < num:
                    res.pop()
                    drop -= 1
                res.append(num)
            return res[:k]

        def delete_digit(nums):
            res = list(nums)
            for i in xrange(len(res)):
                if i == len(res) - 1 or res[i] < res[i + 1]:
                    res = res[:i] + res[i+1:]
                    break
            return res

        def merge(a, b):
            return [max(a, b).pop(0) for _ in xrange(len(a)+len(b))]

        m, n = len(nums1), len(nums2)

        max_digits1, max_digits2 = [[] for _ in xrange(k + 1)], [[] for _ in xrange(k + 1)]
        get_max_digits(nums1, max(0, k - n), min(k, m), max_digits1)
        get_max_digits(nums2, max(0, k - m), min(k, n), max_digits2)

        return max(merge(max_digits1[i], max_digits2[k-i]) \
                   for i in xrange(max(0, k - n), min(k, m) + 1))


#java
js = '''
public class Solution {
    public int[] maxNumber(int[] nums1, int[] nums2, int k) {
        int[] result = new int[k];
        Arrays.fill(result, Integer.MIN_VALUE);
        for (int i = Math.max(0, k - nums2.length); i <= Math.min(nums1.length, k); i++) {
            int[] cur1 = maxKNumbers(nums1, i);
            int[] cur2 = maxKNumbers(nums2, k - i);
            int[] cur = merge(cur1, cur2);
            if (compare(result, 0, cur, 0) < 0) {
                result = cur;
            }
        }
        return result;
    }

    private int[] maxKNumbers(int[] nums, int k) {
        int[] result = new int[k];
        int end = -1;
        for (int i = 0; i < nums.length; i++) {
            while (end >= 0 && result[end] < nums[i] && k - end <= nums.length - i) {
                end--;
            }
            if (end < k - 1) {
                result[++end] = nums[i];
            }
        }
        return result;
    }

    private int[] merge(int[] nums1, int[] nums2) {
        int len1 = nums1.length;
        int len2 = nums2.length;
        int[] result = new int[len1 + len2];
        int index1 = 0;
        int index2 = 0;
        int index = 0;
        while (index1 < len1 && index2 < len2) {
            if (compare(nums1, index1, nums2, index2) > 0) {
                result[index++] = nums1[index1++];
            } else {
                result[index++] = nums2[index2++];
            }
        }
        while (index1 < len1) {
            result[index++] = nums1[index1++];
        }
        while (index2 < len2) {
            result[index++] = nums2[index2++];
        }
        return result;
    }

    private int compare(int[] nums1, int index1, int[] nums2, int index2) {
        while (index1 < nums1.length && index2 < nums2.length) {
            int compare = Integer.compare(nums1[index1++], nums2[index2++]);
            if (compare != 0) {
                return compare;
            }
        }
        return index1 == nums1.length ? -1 : 1;
    }
}
'''