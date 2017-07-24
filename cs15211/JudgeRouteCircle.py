__source__ = 'https://leetcode.com/problems/judge-route-circle/description/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 657. Judge Route Circle
#
# Initially, there is a Robot at position (0, 0). Given a sequence of its moves,
# judge if this robot makes a circle, which means it moves back to the original place.
#
# The move sequence is represented by a string. And each move is represent by a character.
# The valid robot moves are R (Right), L (Left), U (Up) and D (down).
# The output should be true or false representing whether the robot makes a circle.
#
# Example 1:
# Input: "UD"
# Output: true
# Example 2:
# Input: "LL"
# Output: false
#
# #Companies
# Google
# Related Topics
# String
# Similar Questions
# Friend Circles
#
import unittest
import collections
#135ms
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
#Thought:
#65.86% 16ms
public class Solution {
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

# 99.94% 9ms
public class Solution {
    public boolean judgeCircle(String moves) {
        int[] table = new int[128];
        for (char c : moves.toCharArray()) {
            table[c]++;
        }
        if (table[68] == table[85] && table[76] == table[82]) return true;
        else return false;
    }
}
'''