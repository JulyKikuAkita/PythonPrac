__source__ = 'https://leetcode.com/problems/plus-one-linked-list/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/plus-one-linked-list.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 369. Plus One Linked List
#
# Given a non-negative number represented as a singly linked list of digits, plus one to the number.
#
# The digits are stored such that the most significant digit is at the head of the list.
#
# Example:
# Input:
# 1->2->3
#
# Output:
# 1->2->4
#
# Companies
# Google
# Related Topics
# Linked List
# Similar Questions
# Plus One
#

import unittest
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Two pointers solution.
class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head

        left, right = dummy, head
        while right.next:
            if right.val != 9:
                left = right
            right = right.next

        if right.val != 9:
            right.val += 1
        else:
            left.val += 1
            right = left.next
            while right:
                right.val = 0
                right = right.next
        return dummy if dummy.val else dummy.next

# Time:  O(n)
# Space: O(1)
class Solution2(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def reverseList(head):
            dummy = ListNode(0)
            curr = head
            while curr:
                dummy.next, curr.next, curr = curr, dummy.next, curr.next
            return dummy.next
        rev_head = reverseList(head)
        curr, carry = rev_head, 1
        while curr and carry:
            curr.val += carry
            carry = curr.val / 10
            curr.val %= 10
            if carry and curr.next is None:
                curr.next = ListNode(0)
            curr = curr.next
        return reverseList(rev_head)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
# 43.85% 0ms
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode plusOne(ListNode head) {
        ListNode result = new ListNode(0);
        result.next = head;
        plus(result);
        return result.val == 0 ? head : result;
    }

    private int plus(ListNode head) {
        int sum = 0;
        if (head.next == null) {
            sum = head.val + 1;
        } else {
            int carry = plus(head.next);
            sum = head.val + carry;
        }
        head.val = sum % 10;
        return sum / 10;
    }
}
'''