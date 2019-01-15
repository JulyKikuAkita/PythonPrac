__source__ = 'https://leetcode.com/problems/linked-list-cycle-ii/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/linked-list-cycle-ii.py
# Time:  O(n)
# Space: O(1)
# Two Pointer
#
# Description: Leetcode # 142. Linked List Cycle II
#
# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
#
# Follow up:
# Can you solve it without using extra space?
#
# Related Topics
# Linked List Two Pointers
# Similar Questions
# Linked List Cycle Find the Duplicate Number
import unittest
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

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = head.next
        print Solution().detectCycle(head)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/linked-list-cycle-ii/solution/

my solution is like this:
using two pointers, one of them one step at a time. another pointer each take two steps.
Suppose the first meet at step k,the length of the Cycle is r. so..2k-k=nr,k=nr
Now, the distance between the start node of list and the start node of cycle is s.
the distance between the start of list and the first meeting node is k
(the pointer which wake one step at a time waked k steps).
The distance between the start node of cycle and the first meeting node is m, so...s=k-m,
s=nr-m=(n-1)r+(r-m),here we takes n = 1..so, using one pointer start from the start node of list,
another pointer start from the first meeting node, all of them wake one step at a time,
the first time they meeting each other is the start of the cycle.

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
# 1ms 49.73%
class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                ListNode result = head;
                while (result != slow) {
                    result = result.next;
                    slow = slow.next;
                }
                return result;
            }
        }
        return null;
    }
}

'''
