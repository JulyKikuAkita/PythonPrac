__source__ = 'https://leetcode.com/problems/nim-game/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/nim-game.py
# Time:  O(1)
# Space: O(1)
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
# 35ms
import unittest

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
#Thought: https://leetcode.com/articles/nim-game/

# 5.05% 0ms
public class Solution {
    public boolean canWinNim(int n) {
        return n % 4 != 0;
    }
}

'''
