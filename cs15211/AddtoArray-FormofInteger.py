__source__ = 'https://leetcode.com/problems/add-to-array-form-of-integer/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 989. Add to Array-Form of Integer
#
# For a non-negative integer X, the array-form of X is an array of its digits in left to right order.
# For example, if X = 1231, then the array form is [1,2,3,1].
#
# Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.
#
# Example 1:
#
# Input: A = [1,2,0,0], K = 34
# Output: [1,2,3,4]
# Explanation: 1200 + 34 = 1234
# Example 2:
#
# Input: A = [2,7,4], K = 181
# Output: [4,5,5]
# Explanation: 274 + 181 = 455
# Example 3:
#
# Input: A = [2,1,5], K = 806
# Output: [1,0,2,1]
# Explanation: 215 + 806 = 1021
# Example 4:
#
# Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
# Output: [1,0,0,0,0,0,0,0,0,0,0]
# Explanation: 9999999999 + 1 = 10000000000
#
#
# Note：
#
# 1 <= A.length <= 10000
# 0 <= A[i] <= 9
# 0 <= K <= 10000
# If A.length > 1, then A[0] != 0
#
import unittest

# 200ms 85.60%
class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        A[-1] += K
        for i in xrange(len(A) - 1, -1, -1):
            carry, A[i] = divmod(A[i], 10)
            if i: A[i-1] += carry
        if carry:
            A = map(int, str(carry)) + A
        return A

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/add-to-array-form-of-integer/solution/
# https://leetcode.com/problems/add-to-array-form-of-integer/discuss/234488/JavaC%2B%2BPython-Take-K-itself-as-a-Carry
# Approach 1: Schoolbook Addition
# Complexity Analysis
# Time Complexity: O(max(N,logK)) where N is the length of A.
# Space Complexity: O(max(N,logK)). 
# 63ms 35.04%
class Solution {
    public List<Integer> addToArrayForm(int[] A, int K) {
        int carry = 0;
        List<Integer> res = new ArrayList();
        for (int i = A.length - 1; i >= 0; i--) {
            res.add(0, (A[i] + K) % 10);
            K = (A[i] + K) / 10;
        }
        
        while (K > 0) {
            res.add(0, K % 10);
            K /= 10;
        }
        return res;
    }
}
'''
