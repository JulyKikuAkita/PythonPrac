__source__ = 'https://leetcode.com/problems/find-and-replace-in-string/'
# Time:  O(NQ)
# Space: O(N)
#
# Description: Leetcode # 833. Find And Replace in String
#
# To some string S, we will perform some replacement operations that
# replace groups of letters with new ones (not necessarily the same size).
#
# Each replacement operation has 3 parameters: a starting index i,
# a source word x and a target word y.  The rule is that if x starts at position i in the original string S,
# then we will replace that occurrence of x with y.  If not, we do nothing.
#
# For example, if we have S = "abcd" and we have some replacement operation i = 2, x = "cd", y = "ffff",
# then because "cd" starts at position 2 in the original string S, we will replace it with "ffff".
#
# Using another example on S = "abcd", if we have both the replacement operation i = 0, x = "ab",
# y = "eee", as well as another replacement operation i = 2, x = "ec", y = "ffff",
# this second operation does nothing because in the original string S[2] = 'c',
# which doesn't match x[0] = 'e'.
#
# All these operations occur simultaneously.
# It's guaranteed that there won't be any overlap in replacement: for example,
# S = "abc", indexes = [0, 1], sources = ["ab","bc"] is not a valid test case.
#
# Example 1:
#
# Input: S = "abcd", indexes = [0,2], sources = ["a","cd"], targets = ["eee","ffff"]
# Output: "eeebffff"
# Explanation: "a" starts at index 0 in S, so it's replaced by "eee".
# "cd" starts at index 2 in S, so it's replaced by "ffff".
# Example 2:
#
# Input: S = "abcd", indexes = [0,2], sources = ["ab","ec"], targets = ["eee","ffff"]
# Output: "eeecd"
# Explanation: "ab" starts at index 0 in S, so it's replaced by "eee".
# "ec" doesn't starts at index 2 in the original S, so we do nothing.
# Notes:
#
# 0 <= indexes.length = sources.length = targets.length <= 100
# 0 < indexes[i] < S.length <= 1000
# All characters in given inputs are lowercase letters.
#
import unittest

#24ms 79.01%
class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        S = list(S)
        for i, x, y in sorted(zip(indexes, sources, targets), reverse = True):
            if all(i+k < len(S) and S[i+k] == x[k] for k in xrange(len(x))):
                S[i:i+len(x)] = list(y)

        return "".join(S)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/find-and-replace-in-string/solution/

Complexity Analysis
Time Complexity: O(NQ), where N is the length of S, and we have QQ replacement operations.
(Our complexity could be faster with a more accurate implementation, but it isn't necessary.)
Space Complexity: O(N)), if we consider targets[i].length <= 100 as a constant bound.

# 4ms 87.01%
class Solution {
    public String findReplaceString(String S, int[] indexes, String[] sources, String[] targets) {
        int N = S.length();
        int[] match = new int[N];
        Arrays.fill(match, -1);

        for (int i = 0; i < indexes.length; i++) {
            if (S.substring(indexes[i],
                            indexes[i] + sources[i].length()).equals(sources[i])) {
                match[indexes[i]] = i;
            }
        }

        StringBuilder sb = new StringBuilder();
        int ix = 0;
        while (ix < N) {
            if (match[ix] >= 0) {
                sb.append(targets[match[ix]]);
                ix += sources[match[ix]].length();
            } else {
                sb.append(S.charAt(ix++));
            }
        }
        return sb.toString();
    }
}
'''