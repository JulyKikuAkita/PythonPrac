__source__ = 'https://leetcode.com/problems/reverse-string/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/reverse-string.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 344. Reverse String
#
# Write a function that takes a string as input and
# returns the string reversed.
#
# Example:
# Given s = "hello", return "olleh".
# Related Topics
# Two Pointers String
# Similar Questions
# Reverse Vowels of a String Reverse String II
# #
import unittest
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        string = list(s)
        i, j = 0, len(string) - 1
        while i < j:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1
        return "".join(string)

# Time:  O(n)
# Space: O(n)
class Solution2(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
#28.64% 4ms
public class Solution {
    public String reverseString(String s) {
        return  new StringBuilder(s).reverse().toString();
    }
}

#49.61% 3ms
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

#49.61% 3ms
public class Solution {
    public String reverseString(String s) {
        char[] tmp = s.toCharArray();
        for (int i=0, j=tmp.length - 1; i < j; i++, j--){
            swap(i, j, tmp);
        }
        return new String(tmp);
    }

    public void swap(int i, int j, char[] arr) {
        char tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }
}
'''