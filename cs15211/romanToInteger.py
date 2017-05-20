__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/roman-to-integer.py
# Time:  O(n)
# Space: O(1)
# Math
#
# Given a roman numeral, convert it to an integer.
#
# Input is guaranteed to be within the xrange from 1 to 3999.
#

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

if __name__ == "__main__":
    print Solution().romanToInt("IIVX")
    print Solution().romanToInt("MMMCMXCIX")
    print Solution().romanToInt("MCMXCVI")  #1996


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


t1=SolutionOther()
#print t1.romanToInt("MCMXCVI")  #1996
#print t1.intToRoman(1996)