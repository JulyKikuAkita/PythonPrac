__source__ = 'https://leetcode.com/problems/prison-cells-after-n-days/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 957. Prison Cells After N Days
#
# There are 8 prison cells in a row, and each cell is either occupied or vacant.
#
# Each day, whether the cell is occupied or vacant changes according to the following rules:
#
# If a cell has two adjacent neighbors that are both occupied or both vacant,
# then the cell becomes occupied.
# Otherwise, it becomes vacant.
#
# (Note that because the prison is a row,
# the first and the last cells in the row can't have two adjacent neighbors.)
#
# We describe the current state of the prison in the following way:
# cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.
#
# Given the initial state of the prison,
# return the state of the prison after N days (and N such changes described above.)
#
# Example 1:
#
# Input: cells = [0,1,0,1,1,0,0,1], N = 7
# Output: [0,0,1,1,0,0,0,0]
# Explanation:
# The following table summarizes the state of the prison on each day:
# Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
# Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
# Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
# Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
# Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
# Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
# Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
# Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
#
# Example 2:
#
# Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
# Output: [0,0,1,1,1,1,1,0]
#
# Note:
#
#     cells.length == 8
#     cells[i] is in {0, 1}
#     1 <= N <= 10^9
#
import unittest
# 60ms 19.12%
class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        def nextday(cells):
            return [int(i > 0 and i < 7 and cells[i-1] == cells[i+1])
                    for i in xrange(8)]
        seen = {}
        while N > 0:
            c = tuple(cells)
            if c in seen:
                N %= seen[c] - N
            seen[c] = N
            if N >= 1:
                N -= 1
                cells = nextday(cells)
        return cells


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/prison-cells-after-n-days/solution/
#
# BruteForce 
# TLE
class Solution {
    public int[] prisonAfterNDays(int[] cells, int N) {
        while (N > 0) {
            N--;
            int[] cells2 = new int[8];
            for (int i = 1; i < 7; ++i)
                cells2[i] = cells[i - 1] == cells[i + 1] ? 1 : 0;
            cells = cells2;
        }
        return cells;
    }
}
Approach 1: Simulation
Complexity Analysis
Time Complexity: O(2^N), where N is the number of cells in the prison.
Space Complexity: O(2^N * N)

# 18ms 33.75%
class Solution {
    public int[] prisonAfterNDays(int[] cells, int N) {
        Map<Integer, Integer> seen = new HashMap();

        // state  = integer representing state of prison
        int state = 0;
        for (int i = 0; i < 8; ++i) {
            if (cells[i] > 0)
                state ^= 1 << i;
        }

        // While days remaining, simulate a day
        while (N > 0) {
            // If this is a cycle, fast forward by
            // seen.get(state) - N, the period of the cycle.
            if (seen.containsKey(state)) {
                N %= seen.get(state) - N;
            }
            seen.put(state, N);

            if (N >= 1) {
                N--;
                state = nextDay(state);
            }
        }

        // Convert the state back to the required answer.
        int[] ans = new int[8];
        for (int i = 0; i < 8; ++i) {
            if (((state >> i) & 1) > 0) {
                ans[i] = 1;
            }
        }
        return ans;
    }

    public int nextDay(int state) {
        int ans = 0;

        // We only loop from 1 to 6 because 0 and 7 are impossible,
        // as those cells only have one neighbor.
        for (int i = 1; i <= 6; ++i) {
            if (((state >> (i-1)) & 1) == ((state >> (i+1)) & 1)) {
                ans ^= 1 << i;
            }
        }

        return ans;
    }
}
 
https://leetcode.com/problems/prison-cells-after-n-days/discuss/205684/JavaPython-Find-the-Loop-or-Mod-14
Well, the length of loop can be 1, 7, or 14.
So once we enter the loop, every 14 steps must be the same state.
The length of cells is even,
so for any state, we can find a previous state.
So all states are in a loop.

# 9ms 97.09%
class Solution {
    public int[] prisonAfterNDays(int[] cells, int N) {
        for (N = (N - 1) % 14 + 1; N > 0; N--) {
            int[] cells2 = new int[8];
            for (int i = 1; i < 7; i++) {
                cells2[i] = cells[i - 1] == cells[i + 1] ? 1: 0;
            }
            cells = cells2;
        }
        return cells;
    }
}
'''
