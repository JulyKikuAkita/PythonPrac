# coding=utf-8
__source__ = 'https://leetcode.com/problems/my-calendar-i/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 729. My Calendar I
#
# Implement a MyCalendar class to store your events.
# A new event can be added if adding the event will not cause a double booking.
#
# Your class will have the method, book(int start, int end).
# Formally, this represents a booking on the half open interval [start, end),
# the range of real numbers x such that start <= x < end.
#
# A double booking happens when two events have some non-empty intersection
# (ie., there is some time that is common to both events.)
#
# For each call to the method MyCalendar.book,
# return true if the event can be added to the calendar successfully without causing a double booking.
# Otherwise, return false and do not add the event to the calendar.
#
# Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
# Example 1:
# MyCalendar();
# MyCalendar.book(10, 20); // returns true
# MyCalendar.book(15, 25); // returns false
# MyCalendar.book(20, 30); // returns true
# Explanation:
# The first event can be booked.  The second can't because time 15 is already booked by another event.
# The third event can be booked, as the first event takes every time less than 20, but not including 20.
# Note:
#
# The number of calls to MyCalendar.book per test case will be at most 1000.
# In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].
#
import unittest

# 392ms 59.94%
class MyCalendar(object):
    def __init__(self):
        self.calendar = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for s, e in self.calendar:
            if s < end and start < e:
                return False
        self.calendar.append((start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

# 436ms 43.27%
class Node:
    __slots__ = 'start', 'end', 'left', 'right'
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None

    def insert(self, node):
        if node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            return self.right.insert(node)
        elif node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)
        else:
            return False

class MyCalendar(object):
    def __init__(self):
        self.root = None

    def book(self, start, end):
        if self.root is None:
            self.root = Node(start, end)
            return True
        return self.root.insert(Node(start, end))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/my-calendar-i/solution/
#
Approach #1: Brute Force [Accepted]
Complexity Analysis
Time Complexity: O(N^2), where N is the number of events booked. 
For each new event, we process every previous event to decide whether the new event can be booked. 
This leads to ∑O(k)=O(N^2) complexity.
Space Complexity: O(N), the size of the calendar.

# 155ms 31.92%
class MyCalendar {
    List<int[]> calendar;
    public MyCalendar() {
        calendar = new ArrayList();
    }
    
    public boolean book(int start, int end) {
        for (int[] iv : calendar) {
            if (iv[0] < end && start < iv[1]) return false;
        }
        calendar.add(new int[]{start, end});
        return true;
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * boolean param_1 = obj.book(start,end);
 */

Approach #2: Balanced Tree [Accepted]
Complexity Analysis
Time Complexity (Java): O(NlogN), where N is the number of events booked. 
For each new event, we search that the event is legal in O(logN) time, 
then insert it in O(1) time.
Time Complexity (Python): O(N^2)worst case, with O(NlogN) on random data. 
For each new event, we insert the event into our binary tree. 
As this tree may not be balanced, it may take a linear number of steps to add each event.
Space Complexity: O(N), the size of the data structures used.

# 93ms 83.77%
class MyCalendar {
    TreeMap<Integer, Integer> calendar;
    public MyCalendar() {
        calendar = new TreeMap();
    }
    
    public boolean book(int start, int end) {
        Integer prev = calendar.floorKey(start);
        Integer next = calendar.ceilingKey(start);
        if (( prev == null || calendar.get(prev) <= start) &&
           (next == null || end <= next)) {
            calendar.put(start, end);
            return true;
        }
        return false;
    }
}
'''
