__source__ = 'https://leetcode.com/problems/android-unlock-patterns/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/android-unlock-patterns.py
# Time:  O(9^2 * 2^9)
# Space: O(9 * 2^9)
#
# Description:
# Given an Android 3x3 key lock screen and two integers m and n,
# where 1<= m <= n <= 9, count the total number of unlock patterns of the Android lock screen,
# which consist of minimum of m keys and maximum n keys.
#
# Rules for a valid pattern:
# Each pattern must connect at least m keys and at most n keys.
# All the keys must be distinct.
# If the line connecting two consecutive keys in the pattern passes through any other keys,
# the other keys must have previously selected in the pattern. No jumps through non selected key is allowed.
# The order of keys used matters.
#
# Explanation:
# | 1 | 2 | 3 |
# | 4 | 5 | 6 |
# | 7 | 8 | 9 |
# Invalid move: 4 - 1 - 3 - 6
# Line 1 - 3 passes through key 2 which had not been selected in the pattern.
#
# Invalid move: 4 - 1 - 9 - 2
# Line 1 - 9 passes through key 5 which had not been selected in the pattern.
#
# Valid move: 2 - 4 - 1 - 3 - 6
# Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern
#
# Valid move: 6 - 5 - 4 - 1 - 9 - 2
# Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern.
#
# Example:
# Given m = 1, n = 1, return 9.
# Companies
# Google
# Related Topics
# Dynamic Programming Backtracking
#
import unittest

# DP solution.
class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def merge(used, i):
            return used | (1 << i)

        def number_of_keys(i):
            number = 0
            while i > 0:
                i &= i - 1
                number += 1
            return number

        def contain(used, i):
            return bool(used & (1 << i))

        def convert(i, j):
            return 3 * i + j

        # dp[i][j]: i is the set of the numbers in binary representation,
        #           dp[i][j] is the number of ways ending with the number j.
        dp = [[0] * 9 for _ in xrange(1 << 9)]
        for i in xrange(9):
            dp[merge(0, i)][i] = 1

        res = 0
        for used in xrange(len(dp)):
            number = number_of_keys(used)
            if number > n:
                continue

            for i in xrange(9):
                if not contain(used, i):
                    continue

                if m <= number <= n:
                    res += dp[used][i]

                x1, y1 = i / 3, i % 3
                for j in xrange(9):
                    if contain(used, j):
                        continue

                    x2, y2 = j / 3, j % 3
                    if ((x1 == x2 and abs(y1 - y2) == 2) or \
                        (y1 == y2 and abs(x1 - x2) == 2) or \
                        (abs(x1 - x2) == 2 and abs(y1 - y2) == 2)) and \
                       not contain(used, convert((x1 + x2) / 2, (y1 + y2) / 2)):
                             continue

                    dp[merge(used, j)][j] += dp[used][i]

        return res


# Time:  O(9^2 * 2^9)
# Space: O(9 * 2^9)
# DP solution.
class Solution2(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def merge(used, i):
            return used | (1 << i)

        def number_of_keys(i):
            number = 0
            while i > 0:
                i &= i - 1
                number += 1
            return number

        def exclude(used, i):
            return used & ~(1 << i)

        def contain(used, i):
            return bool(used & (1 << i))

        def convert(i, j):
            return 3 * i + j

        # dp[i][j]: i is the set of the numbers in binary representation,
        #            d[i][j] is the number of ways ending with the number j.
        dp = [[0] * 9 for _ in xrange(1 << 9)]
        for i in xrange(9):
            dp[merge(0, i)][i] = 1

        res = 0
        for used in xrange(len(dp)):
            number = number_of_keys(used)
            if number > n:
                continue

            for i in xrange(9):
                if not contain(used, i):
                    continue

                x1, y1 = i / 3, i % 3
                for j in xrange(9):
                    if i == j or not contain(used, j):
                        continue

                    x2, y2 = j / 3, j % 3
                    if ((x1 == x2 and abs(y1 - y2) == 2) or \
                        (y1 == y2 and abs(x1 - x2) == 2) or \
                        (abs(x1 - x2) == 2 and abs(y1 - y2) == 2)) and \
                       not contain(used, convert((x1 + x2) / 2, (y1 + y2) / 2)):
                             continue

                    dp[used][i] += dp[exclude(used, i)][j]

                if m <= number <= n:
                    res += dp[used][i]

        return res


# Time:  O(9!)
# Space: O(9)
# Backtracking solution. (TLE)
class Solution_TLE(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def merge(used, i):
            return used | (1 << i)

        def contain(used, i):
            return bool(used & (1 << i))

        def convert(i, j):
            return 3 * i + j

        def numberOfPatternsHelper(m, n, level, used, i):
            number = 0
            if level > n:
                return number

            if m <= level <= n:
                number += 1

            x1, y1 = i / 3, i % 3
            for j in xrange(9):
                if contain(used, j):
                    continue

                x2, y2 = j / 3, j % 3
                if ((x1 == x2 and abs(y1 - y2) == 2) or \
                    (y1 == y2 and abs(x1 - x2) == 2) or \
                    (abs(x1 - x2) == 2 and abs(y1 - y2) == 2)) and \
                   not contain(used, convert((x1 + x2) / 2, (y1 + y2) / 2)):
                         continue

                number += numberOfPatternsHelper(m, n, level + 1, merge(used, j), j)

            return number


        number = 0
        # 1, 3, 7, 9
        number += 4 * numberOfPatternsHelper(m, n, 1, merge(0, 0), 0)
        # 2, 4, 6, 8
        number += 4 * numberOfPatternsHelper(m, n, 1, merge(0, 1), 1)
        # 5
        number += numberOfPatternsHelper(m, n, 1, merge(0, 4), 4)
        return number

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/android-unlock-patterns/#/solution

# 19.62
public class Solution {

    private boolean used[] = new boolean[9];

    public int numberOfPatterns(int m, int n) {
        int res = 0;
        for (int len = m; len <= n; len++) {
            res += calcPatterns(-1, len);
            for (int i = 0; i < 9; i++) {
                used[i] = false;
            }
        }
        return res;
    }

    private boolean isValid(int index, int last) {
        if (used[index])
            return false;
        // first digit of the pattern
        if (last == -1)
            return true;
        // knight moves or adjacent cells (in a row or in a column)
        if ((index + last) % 2 == 1)
            return true;
        // indexes are at both end of the diagonals for example 0,0, and 8,8
        int mid = (index + last)/2;
        if (mid == 4)
            return used[mid];
        // adjacent cells on diagonal  - for example 0,0 and 1,0 or 2,0 and //1,1
        if ((index%3 != last%3) && (index/3 != last/3)) {
            return true;
        }
        // all other cells which are not adjacent
        return used[mid];
    }

    private int calcPatterns(int last, int len) {
        if (len == 0)
            return 1;
        int sum = 0;
        for (int i = 0; i < 9; i++) {
            if (isValid(i, last)) {
                used[i] = true;
                sum += calcPatterns(i, len - 1);
                used[i] = false;
            }
        }
        return sum;
    }
}



# 90%
public class Solution {
    public static final int[][] SKIP_LIST;
    static {
        SKIP_LIST = new int[10][10];
        SKIP_LIST[1][3] = SKIP_LIST[3][1] = 2;
        SKIP_LIST[1][7] = SKIP_LIST[7][1] = 4;
        SKIP_LIST[3][9] = SKIP_LIST[9][3] = 6;
        SKIP_LIST[7][9] = SKIP_LIST[9][7] = 8;
        SKIP_LIST[1][9] = SKIP_LIST[2][8] = SKIP_LIST[3][7] = SKIP_LIST[4][6] = SKIP_LIST[6][4] = SKIP_LIST[7][3] = SKIP_LIST[8][2] = SKIP_LIST[9][1] = 5;
    }

    public int numberOfPatterns(int m, int n) {
        if (m < 1 || m > 9 || n < m || n > 9) {
            return 0;
        }
        return (dfs(m, n, 0, new boolean[10], 1) << 2) + (dfs(m, n, 0, new boolean[10], 2) << 2) + dfs(m, n, 0, new boolean[10], 5);
    }

    private int dfs(int m, int n, int curStep, boolean[] isVisited, int curPos) {
        int result = 0;
        isVisited[curPos] = true;
        curStep++;
        if (curStep >= m) {
            result++;
        }
        if (curStep < n) {
            for (int i = 1; i <= 9; i++) {
                if (!isVisited[i] && (SKIP_LIST[curPos][i] == 0 || isVisited[SKIP_LIST[curPos][i]])) {
                    result += dfs(m, n, curStep, isVisited, i);
                }
            }
        }
        isVisited[curPos] = false;
        return result;
    }
}
'''