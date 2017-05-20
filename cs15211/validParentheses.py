__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/valid-parentheses.py
# Time:  O(n)
# Space: O(n)
# Stack
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}"
# are all valid but "(]" and "([)]" are not.
#

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

if __name__ == "__main__":
    print Solution().isValid("()[]{}")
    print Solution().isValid("()[{]}")

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

# java Solution
# http://www.programcreek.com/2012/12/leetcode-valid-parentheses-java/


t1=Solution()
#print t1.isValid("()[]{}")
print t1.isValid("(]]")
print t1.isValid("([])")

#java
js = '''
public class Solution {
    public boolean isValid(String s) {
        if(s.length() % 2 != 0) return false;
        Stack<Character> stack = new Stack<>();


	    for(char c : s.toCharArray()){
	        if (c == '(' || c == '{' || c == '[') {
	            stack.push(c);
	        }else{
	            if (stack.isEmpty() || !isMatch(stack.pop(), c))
	                return false;
	        }
	    }

	    return stack.isEmpty();
    }
    private boolean isMatch(char c1, char c2){
        return (c1 == '(' && c2 == ')') || (c1 == '{' && c2 == '}') || (c1 == '[' && c2 == ']');
    }
}

'''