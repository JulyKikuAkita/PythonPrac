__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/first-bad-version.py
# Time:  O(logn)
# Space: O(1)
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

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
# Facebook
# Binary Search

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = (left + right ) / 2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

#java
js = '''
/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

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