__source__ = 'https://leetcode.com/problems/backspace-string-compare/description/'
# Time:  O(N)
# Space: O(N)
#
# Description: Leetcode #
# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
#
# Example 1:
#
# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# Example 2:
#
# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
# Example 3:
#
# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
# Example 4:
#
# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".
# Note:
#
# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S and T only contain lowercase letters and '#' characters.
# Follow up:
#
# Can you solve it in O(N) time and O(1) space?
#
import unittest


class Solution(object):
    pass  # your function here


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/backspace-string-compare/solution/

Approach #2: Two Pointer [Accepted]
Time Complexity: O(M + N), where M, N are the lengths of S and T respectively.
Space Complexity: O(1)

class Solution {
    public boolean backspaceCompare(String S, String T) {
        int i = S.length() - 1, j = T.length() - 1;
        int skipS = 0, skipT = 0;

        while ( i >= 0 || j >= 0){
            while (i >= 0) {
                if (S.charAt(i) == '#') {
                    skipS++; i--;
                } else if(skipS > 0) {
                    skipS--; i--;
                } else break;
            }

            while (j >= 0) {
                if (T.charAt(j) == '#') {
                    skipT++; j--;
                } else if (skipT > 0) {
                    skipT--; j--;
                } else break;
            }

            if ( i >= 0 && j >= 0 && S.charAt(i) != T.charAt(j)) return false;
            if ( (i >= 0) != (j >=0)) return false;
            i--; j--;
        }
        return true;
    }
}
'''