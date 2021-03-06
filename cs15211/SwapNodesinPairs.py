__source__ = 'https://leetcode.com/problems/swap-nodes-in-pairs/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/swap-nodes-in-pairs.py
# Time:  O(n)
# Space: O(1)
# LinkedList
#
# Description: Leetcode #  24. Swap Nodes in Pairs
#
# Given a linked list, swap every two adjacent nodes and return its head.
#
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
# Your algorithm should use only constant space.
# You may not modify the values in the list, only nodes itself can be changed.
#
# Companies
# Microsoft Bloomberg Uber
# Related Topics
# Linked List
# Similar Questions
# Reverse Nodes in k-Group
import unittest
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current.next and current.next.next:
            next_one, next_two, next_three = current.next, current.next.next, current.next.next.next
            current.next = next_two
            next_two.next = next_one
            next_one.next = next_three
            current = next_one
        return dummy.next


    def swapPairsif(self, head):

        dummy = ListNode(0)
        dummy.next = head
        cur = dummy

        while cur.next and cur.next.next:
            tmp = cur.next.next
            (cur.next).next = cur
            cur.next.next = tmp.next
            tmp.next = cur.next
            cur.next = tmp
            cur = cur.next.next
        return dummy.next

class SolutionOther:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head == None or head.next == None:
            return head
        newHead = head.next

        current = head
        previous = None

        while current != None and current.next != None:
            if previous != None:
                previous.next = current.next
            previous = current

            temp = current.next.next
            current.next.next = current
            current.next = temp

            current = current.next
        return newHead

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        #test
        c1 = ListNode(1)
        c2 = ListNode(2)
        c3 = ListNode(3)
        #c4 = ListNode(4)
        c1.next = c2
        c2.next = c3
        #c3.next = c4

        head = ListNode(1)
        head.next, head.next.next, head.next.next.next = ListNode(2), ListNode(3), ListNode(4)
        print Solution().swapPairs(head)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
# BFS
# 2ms 99.98%
class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode fakeHead = new ListNode(0);
        fakeHead.next = head;
        ListNode cur = fakeHead;
        while (cur.next != null && cur.next.next != null) {
            ListNode next1 = cur.next;
            ListNode next2 = cur.next.next;
            ListNode next3 = next2.next;
            next2.next = cur.next;
            next1.next = next3;
            cur.next = next2;
            cur = next1;
        }
        return fakeHead.next;
    }
}


# DFS
# 2ms 99.98%
class Solution {
    public ListNode swapPairs(ListNode head) {
        if ((head == null)||(head.next == null))
            return head;
        ListNode n = head.next;
        head.next = swapPairs(head.next.next);
        n.next = head;
        return n;
    }
}
'''
