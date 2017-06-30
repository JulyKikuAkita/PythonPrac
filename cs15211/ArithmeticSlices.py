__source__ = 'https://leetcode.com/problems/arithmetic-slices/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/arithmetic-slices.py
# Time:  O(n)
# Space: O(1)
#
# Description:
# A sequence of number is called arithmetic if it consists of at least three elements
# and if the difference between any two consecutive elements is the same.
#
# For example, these are arithmetic sequence:
#
# 1, 3, 5, 7, 9
# 7, 7, 7, 7
# 3, -1, -5, -9
# The following sequence is not arithmetic.
#
# 1, 1, 2, 5, 7
#
# A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair
# of integers (P, Q) such that 0 <= P < Q < N.
#
# A slice (P, Q) of array A is called arithmetic if the sequence:
# A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.
#
# The function should return the number of arithmetic slices in the array A.
#
# Example:
#
# A = [1, 2, 3, 4]
#
# return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
#
#  Aetion Baidu
# Hide Tags Dynamic Programming Math
# Hide Similar Problems (H) Arithmetic Slices II - Subsequence
#

import unittest

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res, i = 0, 0
        while i+2 < len(A):
            start = i
            while i+2 < len(A) and A[i+2] + A[i] == 2*A[i+1]:
                res += i - start + 1
                i += 1
            i += 1
        return res

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
public class Solution {
    public int numberOfArithmeticSlices(int[] A) {
        int curr = 0, sum = 0;
        for (int i = 2; i < A.length; i++){
             if (A[i] - A[i-1] == A[i-1] - A[i-2]) {
                 curr += 1;
                 sum += curr;
             } else {
                 curr = 0;
             }
        }
        return sum;
    }
}
'''