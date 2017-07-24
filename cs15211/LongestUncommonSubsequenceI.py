__source__ = 'https://leetcode.com/problems/longest-uncommon-subsequence-i/#/description'
# Time:  O(n) or O(min(x,y)), more precisely
# O(|a| if |a|==|b| else 1) due to  equals probably only compares the characters if the lengths are the same
# Space: O(1)
#
# Description: Leetcode # 521. Longest Uncommon Subsequence I
#
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
# Companies
# Google
# Related Topics
# String
# Similar Questions
# Longest Uncommon Subsequence II
#
import unittest
#49ms
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
These three cases are possible with string a and b:

1) a == b If both the strings are identical, it is obvious that no subsequence will be uncommon. Hence, return -1.

2) length(a)=length(b) and a != b. Example: abcabc and abdabd.
In this case we can consider any string i.e. abcabc or abdabd as a required subsequence,
as out of these two strings one string will never be a subsequence of other string.
Hence, return length(a) or length(b).

3) length(a) != length(b). Example abcdabcd and abcabc.
In this case we can consider bigger string as a required subsequence because bigger string can't be a
subsequence of smaller string. Hence, return max(length(a),length(b))max(length(a),length(b)).

Approach #2 Simple Solution[Accepted]
Time complexity : O(min(x,y)). where x and y are the lengths of strings a and b respectively.
    Here equals method will take min(x,y) time .
Space complexity : O(1). No extra space require

#59.97% 3ms
public class Solution {
    public int findLUSlength(String a, String b) {
        return a.equals(b) ? -1 : Math.max(a.length(), b.length());
    }
}

# Approach #1 Brute Force [Time Limit Exceeded]
In the brute force approach we will generate all the possible 2 ^n subsequences of both the strings
and store their number of occurences in a hashmap.
Longest subsequence whose frequency is equal to 11 will be the required subsequence.
And, if it is not found we will return -1.

Time complexity : O(2^x+2^y). where x and y are the lengths of strings aa and bb respectively .
Number of subsequences will be 2^x+2^y
Space complexity : O(2^x+2^y) 2^x+2^y subsequences will be generated.

public class Solution {
    public int findLUSlength(String a, String b) {
        HashMap < String, Integer > map = new HashMap < > ();
        for (String s: new String[] {a, b}) {
            for (int i = 0; i < (1 << s.length()); i++) {
                String t = "";
                for (int j = 0; j < s.length(); j++) {
                    if (((i >> j) & 1) != 0)
                        t += s.charAt(j);
                }
                if (map.containsKey(t))
                    map.put(t, map.get(t) + 1);
                else
                    map.put(t, 1);
            }
        }
        int res = -1;
        for (String s: map.keySet()) {
            if (map.get(s) == 1)
                res = Math.max(res, s.length());
        }
        return res;
    }
}
'''