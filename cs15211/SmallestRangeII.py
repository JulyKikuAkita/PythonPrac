__source__ = 'https://leetcode.com/problems/smallest-range-ii/'
# Time:  O(NlogN)
# Space: O(1)
#
# Description: Leetcode # 910. Smallest Range II
#
# Given an array A of integers,
# for each integer A[i] we need to choose either x = -K or x = K,
# and add x to A[i] (only once).
#
# After this process, we have some array B.
#
# Return the smallest possible difference between the maximum value of B and the minimum value of B.
#
# Example 1:
#
# Input: A = [1], K = 0
# Output: 0
# Explanation: B = [1]
# Example 2:
#
# Input: A = [0,10], K = 2
# Output: 6
# Explanation: B = [2,8]
# Example 3:
#
# Input: A = [1,3,6], K = 3
# Output: 3
# Explanation: B = [4,6,3]
#
# Note:
#
# 1 <= A.length <= 10000
# 0 <= A[i] <= 10000
# 0 <= K <= 10000
#
import unittest

# 64ms 90.99%
class Solution(object):
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        mi, ma = A[0], A[-1]
        ans = ma - mi
        for i in xrange(len(A) - 1):
            a, b = A[i], A[i+1]
            ans = min(ans, max(ma-K, a+K) - min(mi+K, b-K))
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/smallest-range-ii/solution/
#
Approach 1: Linear Scan
Complexity Analysis
Time Complexity: O(NlogN), where NN is the length of the A.
Space Complexity: O(1), plus the space used by the builtin sorting algorithm. 

# 13ms 91.37%
class Solution {
    public int smallestRangeII(int[] A, int K) {
        int N = A.length;
        Arrays.sort(A);
        int ans = A[N-1] - A[0];
        
        for (int i = 0; i < A.length - 1; i++) {
            int a = A[i], b = A[i + 1];
            int high = Math.max(A[N - 1] - K, a + K);
            int low = Math.min(A[0] + K, b - K);
            ans = Math.min(ans, high - low);
        }
        return ans;
    }
}

# 12ms 99.36%
class Solution {
    public int smallestRangeII(int[] A, int K) {
        Arrays.sort(A);
        int res = A[A.length - 1] - A[0];
        int left = A[0] + K, right = A[A.length -1] - K;
        for (int i = 0; i < A.length - 1; i++) {
            int maxI = Math.max(A[i] + K, right);
            int minI = Math.min(A[i + 1] - K, left);
            res = Math.min(res, maxI - minI);
        }
        return res;
    }
}
'''
