__source__ = 'https://leetcode.com/problems/meeting-rooms-ii/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/meeting-rooms-ii.py
# Time:  O(nlogn)
# Space: O(n)
#
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
# find the minimum number of conference rooms required.
#
# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return 2.
#
#Topics:
# Heap Greedy Sort
# You might like:
# (M) Merge Intervals (E) Meeting Rooms (M) Minimum Number of Arrows to Burst Balloons
# Company:
# Google Snapchat Facebook
#

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

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
#
# Java :
java = '''
/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
 80.43%
public class Solution {
    public int minMeetingRooms(Interval[] intervals) {
        int len = intervals.length;
        int[] starts = new int[len];
        int[] ends = new int[len];
        for (int i = 0; i < len; i++) {
            starts[i] = intervals[i].start;
            ends[i] = intervals[i].end;
        }
        Arrays.sort(starts);
        Arrays.sort(ends);
        int startIndex = 0;
        int endIndex = 0;
        int result = 0;
        int cur = 0;
        while (startIndex < len) {
            if (starts[startIndex] < ends[endIndex]) {
                cur++;
                result = Math.max(result, cur);
                startIndex++;
            } else {
                cur--;
                endIndex++;
            }
        }
        return result;
    }
}

53.4%
public class Solution {
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

same as above
public class Solution {
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

47% //sort only intervals.end
public class Solution {
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