__source__ = 'https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/find-minimum-in-rotated-sorted-array-ii.py
# Time:  O(logn) ~ O(n)
# Space: O(1)
# Binary Search
#
# Description: Leetcode # 154. Find Minimum in Rotated Sorted Array II
#
# Follow up for "Find Minimum in Rotated Sorted Array":
# What if duplicates are allowed?
#
# Would this affect the run-time complexity? How and why?
# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# Find the minimum element.
#
# The array may contain duplicates.
#
# Related Topics
# Array Binary Search
# Similar Questions
# Find Minimum in Rotated Sorted Array
#
import unittest
class Solution(object):
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

class Solution2(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0

        start = 0
        end = len(nums) - 1

        # not work with increaing arr if only start +1 < end
        while start + 1 < end and nums[start] >= nums[end]: # if not >=, [3, 1, 3] fails
            mid = start + (end - start) / 2
            if nums[mid] > nums[start]:
                start = mid
            elif nums[mid] < nums[start]:
                end = mid
            else:
                start += 1

        return min(nums[start], nums[end])

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        #print Solution().findMin([3, 1, 1, 2, 2, 3])
        #print Solution2().findMin([2, 2, 2, 3, 3, 1])
        #print Solution2().findMin([3, 1, 1])
        print Solution2().findMin([3, 1, 3])

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# 0ms 100%
class Solution {
    public int findMin(int[] nums) {
        int min = Integer.MAX_VALUE;
        int start = 0;
        int end = nums.length - 1;
        while (start <= end) {
            int mid = start + (end - start) / 2;
            if (nums[start] < nums[mid]) {
                if (nums[mid] <= nums[end]) {
                    min = Math.min(min, nums[start]);
                    end = mid - 1;
                } else {
                    min = Math.min(min, nums[end]);
                    start = mid + 1;
                }
            } else if (nums[start] > nums[mid]) {
                min = Math.min(min, nums[mid]);
                end = mid - 1;
            } else {
                min = Math.min(min, nums[start]);
                start++;
            }
        }
        return min;
    }
}

# DFS
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

# 0ms 100%
class Solution {
    public int findMin(int[] nums) {
        if( nums == null || nums.length == 0) return -1;
        int start = 0;
        int end = nums.length - 1;

        while(start + 1 < end && nums[start] >= nums[end]){
            int mid = start + (end - start) /2 ;
            if(nums[mid] > nums[start]){
                start = mid;
            }else if(nums[mid] < nums[start]){
                end = mid;
            }else{
                start += 1;
            }
        }
        return Math.min(nums[start], nums[end]);
    }
}
'''