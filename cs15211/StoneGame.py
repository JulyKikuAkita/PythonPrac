__source__ = 'https://leetcode.com/problems/stone-game/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 877. Stone Game
#
# Alex and Lee play a game with piles of stones.
# There are an even number of piles arranged in a row,
# and each pile has a positive integer number of stones piles[i].
#
# The objective of the game is to end with the most stones.
# The total number of stones is odd, so there are no ties.
#
# Alex and Lee take turns, with Alex starting first.
# Each turn, a player takes the entire pile of stones from either the beginning
# or the end of the row.  This continues until there are no more piles left,
# at which point the person with the most stones wins.
#
# Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.
#
#
#
# Example 1:
#
# Input: [5,3,4,5]
# Output: true
# Explanation:
# Alex starts first, and can only take the first 5 or the last 5.
# Say he takes the first 5, so that the row becomes [3, 4, 5].
# If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
# If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
# This demonstrated that taking the first 5 was a winning move for Alex, so we return true.
#
#
# Note:
#
# 2 <= piles.length <= 500
# piles.length is even.
# 1 <= piles[i] <= 500
# sum(piles) is odd.
#
import unittest

class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        return True

class SolutionDP(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]

        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        return dp[0][n - 1] > 0

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/stone-game/solution/
# 10ms 36.14%
Approach 1: Dynamic Programming
Complexity Analysis
Time Complexity: O(N^2), where N is the number of piles.
Space Complexity: O(N^2), the space used storing the intermediate results of each subgame.

#10ms 36.14%
class Solution {
    public boolean stoneGame(int[] piles) {
         int N = piles.length;

        // dp[i+1][j+1] = the value of the game [piles[i], ..., piles[j]].
        int[][] dp = new int[N+2][N+2];

        for (int size = 1; size <= N; ++ size) {
            for (int i = 0; i + size <= N; ++i) {
                int j = i + size - 1;
                int parity = ( j + i + N) % 2; // j - i - N; but +x = -x (mod 2)
                if (parity == 1) {
                    dp[i + 1][j + 1] = Math.max(piles[i] + dp[i +2][j + 1], piles[j] + dp[i + 1][j]);
                } else {
                    dp[i + 1][j + 1] = Math.min(-piles[i] + dp[i +2][j + 1], -piles[j] + dp[i + 1][j]);
                }
            }
        }
        return dp[1][N] > 0;
    }
}
Approach 2: Mathematical
Complexity Analysis
Time and Space Complexity: O(1)

class Solution {
    public boolean stoneGame(int[] piles) {
        return true;
    }
}


#2ms 99.64%
class Solution {
    public boolean stoneGame(int[] piles) {
        int left = 0;
        int right = piles.length-1;
        int alex = 0;
        int lee = 0;
        boolean alexTurn = true;

        while (left < right) {
            if (alexTurn) {
                if (piles[left] > piles[right]) {
                    alex += piles[left];
                    left++;
                } else {
                    alex += piles[right];
                    right--;
                }
            } else {
                if (piles[left] > piles[right]) {
                    lee += piles[left];
                    left++;
                } else {
                    lee += piles[right];
                    right--;
                }
            }
        }
        return alex > lee;
    }
}
'''