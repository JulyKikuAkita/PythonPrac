__source__ = 'https://leetcode.com/problems/remove-nth-node-from-end-of-list/'
# https://github.com/kamyu104/LeetCode#linked-list
# Time:  O(n)
# Space: O(1)
# Two Pointer
#
# Description: Leetcode # 19. Remove Nth Node From End of List
#
# Given a linked list, remove the nth node from the end of list and return its head.
#
# For example,
#
#    Given linked list: 1->2->3->4->5, and n = 2.
#
#    After removing the second node from the end, the linked list becomes 1->2->3->5.
#
# Note:
# Given n will always be valid.
# Try to do this in one pass.
#
# Related Topics
# Linked List Two Pointers
import unittest
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self is None:
            return "Nil"
        else:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        fast, slow = dummy, dummy # if == head, fails when n = 1

        for i in range(n):
            fast = fast.next

        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next  # if slow = fast, fails when n =1
        return dummy.next

class SolutionOther:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        tempH = ListNode(0)
        tempH.next = head

        count,tmpN = 0, head
        #exception if n > total number of node
        if n <= 0:
            return head

        while count < n:
            tmpN = tmpN.next
            count += 1

        markN = tempH
        while tmpN:
            tmpN, markN = tmpN.next, markN.next
        markN.next = markN.next.next

        return tempH.next

#test
test = SolutionOther()
n1, n2, n3 = ListNode(0), ListNode(1),ListNode(2)
n1.next = n2
n2.next = n3

ans = test.removeNthFromEnd(n1,3)
while ans:
    print ans.val
    ans = ans.next

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        print Solution().removeNthFromEnd(head, 2)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/remove-nth-node-from-end-of-list/solution/

# Two pass: get to know linked node length at first loop
# 9ms 47.49%
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        int length = 0;
        while(head != null){
            length++;
            head = head.next;
        }
        length = length - n;
        head = dummy;
        while(length > 0){
            head = head.next;
            length--;
        }
        head.next = head.next.next;
        return dummy.next;
    }
}

# One pass, slow and fast separate by n
# 9ms 47.49%
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode fakeHead = new ListNode(0);
        fakeHead.next = head;
        ListNode slow = fakeHead;
        ListNode fast = fakeHead;

        for (int i = 0; i < n ; i++){
            fast = fast.next;
        }

        while( fast.next != null) {
            slow = slow.next;
            fast = fast.next;
        }
        slow.next = slow.next.next;
        return fakeHead.next;
    }
}
'''
