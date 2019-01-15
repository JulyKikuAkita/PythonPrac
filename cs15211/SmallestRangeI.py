__source__ = 'https://leetcode.com/problems/smallest-range-i/'
# Time:  O(N)
# Space: O(1)
#
# Description: Leetcode # 908. Smallest Range I
#
# Given an array A of integers,
# for each integer A[i] we may choose any x with -K <= x <= K, and add x to A[i].
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
# Output: 0
# Explanation: B = [3,3,3] or B = [4,4,4]
#
#
# Note:
#
# 1 <= A.length <= 10000
# 0 <= A[i] <= 10000
# 0 <= K <= 10000
#
import unittest

# 28ms 80.40%
class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        return max(0, max(A) - min(A) - 2*K)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/smallest-range-i/solution/
#
Approach 1: Mathematical
Complexity Analysis
Time Complexity: O(N), where N is the length of A.
Space Complexity: O(1) 
max(B) - min(B) is at least ans = (max(A) - K) - (min(A) + K).

# 7ms 49.10%
class Solution {
    public int smallestRangeI(int[] A, int K) {
        int min = A[0], max = A[0];
        for (int x : A) {
            min = Math.min(min, x);
            max = Math.max(max, x);
        }
        return Math.max(0, max - min - 2 * K);
    }
}

'''
