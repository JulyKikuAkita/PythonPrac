__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/divide-two-integers.py
# Time:  O(logn)
# Space: O(1)
# Math
#
# Divide two integers without using multiplication, division and mod operator.
# -> insead of dicidend -= divisor each cycle, do it with dichotomy
# Math Binary Search
import unittest
class Solution(unittest.TestCase):
    # @return an integer
    def divide(self, dividend, divisor):
        result, dvd, dvs = 0, abs(dividend), abs(divisor)

        while dvd >= dvs:
            inc = dvs
            i = 0
            while dvd >= inc:
                dvd -= inc
                result += 1 << i
                inc <<= 1
                i += 1
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            return - result
        else:
            return result if result < 0x7FFFFFFF else 0x7FFFFFFF


    def divide2(self, dividend, divisor):
        flag, ans = 0, 0
        if dividend < 0:
            flag, dividend = flag^1, -dividend
        if divisor < 0 :
            flag, divisor = flag^1, -divisor
        while dividend >= divisor:
            count, newDivisor = 1, divisor
            while newDivisor + newDivisor <= dividend:
                newDivisor += newDivisor
                count += count
                print count
            dividend -= newDivisor
            ans += count
        return ans if flag == 0 else -ans

    def test(self):
        self.assertEqual(2147483647, Solution().divide(2147483648, 1))
        self.assertEqual(2147483647, Solution().divide2(2147483648, 1))


if __name__ == "__main__":
    print Solution().divide(123, 12)
    print Solution().divide(123, -12)
    print Solution().divide(-123, 12)
    print Solution().divide(-123, -12)

#java
js = '''
public class Solution {
    public int divide(int dividend, int divisor) {
        if (divisor == 0 || (dividend == Integer.MIN_VALUE && divisor == -1)) {
            return Integer.MAX_VALUE;
        } else if (dividend == 0) {
            return 0;
        }
        long longDividend = Math.abs((long) dividend);
        long longDivisor = Math.abs((long) divisor);
        int result = 0;
        while (longDividend >= longDivisor) {
            int count = 1;
            long cur = longDivisor;
            while (cur << 1 <= longDividend) {
                cur <<= 1;
                count <<= 1;
            }
            result += count;
            longDividend -= cur;
        }
        return (dividend > 0 && divisor > 0) || (dividend < 0 && divisor < 0) ? result : -result;
    }
}
//import org.junit.*;
//Assert.assertEquals(2147483647, sol.divide(2147483648, 1));

'''