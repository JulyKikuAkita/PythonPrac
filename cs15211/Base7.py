__source__ = 'https://leetcode.com/problems/base-7/#/description'
# Time:  O(n)
# Space: O()
#
# Description: 504. Base 7
#
# Given an integer, return its base 7 string representation.
#
# Example 1:
# Input: 100
# Output: "202"
# Example 2:
# Input: -7
# Output: "-10"
# Note: The input will be in range of [-1e7, 1e7].

import unittest
# 20ms 100%
class Solution(object):
    def convertToBase7(self, num):
        if num < 0: return '-' + self.convertToBase7(-num)
        if num < 7: return str(num)
        return self.convertToBase7(num / 7) + str(num % 7)
    def convertToBase7_2(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        n, res = abs(num), ''
        while n:
            res = str(n % 7) + res
            n //= 7
        return res if num > 0 else '-' + res


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: Just keep dividing the current number by 7...

# 6ms 100%
class Solution {
    public String convertToBase7(int num) {
        if ( num < 0) return '-' + convertToBase7(-num);
        if ( num < 7) return num + "";
        return convertToBase7(num / 7) + num % 7;
    }
}

# 7ms 99.13%
public class Solution {
    public String convertTo7(int num) {
        if (num == 0) return "0";

        StringBuilder sb = new StringBuilder();
        boolean negative = false;

        if (num < 0) {
            negative = true;
        }
        while (num != 0) {
            sb.append(Math.abs(num % 7));
            num = num / 7;
        }

        if (negative) {
            sb.append("-");
        }

        return sb.reverse().toString();
    }
}
'''