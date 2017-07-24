__source__ = 'https://leetcode.com/problems/powx-n/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/powx-n.py
# Time:  O(logn)
# Space: O(logn)
# Binary Search
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




if __name__ == "__main__":
    print Solution().pow(2, 3)
    print Solution().pow(3, 5)
    print Solution().pow(3, -5)



#Java
# http://algobox.org/powx-n/
Java = '''


#what if n == -2147483648

#62.64% 20ms # divide and conquer
public class Solution {
    public double myPow(double x, int n) {
        if (n >=0) return positiveMyPow(x, n);
        else return 1/positiveMyPow(x, n);
    }

    public double positiveMyPow(double x, int n) {
        if (n==0) return 1;
        double tmp = positiveMyPow(x, n/2);
        if (n%2 == 0) return tmp * tmp;
        else {
            return tmp * tmp * x;
        }
    }
}

Iteration:
N = 9 = 2^3 + 2^0 = 1001 in binary. Then:

x^9 = x^(2^3) * x^(2^0)

We can see that every time we encounter a 1 in the binary representation of N,
we need to multiply the answer with x^(2^i) where i is the ith bit of the exponent.
Thus, we can keep a running total of repeatedly squaring x - (x, x^2, x^4, x^8, etc)
and multiply it by the answer when we see a 1.

To handle the case where N=INTEGER_MIN we use a long (64-bit) variable. Below is solution:
#33% 22ms
public class Solution {
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

'''
