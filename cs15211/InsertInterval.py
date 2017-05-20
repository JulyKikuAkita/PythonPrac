__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/insert-interval.py
# Time:  O(n)
# Space: O(1)
# Sort
#
# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
#
# You may assume that the intervals were initially sorted according to their start times.
#
# Example 1:
# Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].
#
# Example 2:
# Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].
#
# This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
#

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "[{}, {}]".format(self.start, self.end)

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        return self.merge(intervals + [newInterval])

    def merge(self, intervals):
        if not intervals:
            return intervals
        intervals.sort(key = lambda x: x.start)
        result = [intervals[0]]
        for i in xrange(1, len(intervals)):
            prev, cur = result[-1], intervals[i]
            if cur.start <= prev.end:
                prev.end = max(prev.end, cur.end)
            else:
                result.append(cur)
        return result



# http://www.cnblogs.com/zuoyuan/p/3782048.html
class SolutionOther:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals.sort(key = lambda x: x.start)
        length = len(intervals)
        res = []

        for i in range(length):
            if res == []:
                res.append(intervals[i])
            else:
                size = len(res)
                if res[size-1].start <= intervals[i].start <= res[size-1].end:
                    res[size-1].end = max(intervals[i].end, res[size-1].end)
                else:
                    res.append(intervals[i])
        return res

#java solution
#http://www.programcreek.com/2012/12/leetcode-insert-interval/

#test
test = SolutionOther()
i1 = Interval(1,3)
i2 = Interval(6,9)
i3 = Interval(2,5)
a1 = [i1, i2]
i4 = Interval(1,2) ; i5 = Interval(3,5) ; i6 = Interval(6,7) ; i7 = Interval(8,10) ; i8 = Interval(12,16); i9 = Interval(4,9)
a2 = [i4, i5, i6, i7,i8]
ans1 = test.insert(a1, i3)
ans2 = test.insert(a2, i9)
for item in ans2:
    print item.start, item.end