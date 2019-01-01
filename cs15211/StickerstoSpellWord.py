__source__ = 'https://leetcode.com/problems/stickers-to-spell-word/'
# Time:  O(2^T * S * T)
# Space: O(2^T)
#
# Description: Leetcode # 691. Stickers to Spell Word
#
# We are given N different types of stickers. Each sticker has a lowercase English word on it.
#
# You would like to spell out the given target string
# by cutting individual letters from your collection of stickers and rearranging them.
#
# You can use each sticker more than once if you want,
# and you have infinite quantities of each sticker.
#
# What is the minimum number of stickers that you need to spell out the target?
# If the task is impossible, return -1.
#
# Example 1:
#
# Input:
#
# ["with", "example", "science"], "thehat"
#
# Output:
#
# 3
#
# Explanation:
#
# We can use 2 "with" stickers, and 1 "example" sticker.
# After cutting and rearrange the letters of those stickers, we can form the target "thehat".
# Also, this is the minimum number of stickers necessary to form the target string.
#
# Example 2:
#
# Input:
#
# ["notice", "possible"], "basicbasic"
#
# Output:
#
# -1
#
# Explanation:
#
# We can't form the target "basicbasic" from cutting letters from the given stickers.
#
# Note:
# stickers has length in the range [1, 50].
# stickers consists of lowercase English words (without apostrophes).
# target has length in the range [1, 15], and consists of lowercase English letters.
# In all test cases, all words were chosen randomly from the 1000 most common US English words,
# and the target was chosen as a concatenation of two random words.
# The time limit may be more challenging than usual.
# It is expected that a 50 sticker test case can be solved within 35ms on average.
#
import unittest
import collections
# 600ms 28.57%
class Solution(object):
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        t_count = collections.Counter(target)
        A = [collections.Counter(sticker) & t_count
             for sticker in stickers]

        for i in range(len(A) - 1, -1, -1):
            if any(A[i] == A[i] & A[j] for j in range(len(A)) if i != j):
                A.pop(i)

        stickers = ["".join(s_count.elements()) for s_count in A]
        dp = [-1] * (1 << len(target))
        dp[0] = 0
        for state in xrange(1 << len(target)):
            if dp[state] == -1: continue
            for sticker in stickers:
                now = state
                for letter in sticker:
                    for i, c in enumerate(target):
                        if (now >> i) & 1: continue
                        if c == letter:
                            now |= 1 << i
                            break
                if dp[now] == -1 or dp[now] > dp[state] + 1:
                    dp[now] = dp[state] + 1

        return dp[-1]


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/stickers-to-spell-word/solution/
#
Approach 1: Optimized Exhaustive Search
Complexity Analysis
Time Complexity: Let N be the number of stickers, and T be the number of letters in the target word. 
A bound for time complexity is O(N^{T+1}*T^2): 
for each sticker, we'll have to try using it up to T+1 times, 
and updating our target count costs O(T), which we do up to T times. 
Alternatively, since the answer is bounded at T, 
we can prove that we can only search up to (N+T-1/T-1) times. 
This would be O((N+T-1/T-1)T2)
Space Complexity: O(N+T), to store stickersCount, 
targetCount, and handle the recursive callstack when calling search.

# 19ms 97.95%
class Solution {
    int best;
    int[][] stickersCount;
    int[] targetCount;

    public void search(int ans, int row) {
        if (ans >= best) return;
        if (row == stickersCount.length) {
            for (int c: targetCount) if (c > 0) return;
            best = ans;
            return;
        }

        int used = 0;
        for (int i = 0; i < stickersCount[row].length; i++) {
            if (targetCount[i] > 0 && stickersCount[row][i] > 0) {
                used = Math.max(used, (targetCount[i] - 1) / stickersCount[row][i] + 1);
            }
        }
        for (int i = 0; i < stickersCount[row].length; i++) {
            targetCount[i] -= used * stickersCount[row][i];
        }

        search(ans + used, row + 1);
        while (used > 0) {
            for (int i = 0; i < stickersCount[row].length; i++) {
                targetCount[i] += stickersCount[row][i];
            }
            used--;
            search(ans + used, row + 1);
        }
    }

    public int minStickers(String[] stickers, String target) {
        int[] targetNaiveCount = new int[26];
        for (char c: target.toCharArray()) targetNaiveCount[c - 'a']++;

        int[] index = new int[26];
        int t = 0;
        for (int i = 0; i < 26; i++) {
            if (targetNaiveCount[i] > 0) {
                index[i] = t++;
            } else {
                index[i] = -1;
            }
        }

        targetCount = new int[t];
        t = 0;
        for (int c: targetNaiveCount) if (c > 0) {
            targetCount[t++] = c;
        }

        stickersCount = new int[stickers.length][t];
        for (int i = 0; i < stickers.length; i++) {
            for (char c: stickers[i].toCharArray()) {
                int j = index[c - 'a'];
                if (j >= 0) stickersCount[i][j]++;
            }
        }

        int anchor = 0;
        for (int i = 0; i < stickers.length; i++) {
            for (int j = anchor; j < stickers.length; j++) if (j != i) {
                boolean dominated = true;
                for (int k = 0; k < t; k++) {
                    if (stickersCount[i][k] > stickersCount[j][k]) {
                        dominated = false;
                        break;
                    }
                }

                if (dominated) {
                    int[] tmp = stickersCount[i];
                    stickersCount[i] = stickersCount[anchor];
                    stickersCount[anchor++] = tmp;
                    break;
                }
            }
        }

        best = target.length() + 1;
        search(0, anchor);
        return best <= target.length() ? best : -1;
    }
}


Approach 2: Dynamic Programming
Complexity Analysis
Time Complexity: O(2^T * S * T) where S be the total number of letters in all stickers, 
and T be the number of letters in the target word. 
We can examine each loop carefully to arrive at this conclusion.
Space Complexity: O(2^T), the space used by dp.

# 162ms 29.45%
class Solution {
    public int minStickers(String[] stickers, String target) {
        int N = target.length();
        int[] dp = new int[1 << N];
        for (int i = 1; i < 1 << N; i++) dp[i] = -1;

        for (int state = 0; state < 1 << N; state++) {
            if (dp[state] == -1) continue;
            for (String sticker: stickers) {
                int now = state;
                for (char letter: sticker.toCharArray()) {
                    for (int i = 0; i < N; i++) {
                        if (((now >> i) & 1) == 1) continue;
                        if (target.charAt(i) == letter) {
                            now |= 1 << i;
                            break;
                        }
                    }
                }
                if (dp[now] == -1 || dp[now] > dp[state] + 1) {
                    dp[now] = dp[state] + 1;
                }
            }
        }
        return dp[(1 << N) - 1];
    }
}
'''
