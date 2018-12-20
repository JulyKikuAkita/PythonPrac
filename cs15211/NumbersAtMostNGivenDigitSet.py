__source__ = 'https://leetcode.com/problems/numbers-at-most-n-given-digit-set/'
# Time:  O(logN)
# Space: O(logN)
#
# Description: Leetcode # 902. Numbers At Most N Given Digit Set
#
# We have a sorted set of digits D, a non-empty subset of {'1','2','3','4','5','6','7','8','9'}.
# (Note that '0' is not included.)
#
# Now, we write numbers using these digits, using each digit as many times as we want.
# For example, if D = {'1','3','5'}, we may write numbers such as '13', '551', '1351315'.
#
# Return the number of positive integers that can be written (using the digits of D)
# that are less than or equal to N.
#
# Example 1:
#
# Input: D = ["1","3","5","7"], N = 100
# Output: 20
# Explanation:
# The 20 numbers that can be written are:
# 1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
#
# Example 2:
#
# Input: D = ["1","4","9"], N = 1000000000
# Output: 29523
# Explanation:
# We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
# 81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
# 2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit numbers.
# In total, this is 29523 integers that can be written using the digits of D.
#
# Note:
#     D is a subset of digits '1'-'9' in sorted order.
#     1 <= N <= 10^9
#
import unittest

# 20ms 100%
class Solution(object):
    def atMostNGivenDigitSet(self, D, N):
        """
        :type D: List[str]
        :type N: int
        :rtype: int
        """
        S = str(N)
        K = len(S)
        dp = [0] * K + [1]
        # dp[i] = total number of valid integers if N was "N[i:]"

        for i in xrange(K-1, -1, -1):
            # Compute dp[i]

            for d in D:
                if d < S[i]:
                    dp[i] += len(D) ** (K-i-1)
                elif d == S[i]:
                    dp[i] += dp[i+1]

        return dp[0] + sum(len(D) ** i for i in xrange(1, K))

# 28ms 24.07%
class Solution2(object):
    def atMostNGivenDigitSet(self, D, N):
        """
        :type D: List[str]
        :type N: int
        :rtype: int
        """
        B = len(D) # bijective-base B
        S = str(N)
        K = len(S)
        A = []  #  The largest valid number in bijective-base-B.

        for c in S:
            if c in D:
                A.append(D.index(c) + 1)
            else:
                i = bisect.bisect(D, c)
                A.append(i)
                # i = 1 + (largest index j with c >= D[j], or -1 if impossible)
                if i == 0:
                    # subtract 1
                    for j in xrange(len(A) - 1, 0, -1):
                        if A[j]: break
                        A[j] += B
                        A[j-1] -= 1

                A.extend([B] * (K - len(A)))
                break

        ans = 0
        for x in A:
            ans = ans * B + x
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/numbers-at-most-n-given-digit-set/solution/
#
Approach 1: Dynamic Programming + Counting
Complexity Analysis
Time Complexity: O(logN), and assuming D.length is constant. 
(We could make this better by pre-calculating the number of d < S[i] 
for all possible digits S[i], but this isn't necessary.)
Space Complexity: O(logN), the space used by S and dp. 
(Actually, we could store only the last 2 entries of dp, 
but this isn't necessary.)
Let dp[i] be the number of ways to write a valid number if N became N[i], N[i+1], .... 
For example, if N = 2345, then dp[0] would be the number of valid numbers at most 2345, 
dp[1] would be the ones at most 345, 
dp[2] would be the ones at most 45, 
and dp[3] would be the ones at most 5.
Then, by our reasoning above, 
dp[i] = (number of d in D with d < S[i]) * ((D.length) ** (K-i-1)), 
plus dp[i+1] if S[i] is in D.

# 4ms 84.97%
class Solution {
    public int atMostNGivenDigitSet(String[] D, int N) {
        String S = String.valueOf(N);
        int K = S.length();
        int[] dp = new int[K+1];
        dp[K] = 1;
        
        for (int i = K - 1; i >= 0; i--) {
            // compute dp[i]
            int Si = S.charAt(i) - '0';
            for (String d : D) {
                if (Integer.valueOf(d) < Si) {
                    dp[i] += Math.pow(D.length, K - i - 1);
                } else if (Integer.valueOf(d) == Si) {
                    dp[i] += dp[i + 1];
                }
            }
        }
        
        for (int i = 1; i < K; i++) {
            dp[0] += Math.pow(D.length, i);
        }
        return dp[0];
    }
}

Approach 2: Mathematical
Complexity Analysis
Time Complexity: O(logN), and assuming D.length is constant.
Space Complexity: O(logN), the space used by A. 

# 3ms 100%
class Solution {
    public int atMostNGivenDigitSet(String[] D, int N) {
        int B = D.length; // bijective-base B
        char[] ca = String.valueOf(N).toCharArray();
        int K = ca.length;
        int[] A = new int[K];
        int t = 0;
        
        for (char c : ca) {
            int c_index = 0; // Largest such that c >= D[c_index - 1]
            boolean match = false;
            for (int i = 0; i < B; i++) {
                if (c >= D[i].charAt(0)) c_index = i + 1;
                if (c == D[i].charAt(0)) match = true;
            }
            
            A[t++] = c_index;
            if (match) continue;
            if (c_index == 0) { //subtract 1
                for (int j = t - 1; j > 0; j--) {
                    if (A[j] > 0) break;
                    A[j] += B;
                    A[j - 1]--;
                }
            }
            while (t < K) 
                A[t++] = B;    
            break;
        }
        int ans = 0;
        for (int x : A) ans = ans * B + x;
        return ans;
    }
}

'''
