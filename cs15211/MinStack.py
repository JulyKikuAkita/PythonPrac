__source__ = 'https://leetcode.com/problems/min-stack/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/min-stack.py
# Time:  O(n)
# Space: O(1)
# Stack
#
# Description: Leetcode # 155. Min Stack
#
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.
#
# Companies
# Google Uber Zenefits Amazon Snapchat Bloomberg
# Related Topics
# Stack Design
# Similar Questions
# Sliding Window Maximum
#
import unittest
class MinStack:
    def __init__(self):
        self.min = None
        self.stack = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        if not self.stack:
            self.stack.append(x)
            self.min = x
        else:
            if x < self.min:
                self.min = x

    # @return nothing
    def pop(self):
        x = self.stack.pop()
        if x < 0:
            self.min = self.min - x

    # @return an integer
    def top(self):
        x = self.stack[-1]
        #print self.min, x
        if x > 0 :  # very weired, why care x > 0?
            return x + self.min
        else:
            return self.min

    # @return an integer
    def getMin(self):
        return self.min

class MinStackOther:
    def __init__(self):
        self.stack = []
        self.minStack = []
        #self.minStack.append(0)

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if len(self.minStack) == 0 or self.minStack[-1] >= x:
            self.minStack.append(x)


    # @return nothing
    def pop(self):
        p = self.stack.pop()
        if p == self.minStack[-1]:
            self.minStack.pop()


    # @return an integer
    def top(self):
        return self.stack[-1]


    # @return an integer
    def getMin(self):
        return self.minStack[-1]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        stack = MinStack()
        stack.push(1)
        stack.push(15)
        stack.push(3)
        print [stack.top(), stack.getMin()]

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

Input:
["MinStack","push","push","push","getMin","pop","getMin"]
[[],[0],[1],[0],[],[],[]]
Output:
[null,null,null,null,0,null,1]
Expected:
[null,null,null,null,0,null,0]

# use only one stack:
# pop min twice
# 54ms 100%
class MinStack {
    private Stack<Integer> stack;
    private int min;

    /** initialize your data structure here. */
    public MinStack() {
        stack = new Stack<>();
        min = Integer.MAX_VALUE;
    }
    
    public void push(int x) {
        if (x <= min) {
            stack.push(min);
            min = x;
        }
        stack.push(x);
    }
    
    public void pop() {
        if (min == stack.pop()) {
            min = stack.pop();
        }
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return min;
    }
}

# 71ms 49.15%
class MinStack {
    Stack<Integer> dataStack;
    Stack<Integer> minStack;

    /** initialize your data structure here. */
    public MinStack() {
        dataStack = new Stack<>();
        minStack = new Stack<>();
    }

    public void push(int x) {
        dataStack.push(x);
        if (minStack.isEmpty() || minStack.peek() >= x) {
            minStack.push(x);
        }
    }

    public void pop() {
        if (minStack.peek().equals(dataStack.pop())) {
            minStack.pop();
        }
    }

    public int top() {
        return dataStack.peek();
    }

    public int getMin() {
        return minStack.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */

# 73ms 45.84%
class MinStack {
    Stack<Integer> stack;
    Stack<Integer> min;

    /** initialize your data structure here. */
    public MinStack() {
        this.stack = new Stack<Integer>();
        this.min = new Stack<Integer>();
    }

    public void push(int x) {
        this.stack.push(x);

        if (this.min.isEmpty() || this.min.peek() >= x) {
            this.min.push(x);
        }
    }

    public void pop() {
        int val = this.stack.pop();

        if (this.min.peek() == val) {
            this.min.pop();
        }
    }

    public int top() {
        return this.stack.peek();
    }

    public int getMin() {
        return this.min.peek();
    }
}

'''
