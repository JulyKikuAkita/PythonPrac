__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/evaluate-reverse-polish-notation.py
# Time:  O(n)
# Space: O(n)
# Stack
#
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
#
# Some examples:
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
#
import operator

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


if __name__ == "__main__":
    print Solution().evalRPN(["2", "1", "+", "3", "*"])
    print Solution().evalRPN(["4", "13", "5", "/", "+"])
    print Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])


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
#Java Solution
# http://www.programcreek.com/2012/12/leetcode-evaluate-reverse-polish-notation/
js = '''
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
'''