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
#
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

# 604ms 87.14%
class Solution(object):
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
# Thought: https://leetcode.com/problems/decode-ways-ii/solution/

# DFS TLE

# Wrong ans
#
# Input: "**********1111111111"
# Output: 881150112
# Expected: 133236775

class Solution {
    int M = 1000000007;
    public int numDecodings(String s) {
        Integer[] memo=new Integer[s.length()];
        return ways(s, s.length() - 1,memo);
    }
    public int ways(String s, int i,Integer[] memo) {
        if (i < 0)
            return 1;
        if(memo[i]!=null)
            return memo[i];
        if (s.charAt(i) == '*') {
            long res = 9 * ways(s, i - 1,memo);
            if (i > 0 && s.charAt(i - 1) == '1')
                res = (res + 9 * ways(s, i - 2,memo)) % M;
            else if (i > 0 && s.charAt(i - 1) == '2')
                res = (res + 6 * ways(s, i - 2,memo)) % M;
            else if (i > 0 && s.charAt(i - 1) == '*')
                res = (res + 15 * ways(s, i - 2,memo)) % M;
            memo[i]=(int)res;
            return memo[i];
        }
        long res = s.charAt(i) != '0' ? ways(s, i - 1,memo) : 0;
        if (i > 0 && s.charAt(i - 1) == '1')
            res = (res + ways(s, i - 2,memo)) % M;
        else if (i > 0 && s.charAt(i - 1) == '2' && s.charAt(i) <= '6')
            res = (res + ways(s, i - 2,memo)) % M;
        else if (i > 0 && s.charAt(i - 1) == '*')
                res = (res + (s.charAt(i)<='6'?2:1) * ways(s, i - 2,memo)) % M;
        memo[i]= (int)res;
        return memo[i];
    }
}


# 25ms 95.22%
class Solution {
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

# 32ms 71.50%
class Solution {
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

# 24ms 97.88%
class Solution {
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

https://discuss.leetcode.com/topic/95518/java-o-n-by-general-solution-for-all-dp-problems
#Bottome-up DP

Here, I try to provide not only code but also the steps and thoughts of solving this problem completely
which can also be applied to many other DP problems.

(1) Try to solve this problem in Backtracking way, because it is the most straight-forward method.

 E.g '12*3'
                   12*3
              /             \
           12*(3)           12(*3)
         /     \            /      \
    12(*)(3)  1(2*)(3)  1(2)(*3)   ""
      /    \      \       /
1(2)(*)(3) ""     ""     ""
    /
   ""
(2) There are many nodes visited multiple times, like 12 and 1. Most importantly,
the subtree of those nodes are "exactly" the same.
The backtracking solution possibly can be improved by DP. Try to merge the same nodes.

        12*3
        /  \
      12*  |
       | \ |
       |  12
       | / |
       1   |
        \  |
          ""
(3) Successfully merge those repeated nodes and find out the optimal substructure, which is:

      current state = COMBINE(next state ,  next next state)
      e.g
              12*
              / \
            COMBINE (few different conditions)
            /     \
           12      1
Therefore, we can solve this problem by DP in bottom-up way instead of top-down memoization.
Now, we formulate the optimal substructure:

    dp[i] = COMBINE dp[i-1] and dp[i-2]
where dp[i] --> number of all possible decode ways of substring s(0 : i-1). Just keep it in mind.
But we need to notice there are some different conditions for this COMBINE operation.

(4) The pseudo code of solution would be:

Solution{
    /* initial conditions */
    dp[0] = ??
       :

    /* bottom up method */
    foreach( i ){
        dp[i] = COMBINE dp[i-1] and dp[i-2] ;
    }

    /* Return */
    return dp[last];
}
The COMBINE part will be something like:

    // for dp[i-1]
    if(condition A)
        dp[i] +=??  dp[i-1];
    else if(condition B)
        dp[i] +=??  dp[i-1];
            :
            :

     // for dp[i-2]
    if(condition C)
        dp[i] +=?? dp[i-2];
    else if(condition D)
        dp[i] +=?? dp[i-2];
             :
(5) The core step of this solution is to find out all possible conditions
and their corresponding operation of combination.

        For dp[i-1]:

                  /           \
                 /             \
            s[i-1]='*'    s[i-1]>0
                |               |
          + 9*dp[i-1]        + dp[i-1]


        For dp[i-2]:

                   /                                  \
                  /                                    \
              s[n-2]='1'||'2'                         s[n-2]='*'
              /            \                       /             \
        s[n-1]='*'         s[n-1]!='*'          s[n-1]='*'       s[n-1]!='*'
         /       \               |                  |              /         \
  s[n-2]='1'  s[n-2]='2'   num(i-2,i-1)<=26         |         s[n-1]<=6    s[n-1]>6
      |            |             |                  |              |            |
 + 9*dp[i-2]   + 6*dp[i-2]     + dp[i-2]       + 15*dp[i-2]    + 2*dp[i-2]   + dp[i-2]

(6) Fill up the initial conditions before i = 2.
Because we need to check if num(i-2,i-1)<=26 for each i, we make the bottom-up process to begin from i=2.
Just fill up the dp[0] and dp[1] by observation and by the definition of dp[i] --> number of
all possible decode ways of substring s(0 : i-1).

         dp[0]=1;
         /      \
    s[0]=='*'  s[0]!='*'
        |         |
    dp[1]=9     dp[1]=1

(7) The final Solution:

# 24ms 97.88%
class Solution {
    public int numDecodings(String s) {
        /* initial conditions */
        long[] dp = new long[s.length()+1];
        dp[0] = 1;
        if(s.charAt(0) == '0'){
            return 0;
        }
        dp[1] = (s.charAt(0) == '*') ? 9 : 1;

        /* bottom up method */
        for(int i = 2; i <= s.length(); i++){
            char first = s.charAt(i-2);
            char second = s.charAt(i-1);

            // For dp[i-1]
            if(second == '*'){
                dp[i] += 9*dp[i-1];
            }else if(second > '0'){
                dp[i] += dp[i-1];
            }

            // For dp[i-2]
            if(first == '*'){
                if(second == '*'){
                    dp[i] += 15*dp[i-2];
                }else if(second <= '6'){
                    dp[i] += 2*dp[i-2];
                }else{
                    dp[i] += dp[i-2];
                }
            }else if(first == '1' || first == '2'){
                if(second == '*'){
                    if(first == '1'){
                       dp[i] += 9*dp[i-2];
                    }else{ // first == '2'
                       dp[i] += 6*dp[i-2];
                    }
                }else if( ((first-'0')*10 + (second-'0')) <= 26 ){
                    dp[i] += dp[i-2];
                }
            }

            dp[i] %= 1000000007;
        }
        /* Return */
        return (int)dp[s.length()];
    }
}

P.S The space complexity can be further improved to O(1)
because the current state i is only related to i-1 and i-2 during the bottom-up.

'''