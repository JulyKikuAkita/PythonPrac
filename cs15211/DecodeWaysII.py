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
# 64ms 32.81%
class Solution {
    private static final int M = 1000000007;

    public int numDecodings(String s) {
        long[] dp = new long[s.length() + 1]; // use long to prevent overflow
        dp[0] = 1;
        dp[1] = ways(s.charAt(0));
        for (int i = 1; i < s.length(); i++) { // off-by-one error, notice s.charAt(i)'s result is stored in dp[i + 1]
            long oneCharWays = ways(s.charAt(i)) * dp[i];
            long twoCharWays = ways(s.charAt(i - 1), s.charAt(i)) * dp[i - 1];
            dp[i + 1] = add(oneCharWays, twoCharWays);
        }
        return (int)dp[s.length()];
    }
    
    // function of addition with mod
    private long add(long num1, long num2) {
        return (num1 % M + num2 % M) % M;
    }
    
    // how many ways to decode using one char
    private long ways(char a) {
        return (a == '*') ? 9 : (a != '0') ? 1 : 0;
    }
    
    // how many ways to decode using two chars
    private long ways(char a, char b) {
        if (a == '*' && b == '*') { // "**" neither is digit
            return 15;
        } else if (a == '*') {      // "*D" snd is a digit
            return (b > '6') ? 1 : 2;
        } else if (b == '*') {      // "D*" fst is a digit
            return (a == '1') ? 9 : (a == '2') ? 6 : 0;
        } else {                    // "DD" both r digits
            int val = Integer.valueOf("" + a + b);
            return (val >= 10 && val <= 26) ? 1 : 0;
        }
    }
}

# 35ms 100%
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

# Approach #1 Using Recursion with memoization [Stack Overflow]
# Complexity Analysis
# Time complexity : O(n). Size of recursion tree can go upto n, since memo array is filled exactly once. 
# Here, n refers to the length of the input string.
# Space complexity : O(n). The depth of recursion tree can go upto n.
# 82ms 23.44%
class Solution {
    int M = 1000000007;
    public int numDecodings(String s) {
        long[] memo = new long[s.length()];
        Arrays.fill(memo, -1);
        return (int)ways(s, s.length() - 1, memo);
    }
    
    private long ways(String s, int i, long[] memo) {
        if (i < 0) return 1;
        if (memo[i] != -1) return memo[i];
        if (s.charAt(i) == '*') {
            long res = 9 * ways(s, i - 1, memo);
            if (i > 0 && s.charAt(i - 1) == '1')
                res = (res + 9 * ways(s, i - 2,memo)) % M;
            else if (i > 0 && s.charAt(i - 1) == '2')
                res = (res + 6 * ways(s, i - 2,memo)) % M;
            else if (i > 0 && s.charAt(i - 1) == '*')
                res = (res + 15 * ways(s, i - 2,memo)) % M;
            memo[i] = res;
            return memo[i];
        }
        long res = s.charAt(i) != '0' ? ways(s, i - 1, memo) : 0;
        if (i > 0 && s.charAt(i - 1) == '1')
            res = (res + ways(s, i - 2, memo)) % M;
        else if (i > 0 && s.charAt(i - 1) == '2' && s.charAt(i) <= '6')
            res = (res + ways(s, i - 2, memo)) % M;
        else if (i > 0 && s.charAt(i - 1) == '*')
            res = (res + (s.charAt(i) <= '6' ? 2 : 1) * ways(s, i - 2, memo)) % M;
        memo[i]= (int)res;
        return memo[i];
    }
}

# Approach #2 Dynamic Programming [Accepted]
# Time complexity : O(n). dp array of size n+1 is filled once only. Here, nn refers to the length of the input string.
# Space complexity : O(n). dp array of size n+1 is used.
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

# Approach #3 Constant Space Dynamic Programming [Accepted]:
# Complexity Analysis
# Time complexity : O(n). Single loop upto n is required to find the required result. 
# Here, n refers to the length of the input string s.
# Space complexity : O(1). Constant space is used.
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

# https://leetcode.com/problems/decode-ways-ii/discuss/200629/27ms-Java-solution-with-succinct-explanation.
# More DP Example
# 58ms 43.75%
class Solution {
    // - Examples:
    // Ways to decode the last one digit w/ or w/o the previous digit to one single leter:
    // 1. xxx12 -> w/o previous digit: (B); w/ previous digit: (L)
    // 2. xxx*1 -> w/o previous digit: (A); w/ preious digit: [11](K), [21](U)
    // 3. xxx1* -> w/o previous digit: (A),(B),...,(I); w/ the previous digit: [10](J), ..., [19](S)
    // 4. xxx** -> w/o previous digit: (A),(B),...,(I); w/ the previous digit: [10](J), ..., [19](S), [20](T), ..., [26](Z).
    
    // - Design of Algorithms
    // Use dynamic programming approuch:
    // To remember for each length of string, how many ways of decoding. 
    // If the current digit is number, it can be used as one letter by itseft, or be combined with previous digit to be used as one letter (2/3 possibilities) based on the current digit, if the previous letter is smaller than 3, or is *.
    // If the current number is *, it can be used as 9 possible single letter, or combined with the previous digit to be used as single letter, if previous number is smaller than 3.
    
    // - Trick:
    // 1. Beyond that, now the encoded string can also contain the character '*', which can be treated as one of the numbers from 1 to 9. It is NOT from 0.
    public int numDecodings(String s) {
        long[] dpm = new long[s.length()+1];
        dpm[0] = 1;
        char[] charArray = s.toCharArray();
        long LETTERS_SMALLER_THAN_TEN = 9;
        long LETTERS_BIGGER_THAN_NINE_NO_DIGIT_IS_ZERO = 26-9-2; 
        long LETTERS_BIGGER_THAN_TWENTY_SMALLER_THAN_TWENTY_SEVEN = 26-20;
        long LETTERS_BIGGER_THAN_TEN_SMALLER_THAN_TENTY = 19-10;
        long MOD_BASE = 1000_000_007L;
        for(int i = 0; i < s.length(); i++) {
            char c = charArray[i];
            if (c == '*') {
                dpm[i+1] += LETTERS_SMALLER_THAN_TEN * dpm[i]; // w/o previous letter: 1-9
                if(i > 0) { // w/ previous letter
                    if (charArray[i-1] == '*') {
                        dpm[i+1] += LETTERS_BIGGER_THAN_NINE_NO_DIGIT_IS_ZERO * dpm[i-1];
                    } else if(charArray[i-1] == '2') {
                        dpm[i+1] += LETTERS_BIGGER_THAN_TWENTY_SMALLER_THAN_TWENTY_SEVEN * dpm[i-1]; // 21-26
                    } else if(charArray[i-1] == '1') {
                        dpm[i+1] += LETTERS_BIGGER_THAN_TEN_SMALLER_THAN_TENTY * dpm[i-1]; // 11-19
                    }
                }
            } else { // current digit is number
                dpm[i+1] += c == '0' ? 0 : dpm[i]; // w/o previous letter
                if(i > 0) { // w/ previous letter
                    if (charArray[i-1] == '*') {
                        dpm[i+1] += (c < '7' ? 2 : 1) * dpm[i-1];
                    } else if(charArray[i-1] == '2') {
                        dpm[i+1] += (c < '7' ? 1 : 0) * dpm[i-1];
                    } else if(charArray[i-1] == '1') {
                        dpm[i+1] += dpm[i-1];
                    }
                }
            }
            dpm[i+1] = dpm[i+1] % MOD_BASE;
        }
        return (int)dpm[s.length()];
    }
}

# https://discuss.leetcode.com/topic/95518/java-o-n-by-general-solution-for-all-dp-problems
# Bottome-up DP

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
