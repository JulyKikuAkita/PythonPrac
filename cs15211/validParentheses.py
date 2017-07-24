__source__ = 'https://leetcode.com/problems/valid-parentheses/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/valid-parentheses.py
# Time:  O(n)
# Space: O(n)
# Stack
#
# Description: Leetcode # 20. Valid Parentheses
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}"
# are all valid but "(]" and "([)]" are not.
#
# Google Airbnb Facebook Twitter Zenefits Amazon Microsoft Bloomberg
# Hide Tags Stack String
# Hide Similar Problems (M) Generate Parentheses (H) Longest Valid Parentheses (H) Remove Invalid Parentheses
# Companies
# Google Airbnb Facebook Twitter Zenefits Amazon Microsoft Bloomberg
# Related Topics
# Stack String
# Similar Questions
# Generate Parentheses Longest Valid Parentheses Remove Invalid Parentheses
#
import unittest
class Solution:
    # @return a boolean
    def isValid(self, s):
        stack, dict = [], {"(": ")", "{": "}", "[": "]"}
        for char in s:
            if char in dict:
                stack.append(char)
            elif len(stack) == 0 or dict[stack.pop()] != char:
                return False
        return len(stack) == 0

class Solution:
    # @return a boolean
    def isValid(self, s):
        parmap = {"(":")","[":"]","{":"}",}
        stack = []
        for i in range(len(s)):

            if parmap.get(s[i]):
                stack.append(s[i])
            #first and last not a pair
            elif len(stack) ==0 or parmap[stack[-1]] != s[i] :
                #print stack, stack[-1]
                return False
            else:
                stack.pop()

        return True if len(stack)==0 else False

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        t1=Solution()
        #print t1.isValid("()[]{}")
        print t1.isValid("(]]")
        print t1.isValid("([])")

        print Solution().isValid("()[]{}")
        print Solution().isValid("()[{]}")

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:

#77.06% 9ms
public class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        for (char c: s.toCharArray()) {
            if (c == '(') stack.push(')');
            else if (c == '{') stack.push('}');
		    else if (c == '[') stack.push(']');
            else if (stack.isEmpty() || stack.pop() != c) return false;
        }
        return stack.isEmpty();
    }
}

# 36.61%  11ms
public class Solution {
    public boolean isValid(String s) {
        Stack<Integer> p = new Stack<>();
        for(int i = 0; i < s.length(); i++) {
            int q = "(){}[]".indexOf(s.substring(i, i + 1));
            if(q % 2 == 1) {
                if(p.isEmpty() || p.pop() != q - 1) return false;
            } else p.push(q);
        }
        return p.isEmpty();
    }
}
'''