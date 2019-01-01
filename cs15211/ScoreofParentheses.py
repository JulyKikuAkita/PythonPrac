__source__ = 'https://leetcode.com/problems/score-of-parentheses/'
# Time:  O(N)
# Space: O(1)
#
# Description: Leetcode # 856. Score of Parentheses
#
# Given a balanced parentheses string S,
# compute the score of the string based on the following rule:
#
# () has score 1
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.
#
#
# Example 1:
#
# Input: "()"
# Output: 1
# Example 2:
#
# Input: "(())"
# Output: 2
# Example 3:
#
# Input: "()()"
# Output: 2
# Example 4:
#
# Input: "(()(()))"
# Output: 6
#
#
# Note:
#
# S is a balanced parentheses string, containing only ( and ).
# 2 <= S.length <= 50
#
import unittest

# 20ms 100%
class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        ans = bal = 0
        for i, x in enumerate(S):
            if x == '(':
                bal += 1
            else:
                bal -= 1
                if S[i-1] == '(':
                    ans += 1 << bal
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/score-of-parentheses/solution/
#
Approach 1: Divide and Conquer
Complexity Analysis
Time Complexity: O(N^2), where N is the length of S. An example worst case is (((((((....))))))).
Space Complexity: O(N), the size of the implied call stack. 

# 4ms 82.83%
class Solution {
    public int scoreOfParentheses(String S) {
        return F(S, 0, S.length());
    }
    
    private int F(String S, int i, int j) {
        //Score of balanced string S[i:j]
        int ans = 0, bal = 0;
        
        // Split string into primitives
        for (int k = i; k < j; ++k) {
            bal += S.charAt(k) == '(' ? 1 : -1;
            if (bal == 0) {
                if (k - i == 1) ans++;
                else ans += 2 * F(S, i+1, k);
                i = k+1;
            }
        }
        return ans;
    }
}

Approach 2: Stack
Complexity Analysis
Time Complexity: O(N), where N is the length of S.
Space Complexity: O(N), the size of the stack. 

# For example, when counting (()(())), our stack will look like this:
# 
#     [0, 0] after parsing (
#     [0, 0, 0] after (
#     [0, 1] after )
#     [0, 1, 0] after (
#     [0, 1, 0, 0] after (
#     [0, 1, 1] after )
#     [0, 3] after )
#     [6] after )

# 4ms 82.83%
class Solution {
    public int scoreOfParentheses(String S) {
        Stack<Integer> stack = new Stack();
        stack.push(0); // The score of the current frame
        
        for (char c: S.toCharArray()) {
            if (c == '(') stack.push(0);
            else {
                int v = stack.pop();
                int w = stack.pop();
                stack.push(w + Math.max(2 * v, 1));
            }
        }
        return stack.pop();
    }


Approach 3: Count Cores
Complexity Analysis
Time Complexity: O(N), where N is the length of S.
Space Complexity: O(1)

# 3ms 100%
# #1. For every ) that immediately follows a (, the answer is 1 << balance, 
# as balance is the number of exterior set of parentheses that contains this core.
class Solution {
    public int scoreOfParentheses(String S) {
        int ans = 0, bal = 0;
        for (int i = 0; i < S.length(); ++i) {
            if (S.charAt(i) == '(') bal++;
            else {
                bal--;
                if (S.charAt(i - 1) == '(') {
                    ans += 1 << bal;
                }
            }
        }
        return ans;
    }
}
'''
