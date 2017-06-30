__source__ = 'https://leetcode.com/problems/minimum-time-difference/#/description'
# Time:  O()
# Space: O()
#
# Description:
# Given a list of 24-hour clock time points in "Hour:Minutes" format,
# find the minimum minutes difference between any two time points in the list.
#
# Example 1:
# Input: ["23:59","00:00"]
# Output: 1
# Note:
# The number of time points in the given list is at least 2 and won't exceed 20000.
# The input time is legal and ranges from 00:00 to 23:59.
# Hide Company Tags Palantir
# Hide Tags String
#
import unittest

# Convert each timestamp to it's integer number of minutes past midnight,
# and sort the array of minutes.
# The required minimum difference must be a difference between two adjacent elements in the circular array
# (so the last element is "adjacent" to the first.) We take the minimum value of all of them.

class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def convert(time):
            return int(time[:2]) * 60 + int(time[3:])
        minutes = map(convert, timePoints)
        minutes.sort()
        return min( (y - x) % (24 * 60)
            for x, y in zip(minutes, minutes[1:] + minutes[:1]) )

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
There is only 24 * 60 = 1440 possible time points.
Just create a boolean array, each element stands for if we see that time point or not.
Then things become simple...
public class Solution {
    public int findMinDifference(List<String> timePoints) {
        boolean[] mark = new boolean[24 * 60];
        for (String time : timePoints) {
            String[] t = time.split(":");
            int h = Integer.parseInt(t[0]);
            int m = Integer.parseInt(t[1]);
            if (mark[h * 60 + m]) return 0;
            mark[h * 60 + m] = true;
        }

        int prev = 0, min = Integer.MAX_VALUE;
        int first = Integer.MAX_VALUE, last = Integer.MIN_VALUE;
        for (int i = 0; i < 24 * 60; i++) {
            if (mark[i]) {
                if (first != Integer.MAX_VALUE) {
                    min = Math.min(min, i - prev);
                }
                first = Math.min(first, i);
                last = Math.max(last, i);
                prev = i;
            }
        }

        min = Math.min(min, (24 * 60 - last + first));

        return min;
    }
}

2. Java sorting with a sentinel node
public class Solution {
    public int findMinDifference(List<String> timePoints) {
        int n = timePoints.size();
        List<Time> times = new ArrayList<>();
        for (String tp : timePoints) {
            String[] strs = tp.split(":");
            times.add(new Time(Integer.parseInt(strs[0]), Integer.parseInt(strs[1])));
        }

        Collections.sort(times);
        // inplace, Time class no need to implement Comparable
        // Collections.sort(times, ( Time a, Time b) -> (a.h == b.h ? a.m - b.m : a.h - b.h));

        Time earlist = times.get(0);
        times.add(new Time(earlist.h + 24, earlist.m));
        int minDiff = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) { //note, i start with 0 and get Diff to i + 1
            int diff = (int) Math.abs(times.get(i).getDiff(times.get(i + 1)));
            minDiff = Math.min(minDiff, diff);
        }
        return minDiff;
    }

}

class Time implements Comparable<Time> {
    int h;
    int m;
    public Time(int h, int m) {
        this.h = h;
        this.m = m;
    }

    public int compareTo(Time other) {
        if (this.h == other.h) {
            return this.m - other.m;
        }
        return this.h - other.h;
    }

    public int getDiff(Time other) {
        return (this.h - other.h) * 60 + (this.m - other.m);
    }
}

3.
public class Solution {
    public int findMinDifference(List<String> timePoints) {
        int mm = Integer.MAX_VALUE;
        List<Integer> time = new ArrayList<>();

        for(int i = 0; i < timePoints.size(); i++){
            Integer h = Integer.valueOf(timePoints.get(i).substring(0, 2));
            time.add(60 * h + Integer.valueOf(timePoints.get(i).substring(3, 5)));
        }

        Collections.sort(time, (Integer a, Integer b) -> a - b);

        for(int i = 1; i < time.size(); i++){
            //System.out.println(time.get(i));
            mm = Math.min(mm, time.get(i) - time.get(i-1));
        }

        int corner = time.get(0) + (1440 - time.get(time.size()-1));
        return Math.min(mm, corner);
    }
}
'''