import heapq

__source__ = 'https://leetcode.com/problems/employee-free-time/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 759. Employee Free Time
#
# We are given a list schedule of employees, which represents the working time for each employee.
#
# Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.
#
# Return the list of finite intervals representing common,
# positive-length free time for all employees, also in sorted order.
#
# Example 1:
# Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
# Output: [[3,4]]
# Explanation:
# There are a total of three employees, and all common
# free time intervals would be [-inf, 1], [3, 4], [10, inf].
# We discard any intervals that contain inf as they aren't finite.
# Example 2:
# Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
# Output: [[5,6],[7,9]]
# (Even though we are representing Intervals in the form [x, y],
# the objects inside are Intervals, not lists or arrays.
# For example, schedule[0][0].start = 1, schedule[0][0].end = 2,
# and schedule[0][0][0] is not defined.)
#
# Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.
#
# Note:
#
# schedule and schedule[i] are lists with lengths in range [1, 50].
# 0 <= schedule[i].start < schedule[i].end <= 10^8.
#
import unittest

#100ms 82.03%
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        OPEN, CLOSE = 0, 1

        events = []
        for emp in schedule:
            for iv in emp:
                events.append((iv.start, OPEN))
                events.append((iv.end, CLOSE))

        events.sort()
        ans = []
        prev = None
        bal = 0
        for t, cmd in events:
            if bal == 0 and prev is not None:
                ans.append(Interval(prev, t))

            bal += 1 if cmd is OPEN else -1
            prev = t
        return ans

#108ms 61.36%
class SolutionPQ(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        ans = []
        pq = [(emp[0].start, ei, 0) for ei, emp in enumerate(schedule)]
        heapq.heapify(pq)
        anchor = min(iv.start for emp in schedule for iv in emp)
        while pq:
            t, e_id, e_jx = heapq.heappop(pq)
            if anchor < t:
                ans.append(Interval(anchor, t))
            anchor = max(anchor, schedule[e_id][e_jx].end)
            if e_jx + 1 < len(schedule[e_id]):
                heapq.heappush(pq, (schedule[e_id][e_jx+1].start, e_id, e_jx+1))
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/employee-free-time/solution/

Approach #1: Events (Line Sweep) [Accepted]
Complexity Analysis
Time Complexity: O(ClogC), where C is the number of intervals across all employees.
Space Complexity: O(C).

#69ms 14.27%
/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
class Solution {
    public List<Interval> employeeFreeTime(List<List<Interval>> schedule) {
        final int OPEN = 0, CLOSE = 1;

        List<int[]> events = new ArrayList();
        for (List<Interval> employee: schedule) {
            for (Interval iv : employee) {
                events.add(new int[]{iv.start, OPEN});
                events.add(new int[]{iv.end, CLOSE});
            }
        }
        Collections.sort(events, (a, b) -> a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);
        List<Interval> ans = new ArrayList();

        int prev = -1, bal = 0;
        for (int[] event : events) {
            // event[0] = time, event[1] = command
            if (bal == 0 && prev >= 0) {
                ans.add(new Interval(prev, event[0]));
            }
            bal += event[1] == OPEN ? 1 : -1;
            prev = event[0];
        }
        return ans;
    }
}

#13ms 97.15%
class Solution {
    public List<Interval> employeeFreeTime(List<List<Interval>> schedule) {
        int size = 0;
        for(List<Interval> list : schedule) size += list.size();
        int[] starts = new int[size];
        int[] ends = new int[size];
        int index = 0;
        for(List<Interval> list : schedule){
            for (Interval ivl : list) {
                starts[index] = ivl.start;
                ends[index++] = ivl.end;
            }
        }

        Arrays.sort(starts);
        Arrays.sort(ends);
        List<Interval> res = new ArrayList<>();
        for (int i = 1; i < size; i++) {
            if (ends[i-1] < starts[i]) {
                res.add(new Interval(ends[i-1], starts[i]));
            }
        }
        return res;
    }
}

Approach #2: Priority Queue [Accepted]
Complexity Analysis
Time Complexity: O(ClogN), where N is the number of employees,
and C is the number of jobs across all employees.
The maximum size of the heap is N, so each push and pop operation is O(logN), and there are O(C) such operations.
Space Complexity: O(N) in additional space complexity.

# 54ms 52.63%
class Solution {
    class Job {
        int eid, index;
        Job(int e, int i) {
            eid = e;
            index = i;
        }
    }

    public List<Interval> employeeFreeTime(List<List<Interval>> schedule) {
        List<Interval> ans = new ArrayList();
        PriorityQueue<Job> pq = new PriorityQueue<Job>( (a, b) ->
            schedule.get(a.eid).get(a.index).start -
            schedule.get(b.eid).get(b.index).start);
        int ei = 0, anchor = Integer.MAX_VALUE;

        for (List<Interval> employee: schedule) {
            pq.offer(new Job(ei++, 0));
            anchor = Math.min(anchor, employee.get(0).start);
        }

        while (!pq.isEmpty()) {
            Job job = pq.poll();
            Interval iv = schedule.get(job.eid).get(job.index);
            if (anchor < iv.start) ans.add(new Interval(anchor, iv.start));
            anchor = Math.max(anchor, iv.end);
            if (++job.index < schedule.get(job.eid).size()) pq.offer(job);
        }
        return ans;
    }
}


'''