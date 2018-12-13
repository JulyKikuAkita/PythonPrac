__source__ = 'https://leetcode.com/problems/implement-stack-using-queues/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/implement-stack-using-queues.py
# Time: push: O(n), pop: O(1), top: O(1)
# Space: O(n)
#
# Description: Leetcode # 225. Implement Stack using Queues
#
# Implement the following operations of a stack using queues.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# empty() -- Return whether the stack is empty.
# Notes:
# You must use only standard operations of a queue -- which
# means only push to back, peek/pop from front, size, and is
# empty operations are valid.
# Depending on your language, queue may not be supported natively.
# You may simulate a queue by using a list or deque (double-ended
# queue), as long as you use only standard operations of a queue.
# You may assume that all operations are valid (for example, no pop
# or top operations will be called on an empty stack).
#
# Companies
# Bloomberg
# Related Topics
# Stack Design
# Similar Questions
# Implement Queue using Stacks
#
import unittest
import collections
class Queue:
    def __init__(self):
        self.data = collections.deque()

    def push(self, x):
        self.data.append(x)

    def peek(self):
        return self.data[0]

    def pop(self):
        return self.data.popleft()

    def size(self):
        return len(self.data)

    def empty(self):
        return len(self.data) == 0


class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.q_ = Queue()

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.q_.push(x)
        for _ in xrange(self.q_.size() - 1):
            self.q_.push(self.q_.pop())

    # @return nothing
    def pop(self):
        self.q_.pop()

    # @return an integer
    def top(self):
        return self.q_.peek()

    # @return an boolean
    def empty(self):
        return self.q_.empty()


# Time: push: O(1), pop: O(n), top: O(1)
# Space: O(n)
class Stack2:
    # initialize your data structure here.
    def __init__(self):
        self.q_ = Queue()
        self.top_ = None

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.q_.push(x)
        self.top_ = x

    # @return nothing
    def pop(self):
        for _ in xrange(self.q_.size() - 1):
            self.top_ = self.q_.pop()
            self.q_.push(self.top_)
        self.q_.pop()

    # @return an integer
    def top(self):
        return self.top_

    # @return an boolean
    def empty(self):
        return self.q_.empty()

class Stack3(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue.append(x)
        for i in xrange(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))

    def pop(self):
        """
        :rtype: nothing
        """
        self.queue.pop(0)

    def top(self):
        """
        :rtype: int
        """
        return self.queue[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/implement-stack-using-queues/solution/

# only one queue
# 56ms 82.44%
class MyStack {
    Queue<Integer> mQ;

    /** Initialize your data structure here. */
    public MyStack() {
        mQ = new LinkedList<>();
    }

    /** Push element x onto stack. */
    public void push(int x) {
        mQ.add(x);
        for (int i = 0; i< mQ.size() - 1; i++) { //except the last one just added
            mQ.add(mQ.poll());
        }
    }

    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        return mQ.poll();
    }

    /** Get the top element. */
    public int top() {
        return mQ.peek();
    }

    /** Returns whether the stack is empty. */
    public boolean empty() {
        return mQ.isEmpty();
    }
}


# Using 2 queue
# 80ms 19.43%
class MyStack {
    Queue<Integer> q1;
    Queue<Integer> q2;

    /** Initialize your data structure here. */
    public MyStack() {
        q1 = new LinkedList<>();
        q2 = new LinkedList<>();
    }

    /** Push element x onto stack. */
    public void push(int x) {
        q1.add(x);
        if (q1.size() > 1) q2.add(q1.poll());
    }

    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        int n = q1.poll();
        while (q2.size() > 0)
            q1.add(q2.poll());
        while (q1.size() > 1)
            q2.add(q1.poll());
        return n;
    }

    /** Get the top element. */
    public int top() {
        return q1.peek();
    }

    /** Returns whether the stack is empty. */
    public boolean empty() {
        return q1.isEmpty() && q2.isEmpty();
    }
}

# Using 2 queue and swap q
# 58ms 71.91%
class MyStack {

    /** Initialize your data structure here. */
    private Queue<Integer> q1, q2;
    int top;

    public MyStack() {
        q1 = new LinkedList<Integer>();
        q2 = new LinkedList<Integer>();
    }

    /** Push element x onto stack. */
    public void push(int x) {
        q2.offer(x);
        top = x;
    }

    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        while(q2.size() > 1) {
            top = q2.poll();
            q1.offer(top);
        }
        int temp = q2.poll();
        swapQ();
        return temp;
    }
    private void swapQ() {
        Queue<Integer> temp = q1;
        q1 = q2;
        q2 = temp;
    }

    /** Get the top element. */
    public int top() {
        return top;
    }

    /** Returns whether the stack is empty. */
    public boolean empty() {
         return q1.isEmpty() && q2.isEmpty();
    }
}

# Stack usually implemented using list
# FYI only, not valid for this q
# 55ms 88.09%
class MyStack {

    LinkedList<Integer> mList;

    /** Initialize your data structure here. */
    public MyStack() {
        mList = new LinkedList<Integer>();
    }

    /** Push element x onto stack. */
    public void push(int x) {
        mList.add(x);
    }

    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        //Reverse List
        if ( mList == null ) return -1;
        else {
            int temp =(mList.getLast());
            mList.removeLast();
            return temp;
        }
    }

    /** Get the top element. */
    public int top() {
        return mList.isEmpty() ? -1 : mList.getLast();
    }

    /** Returns whether the stack is empty. */
    public boolean empty() {
        return mList.isEmpty();
    }
}
/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */
'''