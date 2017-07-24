__source__ = 'https://leetcode.com/problems/decode-ways-ii/description/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 639. Decode Ways II
#
# A message containing letters from A-Z is being encoded to numbers using the following mapping way:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Beyond that, now the encoded string can also contain the character '*',
# which can be treated as one of the numbers from 1 to 9.
#
# Given the encoded message containing digits and the character '*', return the total number of ways to decode it.
#
# Also, since the answer may be very large, you should return the output mod 109 + 7.
#
# Example 1:
# Input: "*"
# Output: 9
# Explanation: The encoded message can be decoded to the string: "A", "B", "C", "D", "E", "F", "G", "H", "I".
# Example 2:
# Input: "1*"
# Output: 9 + 9 = 18
# Note:
# The length of the input string will fit in range [1, 105].
# The input string will only contain the character '*' and digits '0' - '9'.
# Companies
# Facebook
# Related Topics
# Dynamic Programming
# Similar Questions
# Decode Ways
#

import unittest

# Let's keep track of:
#
# e0 = current number of ways we could decode, ending on any number;
# e1 = current number of ways we could decode, ending on an open 1;
# e2 = current number of ways we could decode, ending on an open 2;
# (Here, an "open 1" means a 1 that may later be used as the first digit of a 2 digit number,
# because it has not been used in a previous 2 digit number.)
#
# With the right idea of what to keep track of, our dp proceeds straightforwardly.
#
# Say we see some character c. We want to calculate f0, f1, f2, the corresponding versions of e0, e1, e2
# after parsing character c.
#
# If c == '*', then the number of ways to finish in total is: we could put * as a single digit number (9*e0),
# or we could pair * as a 2 digit number 1* in 9*e1 ways, or we could pair * as a 2 digit number 2* in 6*e2 ways.
# The number of ways to finish with an open 1 (or 2) is just e0.
#
# If c != '*', then the number of ways to finish in total is: we could put c as a single digit if it is not zero
# ((c>'0')*e0), or we could pair c with our open 1, or we could pair c with our open 2
# if it is 6 or less ((c<='6')*e2).
# The number of ways to finish with an open 1 (or 2) is e0 iff c == '1' (or c == '2').
class Solution(object):
    # 952ms
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        e0, e1, e2 = 1, 0, 0
        for c in s:
            if c == '*':
                f0 = 9*e0 + 9*e1 + 6*e2
                f1 = e0
                f2 = e0
            else:
                f0 = (c > '0') * e0 + e1 + (c <= '6') * e2
                f1 = (c == '1') * e0
                f2 = (c == '2') * e0
            e0, e1, e2 = f0 % MOD, f1, f2
        return e0
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/decode-ways-ii/solution/
# 98.39% 45ms
public class Solution {
    static final int[][] map = new int[58][58];
    static {
        Arrays.fill(map['*'], 1);
        map['*']['*'] = 15;
        map['*']['0'] = 2;
        map['*']['1'] = 2;
        map['*']['2'] = 2;
        map['*']['3'] = 2;
        map['*']['4'] = 2;
        map['*']['5'] = 2;
        map['*']['6'] = 2;
        Arrays.fill(map['1'], 1);
        map['1']['*'] = 9;
        Arrays.fill(map['2'], 1);
        map['2']['*'] = 6;
        map['2']['7'] = 0;
        map['2']['8'] = 0;
        map['2']['9'] = 0;
        Arrays.fill(map[0], 1);
        map[0]['*'] = 9;
        map[0]['0'] = 0;
    }

    public int numDecodings(String s) {
        long cur = 1, pre = 0;
        char ch = 0, ch1 = '0';
        for (int i = s.length() - 1; i >= 0; i--) {
            ch = s.charAt(i);
            cur = (map[ch][ch1] * pre + map[0][(ch1 = ch)] * (pre = cur)) % 1000000007;
        }

        return (int) cur;
    }
}

# 76.81% 60ms
public class Solution {
    int M = 1000000007;
    public int numDecodings(String s) {
        long[] dp = new long[s.length() + 1];
        dp[0] = 1;
        dp[1] = s.charAt(0) == '*' ? 9 : s.charAt(0) == '0' ? 0 : 1;
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == '*') {
                dp[i + 1] = 9 * dp[i];
                if (s.charAt(i - 1) == '1')
                    dp[i + 1] = (dp[i + 1] + 9 * dp[i - 1]) % M;
                else if (s.charAt(i - 1) == '2')
                    dp[i + 1] = (dp[i + 1] + 6 * dp[i - 1]) % M;
                else if (s.charAt(i - 1) == '*')
                    dp[i + 1] = (dp[i + 1] + 15 * dp[i - 1]) % M;
            } else {
                dp[i + 1] = s.charAt(i) != '0' ? dp[i] : 0;
                if (s.charAt(i - 1) == '1')
                    dp[i + 1] = (dp[i + 1] + dp[i - 1]) % M;
                else if (s.charAt(i - 1) == '2' && s.charAt(i) <= '6')
                    dp[i + 1] = (dp[i + 1] + dp[i - 1]) % M;
                else if (s.charAt(i - 1) == '*')
                    dp[i + 1] = (dp[i + 1] + (s.charAt(i) <= '6' ? 2 : 1) * dp[i - 1]) % M;
            }
        }
        return (int) dp[s.length()];
    }
}

#55.62% 70ms
public class Solution {
    public int numDecodings(String s) {
        if (s == null || s.length() == 0 || s.charAt(0) == '0') {
            return 0;
        }
        long first = 1;
        long second = s.charAt(0) == '*' ? 9 : 1;
        for (int i = 1; i < s.length(); i++) {
            long third = 0;
            char ch = s.charAt(i);
            char prevCh = s.charAt(i - 1);
            if (ch == '*') {
                third = 9 * second;
            } else if (ch != '0') {
                third = second;
            }

            if (prevCh == '1' || prevCh == '*') {
                if (ch == '*') {
                    third += 9 * first;
                } else {
                    third += first;
                }
            }
            if ((prevCh == '2' || prevCh == '*')) {
                 if (ch == '*') {
                     third += 6 * first;
                 } else if (ch < '7') {
                     third += first;
                 }
            }
            first = second;
            second = third % 1000000007;
        }
        return (int) second;
    }
}
'''