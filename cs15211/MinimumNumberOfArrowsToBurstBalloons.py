__source__ = 'https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/minimum-number-of-arrows-to-burst-balloons.py
# Time:  O(nlogn)
# Space: O(1)
#
# Description: 452. Minimum Number of Arrows to Burst Balloons
#
# There are a number of spherical balloons spread in two-dimensional space. For each balloon,
# provided input is the start and end coordinates of the horizontal diameter.
# Since it's horizontal, y-coordinates don't matter and
# hence the x-coordinates of start and end of the diameter suffice.
# Start is always smaller than end. There will be at most 104 balloons.
#
# An arrow can be shot up exactly vertically from different points along the x-axis.
# A balloon with xstart and xend bursts by an arrow shot at x if xstart <= x <= xend.
# There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely.
# The problem is to find the minimum number of arrows that must be shot to burst all balloons.
#
# Example:
#
# Input:
# [[10,16], [2,8], [1,6], [7,12]]
#
# Output:
# 2
#
# Explanation:
# One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6])
# and another arrow at x = 11 (bursting the other two balloons).
# Hide Company Tags Microsoft
# Hide Tags Greedy
# Hide Similar Problems (M) Meeting Rooms II (M) Non-overlapping Intervals
#
import unittest
# Sort intervals by ending value;
# Only count valid intervals we need, and skip overlapping intervals
# return the count

# 76ms 100%
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points = sorted(points, key = lambda x: x[1])
        res, end = 0, -float('inf')
        for interval in points:
            if interval[0] > end:
                res += 1
                end = interval[1]
        return res

    def findMinArrowShots2(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0

        points.sort()

        result = 0
        i = 0
        while i < len(points):
            j = i + 1
            right_bound = points[i][1]
            while j < len(points) and points[j][0] <= right_bound:
                right_bound = min(right_bound, points[j][1])
                j += 1
            result += 1
            i = j
        return result

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
Idea:
We know that eventually we have to shoot down every balloon, 
so for each ballon there must be an arrow
whose position is between balloon[0] and balloon[1].
Given that, we can sort the array of balloons by their ending position.
Then we make sure that while we take care of each balloon from the beginning,
we can shoot as many following balloons as possible.

So what position should we pick? We should shoot as right as possible,
because all balloons' end position is to the right of the current one.
Therefore the position should be currentBalloon[1],
because we still need to shoot down the current one.

This is exactly what I do in the for loop: check how many balloons
I can shoot down with one shot aiming at the ending position of the current balloon.
Then I skip all these balloons and start again from the next one
(or the leftmost remaining one) that needs another arrow.

Example:

balloons = [[7,10], [1,5], [3,6], [2,4], [1,4]]
After sorting, it becomes:

balloons = [[2,4], [1,4], [1,5], [3,6], [7,10]]
So first of all, we shoot at position 4,
we go through the array and see that all first 4 balloons can be taken care of by this single shot.
Then we need another shot for one last balloon. So the result should be 2.

# 74ms 30.20%
class Solution {
    public int findMinArrowShots(int[][] points) {
        if (points.length == 0) {
            return 0;
        }

        Arrays.sort(points, (a,b) -> a[1]-b[1]);
        int end = points[0][1];
        int count = 1;
        for(int i = 1; i < points.length; i++) {
            if (end < points[i][0]) {
                count++;
                end = points[i][1];
            }
        }
        return count;
    }
}
'''
