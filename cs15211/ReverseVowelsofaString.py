__author__ = 'July'
'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".
'''
# Google
# Two Pointers String

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        start = 0
        end = len(s) - 1
        while start < end:
            while start < end and not self.isVowel(s[start]):
                start += 1
            while start < end and not self.isVowel(s[end]):
                end -= 1
            if start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        return ''.join(s)

    def isVowel(self, c):
        if c in 'aeiouAEIOU':
            return True
        else:
            return False

#java
js = '''
public class Solution {
    public String reverseVowels(String s) {
        char[] arr = s.toCharArray();
        int start = 0;
        int end = arr.length - 1;
        while (start < end) {
            while (start < end && !isVowel(arr[start])) {
                start++;
            }
            while (start < end && !isVowel(arr[end])) {
                end--;
            }
            if (start < end) {
                char c = arr[start];
                arr[start] = arr[end];
                arr[end] = c;
                start++;
                end--;
            }
        }
        return new String(arr);
    }

    private boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U';
    }
}
'''