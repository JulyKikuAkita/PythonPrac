__source__ = 'https://leetcode.com/problems/prime-palindrome/'
# Time:  O(N)
# Space: O(1)
#
# Description: Leetcode # 866. Prime Palindrome
#
# Find the smallest prime palindrome greater than or equal to N.
#
# Recall that a number is prime if it's only divisors are 1 and itself, and it is greater than 1.
#
# For example, 2,3,5,7,11 and 13 are primes.
#
# Recall that a number is a palindrome if it reads the same from left to right
# as it does from right to left.
#
# For example, 12321 is a palindrome.
#
# Example 1:
#
# Input: 6
# Output: 7
# Example 2:
#
# Input: 8
# Output: 11
# Example 3:
#
# Input: 13
# Output: 101
#
#
# Note:
#
# 1 <= N <= 10^8
# The answer is guaranteed to exist and be less than 2 * 10^8.
#
import unittest

# 224ms 48.57%
class Solution(object):
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        def is_prime(n):
            return n > 1 and all(n%d for d in xrange(2, int(n**.5) + 1))

        for length in xrange(1, 6):
            #Check for odd-length palindromes
            for root in xrange(10**(length - 1), 10**length):
                s = str(root)
                x = int(s + s[-2::-1]) #eg. s = '123' to x = int('12321')
                if x >= N and is_prime(x):
                    return x
                    #If we didn't check for even-length palindromes:
                    #return min(x, 11) if N <= 11 else x

            #Check for even-length palindromes
            for root in xrange(10**(length - 1), 10**length):
                s = str(root)
                x = int(s + s[-1::-1]) #eg. s = '123' to x = int('123321')
                if x >= N and is_prime(x):
                    return x

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/prime-palindrome/solution/

Approach 1: Iterate Palindromes
Complexity Analysis
Time Complexity: Based on our analysis above,
we performed on the order of O(N) operations (not counting log factors from dealing with integers),
given we knew the existence of prime palindrome 100030001.
Interestingly, the time complexity is an open problem in mathematics,
as it is not even known whether there are infinitely many prime palindromes,
or whether palindromes behave as random integers for our purposes here -
see ["Almost All Palindromes are Composite"] for more.
Space Complexity: O(logN), the space used by s (or sb in Java.)

Each palindrome of d digits has a palindromic root, it's first k= (d+1)/ 2 digits.
The next palindrome is formed by the next root.
For example, if 123123 is a root for the 5 digit palindrome 1232112321,
then the next palindrome is 1242112421 with root 124124.
Notice that roots and palindromes are not a bijection,
as palindromes 123321123321 and 1232112321 have the same root.

# 106ms 17.54%
class Solution {
    public int primePalindrome(int N) {
        for (int L = 1; L <= 5; ++L) {
            //Check for odd-length palindromes
            for (int root = (int)Math.pow(10, L - 1); root < (int)Math.pow(10, L); ++root) {
                StringBuilder sb = new StringBuilder(Integer.toString(root));
                for (int k = L-2; k >= 0; --k)
                    sb.append(sb.charAt(k));
                int x = Integer.valueOf(sb.toString());
                if (x >= N && isPrime(x))
                    return x;
                    //If we didn't check for even-length palindromes:
                    //return N <= 11 ? min(x, 11) : x
            }
            //Check for even-length palindromes
            for (int root = (int)Math.pow(10, L - 1); root < (int)Math.pow(10, L); ++root) {
                StringBuilder sb = new StringBuilder(Integer.toString(root));
                for (int k = L-1; k >= 0; --k)
                    sb.append(sb.charAt(k));
                int x = Integer.valueOf(sb.toString());
                if (x >= N && isPrime(x))
                    return x;
            }
        }
        throw null;
    }

    private boolean isPrime(int N) {
        if (N < 2) return false;
        int R = (int) Math.sqrt(N);
        for (int d = 2; d <= R; d++) {
            if (N % d == 0) return false;
        }
        return true;
    }
}

Approach 2: Brute Force with Mathematical Shortcut
Complexity Analysis
Time Complexity: O(N), with the caveats explained in Approach #1,
and ignoring the logN factor when checking an integer for palindromes.
Space Complexity: O(1)
For each number, check whether it is a palindrome.
If it is, check whether it is a prime. If the number is 8 digits, skip to the 9 digit numbers.

# 21ms 76.78%
class Solution {
    public int primePalindrome(int N) {
        while (true) {
            if (N == reverse(N) && isPrime(N))
                return N;
            N++;
            if (10_000_000 < N && N < 100_000_000)
                N = 100_000_000;
        }
    }

    private boolean isPrime(int N) {
        if (N < 2) return false;
        int R = (int) Math.sqrt(N);
        for (int d = 2; d <= R; d++) {
            if (N % d == 0) return false;
        }
        return true;
    }

    private int reverse(int N) {
        int ans = 0;
        while (N > 0) {
            ans = 10 * ans + ( N % 10);
            N /= 10;
        }
        return ans;
    }
}

# 6ms 95.26%
class Solution {
    public int primePalindrome(int N) {
        if (N > 7 && N <= 11) {
            return 11; //11 is the only even-palindrome that's prime.
        }
        for (int i = 0; i < 100000; i++) {
            int p = odd_palindrome(i);
            if (p >= N && isPrime(p)) return p;
        }
        return -1;
    }

    // for example 12321, head is 123, tail is 21
	int odd_palindrome(int head) {
        int tail = 0;
        int exp = 1; //10 exponent number
        for (int r = head / 10; r > 0; r /= 10) {
            int d = r % 10;
            tail = tail * 10 + d;
            exp *= 10;
        }
        return head * exp + tail;
    }

    private boolean isPrime(int n) {
        if (n <= 1) return false;
        else if (n <= 3) return true;
        else if (n % 2 == 0 || n % 3 == 0) return false;
        for (int i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) //dividble by 5 or 7
                return false;
        }
        return true;
    }
}
'''