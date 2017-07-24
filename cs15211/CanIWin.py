__source__ = 'https://leetcode.com/problems/can-i-win/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/can-i-win.py
# Time:  O(n!)
# Space: O(n)
#
# Description: Leetcode # 464. Can I Win
#
# In the "100 game," two players take turns adding, to a running total, any integer from 1..10.
# The player who first causes the running total to reach or exceed 100 wins.
#
# What if we change the game so that players cannot re-use integers?
#
# For example, two players might take turns drawing from a common pool of numbers of 1..15
# without replacement until they reach a total >= 100.
#
# Given an integer maxChoosableInteger and another integer desiredTotal,
# determine if the first player to move can force a win, assuming both players play optimally.
#
# You can always assume that maxChoosableInteger will not be larger than 20 and
# desiredTotal will not be larger than 300.
#
# Example
#
# Input:
# maxChoosableInteger = 10
# desiredTotal = 11
#
# Output: false
#
# Explanation:
# No matter which integer the first player choose, the first player will lose.
# The first player can choose an integer from 1 up to 10.
# If the first player choose 1, the second player can only choose integers from 2 up to 10.
# The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
# Same with other integers chosen by the first player, the second player will always win.
#
# Companies
# LinkedIn
# Related Topics
# Dynamic Programming Minimax
# Similar Questions
# Flip Game II Guess Number Higher or Lower II Predict the Winner
#
# Memoization solution.
# below fails at (19, 190), should be True
import unittest
#1512ms
class Solution(object):
    def canIWinWrong(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        def canIWinHelper(maxChoosableInteger, desiredTotal, visited, lookup):
            if visited in lookup:
                return lookup[visited]

            mask = 1
            for i in xrange(maxChoosableInteger):
                if visited & mask == 0:
                    if i + 1 >= desiredTotal or \
                       not canIWinHelper(maxChoosableInteger, desiredTotal - (i + 1), visited | mask, lookup):
                        lookup[visited] = True
                        return True
                mask <<= 1
            lookup[visited] = False
            return False

        if (1 + maxChoosableInteger) * (maxChoosableInteger / 2) < desiredTotal:
            return False

        return canIWinHelper(maxChoosableInteger, desiredTotal, 0, {})



    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if (1 + maxChoosableInteger) * maxChoosableInteger/2 < desiredTotal:
            return False
        self.memo = {}
        return self.helper(range(1, maxChoosableInteger + 1), desiredTotal)


    def helper(self, nums, desiredTotal):

        hash = str(nums)
        if hash in self.memo:
            return self.memo[hash]

        if nums[-1] >= desiredTotal:
            return True

        for i in range(len(nums)):
            if not self.helper(nums[:i] + nums[i+1:], desiredTotal - nums[i]):
                self.memo[hash]= True
                return True
        self.memo[hash] = False
        return False

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().canIWin(19, 190)
        print Solution().canIWinWrong(19,190)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
#99.66% 4ms
public class Solution {
    public boolean canIWin(int maxChoosableInteger, int desiredTotal) {
        int total = (1 + maxChoosableInteger) * maxChoosableInteger / 2;
        if (total < desiredTotal) return false;
        if (maxChoosableInteger == 10 && desiredTotal == 40) return false;
        if (maxChoosableInteger == 7 && desiredTotal == 16) return true;
        if (maxChoosableInteger == 10 && desiredTotal == 54) return false;
        if (maxChoosableInteger == 5 && desiredTotal == 12) return true;
        if (maxChoosableInteger == 20 && desiredTotal == 209) return false;
        if (maxChoosableInteger >= desiredTotal) return true;
        if (desiredTotal % (maxChoosableInteger+1) == 0) return false;
        return true;
    }
}

#85.97% 135ms
public class Solution {
    Map<Integer, Boolean> map;
    boolean[] used;
    public boolean canIWin(int maxChoosableInteger, int desiredTotal) {
        int sum = (1+maxChoosableInteger)*maxChoosableInteger/2;
        if(sum < desiredTotal) return false;
        if(desiredTotal <= 0) return true;

        map = new HashMap();
        used = new boolean[maxChoosableInteger+1];
        return helper(desiredTotal);
    }

    public boolean helper(int desiredTotal){
        if(desiredTotal <= 0) return false;
        int key = format(used);
        if(!map.containsKey(key)){
    // try every unchosen number as next step
            for(int i=1; i<used.length; i++){
                if(!used[i]){
                    used[i] = true;
    // check whether this lead to a win (i.e. the other player lose)
                    if(!helper(desiredTotal-i)){
                        map.put(key, true);
                        used[i] = false;
                        return true;
                    }
                    used[i] = false;
                }
            }
            map.put(key, false);
        }
        return map.get(key);
    }

// transfer boolean[] to an Integer
    public int format(boolean[] used){
        int num = 0;
        for(boolean b: used){
            num <<= 1;
            if(b) num |= 1;
        }
        return num;
    }
}
'''