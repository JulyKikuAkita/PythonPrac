__source__ = 'https://leetcode.com/problems/find-peak-element/description/'
# Time:  O(logn)
# Space: O(1)
#
# Description: Leetcode # 217. Contains Duplicate
#
# A peak element is an element that is greater than its neighbors.
#
# Given an input array where num[i] != num[i+1], find a peak element and return its index.
#
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
#
# You may imagine that num[-1] = num[n] = -infinite.
#
# For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
#
# Note:
# Your solution should be in logarithmic complexity.
# Companies
# Microsoft Google
# Related Topics
# Binary Search Array
#
import unittest
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        low, high = 0, len(num) - 1

        while low < high:
            mid = (low + high) / 2
            if ( mid == 0 or num[mid] >= num[mid - 1]) and \
               ( mid == len(num) - 1 or num[mid] >= num[mid+1] ):
                return mid
            elif mid > 0 and num[mid - 1] > num[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return low

# http://bookshadow.com/weblog/2014/12/06/leetcode-find-peak-element/
class SolutionOther:
    # @param num, a list of integer
    # @return an integer
    #o(logn)
    def findPeakElement(self, num):
        size = len(num)
        if size == 1: return 0
        return self.search(num, 0, size-1)
    def search(self, num, start, end):
        if start == end:
            return start
        if end == start + 1:
            if num[start] < num[end]:
                return end
            else:
                return start
        mid = (start + end)/2
        if num[mid] < num[mid-1]:
            return self.search(num, start, mid-1)
        if num[mid] < num[mid+1]:
            return self.search(num, mid, end)
        return mid

    # o(n)
    def findPeakElementOn(self, num):
        size = len(num)
        for x in range(1, size-1):
            if num[x] > num[x-1] and num[x] > num[x+1]:
                return x

        return [0, size-1][num[0] < num[size-1]]

class Solution2(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return -1

        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start ) / 2
            if nums[mid] > nums[mid+1]:
                end = mid
            else:
                start = mid

        if nums[start] > nums[end]:
            return start
        else:
            return end

##### Same expression#############
#  return [false_val, true_val][true or false]
#  return [start, end][num[start] < num[end]]
#
# if num[start] < num[end]:
#                return end
#            else:
#                return start

# test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        # print Solution().findPeakElement([1,2,1])
        print Solution().findPeakElement([1,2,3, 1])
        test = SolutionOther()
        arr = [1, 2, 3, 1]
        print test.findPeakElement(arr)
        print test.findPeakElementOn(arr)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/find-peak-element/solution/

#33.97%  0ms
1. O(n) linear scan:
public class Solution {
    public int findPeakElement(int[] nums) {
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] > nums[i + 1])
                return i;
        }
        return nums.length - 1;
    }
}

Thought: https://leetcode.com/problems/find-peak-element/solution/
This problem is similar to Local Minimum. And according to the given condition,
num[i] != num[i+1], there must exist a O(logN) solution. So we use binary search for this problem.

If num[i-1] < num[i] > num[i+1], then num[i] is peak
If num[i-1] < num[i] < num[i+1], then num[i+1...n-1] must contains a peak
If num[i-1] > num[i] > num[i+1], then num[0...i-1] must contains a peak
If num[i-1] > num[i] < num[i+1], then both sides have peak
(n is num.length)

public class Solution {
    public int findPeakElement(int[] nums) {
        int start = 0;
        int end = nums.length - 1;
        while (start < end) {
            int mid = start + (end - start) / 2;
            if (nums[mid] > nums[mid + 1]) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }
        return start;
    }
}

#33.97%  0ms
public class Solution {
    public int findPeakElement(int[] nums) {
        if(nums == null || nums.length == 0) return 0;

        int start = 0;
        int end = nums.length - 1;
        while(start + 1 < end){
            int mid = start + (end - start ) / 2;
            if(nums[mid] > nums[mid+1]){
                end = mid;
            }else{
                start = mid;
            }
        }

        return nums[start] > nums[end] ? start: end;
    }
}
'''