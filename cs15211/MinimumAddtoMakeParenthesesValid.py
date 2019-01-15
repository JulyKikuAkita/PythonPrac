__source__ = 'https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/'
# Time:  O(N)
# Space: O(1)
#
# Description: Leetcode # 921. Minimum Add to Make Parentheses Valid
#
# Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')',
# and in any positions ) so that the resulting parentheses string is valid.
#
# Formally, a parentheses string is valid if and only if:
#
#     It is the empty string, or
#     It can be written as AB (A concatenated with B), where A and B are valid strings, or
#     It can be written as (A), where A is a valid string.
#
# Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.
#
# Example 1:
#
# Input: "())"
# Output: 1
#
# Example 2:
#
# Input: "((("
# Output: 3
#
# Example 3:
#
# Input: "()"
# Output: 0
#
# Example 4:
#
# Input: "()))(("
# Output: 4
#
# Note:
#     S.length <= 1000
#     S only consists of '(' and ')' characters.
#
import unittest

# 20ms 100%
class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        ans = bal = 0
        for symbol in S:
            bal += 1 if symbol == '(' else -1
            # It is guaranteed bal >= -1
            if bal == -1:
                ans += 1
                bal += 1
        return ans + bal

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/solution/
#
Approach 1: Balance
Complexity Analysis
Time Complexity: O(N), where N is the length of S.
Space Complexity: O(1)
# 4ms 99.83%
class Solution {
    public int minAddToMakeValid(String S) {
        int ans = 0, bal = 0;
        for (int i = 0; i < S.length(); ++i) {
            bal += S.charAt(i) == '(' ? 1 : -1;
            // It is guaranteed bal >= -1
            if (bal == -1) {
                ans++;
                bal++;
            }
        }
        return ans + bal;
    }
}

# 4ms 99.83%
class Solution {
    public int minAddToMakeValid(String S) {
        int res = 0, cnt = 0;
        for (char c : S.toCharArray()) {
            if (c == '(') cnt++;
            else cnt--;
            if (cnt < 0) {
                res -= cnt;
                cnt = 0;
            }
        }
        if (cnt > 0) res += cnt;
        return res;
    }
}

# Stack
# 11ms 18.59% 
class Solution {
    public int minAddToMakeValid(String S) {
        Stack<Character> stack = new Stack();
        int count = 0;
        for (int i = 0; i < S.length(); i++) {
            if (S.charAt(i) == '(') stack.push('(');
            else {
                if (stack.isEmpty()) count++;
                else stack.pop();
            }
        }
        return count + stack.size();
    }
}
'''
