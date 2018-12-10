__source__ = 'https://leetcode.com/problems/design-hit-counter/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/design-hit-counter.py
# Time:  O(1), amortized
# Space: O(k), k is the count of seconds.
#
# Description: Leetcode # 362. Design Hit Counter
#
# Design a hit counter which counts the number of hits received in the past 5 minutes.
#
# Each function accepts a timestamp parameter (in seconds granularity)
# and you may assume that calls are being made to the system in chronological order
# (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.
#
# It is possible that several hits arrive roughly at the same time.
#
# Example:
# HitCounter counter = new HitCounter();
#
# // hit at timestamp 1.
# counter.hit(1);
#
# // hit at timestamp 2.
# counter.hit(2);
#
# // hit at timestamp 3.
# counter.hit(3);
#
# // get hits at timestamp 4, should return 3.
# counter.getHits(4);
#
# // hit at timestamp 300.
# counter.hit(300);
#
# // get hits at timestamp 300, should return 4.
# counter.getHits(300);
#
# // get hits at timestamp 301, should return 3.
# counter.getHits(301);
# Follow up:
# What if the number of hits per second could be very large? Does your design scale?
#
# Companies
# Google Dropbox
# Related Topics
# Design
# Similar Questions
# Logger Rate Limiter
#

# Time:  O(1), amortized
# Space: O(k), k is the count of seconds.

from collections import deque
import unittest
class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__k = 300
        self.__dq = deque()
        self.__count = 0

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.getHits(timestamp)
        if self.__dq and self.__dq[-1][0] == timestamp:
            self.__dq[-1][1] += 1
        else:
            self.__dq.append([timestamp, 1])
        self.__count += 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        while self.__dq and self.__dq[0][0] <= timestamp - self.__k:
            self.__count -= self.__dq.popleft()[1]
        return self.__count

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# 55ms 95.74%
class HitCounter {
    private int[] buckets;
    private int prev;
    private int count;

    /** Initialize your data structure here. */
    public HitCounter() {
        buckets = new int[300];
    }

    /** Record a hit.
        @param timestamp - The current timestamp (in seconds granularity). */
    public void hit(int timestamp) {
        clearStaleData(timestamp);
        prev = timestamp;
        buckets[(timestamp - 1) % buckets.length]++;
        count++;
    }

    /** Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity). */
    public int getHits(int timestamp) {
        clearStaleData(timestamp);
        prev = timestamp;
        return count;
    }

    private void clearStaleData(int cur) {
        if (cur - prev >= buckets.length) {
            count = 0;
            Arrays.fill(buckets, 0);
        } else {
            prev++;
            int index = (prev - 1) % buckets.length;
            while (prev <= cur) {
                count -= buckets[index];
                buckets[index] = 0;
                prev++;
                index++;
                if (index == buckets.length) {
                    index = 0;
                }
            }
        }
    }
}

/**
 * Your HitCounter object will be instantiated and called as such:
 * HitCounter obj = new HitCounter();
 * obj.hit(timestamp);
 * int param_2 = obj.getHits(timestamp);
 */

 # 70ms 14.68%
 class HitCounter {
    private Queue<Integer> queue;

    /** Initialize your data structure here. */
    public HitCounter() {
        queue = new LinkedList<Integer>();
    }

    /** Record a hit.
        @param timestamp - The current timestamp (in seconds granularity). */
    public void hit(int timestamp) {
        queue.offer(timestamp);
    }

    /** Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity). */
    public int getHits(int timestamp) {
        while (!queue.isEmpty() && queue.peek() <= timestamp - 300)
            queue.poll();
        return queue.size();
    }
}

# 56ms 91.96%
class HitCounter {
    int times[] = new int[300];
    int hits[] = new int[300];

    /** Initialize your data structure here. */
    public HitCounter() {


    }

    /** Record a hit.
        @param timestamp - The current timestamp (in seconds granularity). */
    public void hit(int timestamp) {
        int i = timestamp % 300;
        if (times[i] != timestamp) {
            times[i] = timestamp;
            hits[i] = 0;
        }
        hits[i]++;
    }

    /** Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity). */
    public int getHits(int timestamp) {
        int res = 0;
        for (int i = 0; i < 300; i++) {
            if (times[i] > timestamp - 300) {
                res += hits[i];
            }
        }
        return res;
    }
}

 '''
