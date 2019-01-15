__source__ = 'https://leetcode.com/problems/binary-trees-with-factors/'
# Time:  O(N ^2)
# Space: O(N)
#
# Description: Leetcode # 823. Binary Trees With Factors
#
# Given an array of unique integers, each integer is strictly greater than 1.
#
# We make a binary tree using these integers and each number may be used for any number of times.
#
# Each non-leaf node's value should be equal to the product of the values of it's children.
#
# How many binary trees can we make?  Return the answer modulo 10 ** 9 + 7.
#
# Example 1:
#
# Input: A = [2, 4]
# Output: 3
# Explanation: We can make these trees: [2], [4], [4, 2, 2]
# Example 2:
#
# Input: A = [2, 4, 5, 10]
# Output: 7
# Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].
#
#
# Note:
#
# 1 <= A.length <= 1000.
# 2 <= A[i] <= 10 ^ 9.
#
import unittest
#28ms 88.16%
class Solution(object):
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        N = len(A)
        A.sort()
        dp = [1] * N
        index = {x: i for i, x in enumerate(A)}
        for i, x in enumerate(A):
            for j in xrange(i):
                if x % A[j] == 0: #A[j] will be left child
                    right = x / A[j]
                    if right in index:
                        dp[i] += dp[j] * dp[index[right]]
                        dp[i] %= MOD
        return sum(dp) % MOD

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/binary-trees-with-factors/solution/
Approach #1: Dynamic Programming [Accepted]
Complexity Analysis
Time Complexity: O(N^2), where N is the length of A. This comes from the two for-loops iterating i and j.
Space Complexity: O(N), the space used by dp and index.

# 53ms 54.34%
class Solution {
    public int numFactoredBinaryTrees(int[] A) {
        int MOD = 1_000_000_007;
        int N = A.length;
        Arrays.sort(A);
        long[] dp = new long[N];
        Arrays.fill(dp, 1);

        Map<Integer, Integer> index = new HashMap();
        for (int i = 0 ; i < N; i++) {
            index.put(A[i], i);
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < i; j++) {
                if (A[i] % A[j] == 0) { //A[j] is left child
                    int right = A[i] / A[j];
                    if (index.containsKey(right)) {
                        dp[i] = (dp[i] + dp[j] * dp[index.get(right)]) % MOD;
                    }

                }
            }
        }

        long ans = 0;
        for ( long x: dp) ans += x;
        return (int) (ans % MOD);
    }
}

#31ms 86.30%
class Solution {
    public int numFactoredBinaryTrees(int[] A) {
        long res = 0L, mod = (long) 1000000007;
        long[] dp = new long[A.length];
        Arrays.fill(dp,1);
        Arrays.sort(A);

        for (int i = 1; i < A.length; i++) {
            int s = 0, e = i - 1;
            while (s <= e) {
                if (A[s] * A[e] > A[i]) e--;
                else if (A[s] * A[e] < A[i]) s++;
                else {
                    dp[i] = ((dp[s] * dp[e] * (A[s] == A[e] ? 1 : 2 ) % mod + dp[i])) % mod;
                    s++;
                }
            }
        }
        for (long d : dp) res = ( d + res) % mod;
        return (int) res;
    }
}

# 19ms 100%
class Solution {
    public int numFactoredBinaryTrees(int[] A) {
        Arrays.sort(A);
        Map<Integer, Integer> valueToIndex = new HashMap<>();
        for(int i = 0; i < A.length; i++) valueToIndex.put(A[i], i);
        int n = A.length;
        long fResult = 0;
        long[] gResults = new long[n];

        for(int i = 0; i < A.length; i++){
            int cur = A[i];
            gResults[i] = 1;
            for (int leftIndex = 0; A[leftIndex] <= Math.sqrt(cur); leftIndex++) {
                int left = A[leftIndex];
                if (cur % left == 0 && valueToIndex.containsKey(cur / left)) {
                    int right = cur / left;
                    int rightIndex = valueToIndex.get(right);

                    if (left != right) {
                        gResults[i] += gResults[leftIndex] * gResults[rightIndex] * 2;
                    } else {
                        gResults[i] += gResults[leftIndex] * gResults[rightIndex];
                    }
                }
            }
            fResult += gResults[i];
        }
        return (int) (fResult % ((int) Math.pow(10, 9) + 7));
    }
}

'''