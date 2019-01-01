# coding=utf-8
__source__ = 'https://leetcode.com/problems/sum-of-subsequence-widths/'
# Time:  O(NlogN)
# Space: O(N)
#
# Description: Leetcode # 891. Sum of Subsequence Widths
#
# Given an array of integers A, consider all non-empty subsequences of A.
#
# For any sequence S, let the width of S be the difference between the maximum and minimum element of S.
#
# Return the sum of the widths of all subsequences of A.
#
# As the answer may be very large, return the answer modulo 10^9 + 7.
#
# Example 1:
#
# Input: [2,1,3]
# Output: 6
# Explanation:
# Subsequences are [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3].
# The corresponding widths are 0, 0, 0, 1, 1, 2, 2.
# The sum of these widths is 6.
#
#
# Note:
#
# 1 <= A.length <= 20000
# 1 <= A[i] <= 20000
#
import unittest

# 108ms 91.67%
class Solution(object):
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        N = len(A)
        A.sort()

        pow2 = [1]
        for i in xrange(1, N):
            pow2.append(pow2[-1] * 2 % MOD)

        ans = 0
        for i, x in enumerate(A):
            ans = (ans + (pow2[i] - pow2[N-1-i]) * x) % MOD
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/sum-of-subsequence-widths/solution/
#
Approach 1: Mathematical
Complexity Analysis
Time Complexity: O(NlogN), where NN is the length of A.
Space Complexity: O(N), the space used by pow2. 
(We can improve this to O(1)O(1) space by calculating these powers on the fly.) 
#  After sorting the array, this allows us to know that the number of subsequences with minimum 
# A[i] and maximum A[j] is 2^{j-i-1}. Hence, the desired answer is:
# ∑(2^{j-i-1}) (A_j - A_i) j>i =0 ∑n−1​(2^i − 2^(N−i−1))Ai​

# 25ms 92.68%
class Solution {
    public int sumSubseqWidths(int[] A) {
        int MOD = 1_000_000_007;
        int N = A.length;
        Arrays.sort(A);

        long[] pow2 = new long[N];
        pow2[0] = 1;
        for (int i = 1; i < N; ++i)
            pow2[i] = pow2[i-1] * 2 % MOD;

        long ans = 0;
        for (int i = 0; i < N; ++i)
            ans = (ans + (pow2[i] - pow2[N-1-i]) * A[i]) % MOD;

        return (int) ans;
    }
}

# 16ms 100%
class Solution {
    public int sumSubseqWidths(int[] A) {
        // Arrays.sort(A);
        countingSort(A);
        int mod = (int) 1e9 + 7;
        long ans = 0;
        long p = 1;
        for(int i = 0; i < A.length; i++){
        	ans = (ans + (A[i] - A[A.length - i - 1]) * p) % mod;
            p = (p << 1) % mod;
        }
        return (int) (ans + mod) % mod;
    }

    private void countingSort(int [] arr){
    	int max = Integer.MIN_VALUE;
    	int min = Integer.MAX_VALUE;

    	for(int a : arr){
    		min = Math.min(min, a);
    		max = Math.max(max, a);
    	}

    	int [] count = new int[max - min + 1];
    	for (int a : arr) {
            ++count[a - min];
        }
        int i = 0, j = 0;
        while (i < count.length) {
            if (--count[i] >= 0) arr[j++] = i + min;
            else i++;
        }
    }
}

'''
