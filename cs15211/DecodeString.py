__source__ = 'https://leetcode.com/problems/decode-string/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/decode-string.py
# Time:  O(n)
# Space: O(h), h is the depth of the recursion
#
# Description: 394. Decode String
#
# Given an encoded string, return it's decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being
# repeated exactly k times. Note that k is guaranteed to be a positive integer.
#
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
#
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for
# those repeat numbers, k. For example, there won't be input like 3a or 2[4].
#
# Examples:
#
# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
#
# Companies
# Google
# Related Topics
# Stack Depth-first Search
# Similar Questions
# Encode String with Shortest Length
#
import unittest
import re

# TLE
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        while '[' in s:
            s = re.sub(r'(\d+)\[([a-z]*)\]', lambda m: int(m.group(1)) * m.group(2), s)
        return s

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# 2ms 91.49%
class Solution {
    public String decodeString(String s) {
        Stack<Integer> count = new Stack<>();
        Stack<String> result = new Stack<>();
        int i = 0;
        result.push("");

        while ( i < s.length()) {
            char c = s.charAt(i);
            if (c >= '0' && c <= '9') {
                int start = i;
                while(s.charAt(i+1) >= '0' && s.charAt(i+1) <= '9') { //note, use i+1
                    i++;
                }
                count.push(Integer.parseInt(s.substring(start, i + 1)));
            } else if (c =='[') {
                result.push("");
            } else if (c == ']') {
                String str = result.pop();
                int times = count.pop();
                StringBuilder sb = new StringBuilder();
                for (int j = 0; j < times; j++) {
                    sb.append(str);
                }
                result.push(result.pop() + sb.toString());
            } else { //when chars
                result.push(result.pop() + c);
            }
            i++;
        }
        return result.pop();
    }
}

# Recursion
# 1ms 100%
class Solution {
    private int index = 0;
    private String decode(String s) {
        StringBuilder sb = new StringBuilder();
        while (index < s.length()) {
            char ch = s.charAt(index);
            if (ch >= '0' && ch <='9') {
                int times = 0;
                for (; ch != '[';) {
                    times = times * 10 + (ch - '0');
                    ch = s.charAt(++index);
                }
                index++;
                String subString = decode(s);
                for (int i = 0; i < times; i++)
                    sb.append(subString);
            } else if (ch == ']') {
                index++;
                break;
            } else {
                sb.append(ch);
                index++;
            }
        }
        return sb.toString();
    }

    public String decodeString(String s) {
        if (s == null || s.length() == 0)
            return "";
        return decode(s);
    }
}
'''