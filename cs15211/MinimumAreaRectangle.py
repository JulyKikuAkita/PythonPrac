__source__ = 'https://leetcode.com/problems/minimum-area-rectangle/'
# Time:  O(N^2)
# Space: O(N)
#
# Description: Leetcode # 939. Minimum Area Rectangle
#
# Given a set of points in the xy-plane,
# determine the minimum area of a rectangle formed from these points,
# with sides parallel to the x and y axes.
#
# If there isn't any rectangle, return 0.
#
# Example 1:
#
# Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
# Output: 4
# Example 2:
#
# Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# Output: 2
#
# Note:
#
# 1 <= points.length <= 500
# 0 <= points[i][0] <= 40000
# 0 <= points[i][1] <= 40000
# All points are distinct.
#
import unittest
import collections

# 996ms 65.69%
class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        columns = collections.defaultdict(list)
        for x, y in points:
            columns[x].append(y)
        lastx = {}
        ans = float('inf')

        for x in sorted(columns):
            column = columns[x]
            column.sort()
            for j, y2 in enumerate(column):
                for i in xrange(j):
                    y1 = column[i]
                    if (y1, y2) in lastx:
                        ans = min(ans, (x - lastx[y1,y2]) * (y2 - y1))
                    lastx[y1, y2] = x
        return ans if ans < float('inf') else 0

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/minimum-area-rectangle/solution/
#
Approach 1: Sort by Column
Complexity Analysis
Time Complexity: O(N^2), where N is the length of points.
Space Complexity: O(N)

# 280ms 73.81%
class Solution {
    public int minAreaRect(int[][] points) {
        Map<Integer, List<Integer>> rows = new TreeMap();
        for (int[] point: points) {
            int x = point[0], y = point[1];
            rows.computeIfAbsent(x, z -> new ArrayList()).add(y);
        }
        
        int ans = Integer.MAX_VALUE;
        Map<Integer, Integer> lastx = new HashMap();
        for (int x: rows.keySet()) {
            List<Integer> row = rows.get(x);
            Collections.sort(row);
            for (int i = 0; i < row.size(); ++i) {
                for (int j = i+1; j < row.size(); ++j) {
                    int y1 = row.get(i), y2 = row.get(j);
                    int code = 40001 * y1 + y2;
                    if (lastx.containsKey(code)){
                        ans = Math.min(ans, (x - lastx.get(code)) * (y2 - y1));
                    }
                    lastx.put(code, x);
                }
            }
        }
        return ans < Integer.MAX_VALUE ? ans : 0;
    }
}

Approach 2: Count by Diagonal Intuition
Complexity Analysis
Time Complexity: O(N^2), where N is the length of points.
Space Complexity: O(N), where H is the height of the tree

# 341ms 51.04%
class Solution {
    public int minAreaRect(int[][] points) {
        Set<Integer> pointSet = new HashSet();
        for (int[] point: points)
            pointSet.add(40001 * point[0] + point[1]);
        
        int ans = Integer.MAX_VALUE;
        for (int i = 0; i < points.length; ++i)
            for (int j = i+1; j < points.length; ++j) {
                if (points[i][0] != points[j][0] && points[i][1] != points[j][1]) {
                    if (pointSet.contains(40001 * points[i][0] + points[j][1]) &&
                            pointSet.contains(40001 * points[j][0] + points[i][1])) {
                        ans = Math.min(ans, Math.abs(points[j][0] - points[i][0]) *
                                            Math.abs(points[j][1] - points[i][1]));
                    }
                }
            }

        return ans < Integer.MAX_VALUE ? ans : 0;
    }
}

# 49ms 100%
class Solution {
    public int minAreaRect(int[][] points) {
        Map<Integer, Set<Integer>> xMap = new HashMap<>();
        Map<Integer, Set<Integer>> yMap = new HashMap<>();
        for (int[] point : points) {
            if (!xMap.containsKey(point[0])) {
                xMap.put(point[0], new HashSet<>());
            }
            xMap.get(point[0]).add(point[1]);

            if (!yMap.containsKey(point[1])) {
                yMap.put(point[1], new HashSet<>());
            }
            yMap.get(point[1]).add(point[0]);
        }

        boolean find = false;
        int minArea = Integer.MAX_VALUE;
        for (Map.Entry<Integer, Set<Integer>> xIdx : xMap.entrySet()) {
            int x = xIdx.getKey();
            Integer[] topYArray = new Integer[xIdx.getValue().size()];
            xIdx.getValue().toArray(topYArray);
            Arrays.sort(topYArray);

            for (int leftY = 0; leftY < topYArray.length - 1; leftY++) {
                int topY = topYArray[leftY];
                if (yMap.get(topY).size() > 1) {
                    int[] rightXArray = new int[yMap.get(topY).size()];
                    int rightXIdx = 0;
                    for (int rightX : yMap.get(topY)) {
                        if (rightX > x) {
                            rightXArray[rightXIdx++] = rightX;
                        }
                    }

                    for (int tmpIdx = 0; tmpIdx < rightXIdx; tmpIdx++) {
                        int bottom = rightXArray[tmpIdx] - x;
                        if (bottom >= minArea) {
                            continue;
                        }
                        for (int rightY = leftY + 1; rightY < topYArray.length; rightY++) {
                            if ((topYArray[rightY] - topY) * bottom >= minArea) {
                                break;
                            }
                            if (xMap.get(rightXArray[tmpIdx]).contains(topYArray[rightY])) {
                                minArea = (topYArray[rightY] - topY) * bottom;
                                find = true;
                            }
                        }
                    }
                }
            }
        }
        return find ? minArea : 0;
    }
}

# 103ms 98.58%
class Solution {
    public int minAreaRect(int[][] points) {
        Set<String> set = new HashSet<>();
        for (int[] point : points) {
            set.add(point[0] + "," + point[1]);
        }
        
        int res = Integer.MAX_VALUE;
        int n = points.length;
        for (int i = 0; i < n; i++) {
            int x1 = points[i][0];
            int y1 = points[i][1];
            for (int j = i + 1; j < n; j++) {
                int x2 = points[j][0];
                int y2 = points[j][1];
                int area = Math.abs(x1 - x2) * Math.abs(y1 - y2);
                if (area == 0 || area >= res) {
                    continue;
                }
                if (set.contains(x1 + "," + y2) && set.contains(x2 + "," + y1)) {
                    res = area;
                }
            }
        }
        return res == Integer.MAX_VALUE ? 0 : res;
    }
}
'''
