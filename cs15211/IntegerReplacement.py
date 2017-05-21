__source__ = 'https://github.com/kamyu104/LeetCode/blob/master/Python/integer-replacement.py'
# Time:  O(logn)
# Space: O(1)

# Given a positive integer n and you can do operations as follow:
#
# If n is even, replace n with n/2.
# If n is odd, you can replace n with either n + 1 or n - 1.
# What is the minimum number of replacements needed for n to become 1?
#
# Example 1:
#
# Input:
# 8
#
# Output:
# 3
#
# Explanation:
# 8 -> 4 -> 2 -> 1
# Example 2:
#
# Input:
# 7
#
# Output:
# 4
#
# Explanation:
# 7 -> 8 -> 4 -> 2 -> 1
# or
# 7 -> 6 -> 3 -> 2 -> 1
#
#  Google Baidu
# Hide Tags Math Bit Manipulation

import unittest
# Iterative solution.
class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n != 1:
            b = n & 3
            if n == 3:
                n -= 1
            elif b == 3:
                n += 1
            elif b == 1:
                n -= 1
            else:
                n /= 2
            result += 1

        return result


# Time:  O(logn)
# Space: O(logn)
# Recursive solution.
class Solution2(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            return [0, 0, 1, 2][n]
        if n % 4 in (0, 2):
            return self.integerReplacement(n / 2) + 1
        elif n % 4 == 1:
            return self.integerReplacement((n - 1) / 4) + 3
        else:
            return self.integerReplacement((n + 1) / 4) + 3


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
1. Bit manipulation
The first step towards solution is to realize that you're allowed to remove the LSB only if it's zero.
And to reach the target as fast as possible, removing digits is the best way to go.
Hence, even numbers are better than odd. This is quite obvious.

What is not so obvious is what to do with odd numbers.
One may think that you just need to remove as many 1's as possible
to increase the evenness of the number. Wrong! Look at this example:

111011 -> 111010 -> 11101 -> 11100 -> 1110 -> 111 -> 1000 -> 100 -> 10 -> 1
And yet, this is not the best way because

111011 -> 111100 -> 11110 -> 1111 -> 10000 -> 1000 -> 100 -> 10 -> 1
See? Both 111011 -> 111010 and 111011 -> 111100 remove the same number of 1's, but the second way is better.

So, we just need to remove as many 1's as possible, doing +1 in case of a tie?
Not quite. The infamous test with n=3 fails for that strategy because 11 -> 10 -> 1 is better than 11 -> 100 -> 10 -> 1.
Fortunately, that's the only exception (or at least I can't think of any other, and there are none in the tests).

So the logic is:

If n is even, halve it.
If n=3 or n-1 has less 1's than n+1, decrement n.
Otherwise, increment n.

Use long to avoid overflow (if n is Integer.MAX_VALUE).

public class Solution {
    public int integerReplacement(int n) {
        int c = 0;
        while (n != 1) {
            if ((n & 1) == 0) {
                n >>>= 1;
            } else if (n == 3 || Integer.bitCount(n + 1) > Integer.bitCount(n - 1)) {
                --n;
            } else {
                ++n;
            }
            ++c;
        }
    return c;
    }
}

Of course, doing bitCount on every iteration is not the best way.
It is enough to examine the last two digits to figure out whether incrementing or decrementing will give more 1's.
Indeed, if a number ends with 01, then certainly decrementing is the way to go. Otherwise,
if it ends with 11, then certainly incrementing is at least as good as decrementing (*011 -> *010 / *100)
or even better (if there are three or more 1's). This leads to the following solution:

public class Solution {
     public int integerReplacement2(int n) {
        int c = 0;
        while (n != 1) {
            if ((n & 1) == 0) {
                n >>>= 1;
            } else if (n == 3 || ((n >>> 1) & 1) == 0) {
                --n;
            } else {
                ++n;
            }
            ++c;
        }
        return c;
    }
}

'''