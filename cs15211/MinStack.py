__source__ = 'https://leetcode.com/problems/min-stack/#/solutions'
# https://github.com/kamyu104/LeetCode/blob/master/Python/min-stack.py
# Time:  O(n)
# Space: O(1)
# Stack
#
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
#
# Topics:
# Stack Design
# You might like:
# (H) Sliding Window Maximum
# Company:
# Google Uber Zenefits Amazon Snapchat Bloomberg
#

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

if __name__ == "__main__":
    stack = MinStack()
    stack.push(1)
    stack.push(15)
    stack.push(3)
    print [stack.top(), stack.getMin()]

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

#Java
java = '''
//use only one stack:
//pop min twice
public class MinStack {
    int min;
    Stack<Integer> s;

    /** initialize your data structure here. */
    public MinStack() {
        s = new Stack();
        min = Integer.MAX_VALUE;
    }

    public void push(int x) {
        if ( x <= min) {
            s.push(min);
            min = x;
        }
        s.push(x);
    }

    public void pop() {
        if (s.pop() == min) {
            min = s.pop();
        }
    }

    public int top() {
        return s.peek();
    }

    public int getMin() {
        return min;
    }
}


public class MinStack {
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
'''