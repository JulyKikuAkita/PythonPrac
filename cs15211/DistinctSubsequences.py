__source__ = 'https://leetcode.com/problems/distinct-subsequences/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/distinct-subsequences.py
# Time:  O(n^2)
# Space: O(n)
# DP
#
# Description: Leetcode # 115. Distinct Subsequences
#
# Given a string S and a string T, count the number of distinct subsequences of T in S.
#
# A subsequence of a string is a new string which is formed from the original string
# by deleting some (can be none) of the characters without disturbing the relative positions
# of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
#
# Here is an example:
# S = "rabbbit", T = "rabbit"
#
# Return 3.
#
# Related Topics
# Dynamic Programming String
#
# Thought:
# When you see string problem that is about subsequence or matching,
# dynamic programming method should come to your mind naturally.
# The key is to find the changing condition.
#
import unittest
class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        ways = [0 for _ in xrange(len(T) + 1)]
        ways[0] = 1
        for S_char in S:
            for j, T_char in reversed(list(enumerate(T))):  # why need to go reversed?
                                                            # consider s = ddd, t = dd, if not reversed, ans = 6 (x)
                                                            # if reversed, ans = 3 (o)
                if S_char == T_char:
                    ways[j + 1] += ways[j]
        return ways[len(T)]

# http://www.programcreek.com/2013/01/leetcode-distinct-subsequences-total-java/
class Solution2:
    # @return an integer
    #dp. still no understand
    def numDistinct(self, S, T):
        dp = [[0 for i in range(len(T)+1)] for j in range(len(S)+1)]
        for j in range(len(S)+1):
            dp[j][0] = 1
        for i in range(1, len(S)+1):
            for j in range(1, min(i+1, len(T)+1)):
                if S[i-1] == T[j-1]:
                    dp[i][j] = dp [i-1][j] + dp[i-1][j-1]
                else:
                    dp[i][j] =dp[i-1][j]

        for i in xrange(len(dp)):
            print dp[i]

        return dp[len(S)][len(T)]

#TEST
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        test = Solution2()
        #print test.numDistinct("ABB", "AB")
        #print test.numDistinct("ABCDE", "ACE")
        #print test.numDistinct("rabbbit", "rabbit")

        S = "rabbbit"
        T = "rabbit"
        #result1 = Solution().numDistinct(S, T)
        result2 = Solution2().numDistinct("ABB", "AB")
        print result2

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
The idea is the following:

we will build an array mem where mem[i+1][j+1] means that S[0..j] contains T[0..i]
that many times as distinct subsequences. Therefor the result will be mem[T.length()][S.length()].
we can build this array rows-by-rows:
the first row must be filled with 1.
That's because the empty string is a subsequence of any string but only 1 time.
So mem[0][j] = 1 for every j. So with this we not only make our lives easier,
but we also return correct value if T is an empty string.
the first column of every rows except the first must be 0.
This is because an empty string cannot contain a non-empty string as a substring -- the very first item of the array:
mem[0][0] = 1, because an empty string contains the empty string 1 time.
So the matrix looks like this:

  S 0123....j
T +----------+
  |1111111111|
0 |0         |
1 |0         |
2 |0         |
. |0         |
. |0         |
i |0         |

From here we can easily fill the whole grid: for each (x, y),
we check if S[x] == T[y] we add the previous item and the previous item in the previous row,
otherwise we copy the previous item in the same row. The reason is simple:

if the current character in S doesn't equal to current character T,
then we have the same number of distinct subsequences as we had without the new character.
if the current character in S equal to the current character T, then the distinct number of subsequences:
the number we had before plus the distinct number of subsequences we had with less longer T and less longer S.

An example:
S: [acdabefbc] and T: [ab]

first we check with a:

           *  *
      S = [acdabefbc]
mem[1] = [0111222222]
then we check with ab:

               *  * ]
      S = [acdabefbc]
mem[1] = [0111222222]
mem[2] = [0000022244]
And the result is 4, as the distinct subsequences are:

      S = [a   b    ]
      S = [a      b ]
      S = [   ab    ]
      S = [   a   b ]
See the code in Java:

# 6ms 70.17%
class Solution {
    public int numDistinct(String S, String T) {
        // array creation
        int[][] mem = new int[T.length()+1][S.length()+1];

        // filling the first row: with 1s
        for(int j=0; j<=S.length(); j++) {
            mem[0][j] = 1;
        }

        // the first column is 0 by default in every other rows but the first, which we need.

        for(int i=0; i<T.length(); i++) {
            for(int j=0; j<S.length(); j++) {
                if(T.charAt(i) == S.charAt(j)) {
                    mem[i+1][j+1] = mem[i][j] + mem[i+1][j];
                } else {
                    mem[i+1][j+1] = mem[i+1][j];
                }
            }
        }
        return mem[T.length()][S.length()];
    }
}

# 5ms 89.79%
class Solution {
    public int numDistinct(String s, String t) {
        int lenS = s.length();
        int lenT = t.length();
        if (lenS < lenT) {
            return 0;
        }
        int[] dp = new int[lenT + 1];
        dp[0] = 1;
        for (int i = 0; i < lenS; i++) {
            for (int j = Math.min(i, lenT - 1); j >= 0; j--) {
                if (s.charAt(i) == t.charAt(j)) {
                    dp[j + 1] += dp[j];
                }
            }
        }
        return dp[lenT];
    }
}

# 5ms 89.79%
class Solution {
    public int numDistinct(String s, String t) {
        int lenS = s.length();
        int lenT = t.length();
        if (lenS < lenT) {
            return 0;
        }
        int[][] dp = new int[lenS + 1][lenT + 1];
        for (int i = 0; i < lenS; i++) {
            dp[i][0] = 1;
            for (int j = 0; j < Math.min(lenS, lenT); j++) {
                if (s.charAt(i) == t.charAt(j)) {
                    dp[i + 1][j + 1] = dp[i][j + 1] + dp[i][j];
                } else {
                    dp[i + 1][j + 1] = dp[i][j + 1];
                }
            }
        }
        return dp[lenS][lenT];
    }
}

# 1ms 100%
class Solution {
    public int numDistinct(String s, String t) {
            int[][] arr = new int[256][t.length()+1];
            int[] cnt = new int[t.length()+1];
            cnt[0] = 1;
            char c;
            for(int i = 0; i < t.length(); i++ ) {
                c = t.charAt(i);
                arr[c][arr[c][0]+1] = i+1;
                arr[c][0]++;
            }
            for( char a: s.toCharArray() ) {
                if( arr[a][0] != 0 ) {
                    for( int i = arr[a][0]; i > 0; i-- ) {
                        cnt[arr[a][i]] += cnt[arr[a][i]-1];
                    }
                }
            }
            return cnt[t.length()];
    }
}
'''