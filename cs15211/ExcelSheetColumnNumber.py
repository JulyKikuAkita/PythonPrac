__source__ = 'https://leetcode.com/problems/excel-sheet-column-number/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/excel-sheet-column-number.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 171. Excel Sheet Column Number
#
# Related to question Excel Sheet Column Title
#
# Given a column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28
#
# Companies
# Microsoft Uber
# Related Topics
# Math
# Similar Questions
# Excel Sheet Column Title

import unittest
class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        result = 0
        for i in xrange(len(s)):
            result *= 26
            result += ord(s[i]) - ord('A') + 1
        return result
if __name__ == "__main__":
    print Solution().titleToNumber("AAAB")

# http://bookshadow.com/weblog/2014/12/28/leetcode-excel-sheet-column-number/
class SolutionOther:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        ans = 0
        for i in range(len(s)):
            #print s[i], ans, ord(s[i])
            ans = ans * 26 + ord(s[i]) - ord('A') + 1
        return ans

# 28ms s78.02%
class Solution2(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return reduce(lambda x, y : x * 26 + y, [ord(c) - 64 for c in list(s)])


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().titleToNumber('AB')

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:

# 1ms 100%
class Solution {
    public int titleToNumber(String s) {
        int result = 0;
        for (int i = 0; i < s.length(); i++) {
            result = result * 26 + (s.charAt(i) - 'A') + 1;
        }
        return result;
    }
}

# 1ms 100%
class Solution {
    public int titleToNumber(String s) {
        int result = 0;
        for (int i = 0; i < s.length(); result = result * 26 + (s.charAt(i) - 'A' + 1), i++);
        return result;
    }
}
'''