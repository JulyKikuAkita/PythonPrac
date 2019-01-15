__source__ = 'https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/find-all-numbers-disappeared-in-an-array.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 448. Find All Numbers Disappeared in an Array
#
# Given an array of integers where 1 <= a[i] <= n (n = size of array),
# some elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime?
# You may assume the returned list does not count as extra space.
#
# Example:
#
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [5,6]
#  Google
# Hide Tags Array
# Hide Similar Problems (H) First Missing Positive (M) Find All Duplicates in an Array
#

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in xrange(len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] *= -1

        result = []
        for i in xrange(len(nums)):
            if nums[i] > 0:
                result.append(i+1)
            else:
                nums[i] *= -1
        return result

    # 164ms 74.04%
    def findDisappearedNumbers2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return list(set(range(1, len(nums) + 1)) - set(nums))

    # 168ms 68.55%
    def findDisappearedNumbers3(self, nums):
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]


if __name__ == '__main__':
    s = Solution()
    r = s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
    print r

Java = '''
Thought:

The basic idea is that we iterate through the input array and mark elements as negative
using nums[nums[i] -1] = -nums[nums[i]-1].
In this way all the numbers that we have seen will be marked as negative.
In the second iteration, if a value is not marked as negative,
it implies we have never seen that index before, so just add it to the return list.

# 12ms 49.47%
class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> res = new ArrayList<>();

        for (int i = 0; i < nums.length; i++) {
            int val = Math.abs(nums[i]) - 1;
            if (nums[val] > 0) {
                nums[val] = -nums[val];
            }
        }

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0) {
                res.add(i + 1);
            }
        }
        return res;
    }
}
'''