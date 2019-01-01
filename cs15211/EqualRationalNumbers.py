__source__ = 'https://leetcode.com/problems/equal-rational-numbers/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 972. Equal Rational Numbers
#
# Given two strings S and T, each of which represents a non-negative rational number,
# return True if and only if they represent the same number.
# The strings may use parentheses to denote the repeating part of the rational number.
#
# In general a rational number can be represented using up to three parts: an integer part,
# a non-repeating part, and a repeating part.
# The number will be represented in one of the following three ways:
#
# <IntegerPart> (e.g. 0, 12, 123)
# <IntegerPart><.><NonRepeatingPart>  (e.g. 0.5, 1., 2.12, 2.0001)
# <IntegerPart><.><NonRepeatingPart><(><RepeatingPart><)> (e.g. 0.1(6), 0.9(9), 0.00(1212))
# The repeating portion of a decimal expansion is conventionally denoted within a pair of round brackets.
# For example:
#
# 1 / 6 = 0.16666666... = 0.1(6) = 0.1666(6) = 0.166(66)
#
# Both 0.1(6) or 0.1666(6) or 0.166(66) are correct representations of 1 / 6.
#
# Example 1:
#
# Input: S = "0.(52)", T = "0.5(25)"
# Output: true
# Explanation:
# Because "0.(52)" represents 0.52525252..., and "0.5(25)" represents 0.52525252525..... ,
# the strings represent the same number.
# Example 2:
#
# Input: S = "0.1666(6)", T = "0.166(66)"
# Output: true
# Example 3:
#
# Input: S = "0.9(9)", T = "1."
# Output: true
# Explanation:
# "0.9(9)" represents 0.999999999... repeated forever, which equals 1.  [See this link for an explanation.]
# "1." represents the number 1, which is formed correctly: (IntegerPart) = "1" and (NonRepeatingPart) = "".
# Note:
#
# Each part consists only of digits.
# The <IntegerPart> will not begin with 2 or more zeros.  (There is no other restriction on the digits of each part.)
# 1 <= <IntegerPart>.length <= 4
# 0 <= <NonRepeatingPart>.length <= 4
# 1 <= <RepeatingPart>.length <= 4
#
import unittest
# 24ms 100%
from fractions import Fraction
class Solution(object):
    def isRationalEqual(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def convert(S):
            if '.' not in S:
                return Fraction(int(S), 1)
            i = S.index('.')
            ans = Fraction(int(S[:i]), 1)
            S = S[i+1:]
            if '(' not in S:
                if S:
                    ans += Fraction(int(S), 10 ** len(S))
                return ans

            i = S.index('(')
            if i:
                ans += Fraction(int(S[:i]), 10 ** i)
            S = S[i+1:-1]
            j = len(S)
            ans += Fraction(int(S), 10**i * (10**j - 1))
            return ans
        return convert(S) == convert(T)
# Cheat:
class Solution2(object):
    def isRationalEqual(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def f(s):
            i = s.find('(')
            if i >= 0:
                s = s[:i] + s[i + 1:-1] * 20
            return float(s[:20])
        return f(S) == f(T)
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/equal-rational-numbers/solution/
# Approach 1: Fraction Class
# Complexity Analysis
# Time Complexity: O(1), if we take the length of S, T as O(1).
# Space Complexity: O(1)
# 8ms 60%
class Solution {
    class Fraction {
        long n, d;
        Fraction(long n, long d) {
            long g = gcd(n, d);
            this.n = n / g;
            this.d = d / g;
        }

        public void iadd(Fraction other) {
            long numerator = this.n * other.d + this.d * other.n;
            long denominator = this.d * other.d;
            long g = gcd(numerator, denominator);
            this.n = numerator / g;
            this.d = denominator / g;
        }

        public long gcd(long x, long y) {
            return x != 0 ? gcd(y % x, x) : y;
        }
    }
    
    public boolean isRationalEqual(String S, String T) {
        Fraction f1 = convert(S);
        Fraction f2 = convert(T);
        return f1.n == f2.n && f1.d == f2.d;
    }
    
    public Fraction convert(String S) {
        int state = 0; //whole, decimal, repeating
        Fraction ans = new Fraction(0, 1);
        int decimal_size = 0;

        for (String part: S.split("[.()]")) {
            state++;
            if (part.isEmpty()) continue;
            long x = Long.valueOf(part);
            int sz = part.length();

            if (state == 1) { // whole
                 ans.iadd(new Fraction(x, 1));
            } else if (state == 2) { // decimal
                 ans.iadd(new Fraction(x, (long) Math.pow(10, sz)));
                 decimal_size = sz;
            } else { // repeating
                 long denom = (long) Math.pow(10, decimal_size);
                 denom *= (long) (Math.pow(10, sz) - 1);
                 ans.iadd(new Fraction(x, denom));
            }
        }
        return ans;
    }
}
# https://leetcode.com/problems/equal-rational-numbers/discuss/214205/Java-Math-explained
# [Java] Math explained
# For 0 < q < 1, 1 + q + q^2 + ... = 1 / (1 - q)
# Link: https://en.wikipedia.org/wiki/Geometric_progression#Infinite_geometric_series
# 0.(52) = 0 + 0.52 * (1 + 0.01 + 0.0001 + ...) = 0 + 0.52 / (1 - 0.01)
# 0.5(25) = 0.5 + 0.025 * (1 + 0.01 + 0.0001 + ...) = 0.5 + 0.025 / (1 - 0.01)
#
# 4ms 100%
class Solution {
    private List<Double> ratios = Arrays.asList(1.0, 1.0 / 9, 1.0 / 99, 1.0 / 999, 1.0 / 9999);

    public boolean isRationalEqual(String S, String T) {
        return Math.abs(computeValue(S) - computeValue(T)) < 1e-9;
    }
    
    // "0.(52)"
    private double computeValue(String s) {
        if (!s.contains("(")) return Double.valueOf(s);
        double intNonRepeatingValue = Double.valueOf(s.substring(0, s.indexOf('(')));
        int nonRepeatingLength = s.indexOf('(') - s.indexOf('.') - 1;
        int repeatingLength = s.indexOf(')') - s.indexOf('(') - 1;
        int repeatingValue = Integer.parseInt(s.substring(s.indexOf('(') + 1, s.indexOf(')')));
        return intNonRepeatingValue + repeatingValue * Math.pow(0.1, nonRepeatingLength) * ratios.get(repeatingLength);
    }
}

# https://leetcode.com/problems/equal-rational-numbers/discuss/214203/JavaC%2B%2BPython-Easy-Cheat
# cheat
# 5ms 60%
class Solution {
    public boolean isRationalEqual(String S, String T) {
        return f(S) == f(T);
    }

    public double f(String S) {
        int i = S.indexOf('(');
        if (i > 0) {
            String base = S.substring(0, i);
            String rep = S.substring(i + 1, S.length() - 1);
            for (int j = 0; j < 20; ++j) base += rep;
            return Double.valueOf(base);
        }
        return Double.valueOf(S);
    }
}
'''
