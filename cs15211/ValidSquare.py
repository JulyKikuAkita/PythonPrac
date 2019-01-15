__source__ = 'https://leetcode.com/problems/valid-square/#/description'
# Time:  O(1)
# Space: O(1)
#
# Description: 593. Valid Square
#
# Given the coordinates of four points in 2D space, return whether the four points could construct a square.
#
# The coordinate (x,y) of a point is represented by an integer array with two integers.
#
# Example:
# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# Output: True
# Note:
#
# All the input integers are in the range [-10000, 10000].
# A valid square has four equal sides with positive length and four equal angles (90-degree angles).
# Input points have no order.
# Hide Company Tags Pure Storage
# Hide Tags Math

import unittest
import collections

#24ms 100%
class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        points = [p1, p2, p3, p4]

        dists = collections.Counter()
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dists[self.getDistance(points[i], points[j])] += 1

        return len(dists.values())==2 and 4 in dists.values() and 2 in dists.values()

    def getDistance(self, p1, p2):
        return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/valid-square/solution/
Just find the square of lenghts, and validate that

1.
There are only two equal longest lenghts.
The non longest lengths are all equal.

# 8ms 94.14%
class Solution {
    public boolean validSquare(int[] p1, int[] p2, int[] p3, int[] p4) {
        long[] lengths = {length(p1, p2), length(p2, p3), length(p3, p4),
            length(p4, p1), length(p1, p3),length(p2, p4)}; // all 6 sides

        long max = 0, nonMax = 0;
        for(long len : lengths) {
            max = Math.max(max, len);
        }
        int count = 0;
        for(int i = 0; i < lengths.length; i++) {
            if(lengths[i] == max) count++;
            else nonMax = lengths[i]; // non diagonal side.
        }
        if(count != 2) return false; // diagonals lenghts have to be same.

        for(long len : lengths) {
            if(len != max && len != nonMax) return false; // sides have to be same length
        }
        return true;
    }

    private long length(int[] p1, int[] p2) {
        return (long)Math.pow(p1[0]-p2[0],2) + (long)Math.pow(p1[1]-p2[1], 2);
    }
}

2. Using Sorting [Accepted]
# 44ms 19.09%
class Solution {
    public double dist(int[] p1, int[] p2) {
        return (p2[1] - p1[1]) * (p2[1] - p1[1]) + (p2[0] - p1[0]) * (p2[0] - p1[0]);
    }
    public boolean validSquare(int[] p1, int[] p2, int[] p3, int[] p4) {
        int[][] p={p1,p2,p3,p4};
        Arrays.sort(p, (l1, l2) -> l2[0] == l1[0] ? l1[1] - l2[1] : l1[0] - l2[0]);
        return dist(p[0], p[1]) != 0 && dist(p[0], p[1]) == dist(p[1], p[3]) && dist(p[1], p[3]) == dist(p[3], p[2]) && dist(p[3], p[2]) == dist(p[2], p[0])   && dist(p[0],p[3])==dist(p[1],p[2]);
    }
}
'''