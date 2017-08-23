__source__ = 'https://leetcode.com/problemset/algorithms/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/dungeon-game.py
# Time:  O(m * n)
# Space: O(m + n)
#
# Description: Leetcode # 174. Dungeon Game
#
# The demons had captured the princess (P) and imprisoned her
# in the bottom-right corner of a dungeon. T
# he dungeon consists of M x N rooms laid out in a 2D grid.
# Our valiant knight (K) was initially positioned in the top-left room
# and must fight his way through the dungeon to rescue the princess.
#
# The knight has an initial health point represented by a positive integer.
# If at any point his health point drops to 0 or below, he dies immediately.
#
# Some of the rooms are guarded by demons,
# so the knight loses health (negative integers) upon entering these rooms;
# other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).
#
# In order to reach the princess as quickly as possible,
# the knight decides to move only rightward or downward in each step.
#
#
# Write a function to determine the knight's minimum initial health
# so that he is able to rescue the princess.
#
# For example, given the dungeon below, the initial health of
# the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.
#
# Notes:
#
# The knight's health has no upper bound.
# Any room can contain threats or power-ups, even the first room the knight enters
# and the bottom-right room where the princess is imprisoned.
#
# Companies
# Microsoft
# Related Topics
# Binary Search Dynamic Programming
# Similar Questions
# Unique Paths Minimum Path Sum
#
import unittest
class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        DP = [float("inf") for _ in dungeon[0]]
        DP[-1] = 1

        for i in reversed(xrange(len(dungeon))):
            DP[-1] = max(DP[-1] - dungeon[i][-1], 1)
            for j in reversed(xrange(len(dungeon[i]) - 1)):
                min_HP_on_exit = min(DP[j], DP[j+1])
                DP[j] = max(min_HP_on_exit - dungeon[i][j], 1)
        return DP[0]

# http://www.programcreek.com/2014/03/leetcode-dungeon-game-java/
class SolutionJava:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        m = len(dungeon)
        n = len(dungeon[0])

        dp = [[0 for j in xrange(n)] for i in xrange(m)]
        dp[m-1][n-1] = max(1 - dungeon[m-1][n-1] , 1)

        #init last col
        for i in reversed(xrange(0, m-1)):
            dp[i][n-1] = max(dp[i+1][n-1] - dungeon[i][n-1], 1)

        #init last row
        for i in reversed(xrange(0, n-1)):
            dp[m-1][i] = max(dp[m-1][i+1] - dungeon[m-1][i], 1)

        #cal dp table
        for i in reversed(xrange(m-1)):
            for j in reversed(xrange(n-1)):
                down = max(dp[i+1][j] - dungeon[i][j], 1)
                right = max(dp[i][j+1] - dungeon[i][j], 1)
                dp[i][j] = min(down, right)
        return dp[0][0]

# Time:  O(m * n logk), where k is the possible maximum sum of loses
# Space: O(m + n)
class Solution2:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        maximum_loses = 0
        for rooms in dungeon:
            for room in rooms:
                if room < 0:
                    maximum_loses += abs(room)
        return self.binarySearch(dungeon, maximum_loses)

    def binarySearch(self, dungeon, maximum_loses):
        start, end = 1, maximum_loses + 1

        while start < end:
            mid = start + (end - start) / 2
            if self.DP(dungeon, mid):
                end = mid
            else:
                start = mid + 1
        return start

    def DP(self, dungeon, HP):
        remain_HP = [ 0 for _ in dungeon[0]]
        remain_HP[0] = HP + dungeon[0][0]
        #print remain_HP, dungeon, dungeon[-1]

        for j in xrange(1, len(remain_HP)):
            if remain_HP[j - 1] > 0:
                remain_HP[j] = max(remain_HP[j - 1] + dungeon[0][j], 0)
        for i in xrange(1, len(dungeon)):
            if remain_HP[0] > 0:
                remain_HP[0] = max(remain_HP[0] + dungeon[i][0], 0)
            else:
                remain_HP[0] = 0

            for j in xrange(1, len(remain_HP)):
                remain = 0
                if remain_HP[j - 1] > 0:
                    remain = max(remain_HP[j - 1] + dungeon[i][j], remain)
                if remain_HP[j] > 0:
                    remain = max(remain_HP[j] + dungeon[i][j], remain)
                remain_HP[j] = remain

        return remain_HP[-1] > 0


#test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        dungeon = [[ -2,  -3,  3], \
               [ -5, -10,  1], \
               [ 10,  30, -5]]
        #print Solution().calculateMinimumHP(dungeon)
        dungeon1 = [[ -200]]
        #print Solution2().calculateMinimumHP(dungeon)

        dungeon2 = [[0, -3]]
        print Solution().calculateMinimumHP(dungeon)
        print SolutionJava().calculateMinimumHP(dungeon)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
# 58.98% 3ms
public class Solution {
    public int calculateMinimumHP(int[][] dungeon) {
        int m = dungeon.length;
        int n = m == 0 ? 0 : dungeon[0].length;
        if (m == 0 || n == 0) {
            return 0;
        }
        int[] dp = new int[n];
        dp[n - 1] = Math.max(1, 1 - dungeon[m - 1][n - 1]);
        for (int j = n - 2; j >= 0; j--) {
            dp[j] = Math.max(1, dp[j + 1] - dungeon[m - 1][j]);
        }
        for (int i = m - 2; i >= 0; i--) {
            dp[n - 1] = Math.max(1, dp[n - 1] - dungeon[i][n - 1]);
            for (int j = n - 2; j >= 0; j--) {
                dp[j] = Math.max(1, Math.min(dp[j], dp[j + 1]) - dungeon[i][j]);
            }
        }
        return dp[0];
    }
}

#99.15% 1ms
public class Solution {
    int row;
    int col;
    public int calculateMinimumHP(int[][] dungeon) {
        row = dungeon.length;
        col = dungeon[0].length;
        int[][] dp = new int[row][col];
        return memorySearch(dungeon, dp, 0, 0);
    }

    private int memorySearch(int[][] dungeon, int[][] dp, int i, int j) {
        if (i >= row || j >= col) {
            return Integer.MAX_VALUE;
        }
        if (dp[i][j] != 0) {
            return dp[i][j];
        }
        int health = Integer.MAX_VALUE;
        health = Math.min(health, memorySearch(dungeon, dp, i, j + 1));
        health = Math.min(health, memorySearch(dungeon, dp, i + 1, j));
        if (health == Integer.MAX_VALUE) {
            health = 1;
        }

        dp[i][j] = Math.max(1, health - dungeon[i][j]);
        return dp[i][j];
    }
}
'''