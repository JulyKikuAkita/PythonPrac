__source__ = 'https://leetcode.com/problems/max-stack/'
# Time:  O(N)
# Space: O(1)
#
# Description: Leetcode # 716. Max Stack
#
# Design a max stack that supports push, pop, top, peekMax and popMax.
#
#     push(x) -- Push element x onto stack.
#     pop() -- Remove the element on top of the stack and return it.
#     top() -- Get the element on the top.
#     peekMax() -- Retrieve the maximum element in the stack.
#     popMax() -- Retrieve the maximum element in the stack, and remove it.
# If you find more than one maximum elements, only remove the top-most one.
#
# Example 1:
#
# MaxStack stack = new MaxStack();
# stack.push(5);
# stack.push(1);
# stack.push(5);
# stack.top(); -> 5
# stack.popMax(); -> 5
# stack.top(); -> 1
# stack.peekMax(); -> 5
# stack.pop(); -> 1
# stack.top(); -> 5
#
# Note:
#     -1e7 <= x <= 1e7
#     Number of operations won't exceed 10000.
#     The last four operations won't be called when stack is empty.
#
import unittest
# 220ms 17.20%
class MaxStack(list):
    def push(self, x):
        m = max(x, self[-1][1] if self else None)
        self.append((x, m))

    def pop(self):
        return list.pop(self)[0]

    def top(self):
        return self[-1][0]

    def peekMax(self):
        return self[-1][1]

    def popMax(self):
        m = self[-1][1]
        b = []
        while self[-1][0] != m:
            b.append(self.pop())

        self.pop()
        map(self.push, reversed(b))
        return m

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/max-stack/solution/
#
Approach #1: Two Stacks [Accepted]
Complexity Analysis
Time Complexity: O(N) for the popMax operation, and O(1) for the other operations, 
where N is the number of operations performed.
Space Complexity: O(N), the maximum size of the stack.

# 141ms 13.84%
class MaxStack {
    Stack<Integer> stack;
    Stack<Integer> maxStack;

    /** initialize your data structure here. */
    public MaxStack() {
        stack = new Stack();
        maxStack = new Stack();
    }
    
    public void push(int x) {
        int max = maxStack.isEmpty() ? x : maxStack.peek();
        maxStack.push(max > x ? max : x);
        stack.push(x);
    }
    
    public int pop() {
        maxStack.pop();
        return stack.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int peekMax() {
        return maxStack.peek();
    }
    
    public int popMax() {
        int max = peekMax();
        Stack<Integer> buffer = new Stack();
        while (top() != max) buffer.push(pop());
        pop();
        while (!buffer.isEmpty()) push(buffer.pop());
        return max;
    }
}

/**
 * Your MaxStack object will be instantiated and called as such:
 * MaxStack obj = new MaxStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.peekMax();
 * int param_5 = obj.popMax();
 */


Approach #2: Double Linked List + TreeMap [Accepted]
Complexity Analysis
Time Complexity: O(logN) for all operations except peek which is O(1), 
where N is the number of operations performed. 
Most operations involving TreeMap are O(logN).
Space Complexity: O(N), the size of the data structures used.

# 85ms 91.18%
class MaxStack {
    TreeMap<Integer, List<Node>> map;
    DoubleLinkedList dll;

    public MaxStack() {
        map = new TreeMap();
        dll = new DoubleLinkedList();
    }

    public void push(int x) {
        Node node = dll.add(x);
        if(!map.containsKey(x))
            map.put(x, new ArrayList<Node>());
        map.get(x).add(node);
    }

    public int pop() {
        int val = dll.pop();
        List<Node> L = map.get(val);
        L.remove(L.size() - 1);
        if (L.isEmpty()) map.remove(val);
        return val;
    }

    public int top() {
        return dll.peek();
    }

    public int peekMax() {
        return map.lastKey();
    }

    public int popMax() {
        int max = peekMax();
        List<Node> L = map.get(max);
        Node node = L.remove(L.size() - 1);
        dll.unlink(node);
        if (L.isEmpty()) map.remove(max);
        return max;
    }
}

class DoubleLinkedList {
    Node head, tail;

    public DoubleLinkedList() {
        head = new Node(0);
        tail = new Node(0);
        head.next = tail;
        tail.prev = head;
    }

    public Node add(int val) {
        Node x = new Node(val);
        x.next = tail;
        x.prev = tail.prev;
        tail.prev = tail.prev.next = x;
        return x;
    }

    public int pop() {
        return unlink(tail.prev).val;
    }

    public int peek() {
        return tail.prev.val;
    }

    public Node unlink(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
        return node;
    }
}

class Node {
    int val;
    Node prev, next;
    public Node(int v) {val = v;}
}

# Double linked list with max
# 73ms 99.79%
class MaxStack {
    
    class ListNode{
        int val;
        int max;
        ListNode next;
        ListNode prev;
        public ListNode(int val, int max){
            this.val = val;
            this.max = max;
        }
    }
    
    ListNode head;
    ListNode tail;

    /** initialize your data structure here. */
    public MaxStack() {
        head = new ListNode(Integer.MIN_VALUE, Integer.MIN_VALUE);
        tail = new ListNode(Integer.MAX_VALUE, Integer.MAX_VALUE);
        
        head.next = tail;
        tail.prev = head;
    }
    
    public void push(int x) {
        ListNode node = new ListNode(x, Math.max(x, tail.prev.max));
        node.next = tail;
        node.prev = tail.prev;
        
        tail.prev = node;
        node.prev.next = node;
        
    }
    
    public int pop() {
        ListNode node = tail.prev;
        
        node.prev.next = node.next;
        node.next.prev = node.prev;
        node.next = null;
        node.prev = null;
        
        return node.val;
    }
    
    public int top() {
        return tail.prev.val;
    }
    
    public int peekMax() {
        return tail.prev.max;
    }
    
    public int popMax() {
        int max = peekMax();
        ListNode curr = tail.prev;
        
        while(curr.val != max){
            curr = curr.prev;
        }
        
        ListNode update = curr.next;
        
        curr.prev.next = curr.next;
        curr.next.prev = curr.prev;
        curr.next = null;
        curr.prev = null;
        
        while(update != tail){
            update.max = Math.max(update.val, update.prev.max);
            update = update.next;
        }
        
        return max;
    }
}
'''
