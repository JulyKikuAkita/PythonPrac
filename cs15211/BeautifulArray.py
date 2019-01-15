__source__ = 'https://leetcode.com/problems/beautiful-array/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 932. Beautiful Array
#
# For some fixed N, an array A is beautiful if it is a permutation of the integers 1, 2, ..., N, such that:
#
# For every i < j, there is no k with i < k < j such that A[k] * 2 = A[i] + A[j].
#
# Given N, return any beautiful array A.  (It is guaranteed that one exists.)
#
# Example 1:
#
# Input: 4
# Output: [2,1,4,3]
# Example 2:
#
# Input: 5
# Output: [3,1,2,5,4]
#
# Note:
#
# 1 <= N <= 1000
#
import unittest

#32ms 83.28%
class Solution(object):
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        memo = {1: [1]}
        def f(N):
            if N not in memo:
                odds = f((N+1)/2)
                evens = f(N/2)
                memo[N] = [2*x-1 for x in odds] + [2*x for x in evens]
            return memo[N]
        return f(N)

#32ms 83.28%
class Solution2(object):
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        res = [1]
        while len(res) < N:
            res = [2 * i - 1 for i in res] + [2 * i  for i in res]
        return [i for i in res if i <= N]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/beautiful-array/solution/
because the left hand side 2*A[k] is even,
we can choose left to have all odd elements, and right to have all even elements.

Approach 1: Divide and Conquer
Complexity Analysis
Time Complexity: O(NlogN). The function f is called only O(logN) times, and each time does O(N) work.
Space Complexity: O(NlogN).

#2ms 100%
class Solution {
    Map<Integer, int[]> memo;
    public int[] beautifulArray(int N) {
        memo = new HashMap();
        return f(N);
    }

    private int[] f(int N) {
        if (memo.containsKey(N)) return memo.get(N);

        int[] ans = new int[N];
        if (N == 1) ans[0] = 1;
        else {
            int t = 0;
            for (int x : f((N + 1) / 2)) //odds
                ans[t++] = 2 * x - 1;
            for (int x : f( N / 2)) //evens
                ans[t++] = 2 * x;
        }
        memo.put(N, ans);
        return ans;
    }
}
'''