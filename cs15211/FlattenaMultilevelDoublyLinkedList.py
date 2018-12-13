__source__ = 'https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 430. Flatten a Multilevel Doubly Linked List
#
# You are given a doubly linked list which in addition to the next and previous pointers,
# it could have a child pointer, which may or may not point to a separate doubly linked list.
# These child lists may have one or more children of their own, and so on,
# to produce a multilevel data structure, as shown in the example below.
#
# Flatten the list so that all the nodes appear in a single-level, doubly linked list.
# You are given the head of the first level of the list.
#
# Example:
#
# Input:
#  1---2---3---4---5---6--NULL
#          |
#          7---8---9---10--NULL
#              |
#              11--12--NULL
#
# Output:
# 1-2-3-7-8-11-12-9-10-4-5-6-NULL
#
import unittest

# DFS
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

# 856ms 95.29%
class Solution(object):
    def flatten(self, head):
        newhead, tail = self.flattenrec(head)
        return newhead

    def flattenrec(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        finalhead = head
        tail = head

        while head != None:
            if (head.child != None):
                newhead, tail = self.flattenrec(head.child)
                if (head.next != None):
                    head.next.prev = tail
                    tail.next = head.next
                head.next = head.child
                head.child = None
                newhead.prev = head
                head = tail
            else:
                head = head.next
                if (tail.next != None):
                    tail = tail.next
        return finalhead, tail

# 1272ms 14.61%
class Solution2(object):
    def flatten(self, head):
        curr=head
        stack=[]
        while(curr):
            if curr.child:
                if curr.next:
                    stack.append(curr.next)
                curr.next,curr.child.prev,curr.child=curr.child,curr,None
            if curr.next is None and len(stack)!=0:
                temp=stack.pop()
                curr.next=temp
                temp.prev=curr
            curr=curr.next
        return head

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

/*
// Definition for a Node.
class Node {
    public int val;
    public Node prev;
    public Node next;
    public Node child;

    public Node() {}

    public Node(int _val,Node _prev,Node _next,Node _child) {
        val = _val;
        prev = _prev;
        next = _next;
        child = _child;
    }
};
*/

# DFS
# 1ms 100%
class Solution {
    public Node flatten(Node head) {
        if (head == null) return null;

        Stack<Node> stack = new Stack<>();
        Node cur = head;

        while (cur != null) {
            if (cur.child != null) {

                if (cur.next != null) { //avoid saving null into stack
                    stack.push(cur.next); //save cur.next into stack
                }

                cur.next = cur.child; // connect cur and cur.child
                cur.next.prev = cur; // connect cur and cur.child
                cur.child = null;
            }
            else if (cur.next == null && !stack.isEmpty()) {
                // if cur reaches to the end while stack still having some nodes, connecting back to upper level
                cur.next = stack.pop();
                cur.next.prev = cur;
            }

            cur = cur.next;
        }

        return head;
    }
}
'''