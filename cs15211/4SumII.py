__source__ = 'https://leetcode.com/problems/4sum-ii/'
# Time:  O(n^2)
# Space: O(n^2)
#
# Description: Leetcode # 454. 4Sum II
#
# # Given four lists A, B, C, D of integer values,
# compute how many tuples (i, j, k, l) there are
# such that A[i] + B[j] + C[k] + D[l] is zero.
#
# To make problem a bit easier, all A, B, C, D have same length of N where 0 <= N <= 500.
# All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.
#
# Example:
#
# Input:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
#
# Output:
# 2
#
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
#
# Related Topics
# Binary Search Hash Table
# Similar Questions
# 4Sum
#
import unittest
import collections
#440ms 33.17%
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        A_B_sum = collections.Counter(a+b for a in A for b in B)
        return sum(A_B_sum[-c-d] for c in C for d in D)

#208ms 97.54%
class Solution2(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        AB_SUM = dict()
        for a in A:
            for b in B:
                sum = a + b
                if sum in AB_SUM:
                    AB_SUM[sum] += 1
                else:
                    AB_SUM[sum] = 1
        count = 0
        for c in C:
            for d in D:
                sum = c + d
                if -sum in AB_SUM:
                    count += AB_SUM[-sum]
        return count

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:

Take the arrays A and B, and compute all the possible sums of two elements.
Put the sum in the Hash map, and increase the hash map value if more than 1 pair sums to the same value.

Compute all the possible sums of the arrays C and D.
If the hash map contains the opposite value of the current sum,
increase the count of four elements sum to 0 by the counter in the map.

Time complexity:  O(n^2)
Space complexity: O(n^2)
#46.95% 195ms
class Solution {
    public int fourSumCount(int[] A, int[] B, int[] C, int[] D) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int i=0; i<C.length; i++) {
            for(int j=0; j<D.length; j++) {
                int sum = C[i] + D[j];
                map.put(sum, map.getOrDefault(sum, 0) + 1);
            }
        }

        int res=0;
        for(int i=0; i<A.length; i++) {
            for(int j=0; j<B.length; j++) {
                res += map.getOrDefault(-1 * (A[i]+B[j]), 0);
            }
        }
        return res;
    }
}

#88ms 90.82%
class Solution {
    public int fourSumCount(int[] A, int[] B, int[] C, int[] D) {
        Map<Integer, Integer> ab = new HashMap<>();
        for (int a : A) {
            for (int b : B) {
                ab.put(a+b, ab.getOrDefault(a+b, 0) + 1);
            }
        }

        int res = 0;
        for (int c : C) {
            for (int d : D) {
                res += ab.getOrDefault(-(c+d), 0);
            }
        }

        return res;
    }
}
'''