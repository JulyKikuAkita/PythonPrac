__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/reverse-linked-list-ii.py
# Time:  O(n)
# Space: O(1)
# LinkedList
#
# Reverse a linked list from position m to n. Do it in-place and in one-pass.
#
# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,
#
# return 1->4->3->2->5->NULL.
#
# Note:
# Given m, n satisfy the following condition:
# 1 <= m <= n <= length of list.
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self == None:
            return "Nil"
        else:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode

    #dont' think it is good code sue to unreadibility
    def reverseBetween(self, head, m, n):
        diff, dummy, cur = n-m-1, ListNode(-1), head
        dummy.next = head
        while cur and m > 1:
            current, last_unswapped, m = cur.next, cur, m-1

        prev, first_swapped = last_unswapped, cur.next
        while cur and diff > 0:
            cur.next, prev, cur, diff = prev, cur, cur.next, diff - 1

        last_unswapped.next, first_swapped.next = prev, cur
        return dummy.next


    # this one from java code is eaiser to understand
    def reverseBetweenif(self, head, m, n):
        if head == None or head.next == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        diff = n - m

        while m > 1:
            cur = cur.next
            m -= 1

        prev, cur = cur, cur.next
        #insert the node after cur to the position after prev
        # dummy -> prev -> m....cur->tmp->n.....
        while cur.next and diff > 0:
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = prev.next
            prev.next = tmp
            diff -= 1

        return dummy.next

class Solution3(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n :
            return head
        dummy = ListNode(0)
        dummy.next = head
        fir = dummy
        rev_tail = dummy

        for i in xrange(m-1):
            fir= fir.next
            rev_tail = rev_tail.next
        rev_head = fir.next
        for i in xrange( n - m + 1):
            rev_tail = rev_tail.next
        sec = rev_tail.next

        fir.next = None
        rev_tail.next = None

        fir.next = self.reverse(rev_head)
        rev_head.next = sec
        return dummy.next

    def reverse(self, head):
        if not head:
            return
        if head.next == None:
            return head
        node = head.next
        head.next = None
        newroot = self.reverse(node)
        node.next = head
        return newroot


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print Solution().reverseBetweenif(head, 2, 4)

    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(3)
    #head1.next.next.next = ListNode(4)
    #head1.next.next.next.next = ListNode(5)
    print Solution().reverseBetweenif(head1, 1, 2)


class SolutionOther:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    # @ 1 <= m <= n <= length of list
    def reverseBetween(self, head, m, n):
        prem, pre, next, nowm = None, None, None,None
        now = head
        index = 1

        while now :
            next = now.next
            if index >= m and index <= n:
                now.next = pre
            if index == m:
                prem, nowm = pre, now
            if index == n:
                nowm.next = next
                if not prem :
                    head = now
                else:
                    prem.next = now

            pre, now = now, next
            index += 1

        return head


#java
js = '''
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        ListNode fakeHead = new ListNode(0);
        fakeHead.next = head;
        ListNode firstTail = fakeHead;
        ListNode reverseTail = fakeHead;
        for (int i = 0; i < m - 1; i++) {
            firstTail = firstTail.next;
            reverseTail = reverseTail.next;
        }
        ListNode reverseHead = firstTail.next;
        for (int i = 0; i < n - m + 1; i++) {
            reverseTail = reverseTail.next;
        }
        ListNode secondHead = reverseTail.next;
        firstTail.next = null;
        reverseTail.next = null;
        reverse(reverseHead);
        firstTail.next = reverseTail;
        reverseHead.next = secondHead;
        return fakeHead.next;
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
'''