__source__ = 'https://leetcode.com/problems/decode-ways/description/'
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
# https://leetcode.com/problems/decode-ways/discuss/30451/Evolve-from-recursion-to-dp

# DFS:
# 8ms 10.85%
class Solution {

    public int numDecodings(String s) {
        if( s == null || s.length() == 0) return 0;
        Map<String, Integer> map = new HashMap<>();
        return dfs(s, map);
    }

    private int dfs(String s, Map<String, Integer> map) {
        if (s.isEmpty()) return 1;
        if (s.length() == 1) return s.charAt(0) == '0' ? 0 : 1;
        if ( map.containsKey(s)) return map.get(s);

        int count = 0;
        int fir = Integer.parseInt(s.substring(s.length() - 1, s.length()));
        if (fir >= 1 && fir <= 9) count += dfs(s.substring(0, s.length() - 1), map);

        if (s.length() > 1) {
            int sec = Integer.parseInt(s.substring(s.length() - 2));
            if (sec >= 10 && sec <= 26) {
                count += dfs(s.substring(0, s.length() - 2), map);
            }
        }
        map.put(s, count);
        return count;
    }
}

# DFS Top-down
# 4ms 62.59%
class Solution {
    public int numDecodings(String s) {
        if (s == null || s.length() == 0) return 0;
        return dfs(s.toCharArray(), 1, new HashMap());
    }
    
    // top down, be aware of idx
    // edge case: "10", "01", "00"
    private int dfs(char[] s, int idx, Map<Integer, Integer> map) {
        if (idx == s.length + 1) return 1;
        if (idx == s.length ) return s[idx -1] == '0' ? 0 : 1;
        if (map.containsKey(idx)) return map.get(idx);
        int count = 0;
        if (s[idx - 1] >= '1' && s[idx - 1] <= '9') count = dfs(s, idx + 1, map);
        if (s[idx - 1] != '0') { //'05' is not a qualified double digit 
            int doubleDigits = (s[idx - 1] - '0') * 10 + s[idx] - '0';
            if (doubleDigits >= 1 && doubleDigits <= 26) count += dfs(s, idx + 2, map);
        }
        map.put(idx, count);
        return count;
    }
}

# DFS Bottom up Geek for Geek
# 4ms 62.59%
class Solution {
    public int numDecodings(String s) {
        if (s == null || s.length() == 0) return 0;
        return dfs(s.toCharArray(), s.length(), new HashMap());
    }
    
    private int dfs(char[] s, int idx, Map<Integer, Integer> map) {
        if (idx == 0) return 1;
        if (idx == 1) return s[0] == '0' ? 0 : 1;
        if (map.containsKey(idx)) return map.get(idx);
        int count = 0;
        
        //If we have a non zero number located at the last digit of the string, then recurse on the rest
        if (s[idx - 1] >= '1' && s[idx - 1] <= '9') count += dfs(s, idx - 1, map);
        
        //Count the last 2 digits of the number
        if (s[idx - 2] == '1' || (s[idx - 2] == '2' && s[idx - 1] <= '6')) count += dfs(s, idx - 2, map);
        map.put(idx, count);
        return count;
    }
}

# convert to DP
dp[i + 1] = dp[i]
dp[i + 1] = dp[i - 1] + dp[i + 1]

# 1ms 96.14%
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

# 1. Recursion O(2^n)
# 580ms 7%
class Solution {
    public int numDecodings(String s) {
        return s.length() == 0 ? 0 : dfs(0, s.toCharArray());   
    }
    
    private int dfs(int i, char[] s) {
        int n = s.length;
        if (i == n) return 1;
        if (s[i] == '0') return 0;
        int res = dfs(i + 1, s);
        if (i < n - 1 && (s[i] == '1' || s[i] == '2' && s[i + 1] < '7')) res += dfs(i + 2, s);
        return res;
    }
}

# 2. Memoization O(n)
# 2ms 92.16%
class Solution {
    public int numDecodings(String s) {
        int n = s.length();
        int[] memo = new int[n + 1];
        Arrays.fill(memo, -1);
        memo[n] = 1;
        return s.length() == 0 ? 0 : dfs(0, s.toCharArray(), memo);   
    }
    
    private int dfs(int i, char[] s, int[] memo) {
        if (memo[i] > -1) return memo[i];
        if (s[i] == '0') return memo[i] = 0;
        int res = dfs(i + 1, s, memo);
        if (i < s.length - 1 && (s[i] == '1' || s[i] == '2' && s[i + 1] < '7')) res += dfs(i + 2, s, memo);
        return memo[i] = res;
    }
}

# 3. DP O(n) time and space, this can be converted from #2 with copy and paste.
# 1ms 100%
class Solution {
    public int numDecodings(String s) {
        int n = s.length();
        char[] arr = s.toCharArray();
        int[] dp = new int[n + 1];
        dp[n] = 1;
        for (int i  = n - 1; i >= 0; i--) {
            if (arr[i] == '0') dp[i] = 0;
            else {
                dp[i] = dp[i + 1];
                if (i < n - 1 && (arr[i] == '1' || arr[i] == '2' && arr[i + 1] < '7')) dp[i] += dp[ i + 2];
            }
        }
        return dp[0];
    }
}

# 4. DP constant space
# 1ms 100%
class Solution {
    public int numDecodings(String s) {
        int p = 1, pp = 0, n = s.length();
        char[] arr = s.toCharArray();
        for (int i  = n - 1; i >= 0; i--) {
            int cur = arr[i] == '0' ? 0 : p;
            if (i < n - 1 && (arr[i] == '1' || arr[i] == '2' && arr[i + 1] < '7')) cur += pp;
            pp = p;
            p = cur;
        }
        return p;
    }
}
'''
