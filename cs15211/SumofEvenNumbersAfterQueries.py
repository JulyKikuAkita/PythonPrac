__source__ = 'https://leetcode.com/problems/sum-of-even-numbers-after-queries/'
# Time:  O(N+Q), where N is the length of A and Q is the number of queries.
# Space: O(Q), though we only allocate O(1) additional space.
#
# Description: Leetcode # 985. Sum of Even Numbers After Queries
#
# We have an array A of integers, and an array queries of queries.
#
# For the i-th query val = queries[i][0], index = queries[i][1], we add val to A[index].
# Then, the answer to the i-th query is the sum of the even values of A.
#
# (Here, the given index = queries[i][1] is a 0-based index, and each query permanently modifies the array A.)
#
# Return the answer to all queries.  Your answer array should have answer[i] as the answer to the i-th query.
#
# Example 1:
#
# Input: A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
# Output: [8,6,2,4]
# Explanation:
# At the beginning, the array is [1,2,3,4].
# After adding 1 to A[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
# After adding -3 to A[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
# After adding -4 to A[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
# After adding 2 to A[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.
#
# Note:
#
# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# 1 <= queries.length <= 10000
# -10000 <= queries[i][0] <= 10000
# 0 <= queries[i][1] < A.length
#
import unittest

class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        S = sum(x for x in A if x % 2 == 0)
        ans = []

        for x, k in queries:
            if A[k] % 2 == 0: S -= A[k]
            A[k] += x
            if A[k] % 2 == 0: S += A[k]
            ans.append(S)

        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/sum-of-even-numbers-after-queries/solution/
# Approach 1: Maintain Array Sum
Complexity Analysis
Time Complexity: O(N+Q), where N is the length of A and Q is the number of queries.
Space Complexity: O(Q), though we only allocate O(1) additional space. 
# 8ms 53.42%
class Solution {
    public int[] sumEvenAfterQueries(int[] A, int[][] queries) {
        if (A.length != queries.length) return A;
        int sum = 0;
        for (int i = 0; i < A.length; i++) {
            if (A[i] % 2 == 0) {
                sum += A[i];
            }
        }
        
        int[] res = new int[A.length];
        for (int i = 0; i < queries.length; i++) {
            int idx = queries[i][1];
            int val = queries[i][0];
            if (A[idx] % 2 == 0) {
                sum -= A[idx];
            } 
            A[idx] += val;
            if (A[idx] % 2 == 0) {
                sum += A[idx];
            }
            res[i] = sum;
        }
        return res;
    }
}
'''
