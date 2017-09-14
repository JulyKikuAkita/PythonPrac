__source__ = 'https://leetcode.com/problems/rotate-function/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/rotate-function.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 396. Rotate Function
#
# Given an array of integers A and let n to be its length.
#
# Assume Bk to be an array obtained by rotating the array A
# k positions clock-wise, we define a "rotation function" F on A as follow:
#
# F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].
#
# Calculate the maximum value of F(0), F(1), ..., F(n-1).
#
# Note:
# n is guaranteed to be less than 105.
#
# Example:
#
# A = [4, 3, 2, 6]
#
# F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
# F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
# F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
# F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
#
# So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.
#
# Companies
# Amazon
# Related Topics
# Math
#
import unittest
#62ms
class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        s = sum(A)
        fi = 0
        for i in xrange(len(A)):
            fi += i * A[i]

        result = fi
        for i in xrange(1, len(A)+1):
            fi += s - len(A) * A[-i]
            result = max(result, fi)
        return result

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:

Java O(n) solution with explanation
F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1]
F(k-1) = 0 * Bk-1[0] + 1 * Bk-1[1] + ... + (n-1) * Bk-1[n-1]
       = 0 * Bk[1] + 1 * Bk[2] + ... + (n-2) * Bk[n-1] + (n-1) * Bk[0]
Then,

F(k) - F(k-1) = Bk[1] + Bk[2] + ... + Bk[n-1] + (1-n)Bk[0]
              = (Bk[0] + ... + Bk[n-1]) - nBk[0]
              = sum - nBk[0]
Thus,

F(k) = F(k-1) + sum - nBk[0]
What is Bk[0]?

k = 0; B[0] = A[0];
k = 1; B[0] = A[len-1];
k = 2; B[0] = A[len-2];
...
int allSum = 0;
int len = A.length;
int F = 0;
for (int i = 0; i < len; i++) {
    F += i * A[i];
    allSum += A[i];
}
int max = F;
for (int i = len - 1; i >= 1; i--) {
    F = F + allSum - len * A[i];
    max = Math.max(F, max);
}
return max;

#22.44% 5ms
public class Solution {
    public int maxRotateFunction(int[] A) {
        int allSum = 0;
        int len = A.length;
        int F = 0;
        for (int i = 0; i < len; i++) {
            F += i * A[i];
            allSum += A[i];
        }
        int max = F;
        for (int i = len - 1; i>= 1; i--) {
            F = F + allSum - len * A[i];
            max =Math.max(F, max);
        }
        return max;
    }
}

#66.51% 4ms
class Solution {
    public int maxRotateFunction(int[] A) {
    int sum = 0;
    for (int i = 0; i < A.length; i++) {
        sum += A[i];
    }

    int base = 0;
    for (int i = 0; i < A.length; i++) {
        base += i * A[i];
    }

    int max = base;
    for (int i = 1; i < A.length; i++) {
        int sumIndex = -i + A.length;
        base += sum - A.length * A[sumIndex];   // base += (sum - A[sumIndex]) - (A.length - 1) * A[sumIndex];
        max = (max < base) ? base : max;
    }
    return max;
 }
}
'''