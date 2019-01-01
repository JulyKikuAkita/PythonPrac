__source__ = 'https://leetcode.com/problems/powx-n/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/powx-n.py
# Time:  O(logn)
# Space: O(logn)
# Binary Search
#
# Description: Leetcode # 50. Pow(x, n)
#
# Implement pow(x, n).
#
# Companies
# LinkedIn Google Bloomberg Facebook
# Related Topics
# Binary Search Math
# Similar Questions
# Sqrt(x) Super Pow
#
import unittest
class Solution(unittest.TestCase):
    # @param x, a float
    # @param n, a integer
    # @return a float
    def myPowInteration(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        m = abs(n)
        ans = 1.0
        while m :
            if m & 1 == 1:
                ans *= x
            x *= x
            m >>= 1
        return ans if n > 0 else 1 / ans

    def pow(self, x, n):
        if n < 0:
            return 1 / self.powRecu(x, -n)

        return self.powRecu(x, n)

    def powRecu(self, x, n):
        if n == 0:
            return 1.0
        if n % 2 == 0:
            return self.powRecu(x * x, n /2)
        else:
            return x * self.powRecu(x * x, n /2)

    def test(self):
        self.assertEqual(8, self.pow(2, 3))
        self.assertEqual(1.00000, self.myPowInteration(1.00000, -2147483648 ))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        print Solution().pow(2, 3)
        print Solution().pow(3, 5)
        print Solution().pow(3, -5)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/powx-n/solution/

# http://algobox.org/powx-n/
# what if n == -2147483648

# divide and conquer
# 12ms 53.60%
class Solution {
    public double myPow(double x, int n) {
        if (n >= 0) return positiveMyPow(x, n);
        else return 1 / positiveMyPow(x, n);
    }

    public double positiveMyPow(double x, int n) {
        if (n == 0) return 1;
        double tmp = positiveMyPow(x, n / 2);
        if (n % 2 == 0) return tmp * tmp;
        else return x * tmp * tmp;
    }
}

# Iteration:
# N = 9 = 2^3 + 2^0 = 1001 in binary. Then:
# x^9 = x^(2^3) * x^(2^0)
# 9ms 80.93%
class Solution {
    public double myPow(double x, int n) {
        long N = n;
        if (N < 0) {
            N = -N;
            x = 1 / x;
        }
        
        double ans = 1;
        double cur = x;
        for (long i = N; i > 0; i /= 2) {
            if (i % 2 == 1) ans = ans * cur;
            cur = cur * cur;
        }
        return ans;
    }
}

We can see that every time we encounter a 1 in the binary representation of N,
we need to multiply the answer with x^(2^i) where i is the ith bit of the exponent.
Thus, we can keep a running total of repeatedly squaring x - (x, x^2, x^4, x^8, etc)
and multiply it by the answer when we see a 1.

To handle the case where N=INTEGER_MIN we use a long (64-bit) variable. Below is solution:
# 13ms 33.33%
class Solution {
    public double myPow(double x, int n) {
        double ans = 1;
        long absN = (long) n;
        if ( absN < 0 ) absN = -absN;

        while (absN > 0) {
            if( (absN & 1) == 1 ) ans *= x;
            absN >>= 1;
            x *= x;
        }
        return n < 0 ?  1 / ans : ans;
    }
}

# 9ms 79.23%
class Solution {
    public double myPow(double x, int n) {
        return Math.pow(x, n);
    }
}
'''
