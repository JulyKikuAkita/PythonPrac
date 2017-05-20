__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/max-points-on-a-line.py
# Time:  O(n^2)
# Space: O(n)
# Hashtable
#
# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
# LinkedIn Apple Twitter
# Hash Table Math


# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        ttlmax = 0

        for i in xrange(len(points)):
            base = points[i]
            count = 0
            x0count = 1
            dict = {}
            for j in xrange(i+1, len(points)):
                cur = points[j]
                #need to consider slope of (1,1) (2,2) or points
                if cur.x == base.x and cur.y == base.y:
                    x0count += 1
                else:
                    slope = float("inf")
                    if cur.x - base.x != 0:
                        slope = 1.0 * (cur.y - base.y)/ (cur.x - base.x)
                    if slope not in dict:
                        dict[slope] = 1
                    else:
                        dict[slope] += 1

            for slope in dict:
                count = max(count, dict[slope]+ x0count)

            ttlmax = max(ttlmax, count, x0count)

        return ttlmax


class SolutionOther:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        length = len(points)
        if length < 3:
            return length
        res = -1
        for i in range(length):
            slope = {'inf': 0 }
            samePointNum = 1
            for j in range(length):
                if i == j :
                    continue
                elif points[i].x == points[j].x and points[i].y != points[j].y:
                    slope['inf'] += 1
                elif points[i].x != points[j].x:
                    k = 1.0 * (points[i].y - points[j].y) / (points[i].x - points[j].x)
                    #print k, slope, samePointNum
                    if k not in slope:
                        slope[k] = 1
                    else:
                        slope[k] += 1
                else:
                    samePointNum += 1
            res = max(res, max(slope.values()) + samePointNum)
        return res

#test
if __name__ == "__main__":
    p1 = Point(0,0)
    p2 = Point(1,1)
    p3 = Point(1,-1)
    print SolutionOther().maxPoints([p1])
    print Solution().maxPoints([p1])
#java
js = '''
/**
 * Definition for a point.
 * class Point {
 *     int x;
 *     int y;
 *     Point() { x = 0; y = 0; }
 *     Point(int a, int b) { x = a; y = b; }
 * }
 */
public class Solution {
    public int maxPoints(Point[] points) {
        int len = points.length;
        if (len == 0) {
            return 0;
        }
        int result = 0;
        Map<Double, Integer> map = new HashMap<>();
        for (int i = 0; i < len; i++) {
            map.clear();
            int duplicate = 1;
            for (int j = 0; j < i; j++) {
                if (points[i].x == points[j].x && points[i].y == points[j].y) {
                    duplicate++;
                    continue;
                } else {
                    double slope = points[i].x == points[j].x ?
                                    Double.MAX_VALUE :
                                    ((double) points[j].y - points[i].y) / ((double) points[j].x - points[i].x);
                    map.put(slope, map.containsKey(slope) ? map.get(slope) + 1 : 1);
                }
            }
            int max = 0;
            for (Map.Entry<Double, Integer> entry : map.entrySet()) {
                max = Math.max(max, entry.getValue());
            }
            result = Math.max(result, max + duplicate);
        }
        return result;
    }
}
'''