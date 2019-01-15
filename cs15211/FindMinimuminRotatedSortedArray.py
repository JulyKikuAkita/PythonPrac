__source__ = 'https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/find-minimum-in-rotated-sorted-array.py
# Time:  O(logn)
# Space: O(1)
# Binary Search
#
# Description: Leetcode # 153. Find Minimum in Rotated Sorted Array
#
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# Find the minimum element.
#
# You may assume no duplicate exists in the array.
#
# Companies
# Microsoft
# Related Topics
# Array Binary Search
# Similar Questions
# Search in Rotated Sorted Array Find Minimum in Rotated Sorted Array II
#
import unittest
class Solution2(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        res = 0x7FFFFFFF

        while start <= end:
            mid = start + (end - start ) / 2
            if nums[start] <= nums[mid]:
                res = min(res, nums[start])
                if nums[mid] < nums[end]:
                    end = mid - 1;
                else:
                    start = mid + 1;
            else:
                res = min(res, nums[mid])
                end = mid - 1;
        return res

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0

        start = 0
        end = len(nums) - 1

        # not work with increaing arr if only start + 1 < end
        while start + 1 < end and nums[start] > nums[end]:
            mid = start + (end - start) / 2
            if nums[mid] >= nums[start]:
                start = mid
            else:
                end = mid

        return min(nums[start], nums[end])

class SolutionOther(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.dfs(nums, 0, len(nums) - 1)

    def dfs(self, nums, start, end):
        if start == end:
            return nums[start]
        if nums[start] < nums[end]:
            return nums[start]

        mid = (start + end) / 2
        left = min(nums[start], nums[mid])
        right = min(nums[mid+1], nums[end])
        if left < right:
            return self.dfs(nums, start, mid)
        elif left > right:
            return self.dfs(nums, mid+1, end)
        else:
            return self.dfs(nums, start+1, end)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        self.assertEqual(1, Solution().findMin([3, 1, 2]))
        self.assertEqual(0, Solution2().findMin([4, 5 ,6, 7, 0 ,1 ,2]))

        arr = [4, 5, 6, 7, 0, 1, 2]
        #print Solution().findMin([1])
        #print Solution().findMin([1, 2])
        #print Solution().findMin([2, 1])
        print Solution().findMin([10,1,10,10,10])
        #print Solution().findMin([2, 3, 1])
        #print SolutionPrac().findMin(arr)
        #print Solution().findMin(arr)
        #print Solution2().findMin(arr)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/solution/

# 0ms 100%
class Solution {
    public int findMin(int[] nums) {
        int start = 0;
        int end = nums.length - 1;
        int min = Integer.MAX_VALUE;
        while (start <= end) {
            int mid = start + (end - start) / 2;
            if (nums[start] <= nums[mid]) {
                min = Math.min(min, nums[start]);
                if (nums[mid] < nums[end]) {
                    end = mid - 1;
                } else {
                    start = mid + 1;
                }
            } else {
                min = Math.min(min, nums[mid]);
                end = mid - 1;
            }
        }
        return min;
    }
}

# 0ms 100%
class Solution {
    public int findMin(int[] nums) {
        int start = 0;
        int end = nums.length - 1;

        while(start < end && nums[start] >= nums[end]){
            int mid = start + (end - start ) / 2;
            if(nums[mid] > nums[start]){
                start = mid + 1;
            }else if(nums[mid] < nums[start]){
                end = mid;
            }else{
                start++;
            }
        }
        return nums[start];
    }
}

# 0ms 100%
class Solution {
    public int findMin(int[] nums) {
        return dfs(nums, 0, nums.length - 1);
    }

    private int dfs(int[] nums, int start, int end ){
        if(start == end){
            return nums[start];
        }

        if(nums[start] < nums[end]){
            return nums[start];
        }

        int mid = start + (end - start) / 2;
        int left = Math.min(nums[start], nums[mid]);
        int right = Math.min(nums[mid+1], nums[end]);
        if(left < right){
            return dfs(nums, start, mid);
        }else if(left > right){
            return dfs(nums, mid+1, end);
        }else{
            return dfs(nums, start+1, end);
        }
    }
}
'''