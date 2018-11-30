__source__ = 'https://leetcode.com/problems/rotate-string/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 796. Rotate String
#
# We are given two strings, A and B.
#
# A shift on A consists of taking string A and moving the leftmost character to the rightmost position.
# For example, if A = 'abcde', then it will be 'bcdea' after one shift on A.
# Return True if and only if A can become B after some number of shifts on A.
#
# Example 1:
# Input: A = 'abcde', B = 'cdeab'
# Output: true
#
# Example 2:
# Input: A = 'abcde', B = 'abced'
# Output: false
# Note:
#
# A and B will have length at most 100.
#
import unittest

#20ms 98.19% O(N^2)
class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if len(A) == 0:
            return True

        for s in xrange(len(A)):
            if all(A[(s+i) % len(A)] == B[i] for i in xrange(len(A))):
                return True
        return False

#20ms 98.19% O(N^2)
class Solution2(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        return len(A) == len(B) and B in A+A

#20ms 98.19% O(N^2)
class Solution3(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        MOD = 10**9 + 7
        P = 113
        Pinv = pow(P, MOD-2, MOD)

        hb = 0
        power = 1
        for x in B:
            code = ord(x) - 96
            hb = (hb + power * code) % MOD
            power = power * P % MOD

        ha = 0
        power = 1
        for x in A:
            code = ord(x) - 96
            ha = (ha + power * code) % MOD
            power = power * P % MOD

        if ha == hb and A == B: return True
        for i, x in enumerate(A):
            code = ord(x) - 96
            ha += power * code
            ha -= code
            ha *= Pinv
            ha %= MOD
            if ha == hb and A[i+1:] + A[:i+1] == B:
                return True
        return False

#20ms 98.19% O(N)
class Solution4(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        N = len(A)
        if N != len(B): return False
        if N == 0: return True

        #Compute shift table
        shifts = [1] * (N+1)
        left = -1
        for right in xrange(N):
            while left >= 0 and B[left] != B[right]:
                left -= shifts[left]
            shifts[right + 1] = right - left
            left += 1

        #Find match of B in A+A
        match_len = 0
        for char in A+A:
            while match_len >= 0 and B[match_len] != char:
                match_len -= shifts[match_len]

            match_len += 1
            if match_len == N:
                return True

        return False

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/rotate-string/solution/
Approach #1: Brute Force [Accepted]
Complexity Analysis
Time Complexity: O(N^2), where N is the length of A. For each rotation s, we check up to N elements in A and B.
Space Complexity: O(1). We only use pointers to elements of A and B.

#2ms 99.54%
class Solution {
    public boolean rotateString(String A, String B) {
        StringBuilder sb = new StringBuilder(A);
        int i = 0;
        if(A.length()==0&&B.length()==0) return true;
        while(i < A.length()){

            sb.append(sb.charAt(0));
            sb.deleteCharAt(0);
            String re = sb.toString();
            i++;
            if(re.equals(B)) return true;
        }
        return false;
    }
}

class Solution {
    public boolean rotateString(String A, String B) {
        StringBuilder sb = new StringBuilder(A);
        int i = 0;
        if(A.length()==0&&B.length()==0) return true;
        while(i < A.length()){

            sb.append(sb.charAt(0));
            sb.deleteCharAt(0);
            String re = sb.toString();
            i++;
            if(re.equals(B)) return true;
        }
        return false;
    }
}

Approach #2: Simple Check [Accepted]
Complexity Analysis
Time Complexity: O(N^2), where N is the length of A.
Space Complexity: O(N), the space used building A+A.

#2ms 99.54%
class Solution {
    public boolean rotateString(String A, String B) {
        return A.length() == B.length() && (A + A).contains(B);
    }
}

class Solution {
    public boolean rotateString(String A, String B) {
        String duplicate = A + A;
        return (A.length() == B.length()) && duplicate.indexOf(B) != -1;
    }
}

Approach #3: Rolling Hash [Accepted]
Complexity Analysis
Time Complexity: O(N), where N is the length of A.
Space Complexity: O(N), to perform the final check A_rotation == B.

#6ms 7.02%
import java.math.BigInteger;

class Solution {
    public boolean rotateString(String A, String B) {
        if (A.equals(B)) return true;

        int MOD = 1_000_000_007;
        int P = 113;
        int Pinv = BigInteger.valueOf(P).modInverse(BigInteger.valueOf(MOD)).intValue();

        long hb = 0, power = 1;
        for (char x : B.toCharArray()) {
            hb = (hb + power * x) % MOD;
            power = power * P % MOD;
        }

        long ha = 0; power = 1;
        char[] ca = A.toCharArray();
        for (char x : ca) {
            ha = (ha + power * x) % MOD;
            power = power * P % MOD;
        }

        for (int i = 0; i < ca.length; i++) {
            char x = ca[i];
            ha += power * x - x;
            ha %= MOD;
            ha *= Pinv;
            ha %= MOD;
            if (ha == hb && (A.substring( i + 1) + A.substring(0, i + 1)).equals(B)) return true;
        }
        return  false;
    }
}

Approach #4: KMP (Knuth-Morris-Pratt) [Accepted]
Complexity Analysis
Time Complexity: O(N), where NN is the length of A.
Space Complexity: O(N), to create the shift table shifts.

#2ms 99.54%
class Solution {
    public boolean rotateString(String A, String B) {
        int N = A.length();
        if (N != B.length()) return false;
        if (N == 0) return true;

        //Compute shift table
        int[] shifts = new int[N + 1];
        Arrays.fill(shifts, 1);
        int left = -1;
        for (int right = 0; right < N; ++right) {
            while (left >= 0 && B.charAt(left) != B.charAt(right)) {
                left -= shifts[left];
            }
            shifts[right + 1] = right - left;
            left++;
        }

        //Find match of B in A+A
        int matchLen = 0;
        for (char c : (A + A).toCharArray()) {
            while (matchLen >= 0 && B.charAt(matchLen) != c) {
                matchLen -= shifts[matchLen];
            }
            if (++matchLen == N) return true;
        }
        return false;
    }
}
'''