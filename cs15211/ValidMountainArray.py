__source__ = 'https://leetcode.com/problems/valid-mountain-array/'
# Time:  O(N)
# Space: O(1)
#
# Description: Leetcode # 941. Valid Mountain Array
#
# Given an array A of integers, return true if and only if it is a valid mountain array.
#
# Recall that A is a mountain array if and only if:
#
# A.length >= 3
# There exists some i with 0 < i < A.length - 1 such that:
# A[0] < A[1] < ... A[i-1] < A[i]
# A[i] > A[i+1] > ... > A[B.length - 1]
#
#
# Example 1:
#
# Input: [2,1]
# Output: false
# Example 2:
#
# Input: [3,5,5]
# Output: false
# Example 3:
#
# Input: [0,3,2,1]
# Output: true
#
#
# Note:
#
# 0 <= A.length <= 10000
# 0 <= A[i] <= 10000
#
import unittest

# 36ms 99.14%
class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        N = len(A)
        i = 0

        # walk up
        while i+1 < N and A[i] < A[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N-1:
            return False

        # walk down
        while i+1 < N and A[i] > A[i+1]:
            i += 1

        return i == N-1

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/valid-mountain-array/solution/
Approach 1: One Pass
Complexity Analysis
Time Complexity: O(N), where N is the length of A.
Space Complexity: O(1)

# 3ms 100%
class Solution {
    public boolean validMountainArray(int[] A) {
        int N = A.length;
        int i = 0;

        // walk up
        while (i+1 < N && A[i] < A[i+1])
            i++;

        // peak can't be first or last
        if (i == 0 || i == N-1)
            return false;

        // walk down
        while (i+1 < N && A[i] > A[i+1])
            i++;

        return i == N-1;
    }
}

# 5ms 64.16%
class Solution {
    public boolean validMountainArray(int[] A) {
        int i = 1, N = A.length;
        while (i < N && A[i - 1] < A[i]) i++;
        if (i == 1 || i == N) return false;
        while (i < N && A[i - 1] > A[i]) i++;
        return i == N;
    }
}

# 4ms 89.31%
class Solution {
    public boolean validMountainArray(int[] A) {
        int i = 0, N = A.length;
        while (i < N - 1 && A[i + 1] > A[i]) i++;
        if (i == 0 || i == N - 1) return false;
        while (i < N - 1 && A[i] > A[i + 1]) i++;
        return i == N - 1;
    }
}

'''