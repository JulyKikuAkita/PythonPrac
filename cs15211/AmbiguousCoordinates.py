# coding=utf-8
import itertools

__source__ = 'https://leetcode.com/problems/ambiguous-coordinates/'
# Time:  O(N^3)
# Space: O(N^3)
#
# Description: Leetcode # 816. Ambiguous Coordinates
#
# We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)".
# Then, we removed all commas, decimal points, and spaces, and ended up with the string S.
# Return a list of strings representing all possibilities for what our original coordinates could have been.
#
# Our original representation never had extraneous zeroes,
# so we never started with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01",
# or any other number that can be represented with less digits.
# Also, a decimal point within a number never occurs without at least one digit occuring before it,
# so we never started with numbers like ".1".
#
# The final answer list can be returned in any order.
# Also note that all coordinates in the final answer have exactly one space between them (occurring after the comma.)
#
# Example 1:
# Input: "(123)"
# Output: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
# Example 2:
# Input: "(00011)"
# Output:  ["(0.001, 1)", "(0, 0.011)"]
# Explanation:
# 0.0, 00, 0001 or 00.01 are not allowed.
# Example 3:
# Input: "(0123)"
# Output: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]
# Example 4:
# Input: "(100)"
# Output: [(10, 0)]
# Explanation:
# 1.0 is not allowed.
#
#
# Note:
#
# 4 <= S.length <= 12.
# S[0] = "(", S[S.length - 1] = ")", and the other elements in S are digits.
#
import unittest

#104ms, 23.46%
class Solution(object):
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        def make(frag):
            N = len(frag)
            for d in xrange(1, N+1):
                left = frag[:d]
                right = frag[d:]
                if ((not left.startswith('0') or left == '0')
                        and (not right.endswith('0'))):
                    yield left + ('.' if d != N else '') + right

        S = S[1:-1]
        return ["({}, {})".format(*cand)
                for i in xrange(1, len(S))
                for cand in itertools.product(make(S[:i]), make(S[i:]))]
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/ambiguous-coordinates/solution/
Approach #1: Cartesian Product [Accepted]
Complexity Analysis
Time Complexity: O(N^3), where N is the length S. We evaluate the sum O(∑k K(N−k)).
Space Complexity: O(N^3, to store the answer.

# 16ms 88.52%
class Solution {
    public List<String> ambiguousCoordinates(String S) {
        List<String> ans = new ArrayList();
        for (int i = 2; i < S.length() - 1; i++) {
            for (String left : make(S, 1, i)) {
                for (String right: make(S, i, S.length() - 1)) {
                    ans.add("(" + left + ", " + right + ")");
                }
            }
        }
        return ans;
    }

    private List<String> make(String S, int i, int j) {
        // Make on S.substring(i, j)
        List<String> ans = new ArrayList();
        for (int d = 1; d <= j-i; ++d) {
            String left = S.substring(i, i + d);
            String right = S.substring(i + d, j);
            if ( (!left.startsWith("0") || left.equals("0")) && !right.endsWith("0")) {
                ans.add(left +  ( d < j - i ? "." : "") + right);
            }
        }
        return ans;
    }
}

'''