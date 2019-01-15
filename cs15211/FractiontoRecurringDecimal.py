__source__ = 'https://leetcode.com/problems/fraction-to-recurring-decimal/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/fraction-to-recurring-decimal.py
# Time:  O(logn), where log n is the length of result strings
# Space: O(1)
# MATH
#
# Description: Leetcode # 166. Fraction to Recurring Decimal
#
# Given two integers representing the numerator and denominator of a fraction,
# return the fraction in string format.
#
# If the fractional part is repeating, enclose the repeating part in parentheses.
#
# For example,
#
# Given numerator = 1, denominator = 2, return "0.5".
# Given numerator = 2, denominator = 1, return "2".
# Given numerator = 2, denominator = 3, return "0.(6)".
#
# Companies
# Google
# Related Topics
# Hash Table Math
#
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
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual("0.(142857)",Solution().fractionToDecimal(1, 7))
        self.assertEqual("-6.25",Solution().fractionToDecimal(-50, 8))
        self.assertEqual("0.001999" ,Solution().fractionToDecimal(-1999, -1000000))

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/fraction-to-recurring-decimal/solution/

# 5ms 31.73%
class Solution {
    public String fractionToDecimal(int numerator, int denominator) {
        StringBuilder result = new StringBuilder();
        String sign = (numerator < 0 == denominator < 0 || numerator == 0) ? "" : "-";
        long num = Math.abs((long) numerator);
        long den = Math.abs((long) denominator);
        result.append(sign);
        result.append(num / den);
        long remainder = num % den;
        if (remainder == 0)
            return result.toString();
        result.append(".");
        HashMap<Long, Integer> hashMap = new HashMap<Long, Integer>();
        while (!hashMap.containsKey(remainder)) {
            hashMap.put(remainder, result.length());
            result.append(10 * remainder / den);
            remainder = 10 * remainder % den;
        }
        int index = hashMap.get(remainder);
        result.insert(index, "(");
        result.append(")");
        return result.toString().replace("(0)", "");
    }
}

# 3ms 99.71%
class Solution {
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


# 2ms 100%
class Solution {
    public String fractionToDecimal(int numerator, int denominator) {
        // negative sign
        boolean negative = (numerator < 0) ^ (denominator < 0);
        long n = Math.abs((long)numerator);
        long d = Math.abs((long)denominator);
        long intPart = n / d;
        long rest = n - intPart * d;
        if (rest == 0) return negative ? String.valueOf(intPart * (-1)) : String.valueOf(intPart); // Integer result
        StringBuilder res = new StringBuilder();
        if (negative) res.append("-");
        res.append(intPart);
        res.append(".");

        long slow;
        long fast;
        long[] temp = new long[2];
        slow = Decimal(rest*10, d)[1];
        fast = Decimal(slow , d)[1];
        while (slow != fast) {
            slow = Decimal(slow, d)[1];
            fast = Decimal(Decimal(fast, d)[1], d)[1];
        }
        slow = rest * 10;
        while (slow != fast && slow != 0) {
            temp = Decimal(slow, d);
            slow = temp[1];
            res.append(temp[0]);       // non-cycle part
            fast = Decimal(fast, d)[1];
        }
        if (slow == 0) return res.toString();  // return when result is finite decimal
        temp = Decimal(slow, d);
        fast = temp[1];
        res.append("(");
        res.append(temp[0]);
        while (slow != fast) {
            temp = Decimal(fast, d);
            fast = temp[1];
            res.append(temp[0]);  // cycle part
        }
        res.append(")");
        return res.toString();
    }

    public long[] Decimal(long rest, long denominator) {
        // return the quotient and remainder (multiplied by 10)
        long r1;
        long r2;
        if (rest < denominator) {
            r1 = 0;
            r2 = rest * 10;
        }
        else {
            r1 = rest / denominator;
            r2 = (rest - denominator * r1) * 10;
        }
        return new long[]{r1, r2};
    }
}

'''