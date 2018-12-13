__source__ = 'https://leetcode.com/problems/happy-number/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/happy-number.py
# Time:  O(k), where k is the steps to be happy number
# Space: O(k)
#
# Description: Leetcode # 202. Happy Number
#
# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum
# of the squares of its digits, and repeat the process until
# the number equals 1 (where it will stay), or it loops endlessly
# in a cycle which does not include 1. Those numbers for which
# this process ends in 1 are happy numbers.
#
# Example: 19 is a happy number
#
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
#
# Companies
# Uber Airbnb Twitter
# Related Topics
# Hash Table Math
# Similar Questions
# Add Digits Ugly Number
#
import unittest
class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        dict = {}
        while n != 1 and n not in dict:
            dict[n] = True
            n = self.nextNumber(n)
        return n == 1

    def nextNumber(self, n):
        new = 0
        for char in str(n):
            new += int(char) ** 2
        return new

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
non-happy number will definitely generate a loop

# 2ms 76.39%
class Solution {
    public boolean isHappy(int n) {
        Set<Integer> cache = new HashSet<>();
        cache.add(n);
        while (n > 0) {
            n = getNextHappyNumber(n);
            if (n == 1) {
                return true;
            } else if (cache.contains(n)) {
                return false;
            } else {
                cache.add(n);
            }
        }
        return false;
    }

    private int getNextHappyNumber(int n) {
        int result = 0;
        while (n > 0) {
            int cur = n % 10;
            result += cur * cur;
            n /= 10;
        }
        return result;
    }
}

# 1ms 97.75%
class Solution {
    public boolean isHappy(int n) {
        Set<Integer> set = new HashSet<Integer>();
        int squareSum, remain;
        while( set.add(n) ) {
            squareSum = 0;
            while (n > 0) {
                remain = n % 10;
                squareSum +=  remain * remain;
                n /= 10;
            }
            if (squareSum == 1) return true;
            else n = squareSum;
        }
        return false;
    }
}

# 1ms 97.75%
class Solution {
    public boolean isHappy(int n) {
        int slow = n, fast = n;
        do {
            slow = getSquareSum(slow);
            fast = getSquareSum(getSquareSum(fast));
        } while (slow != fast);
        return slow == 1;
    }

    private int getSquareSum(int n) {
        int squareSum = 0, remain = 0;
        while (n > 0) {
            remain = n % 10;
            squareSum += remain * remain;
            n /= 10;
        }
        return squareSum;
    }
}
'''