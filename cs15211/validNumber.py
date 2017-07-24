__source__ = 'https://leetcode.com/problems/valid-number/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/valid-number.py
# Time:  O(n)
# Space: O(1)
# Math
#
# Validate if a given string is numeric.
#
# Some examples:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# Note: It is intended for the problem statement to be ambiguous.
# You should gather all requirements up front before implementing one.
#
# Companies
# LinkedIn
# Related Topics
# Math String
# Similar Questions
# String to Integer (atoi)
#

import unittest
class InputType:
    INVALID    = 0
    SPACE      = 1
    SIGN       = 2
    DIGIT      = 3
    DOT        = 4
    EXPONENT   = 5

# regular expression: "^\s*[\+\-]?((\d+(\.\d*)?)|\.\d+)([eE][+-]?\d+)?\s*$"
# automata: http://images.cnitblog.com/i/627993/201405/012016243309923.png
class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        transition_table = [[-1,  0,  3,  1,  2, -1],     # next states for state 0
                            [-1,  8, -1,  1,  4,  5],     # next states for state 1
                            [-1, -1, -1,  4, -1, -1],     # next states for state 2
                            [-1, -1, -1,  1,  2, -1],     # next states for state 3
                            [-1,  8, -1,  4, -1,  5],     # next states for state 4
                            [-1, -1,  6,  7, -1, -1],     # next states for state 5
                            [-1, -1, -1,  7, -1, -1],     # next states for state 6
                            [-1,  8, -1,  7, -1, -1],     # next states for state 7
                            [-1,  8, -1, -1, -1, -1]]     # next states for state 8
        state = 0
        for char in s:
            inputType = InputType.INVALID
            if char.isspace():
                inputType = InputType.SPACE
            elif char == '+' or char == '-':
                inputType = InputType.SIGN
            elif char.isdigit():
                inputType = InputType.DIGIT
            elif char == '.':
                inputType = InputType.DOT
            elif char == 'e' or char =='E':
                inputType = InputType.EXPONENT

            state = transition_table[state][inputType]

            if state == -1:
                return False

        return state == 1 or state == 4 or state == 7 or state == 8

class Solution2:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        import re #regular repression
        return bool(re.match("^\s*[\+\-]?((\d+(\.\d*)?)|\.\d+)([eE][+-]?\d+)?\s*$", s))

class SolutionOther:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        if s.isdigit():
            return True
        else:
            try:
                float(s)
                return True
            except ValueError:
                return False

#test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        my_test=SolutionOther()
        print my_test.isNumber("0.1")
        print my_test.isNumber("0")
        print my_test.isNumber("abc")
        print my_test.isNumber("1 a")
        print my_test.isNumber("2e10")
        print my_test.isNumber("log2")

        print Solution().isNumber(" 0.1 ")
        print Solution().isNumber("abc")
        print Solution().isNumber("1 a")
        print Solution().isNumber("2e10")

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/contains-duplicate/solution/
import java.util.regex.Pattern;

# 7.21%
# 41ms
public class Solution {
    public boolean isNumber(String s) {
        String regex = "\\s*[+-]?(\\d+\\.|\\.\\d+|\\d+){1}\\d*(e[+-]?\\d+)?\\s*";
        return Pattern.matches(regex, s);
    }
}

# 41.77%  4ms
class Solution {
    public boolean isNumber(String s) {
        s = s.trim();

        boolean pointSeen = false;
        boolean eSeen = false;
        boolean numberSeen = false;
        boolean numberAfterE = true;
        for(int i=0; i<s.length(); i++) {
            if('0' <= s.charAt(i) && s.charAt(i) <= '9') {
                numberSeen = true;
                numberAfterE = true;
            } else if(s.charAt(i) == '.') {
                if(eSeen || pointSeen) {
                    return false;
                }
                pointSeen = true;
            } else if(s.charAt(i) == 'e') {
                if(eSeen || !numberSeen) {
                    return false;
                }
                numberAfterE = false;
                eSeen = true;
            } else if(s.charAt(i) == '-' || s.charAt(i) == '+') {
                if(i != 0 && s.charAt(i-1) != 'e') {
                    return false;
                }
            } else {
                return false;
            }
        }

        return numberSeen && numberAfterE;
    }
}
'''