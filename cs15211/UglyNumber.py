__source__ = 'https://leetcode.com/problems/ugly-number/#/solutions'
# https://github.com/kamyu104/LeetCode/blob/master/Python/ugly-number.py
# Time:  O(logn)
# Space: O(1)
#
# Description: Leetcode # 263. Ugly Number
#
# Write a program to check whether a given number is an ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include
# 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it
# includes another prime factor 7.
#
# Note that 1 is typically treated as an ugly number.
#
# Related Topics
# Math
# Similar Questions
# Happy Number Count Primes Ugly Number II
#
import unittest
class Solution:
    # @param {integer} num
    # @return {boolean}
    def isUgly(self, num):
        if num == 0:
            return False
        for i in [2,3,5]:
            while num % i == 0:
                num /= i
        return num == 1

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#13.15% 2ms
public class Solution {
    public boolean isUgly(int num) {
        if(num < 1) return false;
        while (num % 2 == 0) num = num >>> 1;
        while (num % 3 == 0) num = num / 3;
        while (num % 5 == 0) num = num / 5;
        return num == 1;
    }
}

#13.15% 2ms
public class Solution {
    public boolean isUgly(int num) {
        if (num <= 0) {
            return false;
        }
        num = removeFactor(num, 2);
        num = removeFactor(num, 3);
        num = removeFactor(num, 5);
        return num == 1;
    }

    private int removeFactor(int num, int factor) {
        while (num % factor == 0) {
            num /= factor;
        }
        return num;
    }
}
'''