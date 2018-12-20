__source__ = 'https://leetcode.com/problems/solve-the-equation/'
# Time:  O(n)
# Space: O(n)
#
# Description: Leetcode # 640. Solve the Equation
#
# Solve a given equation and return the value of x in the form of string "x=#value".
# The equation contains only '+', '-' operation, the variable x and its coefficient.
#
# If there is no solution for the equation, return "No solution".
#
# If there are infinite solutions for the equation, return "Infinite solutions".
#
# If there is exactly one solution for the equation, we ensure that the value of x is an integer.
#
# Example 1:
# Input: "x+5-3+x=6+x-2"
# Output: "x=2"
# Example 2:
# Input: "x=x"
# Output: "Infinite solutions"
# Example 3:
# Input: "2x=x"
# Output: "x=0"
# Example 4:
# Input: "2x+3x-6x=x+2"
# Output: "x=-1"
# Example 5:
# Input: "x=x+2"
# Output: "No solution"
# Companies
# Amazon
# Related Topics
# Math
# Similar Questions
# Fraction Addition and Subtraction
#
import unittest

class Solution(object):
    pass  # your function here


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/solve-the-equation/solution/

# Approach #2 Using regex for spliting [Accepted]
# 11ms 13.21%
class Solution {
    public String coeff(String x) {
        if (x.length() > 1 && x.charAt(x.length() - 2) >= '0' && x.charAt(x.length() - 2) <= '9')
            return x.replace("x", "");
        return x.replace("x", "1");
    }
    public String solveEquation(String equation) {
        String[] lr = equation.split("=");
        int lhs = 0, rhs = 0;
        for (String x: lr[0].split("(?=\\+)|(?=-)")) {
            if (x.indexOf("x") >= 0) {

                lhs += Integer.parseInt(coeff(x));
            } else
                rhs -= Integer.parseInt(x);
        }
        for (String x: lr[1].split("(?=\\+)|(?=-)")) {
            if (x.indexOf("x") >= 0)
                lhs -= Integer.parseInt(coeff(x));
            else
                rhs += Integer.parseInt(x);
        }
        if (lhs == 0) {
            if (rhs == 0)
                return "Infinite solutions";
            else
                return "No solution";
        } else
            return "x=" + rhs / lhs;
    }
}

# 3ms 91.58%
class Solution {
    private final String NoSolution = "No solution";
    private final String InfiniteSolutions = "Infinite solutions";
    private final char X = 'x';
    private final char Plus = '+';
    private final char Minus = '-';
    private final char Equal = '=';
    private final char Zero = '0';

    public String solveEquation(String equation) {
        if (null == equation || equation.length() == 0) return NoSolution;

        int xSum = 0;
        int noSum = 0;
        int beforeEqual = 1;
        int isPositive = 1;

        int len = equation.length();
        char c;
        int temp = 0;
        int num;
        for (int i = 0; i < len; i++) {
            c = equation.charAt(i);
            if (c == Equal) {
                if(temp!=0){
                    num = -1 * beforeEqual * isPositive * temp;
                    noSum += num;
                    temp = 0;
                }
                beforeEqual = -1;
                isPositive = 1;
            } else if (c == Plus || c == Minus) {
                if (temp != 0) {
                    num = -1 * beforeEqual * isPositive * temp;
                    noSum += num;
                    temp = 0;
                }
                if (c == Plus) {
                    isPositive = 1;
                } else {
                    isPositive = -1;
                }
            } else if (c == X) {
                if (temp == 0) {
                    if (i > 0 && equation.charAt(i - 1) == Zero) {

                    } else {
                        temp = 1;
                    }
                }
                num = beforeEqual * isPositive * temp;
                xSum += num;
                temp = 0;
                isPositive = 1;
            } else {
                temp = temp * 10 + (c - Zero);
            }
        }
        if (temp != 0) {
            noSum += -1 * beforeEqual * isPositive * temp;
        }

        if (xSum == 0) {
            if (noSum == 0) {
                return InfiniteSolutions;
            }
            return NoSolution;
        }

        num = noSum / xSum;

        return "x=" + num;
    }
}
'''
