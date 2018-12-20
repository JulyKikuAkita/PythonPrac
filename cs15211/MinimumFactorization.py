__source__ = 'https://leetcode.com/problems/minimum-factorization/'
# Time:  O(8loga)
# Space: O(1)
#
# Description: 625. Minimum Factorization
#
# Given a positive integer a, find the smallest positive integer b whose multiplication of each digit equals to a.
#
# If there is no answer or the answer is not fit in 32-bit signed integer, then return 0.
#
# Example 1
# Input:
#
# 48
# Output:
# 68
# Example 2
# Input:
#
# 15
# Output:
# 35
# Hide Company Tags Tencent
# Hide Tags Recursion Math
#
import unittest

class Solution(object):
    pass  # your function here


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
Thought: https://leetcode.com/problems/minimum-factorization/solution/

# 7ms 44.55%
class Solution {
    public int smallestFactorization(int a) {
        if (a < 2)
            return a;
        long res = 0, mul = 1;
        for (int i = 9; i >= 2; i--) {
            while (a % i == 0) {
                a /= i;
                res = mul * i + res;
                mul *= 10;
            }
        }
        return a < 2 && res <= Integer.MAX_VALUE ? (int)res : 0;
    }
}

2.
# Thought: http://www.geeksforgeeks.org/find-smallest-number-whose-digits-multiply-given-number-n/
# 5ms 94.55%
class Solution {
    public int smallestFactorization(int n) {
        int i, j = 0;
        int MAX = 50;
        // To sore digits of result in reverse order
        int[] res = new int[MAX];

        // Case 1: If number is smaller than 10
        if (n < 10) return n;

        // Case 2: Start with 9 and try every possible digit
        for (i = 9; i > 1; i--) {
            // If current digit divides n, then store all
            // occurrences of current digit in res
            while ( n % i == 0) {
                n = n / i;
                res[j] = i;
                j++;
            }
        }

        // If n could not be broken in form of digits (prime factors of n
        // are greater than 9)
        if (n > 10) return 0;

        // Get the result array in reverse order
        long result = 0;
        for (i = j - 1; i >= 0; i--) {
            result = result * 10 + res[i];
            if (result > Integer.MAX_VALUE) return 0;
        }

        return result <= Integer.MAX_VALUE ? (int)result : 0;
    }
}

'''
