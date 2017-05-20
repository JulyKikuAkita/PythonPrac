__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/rotate-list.py
# Time:  O(n)
# Space: O(1)
# LinkedList
#
# Given a list, rotate the list to the right by k places, where k is non-negative.
#
# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

#create a loop and find break point by calculating k and list length
class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head is None :
            return head
        cur, len = head, 1
        # while cur: len = list length + 1 ;
        # whle cur.next: list = list length
        while cur.next:
            cur = cur.next
            len += 1

        #crete loop: point lastnode.next to head
        cur.next = head
        shift = len - len % k - 1

        cur = head
        while shift > 0:
            cur = cur.next
            shift -= 1

        newhead = cur.next
        cur.next = None
        return newhead


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print Solution().rotateRight(head, 2)


class Solution2(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k == 0:
            return head
        #step 1
        fast = head
        cnt = self.getCnt(head)
        k = k % cnt
        for i in xrange(k):
            fast = fast.next
        #step 2
        if fast == head:
            return head

        slow = head
        while fast.next:
            fast = fast.next
            slow = slow.next

        #step 3
        fast.next = head
        newHead = slow.next
        slow.next = None

        return newHead
    def getCnt(self, head):
        cnt = 0
        while head:
            head = head.next
            cnt += 1
        return cnt
#test

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2; l2.next = l3 ; l3.next = l4 ; l4.next = l5 ; l5.next = None

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
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || k <= 0) {
            return head;
        }
        int length = getLength(head);
        ListNode firstHead = head;
        ListNode firstTail = head;
        for (int i = 0; i < length - k % length - 1; i++) {
            firstTail = firstTail.next;
        }
        ListNode secondHead = firstTail.next;
        firstTail.next = null;
        reverse(firstHead);
        ListNode secondTail = reverse(secondHead);
        firstHead.next = secondTail;
        return reverse(firstTail);
    }

    private int getLength(ListNode head) {
        int count = 0;
        while (head != null) {
            count++;
            head = head.next;
        }
        return count;
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