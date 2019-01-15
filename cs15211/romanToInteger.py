__source__ = 'https://leetcode.com/problems/roman-to-integer/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/roman-to-integer.py
# Time:  O(n)
# Space: O(1)
# Math
#
# Description: Leetcode # 13. Roman to Integer
#
# Given a roman numeral, convert it to an integer.
#
# Input is guaranteed to be within the xrange from 1 to 3999.
#
# Companies
# Microsoft Bloomberg Uber Facebook Yahoo
# Related Topics
# Math String
# Similar Questions
# Integer to Roman
#
import unittest
class Solution:
    # @return an integer
    def romanToInt(self, s):
        numeral_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M": 1000}
        ans = 0
        for i in xrange(len(s)):
            ans += numeral_map[s[i]]
            if i > 0 and numeral_map[s[i]] > numeral_map[s[i-1]]:
                ans -= 2*(numeral_map[s[i-1]])
        return ans

class SolutionOther:
    # @return an integer
    def romanToInt(self, s):
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        answer =0
        for i in range(len(s)):
            if i+1 < len(s) and roman[s[i]] < roman[s[i+1]] :
                answer -= roman[s[i]]
                #print "-", s[i], answer, i, len(s)
            else:
                answer += roman[s[i]]
                #print "+", s[i], answer,  i, len(s)

        return answer

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
        print Solution().containsDuplicate([12344555,12344555])
        print Solution().romanToInt("IIVX")
        print Solution().romanToInt("MMMCMXCIX")
        print Solution().romanToInt("MCMXCVI")  #1996
        #print t1.romanToInt("MCMXCVI")  #1996
        #print t1.intToRoman(1996)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: 

# 53ms 56.20%
class Solution {
    public static final Map<Character, Integer> ROMAN_MAP;
    static {
        Map<Character, Integer> map = new HashMap<>();
        map.put('M', 1000);
        map.put('D', 500);
        map.put('C', 100);
        map.put('L', 50);
        map.put('X', 10);
        map.put('V', 5);
        map.put('I', 1);
        ROMAN_MAP = Collections.unmodifiableMap(map);
    }

    public int romanToInt(String s) {
        int result = 0;
        char[] arr = s.toCharArray();
        if (arr.length == 0) {
            return 0;
        }
        int prev = Integer.MAX_VALUE;
        int cur = 0;
        for (int i = 0; i < arr.length; i++) {
            cur = ROMAN_MAP.get(arr[i]);
            if (cur > prev) {
                result = result - (prev << 1) + cur;
            } else {
                result += cur;
            }
            prev = cur;
        }
        return result;
    }
}


# 40ms 88.14%
class Solution {
    public int romanToInt(String s) {
        char[] sc = s.toCharArray();
        int sum = 0;
        for (int index = sc.length - 1; index >= 0; index--) {
            if (sc[index] == 'I') {
                sum += (sum < 5 ? 1 : -1);
            } else if (sc[index] == 'V') {
                sum += 5;
            } else if (sc[index] == 'X') {
                sum += (sum < 50 ? 10 : -10);
            } else if (sc[index] == 'L') {
                sum += 50;
            } else if (sc[index] == 'C') {
                sum += (sum < 500 ? 100 : -100);
            } else if (sc[index] == 'D') {
                sum += 500;
            } else if (sc[index] == 'M') {
                sum += 1000;
            }
        }
        return sum;
    }
}
'''
