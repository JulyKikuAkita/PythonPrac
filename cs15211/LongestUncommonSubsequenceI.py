__source__ = 'https://leetcode.com/problems/longest-uncommon-subsequence-i/#/description'
# Time:  O(n) or O(min(x,y)), more precisely  O(|a| if |a|==|b| else 1) due to  equals probably only compares the characters if the lengths are the same
# Space: O(1)
#
# Description:
# Given a group of two strings, you need to find the longest uncommon subsequence of this group of two strings.
# The longest uncommon subsequence is defined as the longest subsequence of one of these strings and
# this subsequence should not be any subsequence of the other strings.
#
# A subsequence is a sequence that can be derived from one sequence by deleting some characters
# without changing the order of the remaining elements. Trivially, any string is a subsequence of itself
# and an empty string is a subsequence of any string.
#
# The input will be two strings, and the output needs to be the length of the longest uncommon subsequence.
# If the longest uncommon subsequence doesn't exist, return -1.
#
# Example 1:
# Input: "aba", "cdc"
# Output: 3
# Explanation: The longest uncommon subsequence is "aba" (or "cdc"),
# because "aba" is a subsequence of "aba",
# but not a subsequence of any other strings in the group of two strings.
# Note:
#
# Both strings' lengths will not exceed 100.
# Only letters from a ~ z will appear in input strings.
# Hide Company Tags Google
# Hide Tags String
# Hide Similar Problems (M) Longest Uncommon Subsequence II

# Explanation:
#
# For strings A, B, when len(A) > len(B), the longest possible subsequence of either A or B is A,
# and no subsequence of B can be equal to A. Answer: len(A).
#
# When len(A) == len(B), the only subsequence of B equal to A is B; so as long as A != B, the answer remains len(A).
# When A == B, any subsequence of A can be found in B and vice versa, so the answer is -1.
#

import unittest
class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b:
            return -1
        return max(len(a), len(b))

# your function here

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/articles/longest-uncommon-subsequence-i/

public class Solution {
    public int findLUSlength(String a, String b) {
        return a.equals(b) ? -1 : Math.max(a.length(), b.length());
    }
}
'''