__source__ = 'https://leetcode.com/problems/logger-rate-limiter/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/logger-rate-limiter.py
# Time:  O(1), amortized
# Space: O(k), k is the max number of printed messages in last 10 seconds
#
# Description: Leetcode # 359. Logger Rate Limiter
#
# Design a logger system that receive stream of messages along with its timestamps,
# each message should be printed if and only if it is not printed in the last 10 seconds.
#
# Given a message and a timestamp (in seconds granularity),
# return true if the message should be printed in the given timestamp, otherwise returns false.
#
# It is possible that several messages arrive roughly at the same time.
#
# Example:
#
# Logger logger = new Logger();
#
# // logging string "foo" at timestamp 1
# logger.shouldPrintMessage(1, "foo"); returns true;
#
# // logging string "bar" at timestamp 2
# logger.shouldPrintMessage(2,"bar"); returns true;
#
# // logging string "foo" at timestamp 3
# logger.shouldPrintMessage(3,"foo"); returns false;
#
# // logging string "bar" at timestamp 8
# logger.shouldPrintMessage(8,"bar"); returns false;
#
# // logging string "foo" at timestamp 10
# logger.shouldPrintMessage(10,"foo"); returns false;
#
# // logging string "foo" at timestamp 11
# logger.shouldPrintMessage(11,"foo"); returns true;
#
# Companies
# Google
# Related Topics
# Hash Table Design
# Similar Questions
# Design Hit Counter
#
import collections
import unittest
# Time:  O(1), amortized
# Space: O(k), k is the max number of printed messages in last 10 seconds
class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__dq = collections.deque()
        self.__printed = set()

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false. The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        while self.__dq and self.__dq[0][0] <= timestamp - 10:
            self.__printed.remove(self.__dq.popleft()[1])
        if message in self.__printed:
            return False
        self.__dq.append((timestamp, message))
        self.__printed.add(message)
        return True

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
# 97.72% 144ms
public class Logger {
    private Map<String, Integer> map;

    /** Initialize your data structure here. */
    public Logger() {
        map = new HashMap<>();
    }

    /** Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity. */
    public boolean shouldPrintMessage(int timestamp, String message) {
        boolean result = !map.containsKey(message) || map.get(message) <= timestamp - 10;
        if (result) {
            map.put(message, timestamp);
        }
        return result;
    }
}

/**
 * Your Logger object will be instantiated and called as such:
 * Logger obj = new Logger();
 * boolean param_1 = obj.shouldPrintMessage(timestamp,message);
 */

 #4.7% 199ms
 public class Logger {
    HashMap<String, Integer> ok;
    /** Initialize your data structure here. */
    public Logger() {
        ok = new HashMap<>();
    }

    /** Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity. */
    public boolean shouldPrintMessage(int timestamp, String message) {
        if(ok.getOrDefault(message, 0) > timestamp) return false;
        ok.put(message, timestamp + 10);
        return true;
    }
}

 '''