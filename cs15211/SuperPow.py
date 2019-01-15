__source__ = 'https://leetcode.com/problems/super-pow/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/super-pow.py
# Time:  O(n), n is the size of b.
# Space: O(1)
#
# Description: Leetcode # 372. Super Pow
#
# Your task is to calculate a^b mod 1337 where a is a positive integer
# and b is an extremely large positive integer given in the form of an array.
#
# Example1:
#
# a = 2
# b = [3]
#
# Result: 8
# Example2:
#
# a = 2
# b = [1,0]
#
# Result: 1024
#
# Related Topics
# Math
# Similar Questions
# Pow(x, n)
#
import unittest
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        def myPow(a, n, b):
            result = 1
            x = a % b
            while n:
                if n & 1:
                    result = result * x % b
                n >>= 1
                x = x * x % b
            return result % b

        result = 1
        for digit in b:
            result = myPow(result, 10, 1337) * myPow(a, digit, 1337) % 1337
        return result

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

One knowledge: ab % k = (a%k)(b%k)%k
Since the power here is an array, we'd better handle it digit by digit.
One observation:
a^1234567 % k = (a^1234560 % k) * (a^7 % k) % k = (a^123456 % k)^10 % k * (a^7 % k) % k
Looks complicated? Let me put it other way:
Suppose f(a, b) calculates a^b % k; Then translate above formula to using f :
f(a,1234567) = f(a, 1234560) * f(a, 7) % k = f(f(a, 123456),10) * f(a,7)%k;
Implementation of this idea:


# 3ms 88.11%
class Solution {
    private static final int MOD = 1337;

    public int superPow(int a, int[] b) {
        int result = 1;
        for (int i = b.length - 1; i >= 0; i--) {
            result = result * superPow(a, b[i]) % MOD;
            a = superPow(a, 10);
        }
        return result;
    }

    private int superPow(int a, int b) {
        int result = 1;
        a %= MOD;
        while (b > 0) {
            if ((b & 1) == 1) {
                result = result * a % MOD;
            }
            a = a * a % MOD;
            b >>= 1;
        }
        return result;
    }
}

1337 only has two divisors 7 and 191 exclusive 1 and itself,
so judge if a has a divisor of 7 or 191, and note that 7 and 191 are prime numbers,
phi of them is itself - 1, then we can use the Euler's theorem,
see it on wiki https://en.wikipedia.org/wiki/Euler's_theorem,
it's just Fermat's little theorem if the mod n is prime.

see how 1140 is calculated out:
phi(1337) = phi(7) * phi(191) = 6 * 190 = 1140

optimized solution update at 2016-7-12
Today, seeing @myanonymos 's comments, and I find several days ago I AC it just by fortunate coincidence,
it's not the best solution. now I get a better idea.

(1) Firstly, if a has both divisor 7 and 191, that's a % 1337 == 0, answer is 0.
(2) Then if a has neither divisor 7 nor 191, that's a and 1337 are coprime,
so ab % 1337 = ab % phi(1337) % 1337 = ab % 1140 % 1337.

(3) Finally, a could has either divisor 7 or 191, that's similar.
Let it be 7 for example.
Let a = 7nx
and let b = 1140p + q, where 0 < q <= 1140
then:

ab % 1337
= ((7nx)b) % 1337
= (7nbxb) % 1337
= ( (7nb % 1337) * (xb % 1337) ) % 1337
= ( (71140np + nq % 1337) * (x1140p + q % 1337) ) % 1337

now note x and 1337 are coprime, so

= ( (71140np + nq % 1337) * (xq % 1337) ) % 1337
= ( 7 * (71140np + nq - 1 % 191) * (xq % 1337) ) % 1337

note 7 and 191 are coprime too, and 1140 is a multiple of 190,
where 190 = phi(191).
What's more we should assure that q != 0, if b % 1140== 0, then let b = 1140. so

= ( 7 * (7nq - 1 % 191) * (xq % 1337) ) % 1337
= ( (7nq % 1337) * (xq % 1337) ) % 1337
= (7nqxq) % 1337
= ((7nx)q) % 1337
= (aq) % 1337

now you see condition (2) and (3) can be merged as one solution,
if you take care of when b % 1440 == 0, and let b += 1140. Actually (1) can be merged too, but not efficient.

# 1ms 100%
class Solution {
    public int superPow(int a, int[] b) {
        if (a % 1337 == 0) return 0;
        int p = 0;
        for (int i : b) p = (p * 10 + i) % 1140;
        if (p == 0) p += 1440;
        return power(a, p, 1337);
    }
    public int power(int a, int n, int mod) {
        a %= mod;
        int ret = 1;
        while (n != 0) {
            if ((n & 1) != 0) ret = ret * a % mod;
            a = a * a % mod;
            n >>= 1;
        }
        return ret;
    }
}

'''
