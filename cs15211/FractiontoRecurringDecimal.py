__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/fraction-to-recurring-decimal.py
# Time:  O(logn), where logn is the length of result strings
# Space: O(1)
# MATH
#
# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
#
# If the fractional part is repeating, enclose the repeating part in parentheses.
#
# For example,
#
# Given numerator = 1, denominator = 2, return "0.5".
# Given numerator = 2, denominator = 1, return "2".
# Given numerator = 2, denominator = 3, return "0.(6)".
# Google
import unittest
class Solution():
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        dvd, dvs = abs(numerator), abs(denominator)
        integer, decimal, dict = "", "", {}

        if dvd > dvs:
            integer = str(dvd / dvs)
            dvd %= dvs
        else:
            integer = "0"

        if dvd > 0:
            integer += "."

        idx = 0

        while dvd:

            if dvd in dict:
                print dict, decimal, dvd, dict[dvd]
                decimal = decimal[:dict[dvd]] + "(" + decimal[dict[dvd]:] + ")"
                break

            dict[dvd] = idx
            idx += 1

            dvd *= 10
            decimal += str(dvd / dvs)
            dvd %= dvs

        if (numerator > 0 and denominator < 0) or (numerator < 0 and denominator > 0):
            return "-" + integer + decimal
        else:
            return integer + decimal

# test
class Test(unittest.TestCase):
    def test(self):
        self.assertEqual("0.(142857)",Solution().fractionToDecimal(1, 7))
        self.assertEqual("-6.25",Solution().fractionToDecimal(-50, 8))
        self.assertEqual("0.001999" ,Solution().fractionToDecimal(-1999, -1000000))


#java
js = '''
public class Solution {
    public String fractionToDecimal(int numerator, int denominator) {
        if (denominator == 0) {
            return "n/a";
        }
        StringBuilder sb = new StringBuilder();
        if ((numerator < 0 && denominator > 0) || (numerator > 0 && denominator < 0)) {
            sb.append("-");
        }
        long longNumerator = Math.abs((long) numerator);
        long longDenominator = Math.abs((long) denominator);
        sb.append(longNumerator / longDenominator);
        longNumerator %= longDenominator;
        if (longNumerator != 0) {
            sb.append('.').append(getFractional(longNumerator, longDenominator));
        }
        return sb.toString();
    }

    private String getFractional(long remaining, long denominator) {
        StringBuilder sb = new StringBuilder();
        Map<Long, Integer> map = new HashMap<>();
        int index = 0;
        while (remaining > 0) {
            remaining *= 10;
            if (map.containsKey(remaining)) {
                StringBuilder result = new StringBuilder();
                result.append(sb.substring(0, map.get(remaining)));
                result.append('(');
                result.append(sb.substring(map.get(remaining)));
                result.append(')');
                return result.toString();
            }
            map.put(remaining, index);
            sb.append(remaining / denominator);
            remaining %= denominator;
            index++;
        }
        return sb.toString();
    }
}
// import org.junit.*;
// Assert.assertEquals("0.(142857)",Solution().fractionToDecimal(1, 7));
'''