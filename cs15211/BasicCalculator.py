__source__ = 'https://leetcode.com/problems/basic-calculator/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/basic-calculator.py
# Time:  O(n)
# Space: O(n)
#
# Description: Leetcode # 224. Basic Calculator
#
# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string may contain open ( and closing parentheses ),
# the plus + or minus sign -, non-negative integers and empty spaces .
#
# You may assume that the given expression is always valid.
#
# Some examples:
# "1 + 1" = 2
# " 2-1 + 2 " = 3
# "(1+(4+5+2)-3)+(6+8)" = 23
#
# Companies
# Google
# Related Topics
# Stack Math
# Similar Questions
# Evaluate Reverse Polish Notation Basic Calculator II Different Ways to Add Parentheses Expression Add Operators
#
import unittest
class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        #considfering if s contains space?
        operands, operators = [], []
        operand = ""
        for i in reversed(xrange(len(s))):
            if s[i].isdigit():
                operand += s[i]
                if i == 0 or not s[i-1].isdigit():
                    operands.append(int(operand[::-1]))
                    operand = ""
            elif s[i] == ')' or s[i] == '+' or s[i] == '-':
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
            operands.append( left - right)

class Solution2(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        digits = []
        operators = []

        tmp = ""
        for w in s[::-1]:
            if w.isdigit():
                tmp += w
            else:
                if len(tmp) > 0:
                    digits.append(int(tmp[::-1]))
                    tmp = ""
                if w == ")" or w ==  "+" or w ==  "-":
                    operators.append(w)
                elif w == "(":
                    while operators[-1] != ")":
                        self.compute(operators, digits)
                    operators.pop()
        if tmp != "":
            digits.append(int(tmp[::-1]))

        while digits and operators:
            self.compute(operators, digits)

        return digits[-1]

    def compute(self, operators, digits):
        opr = operators.pop()
        x = digits.pop()
        y = digits.pop()
        sum = 0
        if opr == "+":
            sum = x + y
        elif opr == "-":
            sum = x - y
        digits.append(sum)

class Solution3(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        stack = [True,True]
        res = 0

        i = 0
        j = 0
        while i < len(s):
            if s[i].isdigit():
                cur = ord(s[i]) - ord('0')
                j = i + 1
                while j < len(s):
                    if s[j].isdigit():
                        cur = cur * 10 + (ord(s[j]) - ord('0'))
                    else:
                        break
                    j += 1
                cur = cur if stack.pop() == True else -cur
                res += cur
            elif s[i] == '+' or s[i] == '(':
                stack.append(stack[-1])
            elif s[i] == '-':
                stack.append(not stack[-1])
            elif s[i] == ')':
                stack.pop()
            i = max(j, i+1)
        return res

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:

# 57.82% 14ms
public class Solution {
    public int calculate(String s) {
        Stack<Boolean> stack = new Stack<>();
        stack.push(true);
        int len = s.length();
        int result = 0;
        int num = 0;
        boolean isPositive = true;
        for (int i = 0; i < len; i++) {
            char c = s.charAt(i);
            if (c >= '0' && c <= '9') {
                num = num * 10 + c - '0';
            } else if (c == '+' || c == '-') {
                result += isPositive ? num : -num;
                num = 0;
                isPositive = c == '+' ? stack.peek() : !stack.peek();
            } else if (c == '(') {
                stack.push(isPositive);
            } else if (c == ')') {
                stack.pop();
            }
        }
        result += isPositive ? num : -num;
        return result;
    }
}


# 99.97% 3ms
class Solution {
    public int calculate(String s) {
        if (s == null) return 0;

        int[] pos = new int[1];

        return help(s, pos);
    }

    int help(String s, int[] pos) {
        int ret = 0;
        int sign = 1;
        int num = 0;
        while(pos[0] < s.length()) {
            char c = s.charAt(pos[0]);
            if (c == '+') {
                ret += num * sign;
                num = 0;
                sign = 1;
            } else if (c == '-') {
                ret += num * sign;
                num = 0;
                sign = -1;
            } else if (c == '(') {
                pos[0]++;
                ret += help(s, pos) * sign;
            } else if (c == ')') {
                return ret + num * sign;
            } else if (c >= '0' && c <= '9') {
                num = num * 10 + c - '0';
            }
            pos[0]++;
        }

        return ret + num * sign;
    }
}

'''