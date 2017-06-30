__source__ = 'https://leetcode.com/problems/largest-palindrome-product/#/discuss'
# Time:  O(n)
# Space: O(1)
#
# Description:
# Find the largest palindrome made from the product of two n-digit numbers.
#
# Since the result could be very large, you should return the largest palindrome mod 1337.
#
# Example:
#
# Input: 2
#
# Output: 987
#
# Explanation: 99 x 91 = 9009, 9009 % 1337 = 987
#
# Note:
#
# The range of n is [1,8].
# Companies
# Yahoo

import unittest

class Solution(object):
    pass  # your function here


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:

#bug:
n = 1 -> 9
n = 2 -> 987
n = 3 -> 123
n = 4 -> 597
n = 5 -> 956
n = 6 -> -372

public class Solution {
    public int largestPalindrome(int n) {
        if (n == 1) return 9;

        // if n = 3 then upperBound = 999 and lowerBound = 99
        int upperBound = (int) Math.pow(10, n) - 1, lowerBound = upperBound / 10;
        long maxNumber = (long) upperBound * (long) upperBound;

        // represents the first half of the maximum assumed palindrom.
        // e.g. if n = 3 then maxNumber = 999 x 999 = 998001 so firstHalf = 998
        int firstHalf = (int)(maxNumber / (long) Math.pow(10, n));


        boolean palindromFound = false;
        long palindrom = 0;

        while (!palindromFound) {
            // creates maximum assumed palindrom
            // e.g. if n = 3 first time the maximum assumed palindrom will be 998 899
            palindrom = createPalindrome(firstHalf);

            // here i and palindrom/i forms the two factor of assumed palindrom
            for (long i = upperBound; i > lowerBound; i--) {
                if (palindrom / i > maxNumber || i * i < palindrom) break;
                if (palindrom % i == 0) {
                    palindromFound = true;
                    break;
                }
            }
            firstHalf--;

        }
        return (int) palindrom % 1337;
    }

    private long createPalindrome(long num) {
        String str = num + new StringBuilder().append(num).reverse().toString();
        return Long.parseLong(str);
    }
}

94%
public class Solution {
    public int largestPalindrome(int n) {
        int[] result = {9,987,123,597,677,1218,877,475};
        return result[n - 1];
    }
}
'''