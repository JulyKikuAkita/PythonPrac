# coding=utf-8
__source__ = 'https://leetcode.com/problems/bold-words-in-string/'
# Time:  O(sum(len(words)))
# Space: O(N)
#
# Description: Leetcode # 758. Bold Words in String
#
# Given a set of keywords words and a string S,
# make all appearances of all keywords in S bold.
# Any letters between <b> and </b> tags become bold.
#
# The returned string should use the least number of tags possible,
# and of course the tags should form a valid combination.
#
# For example, given that words = ["ab", "bc"] and S = "aabcd",
# we should return "a<b>abc</b>d". Note that returning "a<b>a<b>b</b>c</b>d" would use more tags,
# so it is incorrect.
#
# Note:
#
# words has length in range [0, 50].
# words[i] has length in range [1, 10].
# S has length in range [0, 500].
# All characters in words[i] and S are lowercase letters.
#
import unittest

#32ms 98.7%
class Solution(object):
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        n = len(S)
        f = [False] * n
        d = set(words)
        for word in d:
            i = 0
            pos = S.find(word, i)
            while pos != -1:
                for j in xrange(pos, pos + len(word)):
                    f[j] = True
                pos = S.find(word, pos + 1)
        i = 0
        ans = []
        while i < n:
            if not f[i]:
                ans.append(S[i])
                i += 1
            else:
                ans.append('<b>')
                while i < n and f[i]:
                    ans.append(S[i])
                    i += 1
                ans.append('</b>')
        return ''.join(ans)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/bold-words-in-string/solution/
Complexity Analysis
Time Complexity: O(N∑w i), where N is the length of S and w_i is the sum of W.
Space Complexity: O(N.

#8ms 90.29%
class Solution {
    public String boldWords(String[] words, String S) {
        boolean[] f = new boolean[S.length()];
        for (String w: words) {
            int start = 0;
            while (start < S.length()) {
                int index = S.indexOf(w, start);
                if (index != -1) {
                    for (int i = index; i < index + w.length(); i++) {
                        f[i] = true;
                    }
                    start = index + 1;
                } else {
                    break;
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < f.length; i++) {
            if ((i == 0 || !f[i-1]) && f[i]) {
                sb.append("<b>");
            }
            sb.append(S.charAt(i));
            if ((i == S.length() - 1 || !f[i + 1]) && f[i]) {
                sb.append("</b>");
            }
        }
        return sb.toString();
    }
}


'''