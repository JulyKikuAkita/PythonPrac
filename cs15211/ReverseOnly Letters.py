__source__ = 'https://leetcode.com/problems/reverse-only-letters/'
# Time:  O(N)
# Space: O(N)
#
# Description: Leetcode # 917. Reverse Only Letters
#
# Given a string S, return the "reversed" string
# where all characters that are not a letter stay in the same place,
# and all letters reverse their positions.
#
# Example 1:
#
# Input: "ab-cd"
# Output: "dc-ba"
# Example 2:
#
# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 3:
#
# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
#
#
# Note:
#
# S.length <= 100
# 33 <= S[i].ASCIIcode <= 122
# S doesn't contain \ or "
#
import unittest

# stack, 20ms 100%
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        letters = [c for c in S if c.isalpha()]
        ans = []
        for c in S:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)
        return "".join(ans)

# 2 pointers, 20ms 100%
class Solution2(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        chars = []
        s = list(S)
        for char in s:
            if char >= "a" and char <= "z" or char >= "A" and char <= "Z" :
                chars.append(char)
        for i in range(len(s)):
            if s[i] >= "a" and s[i] <= "z" or s[i] >= "A" and s[i] <= "Z" :
                s[i] = chars.pop()
        return "".join(s)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/reverse-only-letters/solution/

# Two pointers
# 6ms 70.99%
class Solution {
    public String reverseOnlyLetters(String S) {
        int i = 0, j = S.length() - 1;
        char[] ans = S.toCharArray();
        while (i < j) {
            if (Character.isLetter(S.charAt(i)) && Character.isLetter(S.charAt(j))) {
                char tmp = ans[i];
                ans[i] = ans[j];
                ans[j] = tmp;
                i++;
                j--;
            }
            if (!Character.isLetter(ans[i])) i++;
            if (!Character.isLetter(ans[j])) j--;
        }
        return new String(ans);
    }
}

Approach 1: Stack of Letters
# 5ms 95.61%
class Solution {
    public String reverseOnlyLetters(String S) {
        Stack<Character> stack = new Stack();
        for (char c : S.toCharArray()) {
            if (Character.isLetter(c)) stack.push(c);
        }

        StringBuilder sb = new StringBuilder();
        for (char c: S.toCharArray()) {
            if (Character.isLetter(c)) {
                sb.append(stack.pop());
            } else {
                sb.append(c);
            }
        }
        return sb.toString();
    }
}
'''
