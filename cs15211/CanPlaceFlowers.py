__source__ = 'https://leetcode.com/problems/can-place-flowers/#/description'
# Time:  O(m) m = len(flowerbed)
# Space: O(1)
#
# Description: 605. Can Place Flowers
#
# Suppose you have a long flowerbed in which some of the plots are planted and some are not. However,
# flowers cannot be planted in adjacent plots - they would compete for water and both would die.
#
# Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty),
# and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.
#
# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: True

# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: False
# Note:
# The input array won't violate no-adjacent-flowers rule.
# The input array size is in the range of [1, 20000].
# n is a non-negative integer which won't exceed the input array size.
# Hide Company Tags LinkedIn
# Hide Tags Array Greedy
# Hide Similar Problems (M) Teemo Attacking


#Explanation
# We need to justify a greedy solution.
#
# Call a plot ready if the very first flower is allowed to be planted there.
# Consider the left-most ready plot x (if it exists). If x+1 is not ready,
# then we increase our answer strictly by planting at x,
# since x does not disturb any ready plots. If x+1 is ready,
# then planting at x instead of x+1 is at least as good, since x disturbs only {x, x+1},
# whereas x+1 disturbs {x, x+1, x+2}.
#
# Now our implementation is trivial. For each plot from left to right,
# if we can plant a flower there, then do so.
# We can plant a flower if the left neighbor is 0 (or we are on the left edge),
# AND the right neighbor is 0 (or we are on the right edge).

import unittest
# 36ms 84.6%
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i, x in enumerate(flowerbed):
            if (not x and (i == 0 or flowerbed[i-1] == 0)
                and (i == len(flowerbed)-1 or flowerbed[i+1] == 0)):
                n -= 1
                flowerbed[i] = 1
        return n <= 0

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/can-place-flowers/solution/
#
Greedily place a flower at every vacant spot encountered from left to right!

# 6ms 92.14%
class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int count = 0;
        for(int i = 0; i < flowerbed.length && count < n; i++) {
             if(flowerbed[i] == 0) {
	            //get next and prev flower bed slot values.
	            //If i lies at the ends the next and prev are considered as 0.
                int next = (i == flowerbed.length - 1) ? 0 : flowerbed[i + 1];
                int prev = (i == 0) ? 0 : flowerbed[i - 1];
                if (next == 0 && prev == 0) {
                    flowerbed[i] = 1;
                    count++;
                }
             }
        }
        return count == n;
    }
}
'''