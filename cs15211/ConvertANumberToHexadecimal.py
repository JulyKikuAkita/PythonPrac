__source__ = 'https://github.com/kamyu104/LeetCode/blob/master/Python/convert-a-number-to-hexadecimal.py'
# Time:  O(logn)
# Space: O(1)
#
# Description:
# Given an integer, write an algorithm to convert it to hexadecimal.
# For negative integer, two’s complement method is used.
#
# IMPORTANT:
# You must not use any method provided by the library which converts/formats
# the number to hex directly. Such solution will result in disqualification of
# all your submissions to this problem. Users may report such solutions after the
# contest ends and we reserve the right of final decision and interpretation
# in the case of reported solutions.
#
# Note:
#
# All letters in hexadecimal (a-f) must be in lowercase.
# The hexadecimal string must not contain extra leading 0s. If the number is zero,
# it is represented by a single zero character '0'; otherwise,
# the first character in the hexadecimal string will not be the zero character.
# The given number is guaranteed to fit within the range of a 32-bit signed integer.
# You must not use any method provided by the library which converts/formats the number to hex directly.
# Example 1:
#
# Input:
# 26
#
# Output:
# "1a"
# Example 2:
#
# Input:
# -1
#
# Output:
# "ffffffff"
#  Bit Manipulation

import unittest
class Solution(object):
    def toHex(self, num):
        return ''.join('0123456789abcdef'[(num >> 4 * i) & 15]
                        for i in range(8)
                        )[::-1].lstrip('0') or '0'
    def toHex2(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return "0"

        res = []
        while num and len(res) != 8:
            h = num & 15
            if h < 10:
                res.append(str(chr(ord('0') + h)))
            else:
                res.append(str(chr(ord('a') + h - 10)))
            num >>= 4
        res.reverse()
        return "".join(res)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# https://ratchapong.com/algorithm-practice/leetcode/convert-a-number-to-hexadecimal
#Thought: each time we take a look at the last four digits of
            binary verion of the input, and maps that to a hex char
            shift the input to the right by 4 bits, do it again
            until input becomes 0.

public class Solution {
    public String toHex(int num) {
        if (num == 0) return "0";
        char[] map = new char[]{'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'};
        StringBuilder sb = new StringBuilder();
        while (num != 0) {
            sb.insert(0, map[num & 0b1111]);
            num = num >>> 4;
        }
        return sb.toString();
    }
}
Worst Case
O(logb(n)) : With respect to the input, the algorithm will always depend on the size of input.
The extra space is needed to store the equivalent string of base 16

Approach: Shifting and Masking
Number is masked against binary of 1111 each time to get the component value
which is then mapped to corresponding character. >>> is used to right-shifted
4
4 bit positions with zero-extension. The zero-extension will naturally deal with negative number.
StringBuilder is used due to its efficiently in inserting character to existing StringBuilder object.
If normal String is used then each insertion by + operation
will have to copy over the immutable String object which is highly inefficient.
For Integer.MAX_VALUE or Integer.MIN_VALUE or any input
with 8 Hexadecimal characters where the iterations would last the longest.
For Integer.MAX_VALUE the algorithm will run for at most log base16 (2^31 - 1) +1 = 8 times


public class Solution {
    public String toHex(int num) {
        long n = num & 0x00000000ffffffffL;
        char[] map = new char[]{'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'};
        StringBuilder sb = new StringBuilder();
        while (n > 0) {
            sb.insert(0, map[(int) (n % 16)]);
            n = n / 16;
        }
        return num == 0 ? "0" : sb.toString();
    }
}

Worst Case
O(logb(n)) : With respect to the input, the algorithm will always depend on the size of input.
The extra space is needed to store the equivalent string of base 16.
Approach: Divide and Modding
To deal with negative number, the number is masked against long data type.
This process will convert it to a positive long number.
A simple while loop is then use to extract each base digit until number becomes 0.

'''