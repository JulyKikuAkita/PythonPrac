__source__ = 'https://leetcode.com/problems/basic-calculator-ii/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/basic-calculator-ii.py
# Time:  O(n)
# Space: O(n)
#
# Description: Leetcode # 227. Basic Calculator II
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
# Companies
# Airbnb
# Related Topics
# String
# Similar Questions
# Basic Calculator Expression Add Operators
#
import unittest
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

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:

#89.99% 21ms
public class Solution {
    public int calculate(String s) {
        int left = 0;
        int right = 0;
        boolean isPositive = true;
        Operator lastOp = null;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (Character.isDigit(c)) {
                int cur = c - '0';
                int j = i + 1;
                while (j < s.length() && Character.isDigit(s.charAt(j))) {
                    cur = cur * 10 + s.charAt(j++) - '0';
                }
                i = j - 1;
                if (lastOp == Operator.MULTIPLY) {
                    right *= cur;
                } else if (lastOp == Operator.DIVIDE) {
                    right /= cur;
                } else {
                    right = cur;
                }
            } else if (c == '+' || c == '-') {
                left += isPositive ? right : -right;
                isPositive = c == '+';
                lastOp = c == '+' ? Operator.ADD : Operator.MINUS;
            } else if (c == '*') {
                lastOp = Operator.MULTIPLY;
            } else if (c == '/') {
                lastOp = Operator.DIVIDE;
            }
        }
        left += isPositive ? right : -right;
        return left;
    }

    enum Operator {
        ADD, MINUS, MULTIPLY, DIVIDE
    }
}

# 99.33% 6ms
class Solution {
	public int calculate(String s) {
        if(s == null || s.length() == 0) return 0;
        boolean divide = false, multiply = false;
        int result = 0, sign = 1, num = 0, preNum = 0;
        for(char c : s.toCharArray()) {
            if(c >= '0' && c <= '9') {
                num = num * 10 + c - '0';
            }
            else if(c == '+' || c == '-' || c == '*' || c == '/') {
                if(divide) {
                    num = preNum/num;
                    divide = false;
                }
                if(multiply) {
                    num = preNum * num;
                    multiply = false;
                }
                if(c == '/') {
                    divide = true;
                    preNum = num * sign;
                    sign = 1;
                }
                else if (c == '*') {
                    sign *= num;
                }
                else {
                    result += sign * num;
                    sign = c == '+' ? 1 : -1;
                }
                num = 0;
            }
        }
        if(num > 0) {
            if(divide) num = preNum / num;
            if(multiply)  num = preNum * num;
            result += sign * num;
        }
        return result;
	}
}

# using stack
# 68.45% 33ms
public class Solution {
    public int calculate(String s) {
        int len;
        if(s==null || (len = s.length())==0) return 0;
        Stack<Integer> stack = new Stack<Integer>();
        int num = 0;
        char sign = '+';
        for(int i=0;i<len;i++){
            if(Character.isDigit(s.charAt(i))){
                num = num*10+s.charAt(i)-'0';
            }
            if((!Character.isDigit(s.charAt(i)) &&' '!= s.charAt(i)) || i == len-1){
                if(sign=='-'){
                    stack.push(-num);
                }
                if(sign=='+'){
                    stack.push(num);
                }
                if(sign=='*'){
                    stack.push(stack.pop()*num);
                }
                if(sign=='/'){
                    stack.push(stack.pop()/num);
                }
                sign = s.charAt(i);
                num = 0;
            }
        }

        int re = 0;
        for(int i:stack){
            re += i;
        }
        return re;
    }
}
'''