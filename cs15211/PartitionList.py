__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/partition-list.py
# Time:  O(n)
# Space: O(1)
# Two Pointers
#
# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the two partitions.
#
# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.
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
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        dummySmaller, dummyGreater = ListNode(-1), ListNode(-1)
        smaller, greater = dummySmaller, dummyGreater

        while head:
            if head.val < x:
                smaller.next = head
                smaller = smaller.next
            else:
                greater.next = head
                greater = greater.next
            head = head.next

        smaller.next = dummyGreater.next
        greater.next = None
        return dummySmaller.next



if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(2)
    print Solution().partition(head, 3)

class SolutionOther:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        if head is None:
            return head
        s_head, l_head = ListNode(0), ListNode(0)
        s_tail, l_tail = s_head, l_head
        while head is not None:
            if head.val < x:
                s_tail.next = head
                s_tail = s_tail.next
            else:
                l_tail.next = head
                l_tail = l_tail.next

            head = head.next

        l_tail.next = None
        s_tail.next = l_head.next

        return s_head.next

#test
#1->4->3->2->5->2  ans is 1->2->2->4->3->5
h1 = ListNode(1); n1 = ListNode(4) ; n2 = ListNode(3); n3 = ListNode(2) ; n4 = ListNode(5); n5 = ListNode(2)
h1.next = n1 ; n1.next = n2; n2.next =n3 ; n3.next = n4; n4.next =n5
test = SolutionOther()
result = test.partition(h1 ,3)
while result:
    print result.val
    result = result.next
