__author__ = 'July'
# Given a string and an integer k, you need to reverse the first k characters
# for every 2k characters counting from the start of the string.
# If there are less than k characters left,
# reverse all of them. If there are less than 2k but greater than or equal to k characters,
# then reverse the first k characters and left the other as original.
# Example:
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Restrictions:
# The string consists of lower English letters only.
# Length of the given string and k will in the range [1, 10000]
#
# Hide Company Tags Google
# Hide Tags String
# Hide Similar Problems (E) Reverse String (E) Reverse Words in a String III
#
class Solution(object):
    def reverseStr2(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        for i in xrange(0, len(s), 2* k):
            s[i:i+k] = reversed(s[i:i+k])
        return "".join(s)

    def reverseStr(self, s, k):
        return s[:k][::-1] + s[k:2*k] + self.reverseStr(s[2*k:], k) if s else ""

java = '''
/**
     * 0            k           2k          3k
     * |-----------|-----------|-----------|---
     * +--reverse--+           +--reverse--+
     */

public class Solution {
    public String reverseStr(String s, int k) {
        char[] arr = s.toCharArray();
        for (int i = 0 ; i < arr.length; i += 2 * k) {
            for (int p = i, q = Math.min(i + k - 1, arr.length - 1); p < q ; p++, q--) {
                char tmp = arr[p];
                arr[p] = arr[q];
                arr[q] = tmp;
            }
        }
        return new String(arr);
    }
}
'''