__source__ = 'https://leetcode.com/problems/design-circular-deque/description/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 641. Design Circular Deque
#
# Design your implementation of the circular double-ended queue (deque).
#
# Your implementation should support following operations:
#
# MyCircularDeque(k): Constructor, set the size of the deque to be k.
# insertFront(): Adds an item at the front of Deque. Return true if the operation is successful.
# insertLast(): Adds an item at the rear of Deque. Return true if the operation is successful.
# deleteFront(): Deletes an item from the front of Deque. Return true if the operation is successful.
# deleteLast(): Deletes an item from the rear of Deque. Return true if the operation is successful.
# getFront(): Gets the front item from the Deque. If the deque is empty, return -1.
# getRear(): Gets the last item from Deque. If the deque is empty, return -1.
# isEmpty(): Checks whether Deque is empty or not.
# isFull(): Checks whether Deque is full or not.
#
#
# Example:
#
# MyCircularDeque circularDeque = new MycircularDeque(3); // set the size to be 3
# circularDeque.insertLast(1);			// return true
# circularDeque.insertLast(2);			// return true
# circularDeque.insertFront(3);			// return true
# circularDeque.insertFront(4);			// return false, the queue is full
# circularDeque.getRear();  			// return 2
# circularDeque.isFull();				// return true
# circularDeque.deleteLast();			// return true
# circularDeque.insertFront(4);			// return true
# circularDeque.getFront();			// return 4
#
#
# Note:
#
# All values will be in the range of [0, 1000].
# The number of operations will be in the range of [1, 1000].
# Please do not use the built-in Deque library.
#
import unittest

# 91.82% 68ms

class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.a = []
        self.size = 0
        self.limit = k

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.size < self.limit:
            self.a = [value] + self.a
            self.size += 1
            return True
        return False

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.size < self.limit:
            self.a = self.a + [value]
            self.size += 1
            return True
        return False

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.size != 0:
            self.size -= 1
            self.a = self.a[1:]
            return True
        return False

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.size != 0:
            self.size -= 1
            self.a = self.a[:-1]
            return True
        return False

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.size != 0:
            return self.a[0]
        return -1

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.size != 0:
            return self.a[-1]
        return -1

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.size == 0

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self.size == self.limit


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: key is to maintain pointer at first/last index
# -> first = (first-1+capacity) % capacity;
#
# 95.71% 64ms
#
class MyCircularDeque {
    int[] arr;
    int first, last, size, limit;
    /** Initialize your data structure here. Set the size of the deque to be k. */
    public MyCircularDeque(int k) {
        arr = new int[k];
        first = 0;//next first, need to calculate remove index
        last = 1;//next last, need to calculate remove index
        size = 0;
        limit = k;
    }

    /** Adds an item at the front of Deque. Return true if the operation is successful. */
    public boolean insertFront(int value) {
        if (isFull()) return false;
        size++;
        arr[first] = value;
        first = (first - 1 + limit) % limit;
        return true;
    }

    /** Adds an item at the rear of Deque. Return true if the operation is successful. */
    public boolean insertLast(int value) {
        if (isFull()) return false;
        size++;
        arr[last] = value;
        last = (last + 1) % limit;
        return true;
    }

    /** Deletes an item from the front of Deque. Return true if the operation is successful. */
    public boolean deleteFront() {
        if (isEmpty()) return false;
        size--;
        first = (first + 1) % limit;
        return true;
    }

    /** Deletes an item from the rear of Deque. Return true if the operation is successful. */
    public boolean deleteLast() {
        if (isEmpty()) return false;
        size--;
        last = (last - 1 + limit) % limit;
        return true;
    }

    /** Get the front item from the deque. */
    public int getFront() {
        return isEmpty() ? -1 : arr[(first + 1 + limit) % limit];
    }

    /** Get the last item from the deque. */
    public int getRear() {
        return isEmpty() ? -1 : arr[(last - 1 + limit) % limit];
    }

    /** Checks whether the circular deque is empty or not. */
    public boolean isEmpty() {
        return size == 0;
    }

    /** Checks whether the circular deque is full or not. */
    public boolean isFull() {
        return limit == size;
    }
}

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque obj = new MyCircularDeque(k);
 * boolean param_1 = obj.insertFront(value);
 * boolean param_2 = obj.insertLast(value);
 * boolean param_3 = obj.deleteFront();
 * boolean param_4 = obj.deleteLast();
 * int param_5 = obj.getFront();
 * int param_6 = obj.getRear();
 * boolean param_7 = obj.isEmpty();
 * boolean param_8 = obj.isFull();
 */
'''