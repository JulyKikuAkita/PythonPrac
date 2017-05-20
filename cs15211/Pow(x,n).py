__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/powx-n.py
# Time:  O(logn)
# Space: O(logn)
# Binary Search
#
# Implement pow(x, n).
#
# LinkedIn Google Bloomberg Facebook
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
js = '''
#what if n == -2147483648
public class Solution {
    public double myPow(double x, int n) {
        if (n >= 0) {
            return myPowPositive(x, n);
        } else {
            return 1 / myPowPositive(x, -n);
        }
    }

    private double myPowPositive(double x, int n) {
        if (n == 0) {
            return 1;
        }
        double half = myPowPositive(x, n / 2);
        if ((n & 1) == 0) {
            return half * half;
        } else {
            return half * half * x;
        }
    }
}

public class Solution2 {
    public double myPow(double x, int n) {
        double ans = 1.0;
        for(long m = n > 0 ? n: -(long)n ; m != 0 ; m >>= 1){
            if ( (m & 1) == 1){
                ans *= x;
            }
            x *= x;
        }
        return n >= 0 ? ans : 1 / ans;
    }
}
'''
