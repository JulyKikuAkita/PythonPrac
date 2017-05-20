__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/shortest-palindrome.py
# Time:  O(n)
# Space: O(n)
# Google PocketGgens
'''
Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it.
Find and return the shortest palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".


'''

# KMP Algorithm
import unittest
class Solution:
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):
        if not s :
            return s
        A = s + s[::-1]
        prefix = self.getPrefix(A)

        return s[prefix[-1]+1:][::-1] + s

    def getPrefix(self, pattern):
        prefix = [-1] * len(pattern)
        j = -1
        for i in xrange(1, len(pattern)):
            while j > -1 and pattern[j + 1] != pattern[i]:
                j = prefix[j]
            if pattern[j+1] == pattern[i]:
                j += 1
            prefix[i] = j
        return prefix


class Solution2(unittest.TestCase):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #KMP prefix table
        ttl_s = s + "#" + s[::-1]
        prefix = [ 0 for _ in xrange(len(ttl_s))]

        for i in xrange(1, len(ttl_s)):
            j = prefix[i-1]
            while j > 0 and ttl_s[i] != ttl_s[j]:
                j = prefix[j-1]
            prefix[i] = j + 1 if ttl_s[i] == ttl_s[j] else j
        res = s[::-1][:len(s)-prefix[-1]:]
        #print res, ttl_s
        return res + s

    def test(self):
        self.assertEqual("bbabb", self.shortestPalindrome("abb"))

# Manacher's Algorithm
class Solution_TLE:
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):
        string = self.preProcess(s)
        palindrome = [0] * len(string)
        center, right = 0, 0
        for i in xrange(1, len(string) - 1):
            i_mirror = 2 * center - i
            if right > i:
                palindrome[i] = min(right - i, palindrome[i_mirror])
            else:
                palindrome[i] = 0

            while string[i + 1 + palindrome[i]] == string[i - 1 - palindrome[i]]:
                palindrome[i] += 1

            if i + palindrome[i] > right:
                center, right = i, i + palindrome[i]

        max_len = 0
        for i in xrange(1, len(string) - 1):
            if i - palindrome[i] == 1:
                max_len = palindrome[i]
        return s[len(s) - 1: max_len-1: -1] + s


    def preProcess(selfs, s):
        if not s:
            return "^$"
        string = "^"
        for i in s:
            string += "#" + i
        string += "#$"
        return string


#test
if __name__ == "__main__":
    print Solution().shortestPalindrome("baaabc")
    print Solution().shortestPalindrome("aba")

#java
js = '''
public class Solution {
    public String shortestPalindrome(String s) {
        String reversed = new StringBuilder(s).reverse().toString();
        char[] full = new StringBuilder().append(s).append('#').append(reversed).toString().toCharArray();
        int[] prefix = new int[full.length];
        for (int i = 1; i < full.length; i++) {
            int j = prefix[i - 1];
            while (j > 0 && full[i] != full[j]) {
                j = prefix[j - 1];
            }
            prefix[i] = j + (full[i] == full[j] ? 1 : 0);
        }
        return new StringBuilder(reversed.substring(0, reversed.length() - prefix[prefix.length - 1])).append(s).toString();
    }
}
'''