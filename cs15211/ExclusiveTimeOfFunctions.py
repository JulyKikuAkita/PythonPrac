__source__ = 'https://leetcode.com/problems/exclusive-time-of-functions/description/'
# Time:  O(n)
# Space: O(n)
#
# Description: Leetcode # Exclusive Time of Functions
#
# Given the running logs of n functions that are executed in a nonpreemptive single threaded CPU,
# find the exclusive time of these functions.
#
# Each function has a unique id, start from 0 to n-1. A function may be called recursively or by another function.
#
# A log is a string has this format :
# function_id:start_or_end:timestamp.
# For example, "0:start:0" means function 0 starts from the very beginning of time 0.
# "0:end:0" means function 0 ends to the very end of time 0.
#
# Exclusive time of a function is defined as the time spent within this function,
# the time spent by calling other functions should not be considered as this function's exclusive time.
# You should return the exclusive time of each function sorted by their function id.
#
# Example 1:
# Input:
# n = 2
# logs =
# ["0:start:0",
#  "1:start:2",
#  "1:end:5",
#  "0:end:6"]
# Output:[3, 4]
#
# Explanation:
# Function 0 starts at time 0, then it executes 2 units of time and reaches the end of time 1.
# Now function 0 calls function 1, function 1 starts at time 2, executes 4 units of time and end at time 5.
# Function 0 is running again at time 6, and also end at the time 6, thus executes 1 unit of time.
# So function 0 totally execute 2 + 1 = 3 units of time, and function 1 totally execute 4 units of time.
# Note:
# Input logs will be sorted by timestamp, NOT log id.
# Your output should be sorted by function id, which means the 0th element of
# your output corresponds to the exclusive time of function 0.
# Two functions won't start or end at the same time.
# Functions could be called recursively, and will always end.
# 1 <= n <= 100
#
# Companies
# Facebook
# Related Topics
# Stack
#
# import unittest
# Thought:
# 1) We examine two approaches - both will be stack based.
#
# In a more conventional approach, let's look between adjacent events,
# with duration time - prev_time. If we started a function,
# and we have a function in the background, then it was running during this time.
# Otherwise, we ended the function that is most recent in our stack.
#
import unittest
# 60ms 97.10%
class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        ans = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            fn, typ, time = log.split(':')
            fn, time = int(fn), int(time)

            if typ == 'start':
                if stack:
                    ans[stack[-1]] += time - prev_time
                stack.append(fn)
                prev_time = time
            else:
                ans[stack.pop()] += time - prev_time + 1
                prev_time = time + 1

        return ans
#
# 2) In the second approach, we try to record the "penalty" a function takes.
# For example, if function 0 is running at time [1, 10], and function 1 runs at time [3, 5],
# then we know function 0 ran for 10 units of time, less a 3 unit penalty. The idea is this:
# Whenever a function completes using T time,
# any functions that were running in the background take a penalty of T.
# Here is a slow version to illustrate the idea:
#
# 72ms 32.71%
class Solution2(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        ans = [0] * n
        #stack = SuperStack()
        stack = []

        for log in logs:
            fn, typ, time = log.split(':')
            fn, time = int(fn), int(time)

            if typ == 'start':
                stack.append(time)
            else:
                delta = time - stack.pop() + 1
                ans[fn] += delta
                #stack.add_across(delta)
                stack = [t+delta for t in stack] #inefficient

        return ans

# This code already ACs, but it isn't efficient.
# However, we can easily upgrade our stack to a "superstack" that supports self.add_across:
# addition over the whole array in constant time.

class SuperStack(object):
    def __init__(self):
        self.A = []
    def append(self, x):
        self.A.append([x, 0])
    def pop(self):
        x, y = self.A.pop()
        if self.A:
            self.A[-1][1] += y
        return x + y
    def add_across(self, y):
        if self.A:
            self.A[-1][1] += y
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/exclusive-time-of-functions/solution/

# 25ms 74.71%
class Solution {
    public int[] exclusiveTime(int n, List < String > logs) {
        Stack < Integer > stack = new Stack < > ();
        int[] res = new int[n];
        String[] s = logs.get(0).split(":");
        stack.push(Integer.parseInt(s[0]));
        int i = 1, prev = Integer.parseInt(s[2]);
        while (i < logs.size()) {
            s = logs.get(i).split(":");
            if (s[1].equals("start")) {
                if (!stack.isEmpty())
                    res[stack.peek()] += Integer.parseInt(s[2]) - prev;
                stack.push(Integer.parseInt(s[0]));
                prev = Integer.parseInt(s[2]);
            } else {
                res[stack.peek()] += Integer.parseInt(s[2]) - prev + 1;
                stack.pop();
                prev = Integer.parseInt(s[2]) + 1;
            }
            i++;
        }
        return res;
    }
}

# 23ms 92.46%
class Solution {
    public int[] exclusiveTime(int n, List<String> logs) {
        int[] res = new int[n];
        Stack<Integer> stack = new Stack<>();
        int prevTime = 0;
        for (String log : logs) {
            String[] parts = log.split(":");
            if (!stack.isEmpty()) res[stack.peek()] +=  Integer.parseInt(parts[2]) - prevTime;
            prevTime = Integer.parseInt(parts[2]);
            if (parts[1].equals("start")) stack.push(Integer.parseInt(parts[0]));
            else {
                res[stack.pop()]++;
                prevTime++;
            }
        }
        return res;
    }
}

# self-defined stack
# 8ms 100%
public class Solution {
    private static class Info {
        int id;
        int time;
        boolean isStart;
        public Info (final String log) {
            final char[] chs = log.toCharArray();
            id = 0;
            int i = 0;
            while (chs[i] != ':')  id = id * 10 + chs[i++] - '0';
            ++i;
            isStart = chs[i] == 's';
            i += isStart ? 6 : 4;
            time = 0;
            while (i < chs.length) time = time * 10 + chs[i++] - '0';
        }
    }

    private static class Stack {
        int[] times;
        final List<Info> stack = new ArrayList<>();
        Stack(int n, List<String> logs) {
            times = new int[n];
            for (String log : logs) {
                Info info = new Info(log);
                if (info.isStart) push(info);
                else pop(info);
            }
        }

        private void push(final Info info) {
            stack.add(info);
        }

        private void pop(final Info info) {
            Info tmp = stack.get(stack.size()-1);
            int totalTime = info.time + 1 - tmp.time;
            times[tmp.id] += totalTime;
            stack.remove(stack.size()-1);
            if (stack.size() > 0) {
                tmp = stack.get(stack.size()-1);
                times[tmp.id] -= totalTime;
            }
        }
    }

    public int[] exclusiveTime(int n, List<String> logs) {
        final Stack stack = new Stack(n, logs);
        return stack.times;
    }

}
'''