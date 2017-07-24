__source__ = 'https://leetcode.com/problems/reverse-integer/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/reverse-integer.py
# Time: O(logn)
# Space: O(1)
#
# Description: Leetcode # 7. Reverse Integer
# Reverse digits of an integer.
#
# Example1: x = 123, return 321
# Example2: x = -123, return -321
#
# click to show spoilers.
#
# Have you thought about this?
# Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!
#
# If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.
#
# Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer,
# then the reverse of 1000000003 overflows. How should you handle such cases?
#
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
#
# Note:
# The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
#
# Companies
# Bloomberg Apple
# Related Topics
# Math
# Similar Questions
# String to Integer (atoi)
#
import unittest
class Solution:
    # @return an integer
    def reverse(self, x):
        ans = 0
        if x >= 0:
            while x:
                ans = ans * 10 + x % 10
                x /= 10
            return ans if ans <= 2147483647 else 0  # Handle overflow.
        else:
            return -self.reverse(-x)

class Solution2(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        overflow = (1 << 31) # unsigned int 2^31 -1
        neg = False
        if x < 0:
            neg = True
            x *= -1

        if x>0xFFFFFFFF:
            return 0

        ans = 0
        while x:
            ans *= 10
            if ans + (x % 10) > overflow:
                return 0

            ans += x % 10
            x /= 10

        if neg:
            ans *= -1
        return ans


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().reverse(123)
        print Solution().reverse(-321)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/contains-duplicate/solution/
# 48.90% 42ms
public class Solution {
    public int reverse(int x) {
        long num = x;
        long result = 0;
        while (num != 0) {
            result = result * 10 + num % 10;
            num /= 10;
        }
        if (result > Integer.MAX_VALUE || result < Integer.MIN_VALUE) {
            return 0;
        } else {
            return (int) result;
        }
    }
}

#42.91% 43ms
public class Solution {
    public int reverse(int x) {
        long num = Math.abs((long) x);
        long result = 0;
        while (num > 0) {
            result = result * 10 + num % 10;
            num /= 10;
        }
        result = x >= 0 ? result : -result;
        return result == (int) result ? (int) result : 0;
    }
}

#42.91% 43ms
public class Solution {
    public int reverse(int x) {
        int reversed_n = 0;

        while (x != 0) {
            int temp = reversed_n * 10 + x % 10;
            x = x / 10;
            if (temp / 10 != reversed_n) {
                reversed_n = 0;
                break;
            }
            reversed_n = temp;
        }
        return reversed_n;
    }
}

#63.27% 40ms
// no type change for overflow
public class Solution {
    public int reverse(int x) {
        int res = 0;
        int orig = Math.abs(x);
        while ( orig > 0 ) {
            int tail = orig % 10;
            int cur = res * 10 + tail;
            if ((cur - tail) / 10 != res) { //overflow
                return 0;
            }
            res = cur;
            orig /= 10;
        }
        return x < 0 ? -res : res;
    }
}
'''