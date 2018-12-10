__source__ = 'https://leetcode.com/problems/evaluate-reverse-polish-notation/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/evaluate-reverse-polish-notation.py
# Time:  O(n)
# Space: O(n)
# Stack
#
# Description: Leetcode # 150. Evaluate Reverse Polish Notation
#
# http://en.wikipedia.org/wiki/Reverse_Polish_notation
#
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
#
# Some examples:
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
#
# Companies
# LinkedIn
# Related Topics
# Stack
# Similar Questions
# Basic Calculator Expression Add Operators
#
import operator
import unittest
class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        dict = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.div}
        stack = []
        for token in tokens:
            if token not in dict:
                stack.append(int(token))
            else:
                sec = stack.pop()
                first = stack.pop() # be aware of the order
                stack.append(int(dict[token](first*1.0, sec))) # div scenario
        return stack.pop()

class SolutionOther:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        for i in tokens:
            if i not in ('+', '-', '*', '/'):
                stack.append(int(i))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if i == '+' :
                    stack.append(op1 + op2)
                elif i == '-':
                    stack.append(op1 - op2)
                elif i == '*':
                    stack.append(op1 * op2)
                else:
                    stack.append(int(op1 * 1.0 /op2))
        return stack[0]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().evalRPN(["2", "1", "+", "3", "*"])
        print Solution().evalRPN(["4", "13", "5", "/", "+"])
        print Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: Stack

# 7ms 83.46%
public class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        for (String token : tokens) {
            if (isOperator(token)) {
                int right = stack.pop();
                int left = stack.pop();
                int result = 0;
                if (token.equals("+")) {
                    result = left + right;
                } else if (token.equals("-")) {
                    result = left - right;
                } else if (token.equals("*")) {
                    result = left * right;
                } else if (token.equals("/")) {
                    result = left / right;
                }
                stack.push(result);
            } else {
                stack.push(Integer.parseInt(token));
            }
        }
        return stack.pop();
    }

    private boolean isOperator(String token) {
        return token.equals("+") || token.equals("-") || token.equals("*") || token.equals("/");
    }
}

# 2ms 100%
class Solution {
    int index;
	public int evalRPN(String[] tokens){
		index = tokens.length-1;
		return recursive(tokens);
	}
	public int recursive(String[] tokens){
		String current = tokens[index--];
		int operand1, operand2;
		switch(current){
		case "+" :
			operand1 = recursive(tokens);
			operand2 = recursive(tokens);
			return operand1 + operand2;
		case "-" :
			operand1 = recursive(tokens);
			operand2 = recursive(tokens);
			return operand2 - operand1;
		case "*" :
			operand1 = recursive(tokens);
			operand2 = recursive(tokens);
			return operand2 * operand1;
		case "/" :
			operand1 = recursive(tokens);
			operand2 = recursive(tokens);
			return operand2 / operand1;  //op1 / op2 got java.lang.ArithmeticException: / by zero
		default:
			return Integer.valueOf(current);
		}
	}
}

# 7ms 83.46%
class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        for (String token : tokens) {
            if (isOperand(token)) {
                int right = stack.pop();
                int left = stack.pop();
                stack.push(calculate(left, right, token));
            } else {
                stack.push(Integer.parseInt(token));
            }
        }
        return stack.pop();
    }

    private boolean isOperand(String token) {
        return token.equals("+") || token.equals("-") || token.equals("*") || token.equals("/");
    }

    private int calculate(int left, int right, String token) {
        switch (token) {
            case "+":
                return left + right;
            case "-":
                return left - right;
            case "*":
                return left * right;
            case "/":
                return left / right;
            default:
                return 0;
        }
    }
}
'''