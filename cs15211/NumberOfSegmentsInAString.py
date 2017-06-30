__source__ = 'https://github.com/kamyu104/LeetCode/blob/master/Python/number-of-segments-in-a-string.py'
# https://leetcode.com/problems/number-of-segments-in-a-string/#/description
# Time:  O(n)
# Space: O(1)
# Count the number of segments in a string,
# where a segment is defined to be a contiguous
# sequence of non-space characters.
#
# Please note that the string does not
# contain any non-printable characters.
#
# Example:
#
# Input: "Hello, my name is John"
# Output: 5
# String

import unittest

class Solution(object):
    def countSegments(self, s):
        return len(s.split())

    def countSegments1(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = int(len(s) and s[-1] != ' ')
        for i in xrange(1, len(s)):
            if s[i] == ' ' and s[i-1] != ' ':
                result += 1
        return result

    def countSegments2(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len([i for i in s.strip().split(' ') if i])


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
public class Solution {
    public int countSegments(String s) {
        return ("x " + s).split(" +").length - 1;
    }

    public int countSegments2(String s) {
        int res = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != ' ' && ( i == 0 || s.charAt(i-1) == ' ')) {
                res++;
            }
        }
        return res;
    }
}
'''