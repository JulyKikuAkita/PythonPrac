__source__ = 'https://leetcode.com/problems/valid-palindrome-ii/description/'
# Time:  O(N)
# Space: O(1)
#
# Description: Leetcode # 680. Valid Palindrome II
#
# Given a non-empty string s, you may delete at most one character.
# Judge whether you can make it a palindrome.
#
# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# Note:
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
#
# Companies
# Facebook
# Related Topics
# String
# Similar Questions
# Valid Palindrome
#
import unittest

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return self.isPalindrome(s, 0, len(s)-1, 0)

    def isPalindrome(self, s, start, end, delCount):
        if delCount > 1:
            return False
        while start < end:
            if s[start] != s[end]:
                break
            start += 1
            end -= 1
        if (start == end) or (start == end+1):
            return True
        return any([self.isPalindrome(s, start+1, end, delCount+1), self.isPalindrome(s, start, end-1, delCount+1)])

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/valid-palindrome-ii/solution/
# 35ms
class Solution {
    public boolean validPalindrome(String s) {
        int l = -1, r = s.length();
        while (++l < --r) {
            if (s.charAt(l) != s.charAt(r)) {
                return isPalindrome(s, l, r + 1) || isPalindrome(s, l-1, r);
            }
        }
        return true;
    }

    public boolean isPalindrome(String s, int l, int r) {
        while (++l < --r) {
            if (s.charAt(l) != s.charAt(r)) return false;
        }
        return true;
    }
}

#48ms
class Solution {
    public boolean validPalindrome(String s) {
        int left = 0, right = s.length() - 1;
        while ( left < right) {
            if (s.charAt(left) == s.charAt(right)) {
                left++;
                right--;
            } else {
                //remove right
                int tempLeft = left, tempRight = right - 1;
                while (tempLeft < tempRight) {
                    if (s.charAt(tempLeft) != s.charAt(tempRight)) break;
                    tempLeft++;
                    tempRight--;
                    if (tempLeft >= tempRight) return true;
                }
                //remove left
                left++;
                while(left < right) {
                    if (s.charAt(left) != s.charAt(right)) return false;
                    left++;
                    right--;
                }
            }
        }
        return true;
    }
}
'''