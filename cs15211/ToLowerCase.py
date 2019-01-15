__source__ = 'https://leetcode.com/problems/to-lower-case/description/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 709. To Lower Case
#
# Implement function ToLowerCase() that has a string parameter str,
# and returns the same string in lowercase.
#
# Example 1:
#
# Input: "Hello"
# Output: "hello"
# Example 2:
#
# Input: "here"
# Output: "here"
# Example 3:
#
# Input: "LOVELY"
# Output: "lovely"
#

import unittest

class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        upper = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        lower = list('abcdefghijklmnopqrstuvwxyz')
        hash = {k:v for k,v in zip(upper,lower)}

        res = ''
        for ch in str:
            if hash.get(ch) != None:
                res = res + hash.get(ch)
            else:
                res = res + ch
        return res


class Solution2(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        ans = str.lower()
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
Simply adding a constant to ASCII characters 'A'-'Z' isn't really a solution to lowercasing text,
and outside of a very limited context will give the wrong answer.


# built-in
# 0ms 100%
class Solution {
    public String toLowerCase(String str) {
        return str.toLowerCase();
    }
}

# 0ms 100%
class Solution {
    public String toLowerCase(String str) {
        char[] a = str.toCharArray();
        for (int i = 0; i < a.length; i++) {
            if ('A' <= a[i] && a[i] <= 'Z') {
                a[i] = (char) (a[i] - 'A' + 'a');
            }
        }
        return new String(a);
    }
}

# 0ms 100%
class Solution {
    public String toLowerCase(String str) {
        StringBuilder res = new StringBuilder();

        for (char s: str.toCharArray()){
            char l = s < 91 && s > 64 ? (char) (s + 32) : s;
            res.append(l);
        }

        return res.toString();
    }
}

# 0ms 100%
class Solution {
    public String toLowerCase(String str) {
        char[] sArr = str.toCharArray();
        for(int i=0; i<sArr.length; i++)
            sArr[i] |= 0x20;
        return String.valueOf(sArr);
    }
}
'''