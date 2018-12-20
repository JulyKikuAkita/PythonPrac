__source__ = 'https://leetcode.com/problems/search-for-a-range/description/'
# Time:  O(logn)
# Space: O(1)
#
# Description: Leetcode # 34. Search for a Range
#
# Given a sorted array of integers, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].
#
# Companies
# LinkedIn
# Related Topics
# Binary Search Array
# Similar Questions
# First Bad Version
#
import unittest
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        # Find the first index where target <= A[idx]
        left = self.binarySearch(lambda x, y: x <= y, A, target) #if == target, move to lower bound
        if left >= len(A) or A[left]!= target:
            return [-1, -1]
        # Find the first index where target < A[idx]
        right = self.binarySearch(lambda x, y: x < y, A, target)  # if == target, move to upper bound
        return [left, right - 1]

    def binarySearch(self, compare, A, target):
        start, end = 0, len(A)
        while start < end:
            mid = (start + end) / 2
            if compare(target, A[mid]):
                end = mid
            else:
                start = mid + 1
        return start

    def binarySearch2(self, compare, A, target):
        start, end = 0, len(A) - 1
        while start <= end:
            mid = (start + end) / 2
            if compare(target, A[mid]):
                end = mid - 1
            else:
                start = mid + 1
        return start

    def binarySearch3(self, compare, A, target):
        start, end = -1, len(A)
        while end - start > 1:
            mid = start + (end - start) / 2
            if compare(target, A[mid]):
                end = mid
            else:
                start = mid
        return end

class SolutionOther:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        return [self.lower_bound(A, target), self.upper_bound(A, target)]

    def lower_bound(self, A, target):
        l, h ,m = 0, len(A), 0
        while l < h:
            m = (l+h) >> 1
            if A[m] < target :
                l = m + 1
            else:  # if == target, move to lower bound
                h = m
            print "lower", l, A[l], h
        return l if l < len(A) and A[l] == target else -1

    def upper_bound(self, A, target):
        l, h, m = 0, len(A), 0
        while l < h :
            m = (l+h) >> 1
            if A[m] <= target: # if == target, move to upper bound
                l = m + 1
            else:
                h = m
            print "upper", l-1, A[l-1],  h
        return l-1 if l-1 < len(A) and A[l-1] == target else -1

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        #test
        test = SolutionOther()
        A = [5, 7, 7, 8, 8, 10]
        print test.searchRange(A, 8)

        print Solution().searchRange([2, 2], 3)
        print Solution().searchRange([5, 7, 7, 8, 8, 10], 8)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:

#69.80% 7ms
public class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] result = new int[] {Integer.MAX_VALUE, 0};
        searchRange(nums, target, 0, nums.length - 1, result);
        return result[0] > result[1] ? new int[] {-1, -1} : result;
    }

    private void searchRange(int[] nums, int target, int start, int end, int[] result) {
        if (start > end) {
            return;
        }
        int mid = start + (end - start) / 2;
        if (nums[mid] < target) {
            searchRange(nums, target, mid + 1, end, result);
        } else if (nums[mid] > target) {
            searchRange(nums, target, start, mid - 1, result);
        } else {
            result[0] = Math.min(result[0], mid);
            result[1] = Math.max(result[1], mid);
            searchRange(nums, target, start, mid - 1, result);
            searchRange(nums, target, mid + 1, end, result);
        }
    }
}


#31.62% 8ms
public class Solution {
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

#31.62% 8ms
public class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] result = new int[] {-1, -1};
        if (nums == null || nums.length == 0) return result;
        int start = 0;
        int end = nums.length - 1;
        while (start < end) {
            int mid = start + (end - start) / 2;
            if (nums[mid] < target) {
                start = mid + 1;
            } else {
                end = mid;
            }
        }
        if (nums[start] != target) {
            return result;
        }
        result[0] = start;
        end = nums.length - 1;
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (nums[mid] > target) {
                end = mid - 1;
            } else {
                start = mid;
            }
        }
        result[1] = nums[end] == target ? end : start;
        return result;
    }
}
'''
