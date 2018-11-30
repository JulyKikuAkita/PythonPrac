__source__ = 'https://leetcode.com/problems/nth-magical-number/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 878. Nth Magical Number
#
# A positive integer is magical if it is divisible by either A or B.
#
# Return the N-th magical number.  Since the answer may be very large, return it modulo 10^9 + 7.
#
#
#
# Example 1:
#
# Input: N = 1, A = 2, B = 3
# Output: 2
# Example 2:
#
# Input: N = 4, A = 2, B = 3
# Output: 6
# Example 3:
#
# Input: N = 5, A = 2, B = 4
# Output: 10
# Example 4:
#
# Input: N = 3, A = 6, B = 4
# Output: 8
#
#
# Note:
#
# 1 <= N <= 10^9
# 2 <= A <= 40000
# 2 <= B <= 40000
#
import unittest

#20ms 100%
class Solution(object):
    def nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        #a = math.gcd(A, B)
        a, b = A, B
        while b:
            a, b = b, a%b
        lcm = A*B/a
        left = 2
        right = 10**14
        while left < right:
            mid = (left+right)/2
            if mid/A + mid/B - mid/lcm <N:
                left = mid +1
            else:
                right = mid
        return left%(10**9+7)


class Solution2(object):
    def nthMagicalNumber(self, N, A, B):
        a, b = A, B
        while b: a, b = b, a % b
        l, r, lcm = 2, 10**14, A * B / a
        while l < r:
            m = (l + r) / 2
            if m / A + m / B - m / lcm < N: l = m + 1
            else: r = m
        return l % (10**9 + 7)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/nth-magical-number/solution/
Approach 1: Mathematical
Complexity Analysis

Time Complexity: O(A+B), assuming a model where integer math operations are O(1).
The calculation of q * L is O(1).
The calculation of the rr-th magical number after q*M is O(M) which is O(A+B.
Space Complexity: O(1).

#5ms 50%
class Solution {
    public int nthMagicalNumber(int N, int A, int B) {
        int MOD = 1_000_000_007;
        int L = A / gcd(A, B) * B;
        int M = L / A + L / B - 1;
        int q = N / M, r = N % M;

        long ans = (long) q * L % MOD;
        if (r == 0)
            return (int) ans;

        int[] heads = new int[]{A, B};
        for (int i = 0; i < r - 1; ++i) {
            if (heads[0] <= heads[1])
                heads[0] += A;
            else
                heads[1] += B;
        }
        ans += Math.min(heads[0], heads[1]);
        return (int) (ans % MOD);
    }

    public int gcd(int x, int y) {
        return x == 0 ? y : gcd(y % x,  x);
    }
}


Approach 2: Binary Search
Complexity Analysis
Time Complexity: O(log(N*max(A,B))).
Space Complexity: O(1).

#3ms 95.73%
class Solution {
    public int nthMagicalNumber(int N, int A, int B) {
        int MOD = 1_000_000_007;
        int L = A / gcd(A, B) * B;

        long lo = 0;
        long hi = (long) 1e15;
        while (lo < hi) {
            long mid = lo + (hi - lo) / 2;
            // If there are not enough magic numbers below mi...
            if (mid / A + mid / B - mid / L < N){
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return (int) (lo % MOD);
    }

    public int gcd(int x, int y) {
        return x == 0 ? y : gcd(y % x, x);
    }
}

'''