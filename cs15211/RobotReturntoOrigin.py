__source__ = 'https://leetcode.com/problems/robot-return-to-origin/'
# Time:  O(N)
# Space: O(1)
#
# Description: Leetcode # 657. Robot Return to Origin
#
# There is a robot starting at position (0, 0), the origin, on a 2D plane.
# Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.
#
# The move sequence is represented by a string, and the character moves[i] represents its ith move.
# Valid moves are R (right), L (left), U (up), and D (down).
# If the robot returns to the origin after it finishes all of its moves,
# return true. Otherwise, return false.
#
#
# Note: The way that the robot is "facing" is irrelevant.
# "R" will always make the robot move to the right once,
# "L" will always make it move left, etc.
# Also, assume that the magnitude of the robot's movement is the same for each move.
#
# Example 1:
#
# Input: "UD"
# Output: true
# Explanation: The robot moves up once, and then down once.
# All moves have the same magnitude,
# so it ended up at the origin where it started. Therefore, we return true.
#
# Example 2:
#
# Input: "LL"
# Output: false
# Explanation: The robot moves left twice. It ends up two "moves" to the left of the origin.
# We return false because it is not at the origin at the end of its moves.
#
import unittest
import collections
# 120ms 33.66%
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        c = collections.Counter(moves)
        return c['L'] == c['R'] and c['U'] == c['D']

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/robot-return-to-origin/solution/
#
# 4ms 100%
class Solution {
    public boolean judgeCircle(String moves) {
        int[] table = new int[128];
        for (char c : moves.toCharArray()) {
            table[c]++;
        }
        if (table[68] == table[85] && table[76] == table[82]) return true;
        else return false;
    }
}

# 8ms 93.56%
class Solution {
    public boolean judgeCircle(String moves) {
        int x = 0;
        int y = 0;
        for (char ch : moves.toCharArray()) {
            if (ch == 'U') y++;
            if (ch == 'D') y--;
            if (ch == 'R') x++;
            if (ch == 'L') x--;
        }
        return x == 0 && y == 0;
    }
}
'''
