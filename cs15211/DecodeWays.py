__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/decode-ways.py
# Time:  O(n)
# Space: O(1)
# DP
#
#  Description: Leetcode # 91. Decode Ways
#
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#
# Given an encoded message containing digits, determine the total number of ways to decode it.
#
# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
#
# The number of ways decoding "12" is 2.
#
# Companies
# Microsoft Uber Facebook
# Related Topics
# Dynamic Programming String
# Similar Questions
# Decode Ways II
#
import unittest
class Solution(unittest.TestCase):
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if len(s) == 0 or s[0] == '0':
            return 0
        prev, prevPrev = 1, 0
        for i in range(len(s)):
            current  = 0
            if s[i] != '0':
                current = prev
            if i > 0 and (s[i - 1] == '1' or s[i - 1] == '2' and s[i] <= '6'):
                current += prevPrev
            prev, prevPrev = current, prev
        return prev

    def numDecodingsDP(self, s):
        if len(s) == 0 :
            return 0
        dp = [1] + [0]* len(s)
        print dp
        #lambda anonymous function
        #check if input is between 1~26
        inputCheck = lambda x: x[0] != '0' and int(x) >= 1 and int(x) <= 26

        for i in range(1, len(s) + 1):
            dp[i] = dp[i-1] if inputCheck(s[i-1:i]) else 0
            if i >= 2:
                dp[i] += dp[i-2] if inputCheck(s[i-2:i]) else 0
        return dp[len(s)]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        #test
        #print test.numDecodings("1")
        #print test.numDecodings("12326")
        #print "123"[1:2]
        #print "abc"[0:2]
        self.assertEqual(3, self.numDecodings("123"))
        self.assertEqual(3, self.numDecodingsDP("123"))
        for i in ["0", "10", "10", "103", "1032", "10323","1232"]:
            print Solution().numDecodings(i)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
# 90.08% 1ms
class Solution {
    public int numDecodings(String s) {
        if (s == null || s.length() == 0) return 0;
        char[] a = s.toCharArray();
        int[] dp = new int[s.length()+1];
        dp[0] = 1;
        dp[1] = a[0] == '0' ? 0 : 1;
        for (int i = 1; i < s.length(); i++) {
            if (a[i] != '0') dp[i + 1] = dp[i];
            int temp = (a[i - 1] - '0') * 10 + (a[i] - '0');
            if (temp >= 10 && temp <= 26) dp[i+1] += dp[i - 1];
        }
        return dp[s.length()];
    }
}

I used a dp array of size n + 1 to save subproblem solutions.
dp[0] means an empty string will have one way to decode,
dp[1] means the way to decode a string of size 1.
I then check one digit and two digit combination and save the results along the way.
In the end, dp[n] will be the end result.

# 25.01% 5ms
public class Solution {
    public int numDecodings(String s) {
        if(s == null || s.length() == 0) {
            return 0;
        }
        int n = s.length();
        int[] dp = new int[n+1];
        dp[0] = 1;
        dp[1] = s.charAt(0) != '0' ? 1 : 0;
        for(int i = 2; i <= n; i++) {
            int first = Integer.valueOf(s.substring(i-1, i));
            int second = Integer.valueOf(s.substring(i-2, i));
            if(first >= 1 && first <= 9) {
               dp[i] += dp[i-1];
            }
            if(second >= 10 && second <= 26) {
                dp[i] += dp[i-2];
            }
        }
        return dp[n];
    }
}

#54.77% 4ms
public class Solution {
    public int numDecodings(String s) {
        int n = s.length();
        if (n == 0) return 0;

        int[] memo = new int[n+1];
        memo[n]  = 1;
        memo[n-1] = s.charAt(n-1) != '0' ? 1 : 0;

        for (int i = n - 2; i >= 0; i--)
            if (s.charAt(i) == '0') continue;
            else memo[i] = (Integer.parseInt(s.substring(i,i+2))<=26) ? memo[i+1]+memo[i+2] : memo[i+1];

        return memo[0];
    }
}

# DFS:
# not working
# "101022" should return 2 but get 0
class Solution {
    public int numDecodings(String s) {
        if (s == null || s.length() == 0) return 0;
        return (int)dfs(s, 0, new HashMap<>());
    }

    public Integer dfs(String s, int idx, Map<String, Integer> map) {
        if (idx == s.length()) return 1;
        Integer count = 0;
        for(int i = idx; i < idx + 2 && i < s.length(); i++) {
            String cur = s.substring(idx, i + 1);
            if (cur.startsWith("0")) break;
            if (map.containsKey(cur)) return map.get(cur);
            if (i == s.length() - 1 && cur.equals("10")) count++;
            if (Integer.parseInt(cur) > 0 && Integer.parseInt(cur) <= 26) {
                count += dfs(s, idx + 1, map);
            }
            map.put(cur, count);
        }
        return count;
    }
}
'''