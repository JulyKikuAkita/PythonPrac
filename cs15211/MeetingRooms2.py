__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/meeting-rooms-ii.py
# Time:  O(nlogn)
# Space: O(n)
'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.

Google Facebook
Heap Greedy Sort

'''

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
#
# http://buttercola.blogspot.com/2015/08/leetcode-meeting-rooms-ii.html
# with priority queue
# http://blog.csdn.net/pointbreak1/article/details/48840671
#test
js = '''
/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
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
'''