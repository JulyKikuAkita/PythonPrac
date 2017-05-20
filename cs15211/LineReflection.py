__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/line-reflection.py
# Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points.
#
# Example 1:
# Given points = [[1,1],[-1,1]], return true.
#
# Example 2:
# Given points = [[1,1],[-1,-1]], return false.
#
# Follow up:
# Could you do better than O(n2)?
#
# Time:  O(n)
# Space: O(n)
#  Google
# Hide Tags Hash Table Math
# Hide Similar Problems (H) Max Points on a Line

# Hash solution.
class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if not points:
            return True
        groups_by_y = collections.defaultdict(set)
        left, right = float("inf"), float("-inf")
        for p in points:
            groups_by_y[p[1]].add(p[0])
            left, right = min(left, p[0]), max(right, p[0])
        mid = left + right
        for group in groups_by_y.values():
            for x in group:
                if mid - x not in group:
                    return False
        return True


# Time:  O(nlogn)
# Space: O(n)
# Two pointers solution.
class Solution2(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if not points:
            return True
        points.sort()
        # Space: O(n)
        points[len(points)/2:] = sorted(points[len(points)/2:], \
                                        lambda x, y: y[1] - x[1] if x[0] == y[0] else \
                                                     x[0] - y[0])
        mid = points[0][0] + points[-1][0]
        left, right = 0, len(points) - 1
        while left <= right:
            if (mid != points[left][0] + points[right][0]) or \
               (points[left][0] != points[right][0] and \
                points[left][1] != points[right][1]):
                return False
            left += 1
            right -= 1
        return True

# Java
js = '''
1. 7 ms
public class Solution {
    public boolean isReflected(int[][] points) {
        if (points.length < 2) {
            return true;
        }
        int minX = Integer.MAX_VALUE;
        int maxX = Integer.MIN_VALUE;
        for (int[] point : points) {
            minX = Math.min(minX, point[0]);
            maxX = Math.max(maxX, point[0]);
        }
        double midX = ((double) minX + maxX) / 2;
        Arrays.sort(points, new Comparator<int[]>() {
            @Override
            public int compare(int[] point1, int[] point2) {
                if (point1[0] != point2[0]) {
                    return Integer.compare(point1[0], point2[0]);
                } else {
                    return point1[0] <= midX ? Integer.compare(point1[1], point2[1]) : Integer.compare(point2[1], point1[1]);
                }
            }
        });
        for (int i = 0, j = points.length - 1; i <= j; i++, j--) {
            if (points[i][0] - minX != maxX - points[j][0] || (points[i][0] - minX != maxX - points[i][0] && points[i][1] != points[j][1])) {
                return false;
            }
        }
        return true;
    }
}

2. long runtime 22ms
public class Solution {
    public boolean isReflected(int[][] points) {
        Map<Integer, List<Long>> map = new HashMap<>();
        long minX = Integer.MAX_VALUE;
        long maxX = Integer.MIN_VALUE;
        for (int[] point : points) {
            minX = Math.min(minX, point[0]);
            maxX = Math.max(maxX, point[0]);
            if (!map.containsKey(point[1])) {
                map.put(point[1], new ArrayList<>());
            }
            map.get(point[1]).add((long) point[0]);
        }
        long sum = minX + maxX;
        for (List<Long> list : map.values()) {
            Collections.sort(list);
            int start = 0;
            int end = list.size() - 1;
            while (start < end) {
                long cur = list.get(start++) + list.get(end--);
                if (cur != sum) {
                    return false;
                }
            }
            if (start == end && (list.get(start) << 1) != sum) {
                return false;
            }
        }
        return true;
    }
}
'''