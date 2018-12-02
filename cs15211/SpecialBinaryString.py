__source__ = 'https://leetcode.com/problems/special-binary-string/'
# Time:  O(N^2)
# Space: O(N)
#
# Description: Leetcode # 761. Special Binary String
#
# Special binary strings are binary strings with the following two properties:
#
# The number of 0's is equal to the number of 1's.
# Every prefix of the binary string has at least as many 1's as 0's.
# Given a special string S, a move consists of choosing two consecutive, non-empty,
# special substrings of S, and swapping them.
# (Two strings are consecutive if the last character of the first string is exactly
# one index before the first character of the second string.)
#
# At the end of any number of moves, what is the lexicographically largest resulting string possible?
#
# Example 1:
# Input: S = "11011000"
# Output: "11100100"
# Explanation:
# The strings "10" [occuring at S[1]] and "1100" [at S[3]] are swapped.
# This is the lexicographically largest string possible after some number of swaps.
# Note:
#
# S has length at most 50.
# S is guaranteed to be a special binary string as defined above.
#
import unittest

#20ms 100%
class Solution(object):
    def makeLargestSpecial(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S: return S
        mountains = []
        anchor = bal = 0
        for i, x in enumerate(S):
            bal += 1 if x == '1' else -1
            if bal == 0:
                mountains.append("1{}0".format(
                    self.makeLargestSpecial(S[anchor+1: i])))
                anchor = i+1

        mountains.sort(reverse = True)
        return "".join(mountains)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/special-binary-string/solution/
Note: special string:
In such a drawing, "1" is a line up one unit,
and "0" is a line down one unit, bwhere all lines are 45 degrees from horizontal.
Then, a binary string is special if and only if its up and down
drawing does not cross below the starting horizontal line.
Now, say a special binary string is a mountain if it has no special proper prefix.
When viewed through the lens of up and down drawings,
a special binary string is a mountain if it touches the starting horizontal line only at
the very beginning and the very end of the drawing.
Notice that every special string can be written as consecutive mountains.

Approach #1: Recursion [Accepted]
Complexity Analysis
Time Complexity: O(N^2), where N is the length of SS.
Space Complexity: O(N)

In that case, it must start with "1" and end with "0", so the answer is "1" + F([S[1], S[2], ..., S[N-2]]) + "0".

#4ms 100%
class Solution {
    public String makeLargestSpecial(String S) {
        if (S.length() == 0) return S;
        int anchor = 0, bal = 0;
        List<String> mountains = new ArrayList();
        for (int i = 0; i < S.length(); i++) {
            bal += S.charAt(i) == '1' ? 1 : -1;
            if (bal == 0) {
                mountains.add("1" + makeLargestSpecial(S.substring(anchor + 1, i)) + "0");
                anchor = i + 1;
            }
        }

        Collections.sort(mountains, Collections.reverseOrder());
        StringBuilder sb = new StringBuilder();
        for (String mtn : mountains) {
            sb.append(mtn);
        }
        return sb.toString();
    }
}
'''