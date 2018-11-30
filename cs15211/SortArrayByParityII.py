__source__ = ''
# Time:  O(N)
# Space: O(1)
#
# Description: Leetcode #
#
# Given an array A of non-negative integers, half of the integers in A are odd,
# and half of the integers are even.
#
# Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
#
# You may return any answer array that satisfies this condition.
#
# Example 1:
#
# Input: [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
#
#
# Note:
#
# 2 <= A.length <= 20000
# A.length % 2 == 0
# 0 <= A[i] <= 1000
#
import unittest

#140ms 96.71%
class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        j = 1
        for i in xrange(0, len(A), 2):
            if A[i] % 2:
                while A[j] % 2:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/sort-array-by-parity-ii/solution/
# 100% 5ms
class Solution {
    public int[] sortArrayByParityII(int[] A) {
        int j = 1;
        for (int i = 0; i < A.length; i += 2)
            if (A[i] % 2 == 1) {
                while (A[j] % 2 == 1)
                    j += 2;

                // Swap A[i] and A[j]
                int tmp = A[i];
                A[i] = A[j];
                A[j] = tmp;
            }

        return A;
    }
}

class Solution {
    public int[] sortArrayByParityII(int[] A) {
        int N = A.length; //always even
        int odd = 1, even = 0;
        while (even < N && odd < N) {
            while (even < N && A[even] % 2 == 0) even += 2;
            while (odd < N && A[odd] % 2 == 1) odd += 2;
            if (even < N && odd < N && even != odd) {
                int tmp = A[even];
                A[even] = A[odd];
                A[odd] = tmp;
            }
            even += 2;
            odd += 2;
        }
        return A;
    }
}

'''