__source__ = 'https://leetcode.com/problems/perfect-rectangle/description/'
# https://leetcode.com/problems/perfect-rectangle/#/description
# Time:  O(n) or o(nlogn) for sweep line
# Space: O(n) set
#
# Description: Leetcode # 391. Perfect Rectangle
#
# Given N axis-aligned rectangles where N > 0,
# determine if they all together form an exact cover of a rectangular region.
#
# Each rectangle is represented as a bottom-left point and a top-right point.
# For example, a unit square is represented as [1,1,2,2].
# (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).
#
#
# Example 1:
#
# rectangles = [
#   [1,1,3,3],
#   [3,1,4,2],
#   [3,2,4,4],
#   [1,3,2,4],
#   [2,3,3,4]
# ]
#
# Return true. All 5 rectangles together form an exact cover of a rectangular region.
#
# Example 2:
#
# rectangles = [
#   [1,1,2,3],
#   [1,3,2,4],
#   [3,1,4,2],
#   [3,2,4,4]
# ]
#
# Return false. Because there is a gap between the two rectangular regions.
#
# Example 3:
#
# rectangles = [
#   [1,1,3,3],
#   [3,1,4,2],
#   [1,3,2,4],
#   [3,2,4,4]
# ]
#
# Return false. Because there is a gap in the top center.
#
# Example 4:
#
# rectangles = [
#   [1,1,3,3],
#   [3,1,4,2],
#   [1,3,2,4],
#   [2,2,4,4]
# ]
#
# Return false. Because two of the rectangles overlap with each other.
#
# Companies
# Google
#
import unittest
#322ms
class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        def recordCorner(point):
            if point in corners:
                corners[point] += 1
            else:
                corners[point] = 1

        corners = {}                                # record all corners
        L, B, R, T, area = float('inf'), float('inf'), -float('inf'), -float('inf'), 0

        for sub in rectangles:
            L, B, R, T = min(L, sub[0]), min(B, sub[1]), max(R, sub[2]), max(T, sub[3])
            ax, ay, bx, by = sub[:]
            area += (bx-ax)*(by-ay)                 # sum up the area of each sub-rectangle
            map(recordCorner, [(ax, ay), (bx, by), (ax, by), (bx, ay)])

        if area != (T-B)*(R-L): return False        # check the area

        big_four = [(L,B),(R,T),(L,T),(R,B)]

        for bf in big_four:                         # check corners of big rectangle
            if bf not in corners or corners[bf] != 1:
                return False

        for key in corners:                         # check existing "inner" points
            if corners[key]%2 and key not in big_four:
                return False

        return True

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
1.
https://discuss.leetcode.com/topic/55923/o-n-solution-by-counting-corners-with-detailed-explaination with graph
The right answer must satisfy two conditions:

the large rectangle area should be equal to the sum of small rectangles
count of all the points should be even(green + red in graph),
and that of all the four corner points(blue) should be one

#75.08% 108ms
public class Solution {
    public boolean isRectangleCover(int[][] rectangles) {
        if (rectangles == null || rectangles.length == 0 || rectangles[0].length == 0) return false;

        //(coordinate of bottom-left point is (1, 1) (x1, y1)
        //and top-right point is (2, 2). (x2, y2)
        int x1 = Integer.MAX_VALUE;
        int x2 = Integer.MIN_VALUE;
        int y1 = Integer.MAX_VALUE;
        int y2 = Integer.MIN_VALUE;

        HashSet<String> set = new HashSet<String>();
        int area = 0;

        //[x1,y1,x2,y2]
        for (int[] rect : rectangles) {
            x1 = Math.min(rect[0], x1);
            y1 = Math.min(rect[1], y1);
            x2 = Math.max(rect[2], x2);
            y2 = Math.max(rect[3], y2);

            area += (rect[2] - rect[0]) * (rect[3] - rect[1]);
            String s1 = rect[0] + " " + rect[1];
            String s2 = rect[0] + " " + rect[3];
            String s3 = rect[2] + " " + rect[3];
            String s4 = rect[2] + " " + rect[1];

            //The method call returns 'true' if this set did not already contain the specified element.
            if (!set.add(s1)) set.remove(s1);
            if (!set.add(s2)) set.remove(s2);
            if (!set.add(s3)) set.remove(s3);
            if (!set.add(s4)) set.remove(s4);
        }
        if (!set.contains(x1 + " " + y1)
                 || !set.contains(x1 + " " + y2)
                 || !set.contains(x2 + " " + y1)
                 || !set.contains(x2 + " " + y2)
                 || set.size() != 4) return false;

        return area == (x2-x1) * (y2-y1);
    }
}

2. O(nlogn)
sweep line solution
Standard sweep line solution.
Basic idea:
Sort by x-coordinate.
Insert y-interval into TreeSet, and check if there are intersections.
Delete y-interval.

#95.62% 81ms
public class Solution {
    public boolean isRectangleCover(int[][] rectangles) {
        PriorityQueue<Event> pq = new PriorityQueue<Event>();
        // border of y-intervals
    	int[] border= {Integer.MAX_VALUE, Integer.MIN_VALUE};
    	for (int[] rect : rectangles) {
    		Event e1 = new Event(rect[0], rect);
    		Event e2 = new Event(rect[2], rect);
    		pq.add(e1);
    		pq.add(e2);
    		if (rect[1] < border[0]) border[0] = rect[1];
    		if (rect[3] > border[1]) border[1] = rect[3];
    	}

    	TreeSet<int[]> set = new TreeSet<int[]> (new Comparator<int[]> () {
    		@Override
                    // if two y-intervals intersects, return 0
    		public int compare (int[] rect1, int[] rect2) {
    			if (rect1[3] <= rect2[1]) return -1;
    			else if (rect2[3] <= rect1[1]) return 1;
    			else return 0;
    		}
    	});
    	int yRange = 0;
    	while (!pq.isEmpty()) {
    		int time = pq.peek().time;
    		while (!pq.isEmpty() && pq.peek().time == time) {
    			Event e = pq.poll();
    			int[] rect = e.rect;
    			if (time == rect[2]) {
    				set.remove(rect);
    				yRange -= rect[3] - rect[1];
    			} else {
    				if (!set.add(rect)) return false;
    				yRange += rect[3] - rect[1];
    			}
    		}
            // check intervals' range
    		if (!pq.isEmpty() && yRange != border[1] - border[0]) {
                            return false;
    			//if (set.isEmpty()) return false;
    			//if (yRange != border[1] - border[0]) return false;
    		}
    	}
    	return true;
    }

    public class Event implements Comparable<Event> {
    	int time;
    	int[] rect;

    	public Event(int time, int[] rect) {
    		this.time = time;
    		this.rect = rect;
    	}

    	public int compareTo(Event that) {
    		if (this.time != that.time) return this.time - that.time;
    		else return this.rect[0] - that.rect[0];
    	}
    }
}

#98.65% 62ms
public class Solution {
     class Segment {
        int start;
        int end;
        int height;
        Segment(int start, int end, int height){
            this.start = start;
            this.end = end;
            this.height = height;
        }
    }
    public boolean isRectangleCover(int[][] rectangles) {
        final boolean[] tag = {false};
        Arrays.sort(rectangles, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[1] == o2[1] && o1[0] == o2[0]) {
                    tag[0] = true;
                    return -1;
                }else if (o1[1] == o2[1])return o1[0] - o2[0];
                else return o1[1] - o2[1];
            }
        });
        if (tag[0]) return false;
        PriorityQueue<Segment> que = new PriorityQueue<>(new Comparator<Segment>() {
            @Override
            public int compare(Segment o1, Segment o2) {
                if (o1.height == o2.height) {
                    return o1.start - o2.start;
                }
                return o1.height - o2.height;
            }
        });

        int i = solve (0, rectangles[0][0], -1, rectangles[0][1], rectangles, que);
        if (i == -1) return false;
        while (i < rectangles.length) {
            Segment seg = que.poll();
            while (!que.isEmpty()) {
                Segment tmp = que.peek();
                if (tmp.height != seg.height || tmp.start != seg.end) break;
                seg.end = que.poll().end;
            }
            if (rectangles[i][0] != seg.start || rectangles[i][1] != seg.height) return false;
            i = solve(i,seg.start,seg.end,seg.height,rectangles,que);
            if (i == -1) return false;
        }
        Segment seg = que.poll();
        while (!que.isEmpty()) {
            Segment cur = que.poll();
            if (cur.height != seg.height) {
                return false;
            }
        }
        return true;
    }

    private int solve(int i, int start, int limit,int base, int[][] rectangles, PriorityQueue<Segment> que) {
        int end = start;
        int h = rectangles[i][3];
        for (; i < rectangles.length; i ++) {
            if (end == limit) break;
            if (rectangles[i][1] != base) {
                if (limit == -1) {
                    if (rectangles[i][0] > end || rectangles[i][2] > end) return -1;
                }else {
                    return -1;
                }
                break;
            }
            if (rectangles[i][0] != end) return -1;
            if (h == rectangles[i][3]) {
                end = rectangles[i][2];
            }else {
                que.offer(new Segment(start, end, h));
                start = rectangles[i][0];
                end = rectangles[i][2];
                h = rectangles[i][3];
            }
        }
        if (limit != -1 && end != limit) return -1;
        que.offer(new Segment(start, end, h));
        return i;
    }

}
'''