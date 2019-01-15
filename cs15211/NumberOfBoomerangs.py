__source__ = 'https://leetcode.com/problems/number-of-boomerangs/'
# Time:  O(n^2)
# Space: O(n)
#
# Description: 447. Number of Boomerangs
#
# Given n points in the plane that are all pairwise distinct,
# a "boomerang" is a tuple of points (i, j, k) such that the distance
# between i and j equals the distance between i and k (the order of the tuple matters).
#
# Find the number of boomerangs. You may assume that n will be at most 500
# and coordinates of points are all in the range [-10000, 10000] (inclusive).
#
# Example:
# Input:
# [[0,0],[1,0],[2,0]]
#
# Output:
# 2
#
# Explanation:
# The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
#  Google
# Hide Tags Hash Table
# Hide Similar Problems (M) Line Reflection
#
import collections
import unittest
class Solution(object):
    # 948ms 44.74%
    def numberOfBoomerangs(self, points):
        res = 0
        for p in points:
            cmap = {}
            for q in points:
                f = p[0]-q[0]
                s = p[1]-q[1]
                cmap[f*f + s*s] = 1 + cmap.get(f*f + s*s, 0)
            for k in cmap:
                res += cmap[k] * (cmap[k] -1)
        return res
    def numberOfBoomerangs3(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        result = 0

        for i in xrange(len(points)):
            group = collections.defaultdict(int)
            for j in xrange(len(points)):
                if j == i:
                    continue
                dx, dy =  points[i][0] - points[j][0], points[i][1] - points[j][1]
                group[dx**2 + dy**2] += 1

            for _, v in group.iteritems():
                if v > 1:
                    result += v * (v-1)

        return result

    def numberOfBoomerangs2(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        cnt = 0
        for a, i in enumerate(points):
            dis_list = []
            for b, k in enumerate(points[:a] + points[a + 1:]):
                dis_list.append((k[0] - i[0]) ** 2 + (k[1] - i[1]) ** 2)
            for z in collections.Counter(dis_list).values():
                if z > 1:
                    cnt += z * (z - 1)
        return cnt


# your function here
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
Time complexity:  O(n^2)
Space complexity: O(n)

# 133ms 57.14%
class Solution {
    public int numberOfBoomerangs(int[][] points) {
        int res = 0;
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < points.length; i++) {
            for (int j = 0; j < points.length; j++) {
                if ( i == j) {
                    continue;
                }
                int d = getDistance(points[i], points[j]);
                map.put(d, map.getOrDefault(d, 0) + 1);

            }

            for (int val: map.values()) {
                res += val * (val - 1);
            }
            map.clear();

        }
        return res;
    }

    private int getDistance(int[] a, int[] b) {
        int dx = a[0] - b[0];
        int dy = a[1] - b[1];

        return dx * dx + dy * dy;
    }
}
'''
