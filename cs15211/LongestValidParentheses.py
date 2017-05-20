__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/longest-valid-parentheses.py
# Time:  O(n)
# Space: O(1)
# Stack
#
# Given a string containing just the characters '(' and ')',
# find the length of the longest valid (well-formed) parentheses substring.
#
# For "(()", the longest valid parentheses substring is "()", which has length = 2.
#
# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
#
# Dynamic Programming String
class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        longest, start, depth  = 0, -1, 0

        # do it from s[head] to s[tail]
        for i in xrange(len(s)):
            if s[i] == "(" :
                depth += 1
            else:
                depth -=1
                if depth < 0:
                    start = i
                    depth = 0

                elif depth == 0:
                    longest = max(longest, i - start)

        # do it from s[tail] to s[head]
        start, depth = len(s), 0
        for i in reversed(xrange(len(s))):
            if s[i] == ")":
                depth += 1
            else:
                depth -=1
                if depth < 0:
                    start = i
                    depth = 0
                elif depth == 0:
                    longest = max(longest, start - i)
        return longest


# Time:  O(n)
# Space: O(n)
class Solution2:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        longest = 0
        last  = -1 # () counts 2, so set last = -1
        stack = []

        for i in xrange(len(s)):
            if s[i] == "(":
                stack.append(i)  # note down the index as the start of continue parentheses
            elif not stack:  # if stack is empty, mark a new start point
                last = i
            else:
                stack.pop()
                if not stack:
                    longest = max(longest, i - last)
                else:
                    longest = max(longest, i - stack[-1])  # if stack not empty, only count succeed parentheses
        return longest


if __name__ == "__main__":
    print Solution().longestValidParentheses("(()")
    print Solution().longestValidParentheses(")()())")
    print Solution().longestValidParentheses("()(()")
    print Solution2().longestValidParentheses("(()")
    print Solution2().longestValidParentheses(")()())")
    print Solution2().longestValidParentheses("()(()")



class SolutionOther:
    # @param s, a string
    # @return an integer
    def longestValidParentheses_exceed_time_limit(self, s):
        rightPar = []
        count = [0] * len(s)
        ans = 0

        for i in range(len(s)):
            if s[i] == '(':
                rightPar.append(i)
            elif s[i] == ')':
                if len(rightPar) > 0:
                    count[i] = i - rightPar[-1] + 1
                    print "i= ", i , rightPar[-1]

                    if i >= count[i] and count[i - count[i]]:
                        count[i] += count[i-count[i]]
                    ans = max(ans, count[i])
                    rightPar.pop()
        return ans

    def longestValidParentheses(self, s):
        if s == '' or s == '(' or s == ')':
            return 0
        stack =[(-1, ')')]
        maxLen = 0

        for i in xrange(len(s)):
            print i, stack
            if s[i] == ')' and stack[-1][1] == '(':
                stack.pop()
                maxLen = max(maxLen, i - stack[-1][0])
            else:
                stack.append((i, s[i]))
        return maxLen

# Java Solution
# http://www.programcreek.com/2014/06/leetcode-longest-valid-parentheses-java/
#test
s = SolutionOther()
#print s.longestValidParentheses("()(()")
#print s.longestValidParentheses('(()()')
print s.longestValidParentheses(')()())')

#java
js = '''
public class Solution {
    public int longestValidParentheses(String s) {
        int len = s.length();
        if (len < 2) {
            return 0;
        }
        int[] dp = new int[len];
        int result = 0;
        for (int i = 1; i < len; i++) {
            if (s.charAt(i) == ')') {
                int left = i - 1 - dp[i - 1];
                if (left >= 0 && s.charAt(left) == '(') {
                    dp[i] = dp[i - 1] + 2;
                    if (left - 1 >= 0) {
                        dp[i] += dp[left - 1];
                    }
                    result = Math.max(result, dp[i]);
                }
            }
        }
        return result;
    }
}


public class Solution {
    public int longestValidParentheses(String s) {
        if( s == null || s.length() < 2){
            return 0;
        }

        Stack<Integer> stack = new Stack<>();
        int start = 0;
        int maxLen = 0;

        for( int i = 0; i < s.length(); i++){
            if(s.charAt(i) == '('){
                stack.push(i);
            }else{
                if(stack.isEmpty()){
                    start = i + 1;
                }else{
                    stack.pop();
                    if(stack.isEmpty()){
                        maxLen = Math.max(maxLen, i - start + 1);
                    }else{
                        maxLen = Math.max(maxLen, i - stack.peek() );
                    }
                }
            }
        }
        return maxLen;
    }
}
'''