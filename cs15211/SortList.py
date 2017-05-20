__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/sort-list.py
# Time:  O(nlogn)
# Space: O(logn) for stack call
# Sort
#
# Sort a linked list in O(n log n) time using constant space complexity.
#

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

if __name__ == "__main__":
    head = ListNode(3)
    head.next = ListNode(4)
    head.next.next = ListNode(1)
    head.next.next.next= ListNode(2)
    print Solution().sortList(head)


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

#test = SolutionOther()
#nh = test.sortList(c1)
#
#while nh:
#    print nh.val
#    nh = nh.next

#java
js = '''
public class Solution {
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