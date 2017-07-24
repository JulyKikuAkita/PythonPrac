__source__ = 'https://leetcode.com/problems/create-maximum-number/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/create-maximum-number.py
# Time:  O(k * (m + n + k)) ~ O(k * (m + n + k^2))
# Space: O(m + n + k^2)
#
# Description: Leetcode # 321. Create Maximum Number
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
#
# Companies
# Google
# Related Topics
# Dynamic Programming Greedy
# Similar Questions
# Remove K Digits

import unittest
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


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
Thought: https://www.hrwhisper.me/leetcode-create-maximum-number/
Many of the posts have the same algorithm. In short we can first solve 2 simpler problem
Create the maximum number of one array
Create the maximum number of two array using all of their digits.

The algorithm is O((m+n)^3) in the worst case. It runs in 22 ms.

#27 %
public class Solution {
    public int[] maxNumber(int[] nums1, int[] nums2, int k) {
        int n = nums1.length;
        int m = nums2.length;
        int[] ans = new int[k];
        for (int i = Math.max(0, k - m); i <= k && i <= n; ++i) {
            int[] candidate = merge(maxArray(nums1, i), maxArray(nums2, k - i), k);
            if (greater(candidate, 0, ans, 0)) ans = candidate;
        }
        return ans;
    }

    public boolean greater(int[] nums1, int i, int[] nums2, int j) {
        while (i < nums1.length && j < nums2.length && nums1[i] == nums2[j]) {
            i++;
            j++;
        }
        return j == nums2.length || (i < nums1.length && nums1[i] > nums2[j]);
    }

    private int[] merge(int[] nums1, int[] nums2, int k) {
        int[] ans = new int[k];
        for (int i = 0, j = 0, r = 0; r < k; ++r)
            ans[r] = greater(nums1, i, nums2, j) ? nums1[i++] : nums2[j++];
        return ans;
    }

    public int[] maxArray(int[] nums, int k) {
        int n = nums.length;
        int[] ans = new int[k];
        for (int i = 0, j = 0; i < n; i++) {
            while(n - i + j > k && j > 0 && ans[j - 1] < nums[i]) j--;
            if (j < k) ans[j++] = nums[i];
        }
        return ans;
    }
}
The basic idea:

To create max number of length k from two arrays, you need to create max number of length i from array one
and max number of length k-i from array two, then combine them together.
After trying all possible i, you will get the max number created from two arrays.

Optimization:

Suppose nums1 = [3, 4, 6, 5], nums2 = [9, 1, 2, 5, 8, 3],
the maximum number you can create from nums1 is [6, 5] with length 2.
For nums2, it's [9, 8, 3] with length 3. Merging the two sequence,
we have [9, 8, 6, 5, 3], which is the max number we can create from two arrays without length constraint.
If the required length k<=5, we can simply trim the result to required length from front.
For instance, if k=3, then [9, 8, 6] is the result.

Suppose we need to create max number with length 2 from num = [4, 5, 3, 2, 1, 6, 0, 8].
The simple way is to use a stack, first we push 4 and have stack [4], then comes 5 > 4,
we pop 4 and push 5, stack becomes [5], 3 < 5, we push 3, stack becomes [5, 3].
Now we have the required length 2, but we need to keep going through the array in case a larger number comes, 2 < 3,
we discard it instead of pushing it because the stack already grows to required size 2. 1 < 3, we discard it. 6 > 3,
we pop 3, since 6 > 5 and there are still elements left, we can continue to pop 5 and push 6, the stack becomes [6],
since 0 < 6, we push 0, the stack becomes [6, 0], the stack grows to required length again. Since 8 > 0, we pop 0,
although 8 > 6, we can't continue to pop 6 since there is only one number, which is 8, left, if we pop 6 and push 8,
we can't get to length 2, so we push 8 directly, the stack becomes [6, 8].

In the basic idea, we mentioned trying all possible length i.
If we create max number for different i from scratch each time,
that would be a waste of time. Suppose num = [4, 9, 3, 2, 1, 8, 7, 6],
we need to create max number with length from 1 to 8. For i==8, result is the original array.
For i==7, we need to drop 1 number from array, since 9 > 4, we drop 4, the result is [9, 3, 2, 1, 8, 7, 6].
For i==6, we need to drop 1 more number, 3 < 9, skip, 2 < 3, skip, 1 < 2, skip, 8 > 1, we drop 1,
the result is [9, 3, 2, 8, 7, 6]. For i==5, we need to drop 1 more, but this time, we needn't check from beginning,
during last scan, we already know [9, 3, 2] is monotonically non-increasing, so we check 8 directly, since 8 > 2,
we drop 2, the result is [9, 3, 8, 7, 6]. For i==4, we start with 8, 8 > 3, we drop 3, the result is [9, 8, 7, 6].
For i==3, we start with 8, 8 < 9, skip, 7 < 8, skip, 6 < 7, skip, by now,
we've got maximum number we can create from num without length constraint.
So from now on, we can drop a number from the end each time.
The result is [9, 8, 7], For i==2, we drop last number 7 and have [9, 8]. For i==1, we drop last number 8 and have [9].

Input:
[2,5,6,4,4,0]
[7,3,8,0,6,5,7,6,2]
15
Output:
[7,3,8,2,5,6,4,4,0,0,6,5,7,6,2]
Expected:
[7,3,8,2,5,6,4,4,0,6,5,7,6,2,0]

# 99.21% 13ms
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