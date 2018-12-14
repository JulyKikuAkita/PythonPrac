# coding=utf-8
__source__ = 'https://leetcode.com/problems/perfect-number/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 507. Perfect Number
#
# We define the Perfect Number is a positive integer t
# hat is equal to the sum of all its positive divisors except itself.
# Now, given an integer n, write a function that returns true
# when it is a perfect number and false when it is not.
# Example:
# Input: 28
# Output: True
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# Note: The input number n will not exceed 100,000,000. (1e8)
#
# Hide Company Tags Fallible
# Hide Tags Math
#
import unittest
# 44ms 25.85%
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        sum = 1
        SQRT = int(num**0.5)
        for i in xrange(2, SQRT + 1):
            if num % i == 0:
                sum += (i + num / i)
        return num == sum

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/perfect-number/solution/

# Approach #4 Euclid-Euler Theorem [Accepted]
# Euclid proved that
# 2^(p−1)*(2^p - 1) is an even perfect number whenever 2^(p−1) is prime, where p is prime.
# for p = 2:   21(22 − 1) = 6
# for p = 3:   22(23 − 1) = 28
# for p = 5:   24(25 − 1) = 496
# for p = 7:   26(27 − 1) = 8128.
# Prime numbers of the form 2^(p−1) are known as Mersenne primes.
# You can see that for small value of pp, its related perfect number goes very high.
# So, we need to evaluate perfect numbers for some primes (2,3,5,7,13,17,19,31) only,
# as for bigger prime its perfect number will not fit in 64 bits.

# 4ms 100%
class Solution {
    public int pn(int prime) {
        // 2^(p−1)*(2^p - 1) is an even perfect number whenever 2^(p−1) is prime
        return (1 << (prime - 1)) * ((1 << prime) - 1);
    }

    public boolean checkPerfectNumber(int num) {
        int[] primes=new int[]{2,3,5,7,13,17,19,31};
        for (int prime: primes) {
            if (pn(prime) == num)
                return true;
        }
        return false;
    }
}

# 6ms 97.90%
class Solution {
    public boolean checkPerfectNumber(int num) {
        if(num <= 1) return false;
        int sum = 1;
        for (int i = 2; i <= Math.sqrt(num); i++){
            if( num % i == 0) {
                sum += i + (num / i);
            }
        }
        return sum == num;
    }
}

'''
