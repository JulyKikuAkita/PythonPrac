__source__ = 'https://leetcode.com/problems/implement-queue-using-stacks/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/implement-queue-using-stacks.py
# Time:  O(1), amortized
# Space: O(n)
#
# Description: Leetcode # 232. Implement Queue using Stacks
#
# Implement the following operations of a queue using stacks.
#
# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.
#
# Notes:
# You must use only standard operations of a stack
# -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, stack may not be supported natively.
# You may simulate a stack by using a list or deque (double-ended queue),
# as long as you use only standard operations of a stack.
# You may assume that all operations are valid
# (for example, no pop or peek operations will be called on an empty queue).
#
# Companies
# Microsoft Bloomberg
# Related Topics
# Stack Design
# Similar Questions
# Implement Stack using Queues
#
import unittest
class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.A, self.B = [], []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.A.append(x)

    # @return nothing
    def pop(self):
        self.peek()
        self.B.pop()

    # @return an integer
    def peek(self):
        if not self.B:
            while self.A:
                self.B.append(self.A.pop())
        return self.B[-1]

    # @return an boolean
    def empty(self):
        return not self.A and not self.B

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
Thought: https://leetcode.com/articles/implement-queue-using-stacks/

#56.32% 98ms
public class MyQueue {
    Stack<Integer> input;
    Stack<Integer> output;
    /** Initialize your data structure here. */
    public MyQueue() {
        input = new Stack();
        output = new Stack();
    }

    /** Push element x to the back of queue. */
    public void push(int x) {
        input.push(x);
    }

    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        peek();
        return output.pop();
    }

    /** Get the front element. */
    public int peek() {
        if (output.empty()) {
            while(!input.empty()){
                output.push(input.pop());
            }
        }
        return output.peek();
    }

    /** Returns whether the queue is empty. */
    public boolean empty() {
        return input.empty() && output.empty();
    }
}

#86.63% 90ms
public class MyQueue {
    Stack<Integer> orig;
    Stack<Integer> bucket;

    /** Initialize your data structure here. */
    public MyQueue() {
        orig=new Stack();
    }

    /** Push element x to the back of queue. */
    public void push(int x) {
        if(orig.empty()){
            orig.push(x);
        }
        else{
            bucket=new Stack();
            while(!orig.empty()){
                bucket.push(orig.pop());
            }
            orig.push(x);
            while(!bucket.empty()){
                orig.push(bucket.pop());
            }
        }
    }

    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        return (int)orig.pop();
    }

    /** Get the front element. */
    public int peek() {
        return orig.peek();
    }

    /** Returns whether the queue is empty. */
    public boolean empty() {
        return orig.empty();
    }
}
/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
'''