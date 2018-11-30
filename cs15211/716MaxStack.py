__source__ = 'https://leetcode.com/problems/max-stack/description/'
# Time:  O(n)
# Space: O(n)

# Design a max stack that supports push, pop, top, peekMax and popMax.
#
# push(x) -- Push element x onto stack.
# pop() -- Remove the element on top of the stack and return it.
# top() -- Get the element on the top.
# peekMax() -- Retrieve the maximum element in the stack.
# popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements,
# only remove the top-most one.
# Example 1:
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
# Note:
# -1e7 <= x <= 1e7
# Number of operations won't exceed 10000.
# The last four operations won't be called when stack is empty.
import unittest


class FooTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setupDown(self):
        pass

    def tearDown(self):
        pass

    def test_foo(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    # run all tests
    unittest.main()

    # run one test
    #unittest.main(defaultTest='FooTest.test_foo', warnings='ignore')

Java = '''
# https://leetcode.com/problems/max-stack/solution/
1.

2. Approach #2: Double Linked List + TreeMap [Accepted]
Time Complexity: O(logN) for all operations except peek which is O(1), where NN is the number of operations performed.
Most operations involving TreeMap are O(logN).

Space Complexity: O(N), the size of the data structures used.
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