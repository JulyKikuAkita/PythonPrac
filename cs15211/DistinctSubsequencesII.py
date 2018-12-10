__source__ = 'https://leetcode.com/problems/distinct-subsequences-ii/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 940. Distinct Subsequences II
#
# Given a string S, count the number of distinct, non-empty subsequences of S .
#
# Since the result may be large, return the answer modulo 10^9 + 7.
#
# Example 1:
#
# Input: "abc"
# Output: 7
# Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".
# Example 2:
#
# Input: "aba"
# Output: 6
# Explanation: The 6 distinct subsequences are "a", "b", "ab", "ba", "aa" and "aba".
# Example 3:
#
# Input: "aaa"
# Output: 3
# Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".
#
# Note:
#
# S contains only lowercase letters.
# 1 <= S.length <= 2000
#
import unittest

# 40ms 84.31%
class Solution(object):
    def distinctSubseqII(self, S):
        """
        :type S: str
        :rtype: int
        """
        dp = [1]
        last = {}
        for i, x in enumerate(S):
            dp.append(dp[-1] * 2)
            if x in last:
                dp[-1] -= dp[last[x]]
            last[x] = i
        return (dp[-1] - 1) % (10**9 + 7)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/distinct-subsequences-ii/solution/
Approach 1: Dynamic Programming
Complexity Analysis
Time Complexity: O(N), where N is the length of S.
Space Complexity: O(N). It is possible to adapt this solution to take O(1) space.

Naively, for say, S = "abcx", we have dp[k] = dp[k-1] * 2.
This is because for dp[2] which counts ("", "a", "b", "c", "ab", "ac", "bc", "abc"),
dp[3] counts all of those, plus all of those with the x ending,
like ("x", "ax", "bx", "cx", "abx", "acx", "bcx", "abcx").

However, for something like S = "abab", let's play around with it. We have:

dp[0] = 2, as it counts ("", "a")
dp[1] = 4, as it counts ("", "a", "b", "ab");
dp[2] = 7 as it counts ("", "a", "b", "aa", "ab", "ba", "aba");
dp[3] = 12, as it counts ("", "a", "b", "aa", "ab", "ba", "bb", "aab", "aba", "abb", "bab", "abab").
We have that dp[3]countsdp[2], plus("b", "aa", "ab", "ba", "aba")with"b"added to it.
Notice that("", "a")are missing from this list, as they get double counted.
In general, the sequences that resulted from putting"b"the last time (ie."b", "ab"`) will get double counted.

This insight leads to the recurrence:
Dp = dp[k] = 2 * dp[k-1] - dp[last[S[k]] - 1] (in case of double counting)

# 10ms 66.47%
class Solution {
    public int distinctSubseqII(String S) {
        int MOD = 1_000_000_007; // 10e7;
        int N = S.length();
        int[] dp = new int[N + 1];
        dp[0] = 1;

        int[] last = new int[26];
        Arrays.fill(last, -1);

        for (int i = 0; i < N; ++i) {
            int x = S.charAt(i) - 'a';
            dp[i + 1] = dp[i] * 2 % MOD;
            if (last[x] >= 0) {
                dp[i + 1] -= dp[last[x]];
            }
            dp[i + 1] %= MOD;
            last[x] = i;
        }
        dp[N]--;
        if (dp[N] < 0) dp[N] += MOD;
        return dp[N];
    }
}

# 11ms 60.16%
class Solution {
    public int distinctSubseqII(String S) {
		//  a b c
		//  a -> a
		//  b -> ab  b
		//  c -> ac abc bc c
		//                      1 append          2 skip
		//  a b a
		//  a ->  a                a                ""
		//  b ->  ab b             ab  b            a ""
		//  a ->  aa aba ba a      aba ba aa a      ab b a ""  -> exclude all answers end with current char
		long[] counter = new long[26];
		long prevSum = 0;
		long mod = (long)(1e9 + 7);
		long curr = 0;
		for (int i = 0; i < S.length(); i++) {
			// append
			curr = prevSum + 1; // append to all previous sub sequences or append itself
			int index = S.charAt(i) - 'a';
			counter[index] = curr;
			for (int j = 0; j < 26; j++) {
				if (j != index) {
					curr += counter[j];
				}
			}
			curr = curr % mod;
			prevSum = curr; // result of substring [0, i]
		}
		return (int)curr;
	}
}

# 8ms 79.79%
class Solution {
    public int distinctSubseqII(String S) {
        int[] dict = new int[26]; // Save 'total' count when a character appears.
        int total = 1; //Empty string, starting at count 1
        for (char c : S.toCharArray()) {
            int combo = total * 2 - dict[c - 'a']; // New - Duplicates
            dict[c - 'a'] = total; // if 'c' ever appears again, it will clash with the current combos.
            total = combo < 0 ? combo + 1000000007 : combo % 1000000007; // mod and fix negative mods
        }
        return total - 1; // Subtract the empty string
    }
}
'''