__source__ = 'https://leetcode.com/problems/first-bad-version/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/first-bad-version.py
# Time:  O(logn)
# Space: O(1)
#
# Description: 278. First Bad Version
#
# You are a product manager and currently leading a team to
# develop a new product. Unfortunately, the latest version of
# your product fails the quality check. Since each version is
# developed based on the previous version, all the versions
# after a bad version are also bad.
#
# Suppose you have n versions [1, 2, ..., n] and you want to
# find out the first bad one, which causes all the following
# ones to be bad.
#
# You are given an API bool isBadVersion(version) which will
# return whether version is bad. Implement a function to find
# the first bad version. You should minimize the number of
# calls to the API.
#
# Companies
# Facebook
# Related Topics
# Binary Search
# Similar Questions
# Search for a Range Search Insert Position Guess Number Higher or Lower

import unittest
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = (left + right ) / 2
            if self.isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

    def isBadVersion(version):
        # provide by api
        pass

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/articles/first-bad-version/
/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

#57.29% 17ms
public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int start = 1;
        int end = n;
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (isBadVersion(mid)) {
                end = mid;
            } else {
                start = mid;
            }
        }
        return isBadVersion(start) ? start : end;
    }
}
'''