__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/decode-ways.py
# Time:  O(n)
# Space: O(1)
# DP
#
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.
#
# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
#
# The number of ways decoding "12" is 2.
#
# Microsoft Uber Facebook
# Dynamic Programming String

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

    def test(self):
        #test
        #print test.numDecodings("1")
        #print test.numDecodings("12326")
        #print "123"[1:2]
        #print "abc"[0:2]
        self.assertEqual(3, self.numDecodings("123"))
        self.assertEqual(3, self.numDecodingsDP("123"))


if __name__ == '__main__':
     for i in ["0", "10", "10", "103", "1032", "10323","1232"]:
        print Solution().numDecodings(i)

#java
js = '''
public class Solution {
    public int numDecodings(String s) {
        char[] arr = s.toCharArray();
        int len = arr.length;
        if (len == 0 || arr[0] == '0') {
            return 0;
        }
        int[] dp = new int[2];
        Arrays.fill(dp, 1);
        for (int i = 1; i < len; i++) {
            int cur = 1 - i & 1;
            if (arr[i] == '0') {
                if (arr[i - 1] == '0' || arr[i - 1] > '2') {
                    return 0;
                }
            } else if (arr[i - 1] == '0' || arr[i - 1] > '2' || (arr[i - 1] == '2' && arr[i] > '6')) {
                dp[cur] = dp[1 - cur];
            } else {
                dp[cur] += dp[1 - cur];
            }
        }
        return dp[len & 1];
    }
}

public class Solution {
    public int numDecodings(String s) {
        char[] arr = s.toCharArray();
        int len = arr.length;
        if( len == 0 || arr[0] == '0') return 0;

        int[] dp = new int[len +1];
        dp[0] = 1;
        for(int i = 1; i <= len; i++){
           if(check(arr, i-1, i)){
               dp[i] = dp[i-1];
           }
           if( i >= 2 && check(arr, i-2, i)){
               dp[i] += dp[i-2];
           }
        }
        return dp[len];
    }

    private boolean check(char[] arr, int start, int end){
        if(arr[start] == '0') return false;
        int cur = 0;
        for(int i = start ; i < end ; i++){
             cur *= 10;
             cur += arr[i] - '0';
             if (cur > 26 ||cur <= 0) return false;
        }
        return true;
    }
}
'''