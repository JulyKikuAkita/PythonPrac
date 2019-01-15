__source__ = 'https://leetcode.com/problems/my-calendar-iii/'
# Time:  O(N^2)
# Space: O(N)
#
# Description: Leetcode # 732. My Calendar III
#
# Implement a MyCalendarThree class to store your events. A new event can always be added.
#
# Your class will have one method, book(int start, int end).
# Formally, this represents a booking on the half open interval [start, end),
# the range of real numbers x such that start <= x < end.
#
# A K-booking happens when K events have some non-empty intersection
# (ie., there is some time that is common to all K events.)
#
# For each call to the method MyCalendar.book,
# return an integer K representing the largest integer such that there exists a K-booking in the calendar.
#
# Your class will be called like this: MyCalendarThree cal = new MyCalendarThree();
# MyCalendarThree.book(start, end)
# Example 1:
#
# MyCalendarThree();
# MyCalendarThree.book(10, 20); // returns 1
# MyCalendarThree.book(50, 60); // returns 1
# MyCalendarThree.book(10, 40); // returns 2
# MyCalendarThree.book(5, 15); // returns 3
# MyCalendarThree.book(5, 10); // returns 3
# MyCalendarThree.book(25, 55); // returns 3
# Explanation:
# The first two events can be booked and are disjoint, so the maximum K-booking is a 1-booking.
# The third event [10, 40) intersects the first event, and the maximum K-booking is a 2-booking.
# The remaining events cause the maximum K-booking to be only a 3-booking.
# Note that the last event locally causes a 2-booking, but the answer is still 3 because
# eg. [10, 20), [10, 40), and [5, 15) are still triple booked.
#
#
# Note:
#
# The number of calls to MyCalendarThree.book per test case will be at most 400.
# In calls to MyCalendarThree.book(start, end), start and end are integers in the range [0, 10^9].
#
import unittest
import collections
# 2896ms 16.35%
class MyCalendarThree(object):
    def __init__(self):
        self.delta = collections.Counter()

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        self.delta[start] += 1
        self.delta[end] -= 1

        active = ans = 0
        for x in sorted(self.delta):
            active += self.delta[x]
            if active > ans: ans = active
        return ans

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/my-calendar-iii/solution/
#
Approach #1: Boundary Count [Accepted]
Complexity Analysis
Time Complexity: O(N^2), where N is the number of events booked. 
For each new event, we traverse delta in O(N) time. In Python, this is O(N^2logN) owing to the extra sort step.
Space Complexity: O(N), the size of delta.

# 167ms 64.74%
class MyCalendarThree {
    TreeMap<Integer, Integer> delta;
    public MyCalendarThree() {
        delta = new TreeMap();
    }
    
    public int book(int start, int end) {
        delta.put(start, delta.getOrDefault(start, 0) + 1);
        delta.put(end, delta.getOrDefault(end, 0) - 1);
        int active = 0, ans = 0;
        for (int d : delta.values()) {
            active += d;
            if (active > ans) ans = active;
        }
        return ans;
    }
}

class SegmentTreeNode {
    int start, end, cnt;
    SegmentTreeNode left, right;

    public SegmentTreeNode(int start, int end, int cnt) {
        this.start = start;
        this.end = end;
        this.cnt = cnt;
    }
}

# 71ms 99.52%
class MyCalendarThree {
    // segment tree - average (n * log(n)) time, O(n) space
    private SegmentTreeNode root = new SegmentTreeNode(Integer.MIN_VALUE, Integer.MAX_VALUE, 0);;
    private int maxCnt = 0;

    public MyCalendarThree() {
        
    }
    
    public int book(int start, int end) {
        add(root, start, end);
        return maxCnt;
    }
    
    private SegmentTreeNode add(SegmentTreeNode r, int start, int end) {
        if (r == null) {
            maxCnt = Math.max(maxCnt, 1);
            return new SegmentTreeNode(start, end, 1);
        } else if (end <= r.start) {
            // no overlap - left
            r.left = add(r.left, start, end);
        } else if (start >= r.end) {
            // no overlap - right
            r.right = add(r.right, start, end);
        } else {
            // some overlap
            if (start < r.start) {
                r.left = add(r.left, start, r.start);
            }
            if (end > r.end) {
                r.right = add(r.right, r.end, end);
            }
            if (start > r.start) {
                SegmentTreeNode oldLeft = r.left;
                r.left = new SegmentTreeNode(r.start, start, r.cnt);
                r.left.left = oldLeft;
                r.start = start;
            }
            if (end < r.end) {
                SegmentTreeNode oldRight = r.right;
                r.right = new SegmentTreeNode(end, r.end, r.cnt);
                r.right.right = oldRight;
                r.end = end;
            }
            // at least some overlap, so cnt++
            maxCnt = Math.max(maxCnt, ++r.cnt);
        }
        return r;
    }

}


'''
