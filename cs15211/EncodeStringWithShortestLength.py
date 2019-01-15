__source__ = 'https://github.com/kamyu104/LeetCode/blob/master/Python/encode-string-with-shortest-length.py'
# Time:  O(n^3) on average
# Space: O(n^2)
#
# Description: 471. Encode String with Shortest Length
#
# Given a non-empty string, encode the string such that its encoded length is the shortest.
#
# The encoding rule is: k[encoded_string],
# where the encoded_string inside the square brackets is being repeated exactly k times.
#
# Note:
# k will be a positive integer and encoded string will not be empty or have extra space.
# You may assume that the input string contains only lowercase English letters.
# The string's length is at most 160.
# If an encoding process does not make the string shorter, then do not encode it.
# If there are several solutions, return any of them is fine.
# Example 1:
#
# Input: "aaa"
# Output: "aaa"
# Explanation: There is no way to encode it such that it is shorter than the input string,
# so we do not encode it.
# Example 2:
#
# Input: "aaaaa"
# Output: "5[a]"
# Explanation: "5[a]" is shorter than "aaaaa" by 1 character.
# Example 3:
#
# Input: "aaaaaaaaaa"
# Output: "10[a]"
# Explanation: "a9[a]" or "9[a]a" are also valid solutions, both of them have the same length = 5,
# which is the same as "10[a]".
# Example 4:
#
# Input: "aabcaabcd"
# Output: "2[aabc]d"
# Explanation: "aabc" occurs twice, so one answer can be "2[aabc]d".
# Example 5:
#
# Input: "abbbabbbcabbbabbbc"
# Output: "2[2[abbb]c]"
# Explanation: "abbbabbbc" occurs twice, but "abbbabbbc" can also be encoded to "2[abbb]c",
# so one answer can be "2[2[abbb]c]".
# Hide Company Tags Google
# Hide Tags Dynamic Programming
# Hide Similar Problems (M) Decode String

import unittest

class Solution(object):
    def encode(self, s):
        """
        :type s: str
        :rtype: str
        """
        def encode_substr(dp, s, i, j):
            temp = s[i:j+1]
            pos = (temp + temp).find(temp, 1)  # O(n) on average
            if pos >= len(temp):
                return temp
            return str(len(temp)/pos) + '[' + dp[i][i + pos - 1] + ']'

        dp = [["" for _ in xrange(len(s))] for _ in xrange(len(s))]
        for length in xrange(1, len(s)+1):
            for i in xrange(len(s)+1-length):
                j = i+length-1
                dp[i][j] = s[i:i+length]
                for k in xrange(i, j):
                    if len(dp[i][k]) + len(dp[k+1][j]) < len(dp[i][j]):
                        dp[i][j] = dp[i][k] + dp[k+1][j]
                encoded_string = encode_substr(dp, s, i, j)
                if len(encoded_string) < len(dp[i][j]):
                    dp[i][j] = encoded_string
        return dp[0][len(s) - 1]
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

Why condition (s+s).find(s,1) < s.size() is equivalent to substring repetition?

Proof: Let N = s.size() and L := (s+s).find(s,1), actually we can prove that the following 2 statements are equivalent:

0 < L < N;
N%L == 0 and s[i] == s[i%L] is true for any i in [0, N). (which means s.substr(0,L) is the repetitive substring)
Consider function char f(int i) { return s[i%N]; }, obviously it has a period N.

"1 => 2": From condition 1, we have for any i in [0,N)

s[i] == (s+s)[i+L] == s[(i+L)%N],
which means L is also a positive period of function f. Note that N == L*(N/L)+N%L, so we have
f(i) == f(i+N) == f(i+L*(N/L)+N%L) == f(i+N%L),
which means N%L is also a period of f. Note that N%L < L but L := (s+s).find(s,1)
is the minimum positive period of function f, so we must have N%L == 0. Note that i == L*(i/L)+i%L, so we have
s[i] == f(i) == f(L*(i/L)+i%L) == f(i%L) == s[i%L],
so condition 2 is obtained.
"2=>1": If condition 2 holds, for any i in [0,N), note that N%L == 0, we have

(s+s)[i+L] == s[(i+L)%N] == s[((i+L)%N)%L] == s[(i+L)%L] == s[i],
which means (s+s).substr(L,N) == s, so condition 1 is obtained.



 We will form 2-D array of Strings.
dp[i][j] = string from index i to index j in encoded form.

We can write the following formula as:-
dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j]) or if we can find some pattern in string from i to j
which will result in more less length.

Time Complexity = O(n^3)

# 313ms 13.44%
class Solution {
    public String encode(String s) {
        String[][] dp = new String[s.length()][s.length()];

        for(int l=0;l<s.length();l++) {
            for(int i=0;i<s.length()-l;i++) {
                int j = i+l;
                String substr = s.substring(i, j+1);
                // Checking if string length < 5. In that case, we know that encoding will not help.
                if(j - i < 4) {
                    dp[i][j] = substr;
                } else {
                    dp[i][j] = substr;
                    // Loop for trying all results that we get after dividing the strings into 2 and combine the
                    //results of 2 substrings
                    for(int k = i; k<j;k++) {
                        if((dp[i][k] + dp[k+1][j]).length() < dp[i][j].length()){
                            dp[i][j] = dp[i][k] + dp[k+1][j];
                        }
                    }

                    // Loop for checking if string can itself found some pattern in it which could be repeated.
                    for(int k=0;k<substr.length();k++) {
                        String repeatStr = substr.substring(0, k+1);
                        if(repeatStr != null
                           && substr.length()%repeatStr.length() == 0
                           && substr.replaceAll(repeatStr, "").length() == 0) {
                              String ss = substr.length()/repeatStr.length() + "[" + dp[i][i+k] + "]";
                              if(ss.length() < dp[i][j].length()) {
                                dp[i][j] = ss;
                              }
                         }
                    }
                }
            }
        }

        return dp[0][s.length()-1];
    }
}
'''