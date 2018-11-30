__source__ = 'https://leetcode.com/problems/design-circular-queue/description/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 622. Design Circular Queue
#
# Design your implementation of the circular queue.
# The circular queue is a linear data structure in which the operations are performed based on FIFO
# (First In First Out) principle and the last position is connected back to the first position to make a circle.
# It is also called "Ring Buffer".
#
# One of the benefits of the circular queue is that we can make use of the spaces in front of the queue.
# In a normal queue, once the queue becomes full,
# we cannot insert the next element even if there is a space in front of the queue.
# But using the circular queue, we can use the space to store new values.
#
# Your implementation should support following operations:
#
# MyCircularQueue(k): Constructor, set the size of the queue to be k.
# Front: Get the front item from the queue. If the queue is empty, return -1.
# Rear: Get the last item from the queue. If the queue is empty, return -1.
# enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
# deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
# isEmpty(): Checks whether the circular queue is empty or not.
# isFull(): Checks whether the circular queue is full or not.
#
#
# Example:
#
# MyCircularQueue circularQueue = new MyCircularQueue(3); // set the size to be 3
# circularQueue.enQueue(1);  // return true
# circularQueue.enQueue(2);  // return true
# circularQueue.enQueue(3);  // return true
# circularQueue.enQueue(4);  // return false, the queue is full
# circularQueue.Rear();  // return 3
# circularQueue.isFull();  // return true
# circularQueue.deQueue();  // return true
# circularQueue.enQueue(4);  // return true
# circularQueue.Rear();  // return 4
#
# Note:
#
# All values will be in the range of [0, 1000].
# The number of operations will be in the range of [1, 1000].
# Please do not use the built-in Queue library.

import unittest


class Solution(object):
    pass  # your function here


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/design-circular-queue/discuss/186592/Java-Simple-Solution
# 62ms, 98.04%

class MyCircularQueue {
    private int[] A;
    private int front;
    private int rear;
    private int size;
    private int capacity;

    /** Initialize your data structure here. Set the size of the queue to be k. */
    public MyCircularQueue(int k) {
        A = new int[k];
        front = 0;
        rear = 0;
        size = 0;
        capacity = k;
    }

    /** Insert an element into the circular queue. Return true if the operation is successful. */
    public boolean enQueue(int value) {
        if (size == capacity) return false;
        rear = (front + size) % capacity;
        A[rear] = value;
        size++;
        return true;
    }

    /** Delete an element from the circular queue. Return true if the operation is successful. */
    public boolean deQueue() {
        if (size == 0) return false;
        front = (front + 1) % capacity;
        size--;
        return true;
    }

    /** Get the front item from the queue. */
    public int Front() {
        if (size == 0) return -1;
        return A[front];
    }

    /** Get the last item from the queue. */
    public int Rear() {
        if (size == 0) return -1;
        return A[rear];
    }

    /** Checks whether the circular queue is empty or not. */
    public boolean isEmpty() {
        return size == 0;
    }

    /** Checks whether the circular queue is full or not. */
    public boolean isFull() {
        return size == capacity;
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */
'''