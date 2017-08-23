__source__ = 'https://leetcode.com/problems/longest-increasing-subsequence/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/longest-increasing-subsequence.py
# Time:  O(nlogn)
# Space: O(n)
#
# Description: Leetcode # 300. Longest Increasing Subsequence
#
# Given an unsorted array of integers,
# find the length of longest increasing subsequence.
#
# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101],
# therefore the length is 4. Note that there may be more
# than one LIS combination, it is only necessary for you to return the length.
#
# Your algorithm should run in O(n^2) complexity.
#
# Follow up: Could you improve it to O(n log n) time complexity?
#
# Companies
# Microsoft
# Related Topics
# Binary Search Dynamic Programming
# Similar Questions
# Increasing Triplet Subsequence Russian Doll Envelopes Maximum Length of Pair Chain
#
import unittest
# Binary search solution.
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        LIS = []
        def insert(target):
            left, right = 0, len(LIS) - 1
            # Find the first index "left" which satisfies LIS[left] >= target
            while left <= right:
                mid = (left + right) / 2
                if LIS[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            # If not found, append the target.
            if left == len(LIS):
                LIS.append(target)
            else:
                LIS[left] = target
        for num in nums:
            insert(num)
        return len(LIS)

# Time:  O(n^2)
# Space: O(n)
# Traditional DP solution.
class Solution2(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []  # dp[i]: the length of LIS ends with nums[i]
        for i in xrange(len(nums)):
            dp.append(1)
            for j in xrange(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) if dp else 0

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/articles/longest-increasing-subsequence/

tails is an array storing the smallest tail of all increasing subsequences with length i+1 in tails[i].
For example, say we have nums = [4,5,6,3], then all the available increasing subsequences are:

len = 1   :      [4], [5], [6], [3]   => tails[0] = 3
len = 2   :      [4, 5], [5, 6]       => tails[1] = 5
len = 3   :      [4, 5, 6]            => tails[2] = 6
We can easily prove that tails is a increasing array.
Therefore it is possible to do a binary search in tails array to find the one needs update.

Each time we only do one of the two:

(1) if x is larger than all tails, append it, increase the size by 1
(2) if tails[i-1] < x <= tails[i], update tails[i]
Doing so will maintain the tails invariant. The the final answer is just the size.

#86.98% 1ms
class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] tails = new int[nums.length];
        int size = 0;
        for (int x : nums) {
            int i = 0, j = size;
            while (i != j) {
                int m = (i + j) / 2;
                if (tails[m] < x)
                    i = m + 1;
                else
                    j = m;
            }
            tails[i] = x;
            if (i == size) ++size;
        }
        return size;
    }
}

#86.98% 1ms
public class Solution {
    public int lengthOfLIS(int[] nums) {
        if (nums.length < 2) {
            return nums.length;
        }
        int[] arr = new int[nums.length];
        int tail = -1;
        for (int i = 0; i < nums.length; i++) {
            if (tail == -1 || arr[tail] < nums[i]) {
                arr[++tail] = nums[i];
            } else {
                int index = findFirstLargerOrEqual(arr, 0, tail, nums[i]);
                arr[index] = nums[i];
            }
        }
        return tail + 1;
    }

    private int findFirstLargerOrEqual(int[] arr, int start, int end, int num) {
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (arr[mid] < num) {
                start = mid;
            } else {
                end = mid;
            }
        }
        return arr[start] < num ? end : start;
    }
}

Approach #4 Dynamic Programming with Binary Search[Accepted]:
#86.98% 1ms
public class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] dp = new int[nums.length];
        int len = 0;
        for (int num : nums) {
            int i = Arrays.binarySearch(dp, 0, len, num);
            if (i < 0) {
                i = -(i + 1);
            }
            dp[i] = num;
            if (i == len) {
                len++;
            }
        }
        return len;
    }
}
'''