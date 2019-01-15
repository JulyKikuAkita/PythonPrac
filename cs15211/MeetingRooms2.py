__source__ = 'https://leetcode.com/problems/meeting-rooms-ii/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/meeting-rooms-ii.py
# Time:  O(nlogn)
# Space: O(n)
#
# Description: Leetcode # 253. Meeting Rooms II
#
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
# find the minimum number of conference rooms required.
#
# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return 2.
#
# Companies
# Google Snapchat Facebook
# Related Topics
# Heap Greedy Sort
# Similar Questions
# Merge Intervals Meeting Rooms Minimum Number of Arrows to Burst Balloons
#
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
#
import unittest
# 40ms 81.38%
class Solution:
    # @param {Interval[]} intervals
    # @return {integer}
    def minMeetingRooms(self, intervals):
        starts, ends = [], []
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)

        starts.sort()
        ends.sort()

        s, e  = 0, 0
        min_rooms, cnt_rooms = 0, 0

        while s < len(starts):
            if starts[s] < ends[e]:
                cnt_rooms += 1 # Acquire a room
                # Update the min number of rooms.
                min_rooms = max(min_rooms, cnt_rooms)
                s += 1

            else:
                cnt_rooms -= 1 # Release a room
                e +=1
        return min_rooms

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/meeting-rooms-ii/solution/
/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
# 
# 2ms 100%
class Solution {
    public int minMeetingRooms(Interval[] intervals) {
        if (intervals == null || intervals.length == 0) return 0;
        int n = intervals.length, index = 0;
        int[] begins = new int[n];
        int[] ends = new int[n];
        for (Interval i: intervals) {
            begins[index] = i.start;
            ends[index] = i.end;
            index++;
        }
        Arrays.sort(begins);
        Arrays.sort(ends);
        int rooms = 0, pre = 0;
        for (int i = 0; i < n; i++) {
            rooms++;

            // room is released
            if (begins[i] >= ends[pre]) {
                rooms--;
                pre++;
            }
        }
        return rooms;
    }
}

# 7ms 75.98%
class Solution {
    public int minMeetingRooms(Interval[] intervals) {
         if (intervals == null || intervals.length == 0)
            return 0;

        // Sort the intervals by start time
        Arrays.sort(intervals, new Comparator<Interval>() {
            public int compare(Interval a, Interval b) { return a.start - b.start; }
        });

        // Use a min heap to track the minimum end time of merged intervals
        PriorityQueue<Interval> heap = new PriorityQueue<Interval>(intervals.length, new Comparator<Interval>() {
            public int compare(Interval a, Interval b) { return a.end - b.end; }
        });

        // start with the first meeting, put it to a meeting room
        heap.offer(intervals[0]);

        for (int i = 1; i < intervals.length; i++) {
            // get the meeting room that finishes earliest
            Interval interval = heap.poll();

            if (intervals[i].start >= interval.end) {
                // if the current meeting starts right after
                // there's no need for a new room, merge the interval
                interval.end = intervals[i].end;
            } else {
                // otherwise, this meeting needs a new room
                heap.offer(intervals[i]);
            }
            // don't forget to put the meeting room back
            heap.offer(interval);
        }
        return heap.size();
        }
}

# same as above
# 48ms 18.04%
class Solution {
    public int minMeetingRooms(Interval[] intervals) {
         if (intervals == null || intervals.length == 0)
            return 0;

        Arrays.sort(intervals, (Interval a, Interval b) -> (a.start - b.start));
        PriorityQueue<Interval> heap = new PriorityQueue<Interval>(intervals.length, (a, b) -> (a.end - b.end));
        heap.offer(intervals[0]);

        for (int i = 1; i < intervals.length; i++) {
            Interval interval = heap.poll();

            if (intervals[i].start < interval.end) { //needs a new room
                heap.offer(interval);
            } else {
                //use the same room
            }
            heap.offer(intervals[i]);
        }
        return heap.size();
        }
}

# sort intervals.end only 
# 42ms 30.99%
class Solution {
    public int minMeetingRooms(Interval[] intervals) {
        if(intervals == null || intervals.length == 0) return 0;
        Arrays.sort(intervals, (Interval a, Interval b) -> a.start - b.start);
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        minHeap.offer(intervals[0].end);
        for (int i = 1; i < intervals.length; i++) {
            int end= minHeap.poll();
            if (intervals[i].start < end) {
                minHeap.offer(intervals[i].end);
                minHeap.offer(end);
            }else {
                minHeap.offer(intervals[i].end);
            }
        }
        return minHeap.size();
    }
}
'''
