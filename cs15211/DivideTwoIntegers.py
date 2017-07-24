__source__ = 'https://leetcode.com/problems/divide-two-integers/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/divide-two-integers.py
# Time:  O(logn)
# Space: O(1)
# Math
#
# Description: Leetcode # 29. Divide Two Integers
#
# Divide two integers without using multiplication, division and mod operator.
# If it is overflow, return MAX_INT.
# -> insead of dicidend -= divisor each cycle, do it with dichotomy
# Related Topics
# Math Binary Search
#
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

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().divide(123, 12)
        print Solution().divide(123, -12)
        print Solution().divide(-123, 12)
        print Solution().divide(-123, -12)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
Let's do an example and see how bit manipulations work.

Suppose we want to divide 15 by 3, so 15 is dividend and 3 is divisor.
Well, division simply requires us to find how many times we can subtract the divisor from the the dividend
without making the dividend negative.

Let's get started. We subtract 3 from 15 and we get 12, which is positive. Let's try to subtract more.
Well, we shift 3 to the left by 1 bit and we get 6. Subtracting 6 from 15 still gives a positive result.
Well, we shift again and get 12. We subtract 12 from 15 and it is still positive.
We shift again, obtaining 24 and we know we can at most subtract 12.
Well, since 12 is obtained by shifting 3 to left twice, we know it is 4 times of 3.
How do we obtain this 4? Well, we start from 1 and shift it to left twice at the same time.
We add 4 to an answer (initialized to be 0). In fact, the above process is like 15 = 3 * 4 + 3.
We now get part of the quotient (4), with a remainder 3.

Then we repeat the above process again. We subtract divisor = 3 from the remaining dividend = 3 and obtain 0.
We know we are done. No shift happens, so we simply add 1 << 0 to the answer.

Now we have the full algorithm to perform division.

According to the problem statement, we need to handle some exceptions, such as overflow.

Well, two cases may cause overflow:

divisor = 0;
dividend = INT_MIN and divisor = -1 (because abs(INT_MIN) = INT_MAX + 1).
Of course, we also need to take the sign into considerations, which is relatively easy.

#16.45% 48ms
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

# 53.48% 40ms
public class Solution {
    public int divide(int dividend, int divisor) {
        if(dividend == -2147483648 && divisor == -1) {
            return 2147483647;
        }
        int result = 0;
        long a = Math.abs((long)dividend);
        long b = Math.abs((long)divisor);
        while(a >= b) {
            int n = 1;
            while(a >= (b << n)) {
                n++;
            }
            n--;
            a = a - (b << n);
            if(n > 31) return Integer.MAX_VALUE;
            result = result + (1 << n);
        }
        if((dividend > 0 && divisor < 0) || (dividend < 0 && divisor > 0))
        {
            result = -result;
        }
        return result;
    }
}

'''