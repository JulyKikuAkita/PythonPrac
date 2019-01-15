__source__ = 'https://leetcode.com/problems/number-of-segments-in-a-string/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/number-of-segments-in-a-string.py
# Time:  O(n)
# Space: O(1)
# Count the number of segments in a string,
# where a segment is defined to be a contiguous
# sequence of non-space characters.
#
# Description: Leetcode # 434. Number of Segments in a String
#
# Please note that the string does not
# contain any non-printable characters.
#
# Example:
#
# Input: "Hello, my name is John"
# Output: 5
# String
#
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

    # 20ms 97.59%
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
# Thought: https://leetcode.com/problems/number-of-segments-in-a-string/solution/

# 5ms 10.30%
class Solution {
    public int countSegments(String s) {
        return ("x " + s).split(" +").length - 1;
    }
}

# 1ms 100%
class Solution {
    public int countSegments(String s) {
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
