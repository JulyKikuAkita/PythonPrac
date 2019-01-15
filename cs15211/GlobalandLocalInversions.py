__source__ = 'https://leetcode.com/problems/global-and-local-inversions/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 775. Global and Local Inversions
#
# We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.
#
# The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].
#
# The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].
#
# Return true if and only if the number of global inversions is equal to the number of local inversions.
#
# Example 1:
#
# Input: A = [1,0,2]
# Output: true
# Explanation: There is 1 global inversion, and 1 local inversion.
#
# Example 2:
#
# Input: A = [1,2,0]
# Output: false
# Explanation: There are 2 global inversions, and 1 local inversion.
#
# Note:
#
#     A will be a permutation of [0, 1, ..., A.length - 1].
#     A will have length in range [1, 5000].
#     The time limit for this problem has been reduced.
#

import unittest

# 56ms 78%
class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        return all(abs(i-x) <= 1 for i,x in enumerate(A))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/global-and-local-inversions/solution/
A local inversion is also a global inversion.
Thus, we only need to check if our permutation has any non-local inversion
(A[i] > A[j], i < j) with j - i > 1.

Approach #1: Brute Force [Time Limit Exceeded]
Complexity Analysis
Time Complexity: O(N^2), where N is the length of A.
Space Complexity: O(1)

# TLE
class Solution {
    public boolean isIdealPermutation(int[] A) {
        int N = A.length;
        for (int i = 0; i < N; ++i)
            for (int j = i+2; j < N; ++j)
                if (A[i] > A[j]) return false;
        return true;
    }
}

Approach #2: Remember Minimum [Accepted]
Complexity Analysis
Time Complexity: O(N), where N is the length of A.
Space Complexity: O(1)

# 8ms 100%
class Solution {
    public boolean isIdealPermutation(int[] A) {
        int N = A.length;
        int floor = N;
        for (int i = N - 1; i >= 2; --i) {
            floor = Math.min(floor, A[i]);
            if (A[i - 2] > floor) return false;
        }
        return true;
    }
}


Approach #3: Linear Scan [Accepted]
If the 0 occurs at index 2 or greater,
then A[0] > A[2] = 0 is a non-local inversion.
So 0 can only occur at index 0 or 1.
If A[1] = 0, then we must have A[0] = 1
otherwise A[0] > A[j] = 1 is a non-local inversion.
Otherwise, A[0] = 0.
To recap, the possibilities are either
A = [0] + (ideal permutation of 1...N-1) or
A = [1, 0] + (ideal permutation of 2...N-1).

A necessary and sufficient condition for these possibilities is that
Math.abs(A[i] - i) <= 1. So we check this for every i.

# 9ms 99.69%
class Solution {
    public boolean isIdealPermutation(int[] A) {
        for (int i = 0; i < A.length; ++i)
            if (Math.abs(A[i] - i) > 1) return false;
        return true;
    }
}
'''