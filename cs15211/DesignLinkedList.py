__source__ = 'https://leetcode.com/problems/design-linked-list/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 707. Design Linked List
#
# Design your implementation of the linked list.
# You can choose to use the singly linked list or the doubly linked list.
# A node in a singly linked list should have two attributes: val and next.
# val is the value of the current node, and next is a pointer/reference to the next node.
# If you want to use the doubly linked list,
# you will need one more attribute prev to indicate the previous node in the linked list.
# Assume all nodes in the linked list are 0-indexed.
#
# Implement these functions in your linked list class:
#
# get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
# addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion,
# the new node will be the first node of the linked list.
# addAtTail(val) : Append a node of value val to the last element of the linked list.
# addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list.
# If index equals to the length of linked list, the node will be appended to the end of linked list.
# If index is greater than the length, the node will not be inserted.
# deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.
# Example:
#
# MyLinkedList linkedList = new MyLinkedList();
# linkedList.addAtHead(1);
# linkedList.addAtTail(3);
# linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
# linkedList.get(1);            // returns 2
# linkedList.deleteAtIndex(1);  // now the linked list is 1->3
# linkedList.get(1);            // returns 3
# Note:
#
# All values will be in the range of [1, 1000].
# The number of operations will be in the range of [1, 1000].
# Please do not use the built-in LinkedList library.
#
import unittest

#212ms 66.67%
class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1

        if self.head is None:
            return -1

        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        node = Node(val)
        node.next = self.head
        self.head = node

        self.size += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        curr = self.head
        if curr is None:
            self.head = Node(val)
        else:
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(val)

        self.size += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
        else:
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            node = Node(val)
            node.next = curr.next
            curr.next = node

            self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index < 0 or index >= self.size:
            return

        curr = self.head
        if index == 0:
            self.head = curr.next
        else:
            for i in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next

        self.size -= 1

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:

# 63ms 99.92%
class MyLinkedList {

    private class ListNode {
        int val;
        ListNode next;
        public ListNode(int val) {
            this.val = val;
            next = null;
        }
    }

    private int size;
    private ListNode head;
    private ListNode tail;

    /** Initialize your data structure here. */
    public MyLinkedList() {
        size = 0;
        head = new ListNode(0);
        tail = new ListNode(0);
        head.next = tail;
        tail.next = head;
    }

    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    public int get(int index) {
        ListNode node = getNode(index);
        if (node == null) return -1;
        else return node.val;
    }

    private ListNode getNode(int index) {
        if (index < 0 || index >= size) return null;
        ListNode cur = head.next;
        for (int i = 0; i < index; i++) {
            cur = cur.next;
        }
        return cur;
    }

    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    public void addAtHead(int val) {
        ListNode t = new ListNode(val);
        t.next = head.next;
        head.next = t;
        if (size == 0) tail.next = t;
        size++;
    }

    /** Append a node of value val to the last element of the linked list. */
    public void addAtTail(int val) {
        ListNode t = new ListNode(val);
        t.next = tail;
        tail.next.next = t;
        tail.next = t;
        size++;
    }

    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    public void addAtIndex(int index, int val) {
        if (index < 0 || index > size) return;
        else if (index == size) addAtTail(val);
        else if (index == 0) addAtHead(val);
        else {
            ListNode prev = getNode(index - 1);
            ListNode t = new ListNode(val);
            t.next = prev.next;
            prev.next = t;
            size++;
        }
    }

    /** Delete the index-th node in the linked list, if the index is valid. */
    public void deleteAtIndex(int index) {
        if (index < 0 || index >= size) return;
        if (index == 0) head.next = head.next.next;
        else {
            ListNode prev = getNode(index - 1);
            prev.next = prev.next.next;
            if (index == size - 1) tail.next = prev;
        }
        size--;
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */

'''