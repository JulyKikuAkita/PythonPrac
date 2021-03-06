__source__ = 'https://leetcode.com/problems/self-crossing/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/self-crossing.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 335. Self Crossing
#
# You are given an array x of n positive numbers.
# You start at point (0,0) and moves x[0] metres to the north,
# then x[1] metres to the west, x[2] metres to the south,
# x[3] metres to the east and so on. In other words,
# after each move your direction changes counter-clockwise.
#
# Write a one-pass algorithm with O(1) extra space to determine,
# if your path crosses itself, or not.
#
# Example 1:
# Given x = [2, 1, 1, 2],
# ┌───┐
# │   │
# └───┼──>
#     │
#
# Return true (self crossing)
# Example 2:
# Given x = [1, 2, 3, 4],
# ┌──────┐
# │      │
# │
# │
# └────────────>
#
# Return false (not self crossing)
# Example 3:
# Given x = [1, 1, 1, 1],
# ┌───┐
# │   │
# └───┼>
#
# Return true (self crossing)
#
# Related Topics
# Math
#
import unittest
class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        if len(x) >= 5 and x[3] == x[1] and x[4] + x[0] >= x[2]:
            # Crossing in a loop:
            #     2
            # 3 ┌────┐
            #   └─══>┘1
            #   4  0  (overlapped)
            return True

        for i in xrange(3, len(x)):
            if x[i] >= x[i - 2] and x[i - 3] >= x[i - 1]:
                # Case 1:
                #    i-2
                # i-1┌─┐
                #    └─┼─>i
                #     i-3
                return True
            elif i >= 5 and x[i - 4] <= x[i - 2] and x[i] + x[i - 4] >= x[i - 2] and \
                            x[i - 1] <= x[i - 3] and x[i - 5] + x[i - 1] >= x[i - 3]:
                # Case 2:
                #    i-4
                #    ┌──┐
                #    │i<┼─┐
                # i-3│ i-5│i-1
                #    └────┘
                #      i-2
                return True
        return False

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
#
# Categorize the self-crossing scenarios, there are 3 of them:
# 1. Fourth line crosses first line and works for fifth line crosses second line and so on...
# 2. Fifth line meets first line and works for the lines after
# 3. Sixth line crosses first line and works for the lines after
# Suppose i is the current line, then:
# 
# i and i-3 can cross
# i and i-4 can cross
# i and i-5 can cross
# no more or no less just exactly the right combination.
# 
# Now it's time for us to restrict the conditions to make them just happen.
# 
# i and i-3
# 
# i>=i-2 && i-1<=i-3
# i and i-4
# 
# i+i-4>=i-2 && i-1==i-3
# i and i-5
# 
# i+i-4>=i-2 && i-2>=i-4 && i-1+i-5>=i-3 && i-1<=i-3
#

# 0ms 100%
class Solution {
    public boolean isSelfCrossing(int[] x) {
        int len = x.length;
        if (len < 4) {
            return false;
        }
        for (int i = 3; i < len; i++) {
            if (check4(x, i) || (i > 3 && check5(x, i)) || (i > 4 && check6(x, i))) {
                return true;
            }
        }
        return false;
    }

    private boolean check4(int[] x, int i) {
        return x[i] >= x[i - 2] && x[i - 1] <= x[i - 3];
    }

    private boolean check5(int[] x, int i) {
        return x[i - 1] == x[i - 3] && x[i] + x[i - 4] >= x[i - 2];
    }

    private boolean check6(int[] x, int i) {
        return x[i - 5] - x[i - 3] + x[i - 1] >= 0 && x[i - 4] <= x[i - 2] && x[i - 3] >= x[i - 1] && x[i - 4] - x[i - 2] + x[i] >= 0;
    }
}

# 0ms 100%
class Solution {
    public boolean isSelfCrossing(int[] x) {
        int n = x.length;
        if (n <= 3) return false;

        for (int i = 3; i < n; i++) {
            //4th line cross 1st
            if (x[i] >= x[i-2] && x[i-1] <= x[i-3]) return true;
            //5th cross 1st
            if (i >= 4) {
                if (x[i] + x[i-4] >= x[i-2] && x[i-1] == x[i-3]) return true;
            }
            //6th cross 1st
            if (i >= 5) { //ex: [3,3,3,2,1,1]
                if (x[i] + x[i-4] >= x[i-2] && x[i-1] + x[i-5] >= x[i-3] && x[i-1] <= x[i-3] && x[i - 4] < x[i-2])
                    return true;
            }
        }
        return false;
    }
}
'''
