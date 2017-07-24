__source__ = 'https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/search-in-rotated-sorted-array-ii.py
# Time:  O(logn) When there are duplicates, the worst case is O(n).
# Space: O(1)
# Binary Search
#
# Follow up for "Search in Rotated Sorted Array":
# What if duplicates are allowed?
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# Write a function to determine if a given target is in the array.
#
# The array may contain duplicates.
#
# Related Topics
# Array Binary Search
# Similar Questions
# Search in Rotated Sorted Array
#
import unittest
class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        low, high = 0, len(A)
        while low < high:
            mid = low + (high - low) / 2

            if A[mid] == target:
                return mid

            if A[low] < A[mid]:
                if A[low] <= target and target < A[mid]:
                    high = mid
                else:
                    low = mid + 1
            elif A[low] > A[mid]:
                if A[mid] < target and target <= A[high - 1]:
                    low = mid + 1
                else:
                    high = mid
            else:
                low += 1
        return False

# below Fail
class SolutionCC150: # fail at [1,3,1,1,1], 3

    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        low, high = 0, len(A) - 1

        while low <= high:
            mid = (low + high) / 2
            if A[mid] == target:
                return True
            if A[low] <= A[mid]:
                if target > A[mid]:
                    low = mid + 1
                elif target >= A[low]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif A[low] > A[mid]:
                if target < A[mid]:
                    high = mid - 1
                elif target <= A[high]:
                    low = mid + 1
                else:
                    high = mid -1
            else:
                low += 1
        return False

class SolutionOther:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        begin, end = 0, len(A) - 1
        while (begin <= end):
            mid = begin + ((end - begin) >> 1)
            if A[mid] == target:
                return True
            if A[mid] == A[begin] and A[mid] == A[end]:
                begin, end = begin + 1, end - 1
            elif (A[mid] > A[begin] and target < A[mid] and target >= A[begin] ) or \
                 (A[mid] < A[begin] and not (target <= A[end] and target > A[mid])):
                end = mid - 1
            else:
                begin = mid + 1
        return False

class SolutionBM(unittest.TestCase):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums or len(nums) < 1 :
            return False

        for i in xrange(len(nums)):
            if nums[i] == target:
                return True

        return False

    def test(self):
        self.assertEqual(1, self.search([1,3,1,1,1], 3))


class TestMethods(unittest.TestCase):
    def test_Local(self):
        print Solution().search([3, 5, 1], 3)
        print Solution().search([2, 2, 3, 3, 4, 1], 1)
        print Solution().search([4, 4, 5, 6, 7, 0, 1, 2], 5)
        print Solution().search([1,3,1,1,1], 3)

        print SolutionCC150().search([3, 5, 1], 3)
        print SolutionCC150().search([2, 2, 3, 3, 4, 1], 1)
        print SolutionCC150().search([4, 4, 5, 6, 7, 0, 1, 2], 5)
        print SolutionCC150().search([1,3,1,1,1], 3)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:

# 12.82% 1ms
public class Solution {
    public boolean search(int[] nums, int target) {
        int start = 0;
        int end = nums.length;

        while(start < end){
            int mid = start + (end - start) / 2;
            if(nums[mid] == target) return true;
            if(nums[start] < nums[mid]){
                if(target >= nums[start] && target < nums[mid]){
                    end = mid;
                }else{
                    start = mid + 1;
                }
            }else if(nums[start] > nums[mid]){
                if(target > nums[mid] && target <= nums[end - 1]){
                    start += 1;
                }
                else{
                    end = mid;
                }
            }else{
                start++;
            }
        }

        return false;
    }
}

# DFS:
# 12.82% 1ms
public class Solution {
    public boolean search(int[] nums, int target) {
        return search(nums, target, 0, nums.length - 1);
    }

    private boolean search(int[] nums, int target, int start, int end) {
        if (start > end) {
            return false;
        }
        int mid = start + (end - start) / 2;
        if (nums[mid] == target) {
            return true;
        }
        if (nums[start] == nums[mid] || nums[mid] == nums[end]) {
            return search(nums, target, start, mid - 1) || search(nums, target, mid + 1, end);
        } else if (nums[start] < nums[mid]) {
            if (nums[start] <= target && target < nums[mid]) {
                return search(nums, target, start, mid - 1);
            } else {
                return search(nums, target, mid + 1, end);
            }
        } else {
            if (nums[mid] < target && target <= nums[end]) {
                return search(nums, target, mid + 1, end);
            } else {
                return search(nums, target, start, mid - 1);
            }
        }
    }
}

# 12.82% 1ms
public class Solution {
    public boolean search(int[] nums, int target) {
        if(nums == null || nums.length < 1) return false;
        int start = 0;
        int end  = nums.length - 1;
        while(start + 1 < end){
            int mid = start + ( end - start )  / 2;
            if( nums[mid] == target) return true;

            while( start < mid && end > mid && nums[start] == nums[mid] && nums[end] == nums[mid]){ //with dup
                start ++;
                end --;
            }

            //System.out.printf("start: %d, end: %d \n", start, end);

            if(nums[mid] >= nums[start]){
                if(target >= nums[start] && target <= nums[mid]){
                    end = mid;
                }else{
                    start = mid;
                }
            }else{
                if(target >= nums[mid] && target <= nums[end]){
                    start = mid;
                }else{
                    end = mid;
                }
            }
        }
        if(nums[start] == target || nums[end] == target) return true;

        return false;
    }
}
'''
