__source__ = 'https://leetcode.com/problems/decode-string/#/description'
# Time:  O(n)
# Space: O(1)
#
# Description:
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
# Hide Company Tags Google
# Hide Tags Depth-first Search Stack
# Hide Similar Problems (H) Encode String with Shortest Length

import unittest
import re
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
#Thought:
public class Solution {
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
'''