__source__ = 'https://leetcode.com/problems/linked-list-cycle/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/linked-list-cycle.py
# Time:  O(n)
# Space: O(1)
# Two Pointer
#
# Description: Leetcode # 141. Linked List Cycle
#
# Given a linked list, determine if it has a cycle in it.
#
# Follow up:
# Can you solve it without using extra space?
#
# Companies
# Amazon Microsoft Bloomberg Yahoo
# Related Topics
# Linked List Two Pointers
# Similar Questions
# Linked List Cycle II
#
# Definition for singly-linked list.
import unittest
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

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = head.next
        print Solution().hasCycle(head)

        t1 = Solution()
        print t1.hasCycle(c1)
        print t1.hasCycle(a1)
        print t1.hasCycle(b1)
        print t1.hasCycle(None)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/linked-list-cycle/solution
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
# Approach #2 (Two Pointers) [Accepted]
# 0ms 100%
class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                return true;
            }
        }
        return false;
    }
}

# Approach #1 (Hash Table) [Accepted]
# 5ms 16.46%
class Solution {
    public boolean hasCycle(ListNode head) {
        Set<ListNode> nodesSeen = new HashSet<>();
        while (head != null) {
            if (nodesSeen.contains(head)) {
                return true;
            } else {
                nodesSeen.add(head);
            }
            head = head.next;
        }
        return false;
    }
}
'''
