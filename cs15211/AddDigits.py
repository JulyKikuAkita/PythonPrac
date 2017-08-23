__source__ = 'https://leetcode.com/problems/add-digits/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/add-digits.py
# Time:  O(1)
# Space: O(1)
#
# Description: Leetcode # 258. Add Digits
#
# Given a non-negative integer num, repeatedly add
# all its digits until the result has only one digit.
#
# For example:
#
# Given num = 38, the process is like: 3 + 8 = 11,
# 1 + 1 = 2. Since 2 has only one digit, return it.
#
# Follow up:
# Could you do it without any loop/recursion in O(1)
# runtime?
#
# Hint:
# A naive implementation of the above process is trivial.
# Could you come up with other methods?
#
# Companies
# Adobe Microsoft
# Related Topics
# Math
# Similar Questions
# Happy Number
#
import unittest
class Solution:
    # @param {integer} num
    # @return {integer}
    def addDigits(self, num):
        return (num - 1) % 9 + 1 if num > 0 else 0

# Time:  O(1)
# Space: O(1)
class Solution2:
    # @param {integer} num
    # @return {integer}
    def addDigits(self, num):
        return self.addDigitsRecu(num, 0)

    def addDigitsRecu(self, num, tmp):
        if num <= 9:
            return num

        while num > 0:
            tmp += num % 10
            num /= 10
        #print tmp, num
        return self.addDigitsRecu(tmp, 0)

#Test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        print Solution().addDigits(38)
        print Solution2().addDigits(38)

if __name__ == '__main__':
    unittest.main()

Java = '''
# 15.47% 2ms
public class Solution {
    public int addDigits(int num) {
        return num == 0 ? 0 : (num - 1) % 9 + 1;
    }
}

# 15.47% 2ms
public class Solution {
    public int addDigits(int num) {
        if (num == 0) return 0;
        return ( num % 9 == 0) ? 9: num % 9;
    }
}

# 15.47% 2ms
public class Solution {
    public int addDigits(int num) {
        if (num / 10 == 0) return num;
        int res = 0;
        while (num != 0) {
            res += num % 10;
            num /= 10;
        }
        return addDigits(res);
    }
}
'''