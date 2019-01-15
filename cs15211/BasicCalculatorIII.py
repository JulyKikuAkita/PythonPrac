__source__ = 'https://leetcode.com/problems/basic-calculator-iii/description/'
# Time:  O()
# Space: O()
#
# https://leetcode.com/problems/basic-calculator-iii/discuss/113592/Development-of-a-generic-solution-for-the-series-of-the-calculator-problems
#
# Description: Leetcode # 772. Basic Calculator III
#
# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -,
# non-negative integers and empty spaces .
#
# The expression string contains only non-negative integers, +, -, *, / operators
# , open ( and closing parentheses ) and empty spaces . The integer division should truncate toward zero.
#
# You may assume that the given expression is always valid.
# All intermediate results will be in the range of [-2147483648, 2147483647].
#
# Some examples:
#
# "1 + 1" = 2
# " 6-4 / 2 " = 4
# "2*(5+5*2)/3+(6/2+8)" = 21
# "(2+6* 3+5- (3*14/7+2)*5)+3"=-12
#
# Note: Do not use the eval built-in library function.
#
import unittest

#28ms 100%
class SolutionBM(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        return eval(s)

#36ms 97.81%
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def calc(num_stk, op_stk):
            b = num_stk.pop()
            a = num_stk.pop()
            op = op_stk.pop()
            if op == "+":
                num_stk.append(a + b)
            elif op == "-":
                num_stk.append(a - b)
            elif op == "*":
                num_stk.append(a * b)
            else:
                num_stk.append(a // b)

        num_stk = []
        op_stk = []
        s = s.replace(" ", "")
        num = ""
        order = {"+":1, "-":1, "*":0, "/":0, "(": 2}
        for c in s:
            if c.isdigit():
                num += c
            else:
                if num:
                    num_stk.append(int(num))
                    num = ""
                # +-*/()
                if c == "(":
                    op_stk.append(c)
                elif c == ")":
                    while op_stk[-1] != "(":
                        calc(num_stk, op_stk)
                    op_stk.pop()
                else:
                    while op_stk and order[op_stk[-1]] <= order[c]:
                        calc(num_stk, op_stk)
                    op_stk.append(c)
        if num:
            num_stk.append(int(num))
        while op_stk:
            calc(num_stk, op_stk)
        return num_stk[0]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/basic-calculator-iii/solution/
# https://leetcode.com/problems/basic-calculator-iii/discuss/113592/Development-of-a-generic-solution-for-the-series-of-the-calculator-problems
# Recursive solution: O(n^2) time, O(n) space


# Iterative solution: O(n) time, O(n) space


# 5ms 98.66%
#
class Solution {
    private int i = 0;
    public int calculate(String s) {
        int res = 0, sign = 1;
        boolean mlt = true;
        while (i < s.length()) {
            char c = s.charAt(i++);
            if (c == ' ') continue;
            if (c == ')') break;
            if (c == '(') {
                int m = calculate(s);
                if (mlt) sign *= m;
                else sign /= m;
            } else if ('0' <= c && c <= '9') {
                int m = c - '0';
                while (i < s.length()) {
                    c = s.charAt(i);
                    if (c < '0' || c > '9') break;
                    m = m * 10 + c - '0';
                    i++;
                }
                if (mlt) sign *= m;
                else sign /= m;
            }
            else if (c == '*') mlt = true;
            else if (c == '/') mlt = false;
            else {
                res += sign;
                sign = c == '+' ? 1: -1;
                mlt = true;
            }
        }
        res += sign;
        return res;
    }
}

#97.55% 6ms
class Solution {
    int i = 0;
    public int calculate(String s) {
        Deque<Character> operators = new LinkedList<>(); //+-*/
        Deque<Integer> operands = new  LinkedList<>();
        int num = 0;
        int sign = 1;
        for (; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == ' ') continue;
            if (c == '(') {
                i++;
                num = calculate(s);
            } else if (c == ')') {
                break;
            } else if (isOperator(c)) {
                operands.push(num * sign);
                num = 0;

                sign = c == '-' ? -1 : 1;
                if (!operators.isEmpty() && isPrecedence(operators.peek())) {
                    int value = performOp(operators.pop(), operands.pop(), operands.pop());
                    operands.push(value);
                }
                operators.push(c == '-' ? '+' : c);
            } else {
                num = num * 10 + (c - '0');
            }
        }
        operands.push(sign * num);
        return evaluate(operators, operands);
    }

    private static int evaluate(Deque<Character> operators, Deque<Integer> operands) {
        while(!operators.isEmpty()) {
            int val = performOp(operators.pop(), operands.pop(),operands.pop());
            operands.push(val);
        }
        return operands.pop();
    }

    private static boolean isPrecedence(char op1) {
        return ( op1 == '*' || op1 == '/');
    }

    private static boolean isOperator(char c) {
        return c == '+' || c == '-' || c == '*' || c == '/';
    }

    private static int performOp(char c, int num1, int num2) {
        switch(c) {
             case '+':
                return num2 + num1;
            case '-':
                return num2 - num1;
            case '*':
                return num2 * num1;
            default:
                return num2 / num1;
        }
    }
}
'''