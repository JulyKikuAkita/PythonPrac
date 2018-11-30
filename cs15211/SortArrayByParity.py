__source__ = 'https://leetcode.com/problems/sort-array-by-parity/description/'
# Time:  O(N)
# Space: O(1) if in-place
#
# Description: Leetcode # 905. Sort Array By Parity
# Given an array A of non-negative integers, return an array consisting of all the even elements of A,
# followed by all the odd elements of A.
#
# You may return any answer array that satisfies this condition.
#
# Example 1:
#
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
#
#
import unittest

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 > A[j] % 2:
                A[i], A[j] = A[j], A[i]
            if A[i] % 2 == 0:
                i += 1
            if A[j] % 2 == 1:
                j -= 1
        return A

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/sort-array-by-parity/solution/
# 12ms 97.6%
class Solution {
    public int[] sortArrayByParity(int[] A) {
        int i = 0, j = A.length - 1;
        while (i < j) {
            if (A[i] % 2 > A[j] % 2) {
                int tmp = A[i];
                A[i] = A[j];
                A[j] = tmp;
            }

            if (A[i] % 2 == 0) i++;
            if (A[j] % 2 == 1) j--;
        }

        return A;
    }
}

#10ms, 100%
class Solution {
    public int[] sortArrayByParity(int[] A) {
        int N = A.length;
        int i = 0, j = N - 1;
        while (i < j) {
            while (i < j && A[i] % 2 == 0) i++;
            while (j > i && A[j] % 2 != 0) j--;
            if ( i >= j) break;
            swap(A, i, j);
            i++;
            j--;
        }
        return A;
    }

    public void swap(int[] A, int i, int j) {
        if (i < 0 || j < 0 || i >= A.length || j >= A.length || i >= j) return;
        int tmp = A[i];
        A[i] = A[j];
        A[j] = tmp;
    }
}

'''