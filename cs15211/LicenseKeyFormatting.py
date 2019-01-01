__source__ = 'https://leetcode.com/problems/license-key-formatting/'
# Time:  O(n)
# Space: O(n)
#
# Description: 482. License Key Formatting
#
# Now you are given a string S,
# which represents a software license key which we would like to format.
# The string S is composed of alphanumerical characters and dashes.
# The dashes split the alphanumerical characters within the string into groups.
# (i.e. if there are M dashes, the string is split into M+1 groups).
# The dashes in the given string are possibly misplaced.
#
# We want each group of characters to be of length K (except for possibly the first group,
# which could be shorter, but still must contain at least one character).
# To satisfy this requirement, we will reinsert dashes. Additionally,
# all the lower case letters in the string must be converted to upper case.
#
# So, you are given a non-empty string S, representing a license key to format,
# and an integer K. And you need to return the license key formatted according to the description above.
#
# Example 1:
# Input: S = "2-4A0r7-4k", K = 4
#
# Output: "24A0-R74K"
#
# Explanation: The string S has been split into two parts, each part has 4 characters.
# Example 2:
# Input: S = "2-4A0r7-4k", K = 3
#
# Output: "24-A0R-74K"
#
# Explanation: The string S has been split into three parts, each part has 3 characters
# except the first part as it could be shorter as said above.
# Note:
# The length of string S will not exceed 12,000, and K is a positive integer.
# String S consists only of alphanumerical characters (a-z and/or A-Z and/or 0-9) and dashes(-).
# String S is non-empty.
# Hide Company Tags Google
#
import unittest
# 1040ms 31.45%
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.upper().replace('-','')
        size = len(S)
        s1 = K if size%K==0 else size%K
        res = S[:s1]
        while s1<size:
            res += '-'+S[s1:s1+K]
            s1 += K
        return res

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# 225ms 17.29%
class Solution {
    public String licenseKeyFormatting(String S, int K) {
        String s1 = S.replace("-", "");
        s1 = s1.toUpperCase();
        
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s1.length(); i++) sb.append(s1.charAt(i));
        int len = sb.length();
        for (int i = K; i < len; i += K) {
            sb.insert(len - i, '-');
        }
        return sb.toString();
    }
}

# 16ms 82.10%
class Solution {
    public String licenseKeyFormatting(String S, int K) {
        int cnt = 0;
        StringBuilder sb = new StringBuilder();
        char[] arr = S.toCharArray();
        for(int i = arr.length - 1; i >= 0; i--) {
            char c = arr[i];
            if (c == '-') {
                continue;
            }
            if (cnt % K == 0 && cnt != 0) {
                sb.append('-');
            }
            sb.append('a' <= c && c <= 'z' ? (char)(c - 'a' + 'A') : c);
            cnt++;
        }
        return sb.reverse().toString();
    }
}
'''
