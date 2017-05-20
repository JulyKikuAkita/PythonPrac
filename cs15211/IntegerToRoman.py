__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/integer-to-roman.py
# Time:  O(n)
# Space: O(1)
# Math
#
# Given an integer, convert it to a roman numeral.
#
# Input is guaranteed to be within the range from 1 to 3999.
#


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


if __name__ == "__main__":
    print Solution().intToRoman(79)
    #print Solution().intToRoman(999)
    #print Solution().intToRoman(3999)



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


t1=SolutionOther()
#print t1.romanToInt("MCMXCVI")  #1996
#print t1.intToRoman(1996)

#java
js = '''
public class Solution {
    public String intToRoman(int num) {
        if(num > 3999 || num < 1) return "";
        int[] integers = new int[] {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] roman = new String[] {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        StringBuilder sb = new StringBuilder();
        int index = 0;

        while(num > 0){
            while(num >= integers[index]){
                sb.append(roman[index]);
                num -= integers[index];
            }
            index += 1;
        }
        return sb.toString();


    }
}
'''