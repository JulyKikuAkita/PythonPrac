__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/valid-perfect-square.py

# Time:  O(logn)
# Space: O(1)

# Given a positive integer num, write a function
# which returns True if num is a perfect square else False.
#
# Note: Do not use any built-in library function such as sqrt.
#
# Example 1:
#
# Input: 16
# Returns: True
# Example 2:
#
# Input: 14
# Returns: False
#  LinkedIn
# Hide Tags Binary Search Math
# Hide Similar Problems (M) Sqrt(x)



class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left, right = 1, num
        while left <= right:
            mid = left + (right - left) / 2
            if mid >= num / mid:
                right = mid - 1
            else:
                left = mid + 1
        return left == num / left and num % left == 0

#java
js = '''
public class Solution {
    public boolean isPerfectSquare(int num) {
        if (num < 0) {
            return false;
        } else if (num == 0) {
            return true;
        }
        long left = 1;
        long right = num;
        while (left <= right) {
            long mid = left + ((right - left) >> 1);
            long sq = mid * mid;
            if (sq < num) {
                left = mid + 1;
            } else if (sq > num) {
                right = mid - 1;
            } else {
                return true;
            }
        }
        return false;
    }
}
'''