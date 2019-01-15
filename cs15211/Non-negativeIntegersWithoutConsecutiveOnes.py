__source__ = 'https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/'
# Time:  O(n)
# Space: O(n)
#
# Description: 600. Non-negative Integers without Consecutive Ones
#
# Given a positive integer n, find the number of non-negative integers less than or equal to n,
# whose binary representations do NOT contain consecutive ones.
#
# Example 1:
# Input: 5
# Output: 5
# Explanation:
# Here are the non-negative integers <= 5 with their corresponding binary representations:
# 0 : 0
# 1 : 1
# 2 : 10
# 3 : 11
# 4 : 100
# 5 : 101
# Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule.
# Note: 1 <= n <= 109
#
# Hide Company Tags Pocket Gems
# Hide Tags Dynamic Programming
# Hide Similar Problems (E) House Robber (M) House Robber II (M) Ones and Zeroes
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
# Thought: https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/solution/
Reference: http://www.geeksforgeeks.org/count-number-binary-strings-without-consecutive-1s/

# 19ms 32.79%
class Solution {
    public int findIntegers(int num) {
        StringBuilder sb = new StringBuilder(Integer.toBinaryString(num)).reverse();
        int n = sb.length();

        int a[] = new int[n];
        int b[] = new int[n];
        a[0] = b[0] = 1;
        for (int i = 1; i < n; i++) {
            a[i] = a[i - 1] + b[i - 1];
            b[i] = a[i - 1];
        }

        int result = a[n - 1] + b[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            if (sb.charAt(i) == '1' && sb.charAt(i + 1) == '1') break;
            if (sb.charAt(i) == '0' && sb.charAt(i + 1) == '0') result -= b[i];
        }

        return result;
    }
}
'''
