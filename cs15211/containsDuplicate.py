__author__ = 'July'

# Time:  O(n)
# Space: O(n)
#
# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array,
# and it should return false if every element is distinct.
#

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        return len(nums) > len(set(nums))

# java solution
# http://www.programcreek.com/2014/05/leetcode-contains-duplicate-java/

if __name__ == "__main__":
    print Solution().containsDuplicate([12344555,12344555])

