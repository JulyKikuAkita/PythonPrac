__source__ = 'https://leetcode.com/problems/merge-intervals/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/merge-intervals.py
# Time:  O(nlogn)
# Space: O(1)
# sort
#
# Given a collection of intervals, merge all overlapping intervals.
#
# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].
#
# Topics:
# Array Sort
# You might like:
# (H) Insert Interval (E) Meeting Rooms (M) Meeting Rooms II (M) Teemo Attacking (M) Add Bold Tag in String
# Company:
# LinkedIn Google Facebook Twitter Microsoft Bloomberg Yelp
#
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "[{}, {}]".format(self.start, self.end)

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        if not intervals:
            return intervals
        intervals.sort(key = lambda x :  x .start)
        result = [intervals[0]]
        for i in xrange(1, len(intervals)):
            prev, cur = result[-1], intervals[i]
            if cur.start <= prev.end:
                prev.end = max(prev.end, cur.end)
            else:
                result.append(cur)
        return result

if __name__ == "__main__":
    print Solution().merge([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15,18)])


#Java Solution:
# http://www.programcreek.com/2012/12/leetcode-merge-intervals/


#java
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
#16%
public List<Interval> merge(List<Interval> intervals) {
    if (intervals.size() <= 1)
        return intervals;

    // Sort by ascending starting point using an anonymous Comparator
    intervals.sort((i1, i2) -> Integer.compare(i1.start, i2.start));

    List<Interval> result = new LinkedList<Interval>();
    int start = intervals.get(0).start;
    int end = intervals.get(0).end;

    for (Interval interval : intervals) {
        if (interval.start <= end) // Overlapping intervals, move the end if needed
            end = Math.max(end, interval.end);
        else {                     // Disjoint intervals, add the previous one and reset bounds
            result.add(new Interval(start, end));
            start = interval.start;
            end = interval.end;
        }
    }

    // Add the last interval
    result.add(new Interval(start, end));
    return result;
}

#99%
public class Solution {
    public List<Interval> merge(List<Interval> intervals) {
        int n = intervals.size();
        int[] starts = new int[n];
        int[] ends = new int[n];
        for (int i = 0; i < n; i++) {
            starts[i] = intervals.get(i).start;
            ends[i] = intervals.get(i).end;
        }
        Arrays.sort(starts);
        Arrays.sort(ends);
        List<Interval> res = new ArrayList<Interval>();
        int startP = 0;
        for (int endP = 0; endP < n; endP++) {
            // when we begin a new intervals
            if (endP == n - 1 || starts[endP + 1] > ends[endP]) {
                res.add(new Interval(starts[startP], ends[endP]));
                startP = endP + 1;
            }
        }
        return res;
    }
}
'''