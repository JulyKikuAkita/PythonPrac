__source__ = 'https://leetcode.com/problems/minimum-window-subsequence/'
# Time:  O(ST)
# Space: O(S)
#
# Description: Leetcode # 727. Minimum Window Subsequence
#
# Given strings S and T, find the minimum (contiguous) substring W of S,
# so that T is a subsequence of W.
#
# If there is no such window in S that covers all characters in T, return the empty string "".
# If there are multiple such minimum-length windows, return the one with the left-most starting index.
#
# Example 1:
#
# Input:
# S = "abcdebdde", T = "bde"
# Output: "bcde"
# Explanation:
# "bcde" is the answer because it occurs before "bdde" which has the same length.
# "deb" is not a smaller window because the elements of T in the window must occur in order.
#
#
# Note:
#
# All the strings in the input will only contain lowercase letters.
# The length of S will be in the range [1, 20000].
# The length of T will be in the range [1, 100].
#
import unittest

#DP 1216ms 44.01%
class Solution(object):
    def minWindow(self, S, T):
        cur = [i if x == T[0] else None
               for i, x in enumerate(S)]
        #At time j when considering T[:j+1],
        #the smallest window [s, e] where S[e] == T[j]
        #is represented by cur[e] = s.
        for j in xrange(1, len(T)):
            last = None
            new = [None] * len(S)
            #Now we would like to calculate the candidate windows
            #"new" for T[:j+1].  'last' is the last window seen.
            for i, u in enumerate(S):
                if last is not None and u == T[j]: new[i] = last
                if cur[i] is not None: last = cur[i]
            cur = new

        #Looking at the window data cur, choose the smallest length
        #window [s, e].
        ans = 0, len(S)
        for e, s in enumerate(cur):
            if s >= 0 and e - s < ans[1] - ans[0]:
                ans = s, e
        return S[ans[0]: ans[1]+1] if ans[1] < len(S) else ""

#108ms 99.15%
class Solution2(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        dp[i][j]: the start position of Minimum Window Subsequence for S[:i] and T[:j]
        """
        m = len(S)
        n = len(T)
        length = float('inf')
        idx1, idx2 = 0, 0
        ans = ""
        while idx1 < m:
            if S[idx1] == T[idx2]:
                idx2 += 1
                if idx2 == n:
                    start, end = idx1, idx1+1
                    idx2 -= 1
                    while idx2 >= 0:
                        if S[start] == T[idx2]:
                            idx2 -= 1
                        start -= 1
                    start += 1
                    if end - start < length:
                        length = end - start
                        ans = S[start:end]
                    idx1 = start
                    idx2 = 0
            idx1 += 1
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:https://leetcode.com/problems/minimum-window-subsequence/solution/
Approach #1: Dynamic Programming (Postfix Variation) [Accepted]
Complexity Analysis
Time Complexity: O(ST), where S,T are the lengths of S, T. We have two for-loops.
Space Complexity: O(S), the length of dp.

#55ms 37.95%
class Solution {
    public String minWindow(String S, String T) {
        int[][] dp = new int[2][S.length()];
        for (int i = 0; i < S.length(); i++) {
            dp[0][i] = S.charAt(i) == T.charAt(0) ? i : -1;
        }

        /*At time j when considering T[:j+1],
          the smallest window [s, e] where S[e] == T[j]
          is represented by dp[j & 1][e] = s, and the
          previous information of the smallest window
          [s, e] where S[e] == T[j-1] is stored as
          dp[~j & 1][e] = s.
        */
        for (int j = 1; j < T.length(); ++j) {
            int last = -1;
            Arrays.fill(dp[j & 1], -1);
            //Now we would like to calculate the candidate windows
            //"dp[j & 1]" for T[:j+1].  'last' is the last window seen.
            for (int i = 0; i < S.length(); ++i) {
                if ( last >= 0 && S.charAt(i) == T.charAt(j)) dp[j & 1][i] = last;
                if (dp[~j & 1][i] >= 0) last = dp[~j & 1][i];
            }
        }

         //Looking at the window data dp[~T.length & 1],
        //choose the smallest length window [s, e].
        int start = 0, end = S.length();
        for (int e = 0; e < S.length(); ++e) {
            int s = dp[~T.length() & 1][e];
            if (s >= 0 && e - s < end - start) {
                start = s;
                end = e;
            }
        }
        return end < S.length() ? S.substring(start, end + 1) : "";
    }
}

Approach #2: Dynamic Programming (Next Array Variation) [Accepted]
Complexity Analysis
Time Complexity: O(ST), where S,T are the lengths of S, T,
and assuming a fixed-sized alphabet.
The precomputation of nxt is O(S), and the other work happens in two for-loops.
Space Complexity: O(S), the size of windows.

#43ms 54.09%
class Solution {
    public String minWindow(String S, String T) {
        int N = S.length();
        int[] last = new int[26];
        int[][] next = new int[N][26];
        Arrays.fill(last, -1);

        for (int i = N - 1; i >= 0; --i) {
            last[S.charAt(i) - 'a'] = i;
            for (int k = 0; k < 26; ++k) {
                next[i][k] = last[k];
            }
        }

        List<int[]> windows = new ArrayList();
        for (int i = 0; i < N; ++i) {
            if (S.charAt(i) == T.charAt(0)) windows.add(new int[]{i, i});
        }

        for (int j = 1; j < T.length(); ++j) {
            int code = T.charAt(j) - 'a';
            for (int[] window: windows) {
                if (window[1] < N - 1 && next[window[1]+1][code] >= 0) {
                    window[1] = next[window[1] + 1][code];
                } else {
                    window[0] = window[1] = -1;
                    break;
                }
            }
        }

        int[] ans = {-1, S.length()};
        for (int[] window: windows) {
            if (window[0] == -1) break;
            if (window[1] - window[0] < ans[1] - ans[0]) {
                ans = window;
            }
        }
        return ans[0] >= 0 ? S.substring(ans[0], ans[1] + 1) : "";
    }
}

# 4ms 100%
class Solution {
    public String minWindow(String S, String T) {
        int i = -1;
        String ans = "";
        char[] s = S.toCharArray();
        char[] t = T.toCharArray();
        while (i < S.length()) {
            for (int j  = 0; j < T.length(); j++) {
                i = S.indexOf(t[j], i + 1);
                if (i == -1) return ans;
            }
            i = i + 1;
            int lastTCharIndex = i;
            for (int j = T.length() - 1; j >= 0; j--) {
                i = S.lastIndexOf(t[j], i - 1);
            }
            if (ans.isEmpty() || ans.length() > lastTCharIndex - i) ans = String.valueOf(s, i, lastTCharIndex - i);
            i++;
        }
        return ans;
    }
}
'''