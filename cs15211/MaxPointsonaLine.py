__source__ = 'https://leetcode.com/problems/max-points-on-a-line/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/max-points-on-a-line.py
# Time:  O(n^2)
# Space: O(n)
# Hashtable
#
# Description: Leetcode # 149. Max Points on a Line
#
# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
#
# Companies
# LinkedIn Apple Twitter
# Related Topics
# Hash Table Math
# Similar Questions
# Line Reflection
#
import unittest
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

# test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        p1 = Point(0,0)
        p2 = Point(1,1)
        p3 = Point(1,-1)
        print SolutionOther().maxPoints([p1])
        print Solution().maxPoints([p1])

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
Given point A, we need to calculate all slopes between A and other points. There will be three cases:

Some other point is the same as point A.

Some other point has the same x coordinate as point A, which will result to a positive infinite slope.

General case. We can calculate slope.

We can store all slopes in a hash table. And we find which slope shows up mostly.
Then add the number of same points to it. Then we know the maximum number of points on the same line for point A.

We can do the same thing to point B, point C...

Finally, just return the maximum result among point A, point B, point C...


check [[0,0],[94911151,94911150],[94911152,94911151]]
/**
 * Definition for a point.
 * class Point {
 *     int x;
 *     int y;
 *     Point() { x = 0; y = 0; }
 *     Point(int a, int b) { x = a; y = b; }
 * }
 */
# Map count points with the same slope
# do not divide by 0 when calculate slope
#89.62% 23ms
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

#99.68% 8ms
class Solution {
    public int maxPoints(Point[] points) {
        int n = points.length;
        if(n < 3) return n;

        Arrays.sort(points, new Comparator<Point>() {
            public int compare(Point a, Point b) {
                if(a.x == b.x) {
                    return a.y - b.y;
                }
                return a.x - b.x;
            }
        });

        //time optimization - true when pair has been checked
        boolean[][] checked = new boolean[n][n];
        int answer = 2;
        /*
            We will go through pairs of points, seeing how many points are on line connecting them.
            Since we sorted our array (primarily by x, then by y if the x values are equal), we know that any
            point k that comes between i and j in our array must also be between points i and j on the plane.
            This means we can go through them in order, starting with the points that have the largest
            possible number of points on their line.
        */
        for(int i=0; i<n; i++) {
            if(answer >= n-i) {
                /*
                    The greatest possible number of points we can have starting at i is n-i.
                    Since it's ordered, we have gone through our greatest possibilities first.
                */
                return answer;
            }
            Point a = points[i];
            for(int j=n-1; j>i; j--) {
                if (j - i + 1 <= answer || checked[i][j]) {
                    /*
                        Once the number of points we can check between i and j is less than
                        our current answer, we won't be able to do any better for this i.
                        We also can break if we checked this combination.
                    */
                    break;
                }
                Point b = points[j];
                int pointCount = 2;
                for(int k=i+1; k<j; k++) {
                    //Check how many points on the line between point[i] and point[j]
                    if(pointCount + j - k <= answer) break;
                    if(pointOnLine(a, b, points[k])) {
                        checked[i][k] = true;
                        checked[k][j] = true;
                        pointCount++;
                    }
                }
                answer = Math.max(pointCount, answer);
            }
        }
        return answer;
    }
    private boolean pointOnLine(Point a, Point b, Point check) {
        return (long) (check.x - a.x) * (b.y - check.y) == (long) (b.x - check.x) * (check.y - a.y);
    }
}
'''