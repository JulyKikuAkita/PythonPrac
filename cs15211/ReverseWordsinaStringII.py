__source__ = 'https://leetcode.com/problems/reverse-words-in-a-string-ii/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/reverse-words-in-a-string-ii.py
# Time: O(n)
# Space:O(1)
#
# Description: Leetcode # 186. Reverse Words in a String II
#
# Given an input string, reverse the string word by word.
# A word is defined as a sequence of non-space characters.
#
# The input string does not contain leading or trailing spaces
# and the words are always separated by a single space.
#
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".
#
# Could you do it in-place without allocating extra space?
#
# Companies
# Amazon Microsoft Uber
# Related Topics
# String
# Similar Questions
# Reverse Words in a String Rotate Array
#
import unittest
class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        #reverse whole sentence
        self.reverse(s, 0, len(s))

        i = 0
        #reverse each word
        for j in xrange(len(s) + 1):
            if j == len(s) or s[j] == ' ':
                self.reverse(s, i, j )
                i = j + 1

    def reverse(self, s, begin, end):
        for i in xrange((end - begin) / 2):
            #print end, begin, (end - begin) / 2
            #s[begin + i], s[end - 1 - i] = s[end - 1 - i], s[begin + i]
            s[begin + i], s[end  - i - 1] = s[end - i - 1], s[begin + i]

class Solution2(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        self.reverse(s, 0, len(s) - 1)
        i = 0
        j = 0
        while i < len(s):
            j = i + 1
            while j < len(s) and s[j] != ' ':
                j += 1
            self.reverse(s, i, j-1)
            i = j+1

    def reverse(self, s, start, end):
        while start <= end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

# Test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        s = ['h','e','l','l','o', ' ', 'w', 'o', 'r', 'l', 'd']
        Solution().reverseWords(s)
        print s

        #s1= ['h','e','l','l','o', ' ', 'w', 'o', 'r', 'l', 'd']
        #s1.reverse()
        #print s1

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# 4ms 26.89%
class Solution {
    public void reverseWords(char[] s) {
        int start = 0;
        int end = 0;
        int realEnd = -1;
        while (start < s.length) {
            while (start < s.length && s[start] == ' ') {
                start++;
            }
            if (start == s.length) {
                break;
            }
            end = start + 1;
            while (end < s.length && s[end] != ' ') {
                end++;
            }
            reverse(s, start, end - 1);
            if (realEnd >= 0) {
                s[++realEnd] = ' ';
            }
            if (realEnd + 1 != start) {
                copy(s, start, end - 1, ++realEnd);
            }
            realEnd += end - start;
            start = end + 1;
        }
        reverse(s, 0, realEnd);
    }

    private void copy(char[] s, int start, int end, int realStart) {
        while (start <= end) {
            s[realStart++] = s[start++];
        }
    }

    private void reverse(char[] s, int start, int end) {
        while (start < end) {
            char c = s[start];
            s[start] = s[end];
            s[end] = c;
            start++;
            end--;
        }
    }
}

# 2ms 100%
class Solution {
    public void reverseWords(char[] s) {
        int len = s.length;
        reverse(s, 0, len - 1);
        int begin = 0;
        for (int i = 1; i < len; i++) {
            if (s[i] == ' ') {
                reverse(s, begin, i - 1);
                begin = i + 1;
                i++;
            }
        }
        reverse(s, begin, len - 1);
    }

    private void reverse(char[] s, int from, int to) {
        for (int lo = from, hi = to; lo < hi; lo++, hi--) {
            char tmp = s[lo];
            s[lo] = s[hi];
            s[hi] = tmp;
        }
    }
}

# 3ms 62.61%
class Solution {
    public void reverseWords(char[] s) {
        reverse(s, 0, s.length-1);
        int i = 0;
        while(i < s.length){
            int j = i + 1;
            while(j < s.length && s[j] != ' '){
                j++;
            }
            reverse(s, i, j-1);
            i = j + 1;
        }
    }

    private void reverse(char[] s, int start, int end){
        while (start < end){
            char c = s[start];
            s[start] = s[end];
            s[end] = c;
            start ++;
            end --;
        }
    }
}
'''
