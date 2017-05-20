__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/basic-calculator-ii.py
# Time:  O(n)
# Space: O(n)
#
# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string contains only non-negative integers, +, -, *, /
# operators and empty spaces . The integer division should truncate toward zero.
#
# You may assume that the given expression is always valid.
#
# Some examples:
# "3+2*2" = 7
# " 3/2 " = 1
# " 3+5 / 2 " = 5
# Note: Do not use the eval built-in library function.
#

class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        operands, operators = [], []
        operand = ""

        for i in reversed(xrange(len(s))):
            if s[i].isdigit():
                operand += s[i]
                if i == 0 or not s[i-1].isdigit():
                    operands.append(int(operand[::-1]))
                    operand = ""
                elif s[i] == ')' or s[i] == '*' or s[i] == '/':
                    operators.append(s[i])
                elif s[i] == '+' or s[i] =='-':
                    while operators and (operators[-1] == '*'  or operators[-1] == '/'):
                        self.compute(operands, operators)
                    operators.append(s[i])
                elif s[i] == '(':
                    while operators[-1] != ')':
                        self.compute(operands, operators)
                    operators.pop()

        while operators:
            self.compute(operands, operators)

        return operands[-1]



    def compute(self, operands, operators):
        left, right = operands.pop(), operands.pop()
        op = operators.pop()
        if op == '+':
            operands.append(left + right)
        elif op == '-':
            operands.append(left - right)
        elif op == '*':
            operands.append(left * right)
        elif op == '/':
            operands.append(left / right)


class Solution2:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        if not s:
            return 0
        s.strip(" ")
        stack = []
        digits = []
        sign = 1
        res = 0
        i = 0
        j = 0
        while i < len(s):
            if s[i].isdigit():
                num = int(s[i])
                j = i+1
                while j < len(s) and s[j].isdigit():
                    num = num * 10 + int(s[j])
                    j += 1
                digits.append(num * sign)
                sign = 1
                while stack and (stack[-1] == '*' or stack[-1] == '/'):
                        self.compute(digits, stack)
            elif s[i] == '+' or s[i] == '*' or s[i] == '/':
                sign = 1
                stack.append(s[i])
            elif s[i] == '-':
                sign = -1
                stack.append('+')
            i = max(i+1, j)
        #print stack, digits
        while stack :
            self.compute(digits, stack)
        return digits[-1]

    def compute(self, operands, operators):
        right, left = operands.pop(), operands.pop()
        op = operators.pop()
        if op == '+':
            operands.append(left + right)
        elif op == '-':
            operands.append(left - right)
        elif op == '*':
            operands.append(left * right)
        elif op == '/':
            if left < 0:
                sum = -(-left/right)
            else:
                sum = left/right
            operands.append(sum)
#Java
# http://blog.csdn.net/u013027996/article/details/46619387
js = '''
public class Solution {
    public int calculate(String s) {
        int result = 0;
        int lastNum = 0;
        int sign = 1;
        char lastOp = '#';
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c >= '0' && c <= '9') {
                int j = i + 1;
                int curNum = c - '0';
                while (j < s.length()) {
                    c = s.charAt(j);
                    if (c >= '0' && c <= '9') {
                        curNum = curNum * 10 + (c - '0');
                        j++;
                    } else {
                        break;
                    }
                }
                if (lastOp == '*') {
                    lastNum *= curNum;
                } else if (lastOp == '/') {
                    lastNum /= curNum;
                } else {
                    lastNum = curNum;
                }
                i = j - 1;
            } else if (c == '+' || c == '-') {
                result += sign * lastNum;
                sign = c == '+' ? 1 : -1;
                lastOp = c;
            } else if (c == '*' || c == '/') {
                lastOp = c;
            }
        }
        result += sign * lastNum;
        return result;
    }
}
'''