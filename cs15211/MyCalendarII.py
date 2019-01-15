# coding=utf-8
__source__ = 'https://leetcode.com/problems/my-calendar-ii/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 731. My Calendar II
#
# Implement a MyCalendarTwo class to store your events.
# A new event can be added if adding the event will not cause a triple booking.
#
# Your class will have one method, book(int start, int end).
# Formally, this represents a booking on the half open interval [start, end),
# the range of real numbers x such that start <= x < end.
#
# A triple booking happens when three events have some non-empty intersection
# (ie., there is some time that is common to all 3 events.)
#
# For each call to the method MyCalendar.book,
# return true if the event can be added to the calendar successfully without causing a triple booking.
# Otherwise, return false and do not add the event to the calendar.
#
# Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
# Example 1:
# MyCalendar();
# MyCalendar.book(10, 20); // returns true
# MyCalendar.book(50, 60); // returns true
# MyCalendar.book(10, 40); // returns true
# MyCalendar.book(5, 15); // returns false
# MyCalendar.book(5, 10); // returns true
# MyCalendar.book(25, 55); // returns true
# Explanation:
# The first two events can be booked.  The third event can be double booked.
# The fourth event (5, 15) can't be booked, because it would result in a triple booking.
# The fifth event (5, 10) can be booked, as it does not use time 10 which is already double booked.
# The sixth event (25, 55) can be booked, as the time in [25, 40) will be double booked with the third event;
# the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.
# Note:
#
# The number of calls to MyCalendar.book per test case will be at most 1000.
# In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].
#
import unittest

# 288ms 93.99%
class MyCalendarTwo(object):

    def __init__(self):
        self.calendar = []
        self.overlaps = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for i, j in self.overlaps:
            if start < j and end > i:
                return False
        for i, j in self.calendar:
            if start < j and end > i:
                self.overlaps.append((max(start, i), min(end, j)))
        self.calendar.append((start, end))
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/my-calendar-ii/solution/
#
Approach #1: Brute Force [Accepted]
Complexity Analysis
Time Complexity: O(N^2), where N is the number of events booked. 
For each new event, we process every previous event to decide whether the new event can be booked. 
This leads to ∑O(k) = O(N^2) complexity.
Space Complexity: O(N), the size of the calendar.

# 195ms 57.88%
class MyCalendarTwo {
    List<int[]> calendar;
    List<int[]> overlaps;

    public MyCalendarTwo() {
        calendar = new ArrayList();
        overlaps = new ArrayList();
    }
    
    public boolean book(int start, int end) {
        for (int[] iv: overlaps) {
            if (iv[0] < end && start < iv[1]) return false;
        }
        for (int[] iv: calendar) {
            if (iv[0] < end && start < iv[1])
                overlaps.add(new int[]{Math.max(start, iv[0]), Math.min(end, iv[1])});
        }
        calendar.add(new int[]{start, end});
        return true;
    }
}

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo obj = new MyCalendarTwo();
 * boolean param_1 = obj.book(start,end);
 */
 
Approach #2: Boundary Count [Accepted]
Complexity Analysis
Time Complexity: O(N^2), where N is the number of events booked. 
For each new event, we traverse delta in O(N) time.
Space Complexity: O(N), the size of delta.

# 271ms 37.51%
class MyCalendarTwo {
    TreeMap<Integer, Integer> delta;
    public MyCalendarTwo() {
        delta = new TreeMap();
    }
    
    public boolean book(int start, int end) {
        delta.put(start, delta.getOrDefault(start, 0) + 1);
        delta.put(end, delta.getOrDefault(end, 0) - 1);
        
        int active = 0;
        for (int d: delta.values()) {
            active += d;
            if (active >= 3) {
                delta.put(start, delta.get(start) - 1);
                delta.put(end, delta.get(end) + 1);
                if (delta.get(start) == 0) delta.remove(start);    
                return false;
            }
        }
        return true;
    }
}

# 81ms 99.74%
class MyCalendarTwo {
    static class Range {
        int intersects;
        int start, end;
        Range left, right;
        Range(int start, int end, int intersects) {
          this.start = start;
          this.end = end;
          this.intersects = intersects;
        }
    }
        
    private Range root;

    public boolean book(int start, int end) {
        if (!canInsert(root, start, end)) return false;
        root = insert(root, start, end);
        return true;
    }
        
    public boolean canInsert(Range parent, int start, int end) {
        if (parent == null) return true;
        if (end <= parent.start) {
            return canInsert(parent.left, start, end);
        } else if (start >= parent.end) {
            return canInsert(parent.right, start, end);
        } else {
            if (parent.intersects >= 2) return false;
            if (start < parent.start && !canInsert(parent.left, start, parent.start)) return false;
            if (end > parent.end && !canInsert(parent.right, parent.end, end)) return false;
            return true;
        }
    }
        
    public Range insert(Range parent, int start, int end) {
        if (parent == null) return new Range(start, end, 1);
        if (end <= parent.start) {
            parent.left = insert(parent.left, start, end);
        } else if (start >= parent.end) {
            parent.right = insert(parent.right, start, end);
        } else {
            if (start < parent.start) {
                parent.left = insert(parent.left, start, parent.start);
            }
            if (end > parent.end) {
                parent.right = insert(parent.right, parent.end, end);
            }
            if (start > parent.start) {
                Range left = new Range(parent.start, start, parent.intersects);
                left.left = parent.left;
                parent.left = left;
                parent.start = start;
            }
            if (end < parent.end) {
                Range right = new Range(end, parent.end, parent.intersects);
                right.right = parent.right;
                parent.right = right;
                parent.end = end;
            }
            parent.intersects++;
        }
        return parent;
    }
}

'''
