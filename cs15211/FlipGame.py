__source__ = 'https://leetcode.com/problems/flip-game/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/flip-game.py
# Time:  O(c * n + n) = O(n * (c+1))
# Space: O(n)
#
# Description: Leetcode # 293. Flip Game
#
# You are playing the following Flip Game with your friend:
# Given a string that contains only these two characters: + and -,
# you and your friend take turns to flip two consecutive "++" into "--".
# The game ends when a person can no longer make a move and therefore the other person will be the winner.
#
# Write a function to compute all possible states of the string after one valid move.
#
# For example, given s = "++++", after one move, it may become one of the following states:
# [
#   "--++",
#   "+--+",
#   "++--"
# ]
# If there is no valid move, return an empty list [].
#
# Companies
# Google
# Related Topics
# String
# Similar Questions
# Flip Game II
#
import unittest

# 20ms 100%
class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        i, n = 0, len(s) - 1

        while i < n:
            if s[i] == '+':
                while i < n and s[i+1] == '+':
                    res.append(s[:i] + "--" + s[i+2:])
                    i += 1
            i += 1
        return res

# Time:  O(c * m * n + n) = O(c * n + n), where m = 2 in this question
# Space: O(n)
# This solution compares O(m) = O(2) times for two consecutive "+", where m is length of the pattern

# 20ms 100%
class Solution2(object):
  def generatePossibleNextMoves(self, s):
      """
      :type s: str
      :rtype: List[str]
      """
      return [s[:i] + "--" + s[i+2:] for i in xrange(len(s) - 1) if s[i:i+2] == '++']

# 32ms 6.43%
class Solution3(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []

        for i in xrange(1, len(s)):
            if s[i-1] == "+" and s[i] == "+":
                res.append(s[:i-1] + "--" + s[i+1:])
        return res

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# 0ms 100%
class Solution {
    public List<String> generatePossibleNextMoves(String s) {
        List<String> result = new ArrayList<>();
        int index = s.indexOf("++");
        while (index >= 0) {
            result.add(new StringBuilder().append(s.substring(0, index)).append("--").append(s.substring(index + 2)).toString());
            index = s.indexOf("++", index + 1);
        }
        return result;
    }
}

# 0ms 100%
public class Solution {
    public List<String> generatePossibleNextMoves(String s) {
        List list = new ArrayList();
        for (int i = -1; (i = s.indexOf("++", i + 1)) >= 0; ) {
            list.add(s.substring(0, i) + "--" + s.substring(i + 2));
        }
        return list;
    }
}

# 1ms 18.97%
public class Solution {
    public List<String> generatePossibleNextMoves(String s) {
        List<String> res = new ArrayList<String>();
        for (int i = 0; i < s.length() - 1; i++) {
            char[] temp = s.toCharArray();
            if (s.charAt(i) == '+' && s.charAt(i + 1) == '+') {
                temp[i] = '-';
                temp[i + 1] = '-';
                res.add(String.valueOf(temp));
            }
        }
        return res;
    }
}
'''