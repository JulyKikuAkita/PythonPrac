__source__ = 'https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/two-sum-ii-input-array-is-sorted.py
# Time:  O(n)
# Space: O(1)
# Two Pointers
#
# Description: Leetcode # 167. Two Sum II - Input array is sorted
#
# Given an array of integers that is already sorted in ascending order,
# find two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such that
# they add up to the target, where index1 must be less than index2.
# Please note that your returned answers (both index1 and index2) are not zero-based.
#
# You may assume that each input would have exactly one solution.
#
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2
#
# Companies
# Amazon
# Related Topics
# Array Two Pointers Binary Search
# Similar Questions
# Two Sum Two Sum IV - Input is a BST
#
import unittest
#Hide Tags Array Two Pointers Binary Search
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        start, end = 0, len(num) - 1

        while start != end:
            sum = num[start] + num[end]
            if sum > target:
                end -= 1
            elif sum < target:
                start += 1
            else:
                return [start + 1, end + 1]

# test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().twoSum([2,7,11,15], 9)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/solution/
# 0ms 100%
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int[] ret = {-1, -1};
        for (int i = 0, j = numbers.length - 1; i < j;) {
            int sum = numbers[i] + numbers[j];
            if (sum == target) {
                ret[0] = i + 1;
                ret[1] = j + 1;
                return ret;
            } else if (sum < target) {
                int n = numbers[i];
                while (numbers[i] == n)
                    i++;
            } else {
                int n = numbers[j];
                while (numbers[j] == n)
                    j--;
                //j--;
            }
        }

        return ret;
    }
}

O(n)
# 1ms 67.44%
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int start = 0;
        int end = numbers.length - 1;
        while (start < end) {
            int sum = numbers[start] + numbers[end];
            if (sum < target) {
                start++;
            } else if (sum > target) {
                end--;
            } else {
                return new int[] {start + 1, end + 1};
            }
        }
        return new int[0];
    }
}


O(logn)
# 0ms 100%
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int start = 0;
        int end = numbers.length - 1;
        while (start < end) {
            int i = start + 1;
            int j = end;
            while (i <= j) {
                int mid = i + (j - i) / 2;
                int sum = numbers[start] + numbers[mid];
                if (sum < target) {
                    i = mid + 1;
                } else if (sum > target) {
                    j = mid - 1;
                } else {
                    return new int[] {start + 1, mid + 1};
                }
            }
            end = j;
            i = start;
            j = end - 1;
            while (i <= j) {
                int mid = i + (j - i) / 2;
                int sum = numbers[mid] + numbers[end];
                if (sum < target) {
                    i = mid + 1;
                } else if (sum > target) {
                    j = mid - 1;
                } else {
                    return new int[] {mid + 1, end + 1};
                }
            }
            start = i;
        }
        return new int[0];
    }
}
'''