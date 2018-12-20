__source__ = 'https://leetcode.com/problems/sort-list/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/sort-list.py
# Time:  O(nlogn)
# Space: O(logn) for stack call
# Sort
#
# Description: Leetcode # 148. Sort List
#
# Sort a linked list in O(n log n) time using constant space complexity.
#
# Related Topics
# Linked List Sort
# Similar Questions
# Merge Two Sorted Lists Sort Colors Insertion Sort List
#
import unittest
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if head == None or head.next == None:
            return head

        fast,slow, prev = head , head, None
        while fast != None and fast.next != None:
            prev, slow, fast = slow, slow.next, fast.next.next
        prev.next = None

        sorted_l1 = self.sortList(slow)
        sorted_l2 = self.sortList(head)

        return self.mergeTwoLists(sorted_l1, sorted_l2)

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                cur.next = l1
                cur, l1 = l1, l1.next  # cannot decalre cur = cur.next, None obj exception
            else:
                cur.next = l2
                cur, l2 = l2, l2.next
        if l1 != None:
            cur.next = l1
        if l2 != None:
            cur.next = l2
        return dummy.next

# Definition for singly-linked list.
# http://www.cnblogs.com/zuoyuan/p/3699508.html
# http://jelices.blogspot.com/2014/06/leetcode-python-sort-list.html  this one implement using merge sort
class SolutionOther:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if head == None or head.next == None:
            return head
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        head1 = head
        head2 = slow.next
        slow.next = None

        head1 = self.sortList(head1)
        head2 = self.sortList(head2)
        head = self.merge(head1, head2)
        return head

    def merge(self, head1, head2):
        if head1 == None:
            return head2
        if head2 == None:
            return head1
        dummy = ListNode(0)
        p = dummy

        while head1 and head2:
            if head1.val < head2.val:
                p.next = head1
                head1 = head1.next
                p = p.next
            else:
                p.next = head2
                head2 = head2.next
                p = p.next

        if head1 == None:
            p.next = head2
        if head2 == None:
            p.next = head1

        return dummy.next

#List
c1 = ListNode(5)
c2 = ListNode(1)
c3 = ListNode(9)

a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)

c1.next = c2
c2.next = c3
c3.next = None

a1.next = a2
a2.next = a3
a3.next = a4

b1= ListNode(1)
#test

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        head = ListNode(3)
        head.next = ListNode(4)
        head.next.next = ListNode(1)
        head.next.next.next= ListNode(2)
        print Solution().sortList(head)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# 7ms 33.52%
class Solution {
    public ListNode sortList(ListNode head) {
        if (head == null) return head;
        if (head.next == null) return head;

        //p1 move 1 step every time, p2 move 2 step every time, pre record node before p1
        ListNode p1 = head;
        ListNode p2 = head;
        ListNode pre = head;

        while(p2 != null && p2.next != null) {
            pre = p1;
            p1 = p1.next;
            p2 = p2.next.next;
        }

        //change pre next to null, make two sub list(head to pre, p1 to p2)
        pre.next = null;
        ListNode h1 = sortList(head);
        ListNode h2 = sortList(p1);
        return merge(h1, h2);
    }

    public ListNode merge(ListNode h1, ListNode h2) {
        if (h1 == null) return h2;
        if (h2 == null) return h1;

        if (h1.val < h2.val) {
            h1.next = merge(h1.next, h2);
            return h1;
        }else {
            h2.next = merge(h1, h2.next);
            return h2;
        }
    }
}

# Different thinking, similar technique
# 5ms 69.10%
class Solution {
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) return head;

        int length = 1;
        ListNode cur = head;
        while(cur != null) {
            length++;
            cur = cur.next;
        }
        int mid = length/2;
        cur = head;
        while(mid > 1) {
            cur = cur.next;
            mid--;
        }
        ListNode newHead = cur.next;
        cur.next = null;
        ListNode h1 = sortList(head);
        ListNode h2 = sortList(newHead);
        return merge(h1, h2);
    }

    public ListNode merge(ListNode h1, ListNode h2) {
        if (h1 == null) return h2;
        if (h2 == null) return h1;
        ListNode head;
        if (h1.val < h2.val) {
            head = h1;
            head.next = merge(h1.next, h2);
        }else {
            head = h2;
            head.next = merge(h1, h2.next); //order should not mater with head pointer, but get stack overflow somehow
        }
        return head;
    }
}

# 4ms 94.54%
class Solution {
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode slow = head;
        ListNode fast = head;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode secondHalf = slow.next;
        slow.next = null;
        ListNode firstHalf = sortList(head);
        secondHalf = sortList(secondHalf);
        return merge(firstHalf, secondHalf);
    }

    private ListNode merge(ListNode first, ListNode second) {
        ListNode result = new ListNode(0);
        ListNode prev = result;
        while (first != null && second != null) {
            if (first.val < second.val) {
                prev.next = first;
                prev = prev.next;
                first = first.next;
            } else {
                prev.next = second;
                prev = prev.next;
                second = second.next;
            }
        }
        while (first != null) {
            prev.next = first;
            prev = prev.next;
            first = first.next;
        }
        while (second != null) {
            prev.next = second;
            prev = prev.next;
            second = second.next;
        }
        return result.next;
    }
}

'''
