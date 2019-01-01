__source__ = 'https://leetcode.com/problems/rotated-digits/'
# Time:  O(logN)
# Space: O(logN)
#
# Description: Leetcode # 788. Rotated Digits
#
# X is a good number if after rotating each digit individually by 180 degrees,
# we get a valid number that is different from X.
# Each digit must be rotated - we cannot choose to leave it alone.
#
# A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves;
# 2 and 5 rotate to each other; 6 and 9 rotate to each other,
# and the rest of the numbers do not rotate to any other number and become invalid.
#
# Now given a positive number N, how many numbers X from 1 to N are good?
#
# Example:
# Input: 10
# Output: 4
# Explanation:
# There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
#
# Note: N  will be in range [1, 10000].
#
import unittest

# 100ms 59.06%
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        ans = 0
        # For each x in [1, N], check whether it's good
        for x in xrange(1, N+1):
            S = str(x)
            # Each x has only rotateable digits, and one of them
            # rotates to a different digit
            ans += (all(d not in '347' for d in S)
                    and any(d in '2569' for d in S))
        return ans

# 20ms 100%
class Solution2(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        A = map(int, str(N))
        memo = {}
        def dp(i, equality_flag, involution_flag):
            if i == len(A): return +(involution_flag)
            if (i, equality_flag, involution_flag) not in memo:
                ans = 0
                for d in xrange(A[i] + 1 if equality_flag else 10):
                    if d in {3, 4, 7}: continue
                    ans += dp(i+1, equality_flag and d == A[i],
                              involution_flag or d in {2, 5, 6, 9})
                memo[i, equality_flag, involution_flag] = ans
            return memo[i, equality_flag, involution_flag]
        return dp(0, True, False)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/rotated-digits/solution/
#
Approach #1: Brute Force [Accepted]
Complexity Analysis
Time Complexity: O(NlogN). For each X, we check each digit.
Space Complexity: O(logN), the space stored either by the string, 
or the recursive call stack of the function good.

# 4ms 96.58%
class Solution {
    public int rotatedDigits(int N) {
        // Count how many n in [1, N] are good.
        int ans = 0;
        for (int n = 1; n <= N; ++n)
            if (good(n, false)) ans++;
        return ans;
    }
    
    // Return true if n is good.
    // The flag is true iff we have an occurrence of 2, 5, 6, 9.
    private boolean good(int n, boolean flag) {
        if (n == 0) return flag;
        int d = n % 10;
        if (d == 3 || d == 4 || d == 7) return false;
        if (d == 0 || d == 1 || d == 8) return good(n / 10, flag);
        return good(n / 10, true);
    }
}

Approach #2: Dynamic Programming On Digits [Accepted]
Complexity Analysis
Time Complexity: O(logN). We do constant-time work for each digit of N.
Space Complexity: O(logN), the space stored by memo.
# If equality_flag is true, the ith digit (0 indexed) will be at most the ith digit of N.
# 2ms 100%
class Solution {
    public int rotatedDigits(int N) {
        char[] A = String.valueOf(N).toCharArray();
        int K = A.length;

        int[][][] memo = new int[K+1][2][2];
        memo[K][0][1] = memo[K][1][1] = 1;
        
        for (int i = K - 1; i >= 0; --i) {
            for (int eqf = 0; eqf <= 1; ++eqf) {
                for (int invf = 0; invf <= 1; ++invf) {
                    // We will compute ans = memo[i][eqf][invf],
                    // the number of good numbers with respect to N = A[i:].
                    // If eqf is true, we must stay below N, otherwise
                    // we can use any digits.
                    // Invf becomes true when we write a 2569, and it
                    // must be true by the end of our writing as all
                    // good numbers have a digit in 2569.
                    int ans = 0;
                    for (char d = '0'; d <= (eqf == 1 ? A[i] : '9'); ++d) {
                        if (d == '3' || d == '4' || d == '7') continue;
                        boolean invo = (d == '2' || d == '5' || d == '6' || d == '9');
                        ans += memo[i+1][d == A[i] ? eqf : 0][invo ? 1 : invf];
                    }
                    memo[i][eqf][invf] = ans;
                }
            }
        }
        return memo[0][1][0];
    }
}

# 2ms 100%
class Solution {
    // need to count:
    // 1) has 2569.
    // 2) has not 347.
    // 3) optional 018.
    // for a digit in N, if the digit is 2569, then other digits can be 2569018,
    // otherwise other digits must contain 2569.
    // starting from right to left, use dp to represent number of good numbers for N's digits.
    // e.g., N is 54, we need to calculate:
    // first digit 4.
    // 0..4
    // 0..9
    // second digit 5.
    // 0 0..9
    // 1 0..9
    // 2 0..9
    // 3 (not valid)
    // 4 (not valid)
    // 5 0..4 note that if the current digit is limited to 5, then previous digit is limited to 4.
    // 5 0..9 this and below is for more digits on the left, say N=154.
    // 6 0..9
    // 7 (not valid)
    // 8 0..9
    // 9 0..9
    public int rotatedDigits(int N) {
        int from0to9must2569 = 0;
        int from0to9any2569018 = 1; // this number should be from0to9must2569 plus only 018
        int from0toXmust2569 = 0;
        int from0toXany2569018 = 1; // this number should be from0toXmust2569 plus only 018
        while(N != 0) {
            int newfrom0to9must2569 = 0;
            int newfrom0to9any2569018 = 0;
            int newfrom0toXmust2569 = 0;
            int newfrom0toXany2569018 = 0;
            // from 0 to 9.
            // 0, 1, 8
            newfrom0to9must2569 += from0to9must2569 * 3;
            newfrom0to9any2569018 += from0to9any2569018 * 3;
            // 2, 5, 6, 9: the current digit is 2569, thus previous digits can be any.
            newfrom0to9must2569 += from0to9any2569018 * 4;
            newfrom0to9any2569018 += from0to9any2569018 * 4;
            // from 0 to x.
            int x = N % 10;
            N /= 10;
            switch(x) {
                case 9:
                    newfrom0toXmust2569 += from0toXany2569018 + from0to9must2569 * 3 + from0to9any2569018 * 3;
                    newfrom0toXany2569018 += from0toXany2569018 + from0to9any2569018 * 3 + from0to9any2569018 * 3;
                    break;
                case 8:
                    newfrom0toXmust2569 += from0toXmust2569 + from0to9must2569 * 2 + from0to9any2569018 * 3;
                    newfrom0toXany2569018 += from0toXany2569018 + from0to9any2569018 * 2 + from0to9any2569018 * 3;
                    break;
                case 7:
                    newfrom0toXmust2569 += 0 + from0to9must2569 * 2 + from0to9any2569018 * 3;
                    newfrom0toXany2569018 += 0 + from0to9any2569018 * 2 + from0to9any2569018 * 3;
                    break;
                case 6:
                    newfrom0toXmust2569 += from0toXany2569018 + from0to9must2569 * 2 + from0to9any2569018 * 2;
                    newfrom0toXany2569018 += from0toXany2569018 + from0to9any2569018 * 2 + from0to9any2569018 * 2;
                    break;
                case 5:
                    newfrom0toXmust2569 += from0toXany2569018 + from0to9must2569 * 2 + from0to9any2569018 * 1;
                    newfrom0toXany2569018 += from0toXany2569018 + from0to9any2569018 * 2 + from0to9any2569018 * 1;
                    break;
                case 4:
                case 3:
                    newfrom0toXmust2569 += 0 + from0to9must2569 * 2 + from0to9any2569018 * 1;
                    newfrom0toXany2569018 += 0 + from0to9any2569018 * 2 + from0to9any2569018 * 1;
                    break;
                case 2:
                    newfrom0toXmust2569 += from0toXany2569018 + from0to9must2569 * 2 + from0to9any2569018 * 0;
                    newfrom0toXany2569018 += from0toXany2569018 + from0to9any2569018 * 2 + from0to9any2569018 * 0;
                    break;
                case 1:
                    newfrom0toXmust2569 += from0toXmust2569 + from0to9must2569 * 1 + from0to9any2569018 * 0;
                    newfrom0toXany2569018 += from0toXany2569018 + from0to9any2569018 * 1 + from0to9any2569018 * 0;
                    break;
                case 0:
                    newfrom0toXmust2569 += from0toXmust2569 + from0to9must2569 * 0 + from0to9any2569018 * 0;
                    newfrom0toXany2569018 += from0toXany2569018 + from0to9any2569018 * 0 + from0to9any2569018 * 0;
                    break;
            }
            from0to9must2569 = newfrom0to9must2569;
            from0to9any2569018 = newfrom0to9any2569018;
            from0toXmust2569 = newfrom0toXmust2569;
            from0toXany2569018 = newfrom0toXany2569018;
        }
        return from0toXmust2569;
    }
}
'''
