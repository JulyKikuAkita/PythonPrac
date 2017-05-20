__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/basic-calculator.py
# Time:  O(n)
# Space: O(n)
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
#  Google
# Hide Tags Stack Math
# Hide Similar Problems (M) Evaluate Reverse Polish Notation (M) Basic Calculator II (M) Different Ways to Add Parentheses (H) Expression Add Operators


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
# python
# http://bookshadow.com/weblog/2015/06/09/leetcode-basic-calculator/
#Java
# http://blog.csdn.net/xudli/article/details/46554835

#java
js = '''
public class Solution {
    public int calculate(String s) {
        int result = 0;
        Stack<Boolean> stack = new Stack<>();
        stack.push(true);
        stack.push(true);
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c >= '0' && c <= '9') {
                int num = c - '0';
                int j = i + 1;
                for (; j < s.length(); j++) {
                    c = s.charAt(j);
                    if (c >= '0' && c <= '9') {
                        num = num * 10 + (c - '0');
                    } else {
                        break;
                    }
                }
                result += stack.pop() ? num : -num;
                i = j - 1;
            } else if (c == '+' || c == '(') {
                stack.push(stack.peek());
            } else if (c == '-') {
                stack.push(!stack.peek());
            } else if (c == ')') {
                stack.pop();
            }
        }
        return result;
    }
}

public class Solution {
    public int calculate(String s) {
        if ( s == null || s.length() == 0) return 0;

        Stack<Integer> stack = new Stack<Integer>();
        int res = 0;
        int sign = 1;

        for (int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if (Character.isDigit(c)){
                int cur = c - '0';
                while( i+1 < s.length() && Character.isDigit(s.charAt(i+1))){
                    cur = 10 * cur + s.charAt(++i) - '0';
                }
                res += cur * sign;
            }
            else if( c == '+'){
                sign = 1;
            }else if( c == '-'){
                sign = -1;
            }else if( c =='('){
                stack.push(res);
                res = 0;
                stack.push(sign);
                sign = 1;
            }else if( c ==')'){
                // first pop is sign
                res = stack.pop() * res + stack.pop();
                sign = 1;
            }
        }

        return res;
    }
}
'''