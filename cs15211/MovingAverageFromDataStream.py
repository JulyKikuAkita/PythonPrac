__source__ = 'https://leetcode.com/problems/moving-average-from-data-stream/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/moving-average-from-data-stream.py
# Time:  O(1)
# Space: O(w)
#
# Description: Leetcode # 346. Moving Average from Data Stream
#
# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
#
# For example,
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3
#
# Companies
# Google
# Related Topics
# Design Queue
#
import unittest
from collections import deque

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.__size = size
        self.__sum = 0
        self.__q = deque([])

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.__q) == self.__size:
            self.__sum -= self.__q.popleft()
        self.__sum += val
        self.__q.append(val)
        return 1.0 * self.__sum / len(self.__q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
#10.80% 181ms
public class MovingAverage {
    private int windowSize;
    private Queue<Integer> queue;
    private double sum;

    /** Initialize your data structure here. */
    public MovingAverage(int size) {
        windowSize = size;
        queue = new LinkedList<>();
    }

    public double next(int val) {
        if (queue.size() == windowSize) {
            sum -= queue.poll();
        }
        queue.add(val);
        sum += val;
        return sum / queue.size();
    }
}

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage obj = new MovingAverage(size);
 * double param_1 = obj.next(val);
 */

#76.77% 143ms
public class MovingAverage {
    private int [] window;
    private int n, insert;
    private long sum;

    /** Initialize your data structure here. */
    public MovingAverage(int size) {
        window = new int[size];
        insert = 0;
        sum = 0;
    }

    public double next(int val) {
        if (n < window.length)  n++;
        sum -= window[insert];
        sum += val;
        window[insert] = val;
        insert = (insert + 1) % window.length;

        return (double)sum / n;
    }
}
'''