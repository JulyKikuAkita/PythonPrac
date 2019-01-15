__source__ = 'https://leetcode.com/problems/nim-game/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/nim-game.py
# Time:  O(1)
# Space: O(1)
#
# Description: # 292. Nim Game
#
# You are playing the following Nim Game with your friend:
# There is a heap of stones on the table, each time one of
# you take turns to remove 1 to 3 stones.
# The one who removes the last stone will be the winner.
# You will take the first turn to remove the stones.
#
# Both of you are very clever and have optimal strategies for
# the game. Write a function to determine whether you can win
# the game given the number of stones in the heap.
#
# For example, if there are 4 stones in the heap, then you will
# never win the game: no matter 1, 2, or 3 stones you remove,
# the last stone will always be removed by your friend.
#
# Companies
# Adobe
# Related Topics
# Brainteaser
# Similar Questions
# Flip Game II
#

import unittest
# 24ms 30.30%
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/nim-game/solution/

# 0ms 100%
class Solution {
    public boolean canWinNim(int n) {
        return n % 4 != 0;
    }
}

'''
