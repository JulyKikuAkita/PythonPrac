__source__ = 'https://leetcode.com/problems/integer-to-english-words/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/integer-to-english-words.py
# Time:  O(logn), n is the value of the integer
# Space: O(1)
#
# Description: Leetcode # 273. Integer to English Words
#
# Convert a non-negative integer to its english words representation.
# Given input is guaranteed to be less than 2^31 - 1.
#
# For example,
# 123 -> "One Hundred Twenty Three"
# 12345 -> "Twelve Thousand Three Hundred Forty Five"
# 1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
#
# Companies
# Microsoft Facebook
# Related Topics
# Math String
# Similar Questions
# Integer to Roman
#
import unittest
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"

        lookup = {0: "Zero", 1:"One", 2: "Two", 3: "Three", 4: "Four", \
                  5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", \
                  10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", \
                  15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", \
                  20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", \
                  70: "Seventy", 80: "Eighty", 90: "Ninety"}
        unit = ["", "Thousand", "Million", "Billion"]

        res, i = [], 0
        while num :
            cur = num % 1000
            if num % 1000:
                res.append(self.threeDigits(cur, lookup, unit[i]))
                #self.isPlural(num, res)
            num //= 1000
            i += 1
        return " ".join(res[::-1])

    # how to make plural show up properly?
    # ex: 299 = two hundreds and ninety nine
    # check online, seems plural is not required
    def isPlural(self, num, res):
        if num % 1000 and num // 1000 > 1:
            return res.append("s")
        elif num % 100 and num // 100 > 1:
            return res.append("s")


    def threeDigits(self, num, lookup, unit):
        res = []
        if num / 100:
            res = [lookup[num / 100] + " " + "Hundred"]
            #self.isPlural(num, res)
        if num % 100:
            res.append(self.twoDigits(num % 100, lookup))
        if unit != "":
            res.append(unit)
        return " ".join(res)

    def twoDigits(self, num, lookup):
        if num in lookup:
            return lookup[num]
        return lookup[ (num / 10) * 10] + " " + lookup[ num % 10]

#test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().numberToWords(299)
        print Solution().numberToWords(0)
        print Solution().numberToWords(200000)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
#43.12% 4ms
public class Solution {
    private static final String[] BASE = new String[] {"Thousand", "Million", "Billion"};
    private static final String[] TENS = new String[] {"Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
    private static final String[] NUMS = new String[] {"One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};

    public String numberToWords(int num) {
        if (num < 0) {
            return "";
        } else if (num == 0) {
            return "Zero";
        } else {
            return intToStr(num).substring(1);
        }
    }

    private String intToStr(int num) {
        if (num >= 1000000000) {
            return intToStr(num / 1000000000) + " Billion" + intToStr(num % 1000000000);
        } else if (num >= 1000000) {
            return intToStr(num / 1000000) + " Million" + intToStr(num % 1000000);
        } else if (num >= 1000) {
            return intToStr(num / 1000) + " Thousand" + intToStr(num % 1000);
        } else if (num >= 100) {
            return intToStr(num / 100) + " Hundred" + intToStr(num % 100);
        } else if (num >= 20) {
            return " " + TENS[num / 10 - 2] + intToStr(num % 10);
        } else if (num > 0) {
            return " " + NUMS[num - 1];
        } else {
            return "";
        }
    }
}

# 90.12% 3ms
public class Solution {
    private static final String[] TENS = new String[] {"Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
    private static final String[] NUMS = new String[] {"One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};

    public String numberToWords(int num) {
        if (num < 0) {
            return "";
        } else if (num == 0) {
            return "Zero";
        } else {
            return numToWord(num).substring(1);
        }
    }

    private String numToWord(int num) {
        if (num >= 1000000000) {
            return new StringBuilder().append(numToWord(num / 1000000000)).append(" Billion").append(numToWord(num % 1000000000)).toString();
        } else if (num >= 1000000) {
            return new StringBuilder().append(numToWord(num / 1000000)).append(" Million").append(numToWord(num % 1000000)).toString();
        } else if (num >= 1000) {
            return new StringBuilder().append(numToWord(num / 1000)).append(" Thousand").append(numToWord(num % 1000)).toString();
        } else if (num >= 100) {
            return new StringBuilder().append(numToWord(num / 100)).append(" Hundred").append(numToWord(num % 100)).toString();
        } else if (num >= 20) {
            return new StringBuilder().append(' ').append(TENS[num / 10 - 2]).append(numToWord(num % 10)).toString();
        } else if (num > 0) {
            return new StringBuilder().append(' ').append(NUMS[num - 1]).toString();
        } else {
            return "";
        }
    }
}

# 90.12% 3ms
class Solution {
    private static final String[] lessThan20 = {"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
    private static final String[] tens = {"", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
    private static final String[] thousands = {"Hundred", "Thousand", "Million", "Billion"};

    private static final int BILLION = 1000000000;
    private static final int MILLION = 1000000;
    private static final int THOUSAND = 1000;
    private static final int HUNDRED = 100;
    private static final int TEN = 10;

    public static String numberToWords(int num) {
        if (num == 0) return "Zero";
        StringBuilder res = new StringBuilder();
        while (num > 0) {
            if (num / BILLION > 0) {
                res.append(numberToWords(num / BILLION)).append(" ").append(thousands[3]).append(" ");
                num %= BILLION;
            } else if (num / MILLION > 0){
                res.append(numberToWords(num / MILLION)).append(" ").append(thousands[2]).append(" ");
                num %= MILLION;
            } else if (num / THOUSAND > 0){
                res.append(numberToWords(num / THOUSAND)).append(" ").append(thousands[1]).append(" ");
                num %= THOUSAND;
            } else if (num / HUNDRED > 0){
                res.append(numberToWords(num / HUNDRED)).append(" ").append(thousands[0]).append(" ");
                num %= HUNDRED;
            } else if (num / TEN > 1){
                res.append(tens[num / 10]).append(" ");
                num %= TEN;
            } else {
                res.append(lessThan20[num]);
                break;
            }
        }
        return res.toString().trim();
    }
}
'''