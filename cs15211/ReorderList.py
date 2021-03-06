__source__ = 'https://leetcode.com/problems/reorder-list/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/reorder-list.py
# Time:  O(n)
# Space: O(1)
# reorder list
#
# Description: Leetcode # 143. Reorder List
#
# Given a singly linked list L: L0->L1->...->Ln-1->Ln,
# reorder it to: L0->Ln->L1->Ln-1->L2->Ln-2->...
#
# You must do this in-place without altering the nodes' values.
#
# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.
#
# Related Topics
# Linked List
#
import unittest
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head == None or head.next == None:
            return head
        fast, slow, prev = head, head, None
        dummyNode = ListNode(0)

        while fast and fast.next :
            fast, slow, prev = fast.next.next, slow.next, slow

        cur = slow
        prev.next = None
        prev = None
        #reverse lastpart
        while cur :
            cur.next, prev, cur = prev, cur, cur.next

        #combine first and last lists
        l1 = head
        l2 = prev
        cur = dummyNode
        while l1 and l2:
            cur.next, cur, l1 = l1, l1, l1.next
            cur.next, cur, l2 = l2, l2, l2.next
        return dummyNode.next

# http://www.cnblogs.com/zuoyuan/p/3700846.html
class SolutionOther:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head == None or head.next == None or head.next.next == None:
            return head

        # break linked list into two equal length
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head1 = head
        head2 = slow.next
        slow.next = None

        #reverse linked list head2
        dummy = ListNode(0)
        dummy.next = head2
        p = head2.next
        head2.next = None
        while p:
            tmp = p
            p = p.next
            tmp.next = dummy.next
            dummy.next = tmp
        head2 = dummy.next

        # merge two linked list head1 and head2
        p1 = head1
        p2 = head2
        while p2:
            tmp1 = p1.next
            tmp2 = p2.next
            p1.next = p2
            p2.next = tmp1
            p1 = tmp1
            p2 = tmp2

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        #head.next.next.next.next = ListNode(5)
        print Solution().reorderList(head)

        #test
        c1 = ListNode(1) ; c2 = ListNode(2) ; c3 = ListNode(3) ; c4 = ListNode(4) ; c5 = ListNode(5); c6 = ListNode(6);c7 = ListNode(7); c8 = ListNode(8)
        c1.next = c2 ; c2.next = c3 ; c3.next = c4; c4.next = c5; c5.next = c6 ; c6.next = c7 ; c7.next = c8
        test = SolutionOther()


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

This question is a combination of Reverse a linked list I & II. 
It should be pretty straight forward to do it in 3 steps :)

# 2ms 99.28%
class Solution {
    public void reorderList(ListNode head) {
        if (head == null || head.next == null) {
            return;
        }
        ListNode fast = head;
        ListNode slow = head;
        while (fast.next != null && fast.next.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }
        ListNode firstHead = head;
        ListNode secondHead = slow.next;
        slow.next = null;
        secondHead = reverse(secondHead);
        ListNode fakeHead = new ListNode(0);
        ListNode cur = fakeHead;
        while (firstHead != null) {
            ListNode firstNext = firstHead.next;
            ListNode secondNext = secondHead == null ? null : secondHead.next;
            cur.next = firstHead;
            cur.next.next = secondHead;
            cur = cur.next.next;
            firstHead = firstNext;
            secondHead = secondNext;
        }
    }

    private ListNode reverse(ListNode head) {
        ListNode prev = null;
        while (head != null) {
            ListNode next = head.next;
            head.next = prev;
            prev = head;
            head = next;
        }
        return prev;
    }
}

# 2ms 99.28%
class Solution {
    public void reorderList(ListNode head) {
        if(head==null||head.next==null) return;

        //Find the middle of the list
        ListNode fast = head, slow = head;
        while( fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        //Reverse the half after middle  1->2->3->4->5->6 to 1->2->3->6->5->4
        ListNode preMid = slow;
        ListNode mid = slow.next;
        while(mid.next != null) {
            ListNode cur = mid.next;
            mid.next = cur.next;
            cur.next = preMid.next;
            preMid.next = cur;
        }

        //Start reorder one by one  1->2->3->6->5->4 to 1->6->2->5->3->4
        slow = head;
        fast = preMid.next;
        while(slow != preMid) {
            preMid.next = fast.next;
            fast.next = slow.next;
            slow.next = fast;
            slow = fast.next;
            fast = preMid.next;
        }
    }
}
'''
