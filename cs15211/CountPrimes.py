__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/count-primes.py
# Time:  O(n)
# Space: O(n)
# Description:
#
# Count the number of prime numbers less than a non-negative number, n
#
# Hint: The number n could be in the order of 100,000 to 5,000,000.
#
# Amazon

from math import sqrt

class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n <= 2:
            return 0

        is_prime = [True] * n
        num = 0
        for i in xrange(2, n):
            if is_prime[i]:
                num += 1
                for j in xrange(i+i, n , i):
                    is_prime[j] = False
        return num

if __name__ == "__main__":
    print Solution().countPrimes(7)

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0

        isPrime = [ True for _ in xrange(n)]
        cnt = 0

        for i in xrange(2, n):
            if i * i > n:
                break
            if isPrime[i]:
                for j in xrange( i*i, n, i):
                    isPrime[j] = False

        return isPrime.count(True) - 2 # don't count 0, 1

#java
js = '''
public class Solution {
    public int countPrimes(int n) {
        if (n < 3) {
            return 0;
        }
        boolean[] notPrime = new boolean[n + 1];
        for (int i = 2; i * i <= n; i++) { // if i <= n :  java.lang.ArrayIndexOutOfBoundsException: -2146737495
            if (!notPrime[i]) {
                for (int j = i * i; j < n + 1; j += i) {
                    notPrime[j] = true;
                }
            }
        }
        int result = 0;
        for (int i = 2; i < n; i++) {
            if (!notPrime[i]) {
                result++;
            }
        }
        return result;
    }
}

The accurate time complexity is O(n\log{\log{n}}) which is not trivial to show.
But, it is easy to show a complexity of O(n\log{n}).

public class Solution {
    public int countPrimes(int n) {
        boolean[] isPrime = new boolean[n];
        for (int i = 2; i < n; ++i) isPrime[i] = true;
        for (int i = 2; i * i < n; ++i)
            if (isPrime[i])
                for (int j = i * i; j < n; j += i)
                    isPrime[j] = false;
        int ans = 0;
        for (boolean b: isPrime) if (b) ans++;
        return ans;
    }
}
'''