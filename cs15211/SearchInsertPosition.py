__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/search-insert-position.py
# Time:  O(logn)
# Space: O(1)
# Binary Search
#
# Given a sorted array and a target value, return the index if the target is found.
#
# If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.
#
# Here are few examples.
# [1,3,5,6], 5 -> 2
# [1,3,5,6], 2 -> 1
# [1,3,5,6], 7 -> 4
# [1,3,5,6], 0 -> 0
#

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        low, high = 0, len(A) - 1

        while low <= high:
            mid = (low + high) / 2
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low


# Java solution
# http://www.programcreek.com/2013/01/leetcode-search-insert-position/
# Time: O(n)
class Naive:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        if not A:
            return 0
        if target <= A[0]: return 0

        for i in xrange(len(A) - 1):
            if target > A[i] and target <= A[i+1]:
                return i+1
        return len(A)

if __name__ == "__main__":
    print Solution().searchInsert([1, 3, 5, 6], 5)
    print Solution().searchInsert([1, 3, 5, 6], 2)
    print Solution().searchInsert([1, 3, 5, 6], 7)
    print Solution().searchInsert([1, 3, 5, 6], 0)

class SolutionOther:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        l, r = 0, len(A)
        while l < r:
            m = (l+r)/2
            if A[m] < target:
                l = m+1
            else:
                r = m
        return l


 #test
test = SolutionOther()
print test.searchInsert([], 8 )
print test.searchInsert([-100, -1], 8 )
print test.searchInsert([1,3,5,7,9], 8 )
print test.searchInsert([1,3,5,7,9], 7 )