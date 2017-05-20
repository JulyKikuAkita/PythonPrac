__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/contains-duplicate-ii.py
# Time:  O(n)
# Space: O(n)
#
# Given an array of integers and an integer k, return true if
# and only if there are two distinct indices i and j in the array
# such that nums[i] = nums[j] and the difference between i and j is at most k.
#

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        dict = {}
        for i, num in enumerate(nums):
            if num not in dict:
                dict[num] = i
            else:
                 # It the value occurs before, check the difference.
                if i - dict[num] <= k:
                    return True
                # Update the index of the value.
                dict[num] = i
        return False


#java solution:
# http://www.programcreek.com/2014/05/leetcode-contains-duplicate-ii-java/

if __name__ == "__main__":
    print Solution().containsNearbyDuplicate([1,5,3,4,5], 2)