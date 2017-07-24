__source__ = 'https://leetcode.com/problems/integer-to-roman/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/integer-to-roman.py
# Time:  O(n)
# Space: O(1)
# Math
#
# Description: Leetcode # 12. Integer to Roman
# Given an integer, convert it to a roman numeral.
#
# Input is guaranteed to be within the range from 1 to 3999.
# Companies
# Twitter
# Related Topics
# Math String
# Similar Questions
# Roman to Integer Integer to English Words

import unittest
class Solution:
    # @return a string
    def intToRoman(self, num):
        numeral_map = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
        keyset, result = sorted(numeral_map.keys()), ""

        while num > 0:
            for key in reversed(keyset):
                while num/key:
                    result += numeral_map[key]
                    num -= key

        return result

class SolutionOther:
    def intToRoman(self, num):
        ronum  = [['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
                  ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
                  ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
                  ['', 'M', 'MM', 'MMM', '  ', ' ', '  ', '   ', '    ', '  ']]
        ans, ind = '', 0
        while num:
            ans = ronum[ind][num%10] + ans
            #print ronum[ind][num%10], ans, num
            num, ind = num / 10, ind + 1

        return ans


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().intToRoman(79)
        #print Solution().intToRoman(999)
        #print Solution().intToRoman(3999)
        #print t1.intToRoman(1996)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/integer-to-roman/solution/

# 35.72% 105ms
# Rrecursion
public class Solution {
    public static final int[] intDict = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    public static final String[] romanDict = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

    /**
     * Recursion
     * Go through the dict, if num >= dict, insert it to head
     * Pass rest of the integer to next recursion
     */
    public String intToRoman(int num) {
        for (int i = 0; i < intDict.length; i++) {
            if (intDict[i] <= num) {
                return romanDict[i] + intToRoman(num - intDict[i]);
            }
        }
        return ""; // Note the return statement
    }
}

# 99.81% 80ms
public class Solution {
    private static final String[] ROMAN = new String[]{"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
    private static final int[] INTEGERS = new int[]{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};

    public String intToRoman(int num) {
        StringBuilder sb = new StringBuilder();
        int index = 0;
        while (num > 0) {
            while (num >= INTEGERS[index]) {
                sb.append(ROMAN[index]);
                num -= INTEGERS[index];
            }
            index++;
        }
        return sb.toString();
    }
}

'''