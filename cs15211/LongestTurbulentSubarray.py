__source__ = 'https://leetcode.com/problems/longest-turbulent-subarray/'
# Time:  O(N)
# Space: O(1)
#
# Description: Leetcode # 978. Longest Turbulent Subarray
#
# A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:
#
# For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
# OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.
# That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.
#
# Return the length of a maximum size turbulent subarray of A.
#
# Example 1:
#
# Input: [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])
# Example 2:
#
# Input: [4,8,12,16]
# Output: 2
# Example 3:
#
# Input: [100]
# Output: 1
#
# Note:
#
# 1 <= A.length <= 40000
# 0 <= A[i] <= 10^9
import unittest
# 128ms 100%
class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        ans = 1
        anchor = 0

        for i in xrange(1, N):
            c = cmp(A[i-1], A[i])
            if c == 0:
                anchor = i
            elif i == N-1 or c * cmp(A[i], A[i+1]) != -1:
                ans = max(ans, i - anchor + 1)
                anchor = i
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/longest-turbulent-subarray/solution/
# Approach 1: Sliding Window
# Complexity Analysis
# Time Complexity: O(N), where N is the length of A.
# Space Complexity: O(1). 
#
# 11ms 100%
class Solution {
    public int maxTurbulenceSize(int[] A) {
        int N = A.length;
        int ans = 1;
        int anchor = 0;

        for (int i = 1; i < N; ++i) {
            int c = Integer.compare(A[i-1], A[i]);
            if (c == 0) anchor = i;
            else if (i == N - 1 || c * Integer.compare(A[i], A[i + 1]) != -1) {
                ans = Math.max(ans, i - anchor + 1);
                anchor = i;
            }
        }
        return ans;
    }
}

# https://leetcode.com/problems/longest-turbulent-subarray/discuss/221935/Java-O(N)-time-O(1)-space
For each A[i]
inc: The length of current valid sequence which ends with two increasing numbers
dec: The length of current valid sequence which ends with two decreasing numbers
# 12ms 100%
class Solution {
    public int maxTurbulenceSize(int[] A) {
        int inc = 1, dec = 1, res = 1;
        for (int i = 1; i < A.length; i++) {
            if (A[i] < A[i - 1]) {
                dec = inc + 1;
                inc = 1;
            } else if (A[i] > A[i - 1]) {
                inc = dec + 1;
                dec = 1;
            } else {
                inc = 1;
                dec = 1;
            }
            res = Math.max(res, Math.max(inc, dec));
        }
        return res;
    }
}
'''
