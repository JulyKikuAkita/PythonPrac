__source__ = 'https://github.com/kamyu104/LeetCode/blob/master/Python/ternary-expression-parser.py'
# https://leetcode.com/problems/ternary-expression-parser/#/description
# Time:  O(n)
# Space: O(1)
#
# Description:
# Given a string representing arbitrarily nested ternary expressions,
# calculate the result of the expression.
# You can always assume that the given expression is valid and only consists of digits 0-9, ?, :,
# T and F (T and F represent True and False respectively).
#
# Note:
#
# The length of the given string is <= 10000.
# Each number will contain only one digit.
# The conditional expressions group right-to-left (as usual in most languages).
# The condition will always be either T or F. That is, the condition will never be a digit.
# The result of the expression will always evaluate to either a digit 0-9, T or F.
# Example 1:
#
# Input: "T?2:3"
#
# Output: "2"
#
# Explanation: If true, then result is 2; otherwise result is 3.
# Example 2:
#
# Input: "F?1:T?4:5"
#
# Output: "4"
#
# Explanation: The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:
#
#              "(F ? 1 : (T ? 4 : 5))"                   "(F ? 1 : (T ? 4 : 5))"
#           -> "(F ? 1 : 4)"                 or       -> "(T ? 4 : 5)"
#           -> "4"                                    -> "4"
# Example 3:
#
# Input: "T?T?F:5:3"
#
# Output: "F"
#
# Explanation: The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:
#
#              "(T ? (T ? F : 5) : 3)"                   "(T ? (T ? F : 5) : 3)"
#           -> "(T ? F : 3)"                 or       -> "(T ? F : 5)"
#           -> "F"                                    -> "F"
# Hide Company Tags Snapchat
# Hide Tags Depth-first Search Stack
# Hide Similar Problems (M) Mini Parser

import unittest
class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        if not expression:
            return ""

        stack = []
        for c in expression[::-1]:
            if stack and stack[-1] == '?':
                stack.pop()  # pop '?'
                first = stack.pop()
                stack.pop()  # pop ':'
                second = stack.pop()

                if c == 'T':
                    stack.append(first)
                else:
                    stack.append(second)
            else:
                stack.append(c)
        return str(stack[-1])

    def parseTernary2(self, expression):
        stack = []
        for c in reversed(expression):
            stack.append(c)
            if stack[-2:-1] == ['?']:
                stack[-5:] = stack[-3 if stack[-1] == 'T' else -5]
        return stack[0]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
# Iterate the expression from tail, whenever encounter a character before '?',
# calculate the right value and push back to stack.
#
# P.S. this code is guaranteed only if "the given expression is valid" base on the requirement.

public String parseTernary(String expression) {
    if (expression == null || expression.length() == 0) return "";
    Deque<Character> stack = new LinkedList<>();

    for (int i = expression.length() - 1; i >= 0; i--) {
        char c = expression.charAt(i);
        if (!stack.isEmpty() && stack.peek() == '?') {

            stack.pop(); //pop '?'
            char first = stack.pop();
            stack.pop(); //pop ':'
            char second = stack.pop();

            if (c == 'T') stack.push(first);
            else stack.push(second);
        } else {
            stack.push(c);
        }
    }

    return String.valueOf(stack.peek());
}
'''