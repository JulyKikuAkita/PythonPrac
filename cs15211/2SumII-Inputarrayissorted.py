__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/two-sum-ii-input-array-is-sorted.py
# Time:  O(n)
# Space: O(1)
# Two Pointers
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
# Amazon
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

#test
if __name__ == "__main__":
    print Solution().twoSum([2,7,11,15], 9)

# java:
js = ''' 40.13%
public class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int start = 0;
        int end = numbers.length - 1;
        while (start < end) {
            int tmpStart = start + 1;
            int tmpEnd = end;
            while (tmpStart <= tmpEnd) {
                int mid = tmpStart + (tmpEnd - tmpStart) / 2;
                long sum = (long) numbers[mid] + numbers[start];
                if (sum < target) {
                    tmpStart = mid + 1;
                } else if (sum > target) {
                    tmpEnd = mid - 1;
                } else {
                    return new int[] {start + 1, mid + 1};
                }
            }
            end = tmpEnd;
            tmpStart = start;
            tmpEnd = end - 1;
            while (tmpStart <= tmpEnd) {
                int mid = tmpStart + (tmpEnd - tmpStart) / 2;
                long sum = (long) numbers[mid] + numbers[end];
                if (sum < target) {
                    tmpStart = mid + 1;
                } else if (sum > target) {
                    tmpEnd = mid - 1;
                } else {
                    return new int[] {mid + 1, end + 1};
                }
            }
            start = tmpStart;
        }
        return null;
    }
}

'''

js2 = ''' 97.81%
public class Solution {
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