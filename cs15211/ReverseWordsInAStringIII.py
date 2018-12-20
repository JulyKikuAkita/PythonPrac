__source__ = 'https://leetcode.com/problems/reverse-words-in-a-string-iii/'
# Time : O(n)
# Space: O(n)
#
# Description: Leetcode # 557. Reverse Words in a String III
#
# Given a string, you need to reverse the order of characters in each word
# within a sentence while still preserving whitespace and initial word order.
#
# Example 1:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Note: In the string,
# each word is separated by single space and there will not be any extra space in the string.
#
# Hide Company Tags Zappos
# Hide Tags String
# Hide Similar Problems (E) Reverse String II
#
import unittest
# 40ms 48.80%
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(map(lambda x: x[::-1], s.split()))

    def reverseWords2(self, s):
        return ' '.join(s.split()[::-1])[::-1]

    def reverseWords3(self, s):
        return ' '.join(x[::-1] for x in s.split())

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().reverseBits(1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/reverse-words-in-a-string-iii/solution/

# 6ms 90.40%
class Solution {
    public String reverseWords(String s) {
        if (s == null || s.length() <= 1) return s;
        char[] arr = s.toCharArray();
        for (int i = 0, j = i ; i < arr.length; i++) {
            if (arr[i] != ' ') {
                j = i;
                while (j + 1 < arr.length && arr[j + 1]  != ' ') {
                    j++;
                }
                reverse(arr, i, j);
                i = j;
            }
        }
        return new String(arr);

    }

    public void reverse(char[] arr, int i, int j) {
        for(; i < j; i++, j--) {
            char tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
        }
    }
}
'''
