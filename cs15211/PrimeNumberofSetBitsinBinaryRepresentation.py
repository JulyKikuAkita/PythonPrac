__source__ = 'https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/'
# Time:  O(D)  where D = R-L is the number of integers considered.
# Space: O(1)
#
# Description: Leetcode # 762. Prime Number of Set Bits in Binary Representation
#
# Given two integers L and R,
# find the count of numbers in the range [L, R] (inclusive) having a prime number of set bits
# in their binary representation.
#
# (Recall that the number of set bits an integer has is the number of 1s present
# when written in binary.
# For example, 21 written in binary is 10101 which has 3 set bits.
# Also, 1 is not a prime.)
#
# Example 1:
#
# Input: L = 6, R = 10
# Output: 4
# Explanation:
# 6 -> 110 (2 set bits, 2 is prime)
# 7 -> 111 (3 set bits, 3 is prime)
# 9 -> 1001 (2 set bits , 2 is prime)
# 10->1010 (2 set bits , 2 is prime)
# Example 2:
#
# Input: L = 10, R = 15
# Output: 5
# Explanation:
# 10 -> 1010 (2 set bits, 2 is prime)
# 11 -> 1011 (3 set bits, 3 is prime)
# 12 -> 1100 (2 set bits, 2 is prime)
# 13 -> 1101 (3 set bits, 3 is prime)
# 14 -> 1110 (3 set bits, 3 is prime)
# 15 -> 1111 (4 set bits, 4 is not prime)
# Note:
#
# L, R will be integers L <= R in the range [1, 10^6].
# R - L will be at most 10000.
#
import unittest

# 300ms 62.29%
class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(bin(x).count('1') in primes
                   for x in xrange(L, R+1))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/solution/
Approach #1: Direct [Accepted]
Complexity Analysis
Time Complexity: O(D), where D = R-L is the number of integers considered.
In a bit complexity model, this would be O(DlogD) as we have to count the bits in O(logD) time.
Space Complexity: O(1)

# 9ms 98.75%
class Solution {
    public int countPrimeSetBits(int L, int R) {
        int ans = 0;
        for (int x = L; x <= R; ++x) {
            if (isSmallPrime(Integer.bitCount(x))) ans++;
        }
        return ans;
    }

    public boolean isSmallPrime(int x) {
        return (x == 2 || x == 3 || x == 5 || x == 7 ||
                x == 11 || x == 13 || x == 17 || x == 19);
    }
}

# 9ms 98.75%
class Solution {
    public int countPrimeSetBits(int L, int R) {
        int count = 0;
        for (int i = L; i <= R; i++)
            if (isPrime(Integer.bitCount(i))) count++;
        return count;
    }
    private boolean isPrime(int x) {
        if (x <= 1) return false;
        for (int i = 2; i * i <= x; i++)
            if (x % i == 0) return false;
        //System.out.print(x + ", ");
        return true;
    }
}
'''