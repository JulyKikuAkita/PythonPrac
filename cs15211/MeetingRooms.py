__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/meeting-rooms.py
# Time:  O(nlogn)
# Space: O(n)
#
#Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
# determine if a person could attend all meetings.
#
# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return false.
#
#  Facebook
# Hide Tags Sort
# Hide Similar Problems (M) Merge Intervals (M) Meeting Rooms II
#
#
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {boolean}
    def canAttendMeetings(self, intervals):
        intervals.sort(key = lambda x: x.start)

        for i in xrange(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False
        return True

# Java
# http://buttercola.blogspot.com/2015/08/leetcode-meeting-rooms.html
var = '''
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
    public boolean canAttendMeetings(Interval[] intervals) {
        if(intervals ==null || intervals.length == 0) return true;
        
        Arrays.sort(intervals, new IntervalComparator());
        for(int i = 1; i < intervals.length; i++){
            if(isOverlappered(intervals[i-1], intervals[i]) ) return false;
        }
        return true;
    }

    public class IntervalComparator implements Comparator<Interval>{
        public int compare(Interval a, Interval b){
            return a.start - b.start;
        }
    }
    
    private boolean isOverlappered(Interval a, Interval b){
        return a.end > b.start;
    }
}

#Java 8:
public class Solution {
    public boolean canAttendMeetings(Interval[] intervals) {
        if(intervals == null || intervals.length == 0) return true;
        Arrays.sort(intervals, (Interval a, Interval b) -> a.start - b.start); //asc
        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i].start < intervals[i-1].end) return false;
        }
        return true;
    }
}

'''