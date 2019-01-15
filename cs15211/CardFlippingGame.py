__source__ = 'https://leetcode.com/problems/card-flipping-game/'
# Time:  O(N)
# Space: O(N)
#
# Description: Leetcode # 822. Card Flipping Game
#
# On a table are N cards,
# with a positive integer printed on the front and back of each card (possibly different).
#
# We flip any number of cards, and after we choose one card.
#
# If the number X on the back of the chosen card is not on the front of any card, then this number X is good.
#
# What is the smallest number that is good?  If no number is good, output 0.
#
# Here, fronts[i] and backs[i] represent the number on the front and back of card i.
#
# A flip swaps the front and back numbers, so the value on the front is now on the back and vice versa.
#
# Example:
#
# Input: fronts = [1,2,4,4,7], backs = [1,3,4,1,3]
# Output: 2
# Explanation: If we flip the second card,
# the fronts are [1,3,4,4,7] and the backs are [1,2,4,1,3].
# We choose the second card, which has number 2 on the back,
# and it isn't on the front of any card, so 2 is good.
#
#
# Note:
#
# 1 <= fronts.length == backs.length <= 1000.
# 1 <= fronts[i] <= 2000.
# 1 <= backs[i] <= 2000.
#
import unittest

#32 ms 91.67%
class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        doubles = set(f for f, b in zip(fronts, backs) if f == b)
        ret = [f for f in fronts if f not in doubles] + [b for b in backs if b not in doubles]
        if not ret:
            return 0
        return min(ret)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/card-flipping-game/solution/

Approach #1: Hash Set [Accepted]
Complexity Analysis
Time Complexity: O(N), where N is the length of fronts (and backs). We scan through the arrays.
Space Complexity: O(N).

#10ms 89.4%
class Solution {
    public int flipgame(int[] fronts, int[] backs) {
        Set<Integer> same = new HashSet();
        for (int i = 0; i < fronts.length; i++) {
            if (fronts[i] == backs[i]) same.add(fronts[i]);
        }

        int ans = 9999;
        for (int x: fronts) {
            if (!same.contains(x)) ans = Math.min(ans, x);
        }

        for (int x : backs) {
            if (!same.contains(x)) ans = Math.min(ans, x);
        }
        return ans % 9999;
    }
}

#6ms 100%
class Solution {
    public int flipgame(int[] fronts, int[] backs) {
        boolean[] s = new boolean[2001];
        for (int i = 0; i < fronts.length; i++) {
            if (fronts[i] == backs[i]) {
                s[fronts[i]] = true;
            }
        }

        int ret = Integer.MAX_VALUE;
        for (int i = 0; i < fronts.length; i++) {
            if (!s[fronts[i]]) {
                ret = Math.min(ret, fronts[i]);
            }
            if (!s[backs[i]]) {
                ret = Math.min(ret, backs[i]);
            }
        }
        return ret == Integer.MAX_VALUE? 0 : ret;
    }
}

'''