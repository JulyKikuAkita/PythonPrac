__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/linked-list-cycle-ii.py
# Time:  O(n)
# Space: O(1)
# Two Pointer
#
# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
#
# Follow up:
# Can you solve it without using extra space?
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        if self:
            return "{}".format(self.val)
        else:
            return None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                fast = head
                while fast is not slow:
                    fast = fast.next
                    slow = slow.next
                return fast


class SolutionOther:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        h1, h2 = head, head
        while h1 and h2:
            if ((not h1.next) or (not h2.next) or (not h2.next.next)):
                return None
            h1 = h1.next
            h2 = h2.next.next

            if (h1 == h2 and h1 ):
                break

        if (not h1 or not h2):
            return None
        h2 = head

        while h1 != h2:
            h1 = h1.next
            h2 = h2.next

        return h1

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = head.next
    print Solution().detectCycle(head)
