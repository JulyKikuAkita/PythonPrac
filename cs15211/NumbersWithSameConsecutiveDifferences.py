__source__ = 'https://leetcode.com/problems/numbers-with-same-consecutive-differences/'
# Time:  O(2^N)
# Space: O(2^N)
#
# Description: Leetcode # 967. Numbers With Same Consecutive Differences
#
# Return all non-negative integers of length N such that
# the absolute difference between every two consecutive digits is K.
#
# Note that every number in the answer must not have leading zeros except for the number 0 itself.
# For example, 01 has one leading zero and is invalid, but 0 is valid.
#
# You may return the answer in any order.
#
# Example 1:
#
# Input: N = 3, K = 7
# Output: [181,292,707,818,929]
# Explanation: Note that 070 is not a valid number, because it has leading zeroes.
#
# Example 2:
#
# Input: N = 2, K = 1
# Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
#
# Note:
#     1 <= N <= 9
#     0 <= K <= 9
#
import unittest
# 76ms 25.71%
class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        ans = {x for x in range(1, 10)}
        for _ in xrange(N-1):
            ans2 = set()
            for x in ans:
                d = x % 10
                if d - K >= 0:
                    ans2.add(10*x + d-K)
                if d + K <= 9:
                    ans2.add(10*x + d+K)
            ans = ans2

        if N == 1:
            ans.add(0)

        return list(ans)
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/numbers-with-same-consecutive-differences/solution/
#
Approach 1: Brute Force
Complexity Analysis
Time Complexity: O(2^N)
Space Complexity: O(2^N) 
# 14ms 44.79%
class Solution {
    public int[] numsSameConsecDiff(int N, int K) {
        Set<Integer> cur = new HashSet();
        for (int i = 1; i <= 9; ++i) cur.add(i);
        for (int steps = 1; steps <= N-1; ++steps) {
            Set<Integer> cur2 = new HashSet();
            for (int x: cur) {
                int d = x % 10;
                if (d - K >= 0)
                    cur2.add(10 * x + (d - K));
                if (d + K <= 9)
                    cur2.add(10 * x + (d + K));
            }
            cur = cur2;
        }

        if (N == 1)
            cur.add(0);

        int[] ans = new int[cur.size()];
        int t = 0;
        for (int x: cur)
            ans[t++] = x;
        return ans;
    }
}

# 8ms 93.55%
class Solution {
    public int[] numsSameConsecDiff(int N, int K) {
        if (N == 1) return new int[]{0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        List<Integer> result = new ArrayList<>();
        for (int i = 1; i < 10; i++) 
            dfs(N, K, 1, i, result);
        int[] ans = new int[result.size()];
        for (int i = 0; i < ans.length; i++) 
            ans[i] = result.get(i);
        return ans;
    }
    
    private void dfs(int N, int K, int index, int num, List<Integer> result) {
        if (index == N) {
            result.add(num);
            return;
        }
        
        int pre = num % 10;
        if (pre + K >= 0 && pre + K <= 9) {
            dfs(N, K, index + 1, num * 10 + pre + K, result);
        }
        if (pre - K >= 0 && pre - K <= 9) {
            if (K == 0) return;
            dfs(N, K, index + 1, num * 10 + pre - K, result);
        }
        return;
    }
}

'''
