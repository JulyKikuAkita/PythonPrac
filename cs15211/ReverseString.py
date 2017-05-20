__author__ = 'July'
'''
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
'''
import unittest
class Solution(unittest.TestCase):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

    def test(self):
        self.assertEqual("olleh", self.reverseString("hello"))
#java
js = '''
public class Solution {
    public String reverseString(String s) {
        if(s == null || s.length() == 0) return "";
        char[] chars = s.toCharArray();

        int start = 0;
        int end = chars.length -1;
        while(start < end){
            char c = chars[start];
            chars[start] = chars[end];
            chars[end] = c;
            start ++;
            end--;
        }
        return new String(chars);
    }
}
'''