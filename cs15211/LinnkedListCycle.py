__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/linked-list-cycle.py
# Time:  O(n)
# Space: O(1)
# Two Pointer
#
# Given a linked list, determine if it has a cycle in it.
#
# Follow up:
# Can you solve it without using extra space?
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
        return False

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = head.next
    print Solution().hasCycle(head)

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        fast = head
        slow = head

        while (fast != None and fast.next != None and fast.next.next != None):
            fast = (fast.next).next
            slow = slow.next
            if fast == slow:
                return True
        return False


# test
c1 = ListNode(1)
c2 = ListNode(2)
c3 = ListNode(3)

a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)

c1.next = c2
c2.next = c3
c3.next = c2

a1.next = a2
a2.next = a3
a3.next = a4

b1= ListNode(1)


## tc
t1 = Solution()
print t1.hasCycle(c1)
print t1.hasCycle(a1)
print t1.hasCycle(b1)
print t1.hasCycle(None)