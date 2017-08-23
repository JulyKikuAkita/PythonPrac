__source__ = 'https://leetcode.com/problems/odd-even-linked-list/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/odd-even-linked-list.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 328. Odd Even Linked List
#
# Given a singly linked list, group all odd nodes
# together followed by the even nodes.
# Please note here we are talking about the node number
# and not the value in the nodes.
#
# You should try to do it in place. The program should run
# in O(1) space complexity and O(nodes) time complexity.
#
# Example:
# Given 1->2->3->4->5->NULL,
# return 1->3->5->2->4->NULL.
#
# Note:
# The relative order inside both the even and odd groups
# should remain as it was in the input.
# The first node is considered odd, the second node even
# and so on ...
#
# Related Topics
# Linked List
#

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import unittest
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            odd_tail, cur = head, head.next
            while cur and cur.next:
                even_head = odd_tail.next
                odd_tail.next = cur.next
                odd_tail = odd_tail.next
                cur.next = odd_tail.next
                odd_tail.next = even_head
                cur = cur.next
        return head

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#61.82% 0ms
#Thought: https://leetcode.com/problems/odd-even-linked-list/solution/
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode oddEvenList(ListNode head) {
        ListNode oddHead = new ListNode(0);
        ListNode evenHead = new ListNode(0);
        ListNode oddCur = oddHead;
        ListNode evenCur = evenHead;
        while (head != null) {
            oddCur.next = head;
            oddCur = head;
            head = head.next;
            if (head == null) {
                break;
            }
            evenCur.next = head;
            evenCur = head;
            head = head.next;
        }
        oddCur.next = evenHead.next;
        evenCur.next = null;
        return oddHead.next;
    }
}

#3.67% 1ms
public class Solution {
    public ListNode oddEvenList(ListNode head) {
        if(head==null||head.next==null) return head;
        ListNode odd=head,ehead=head.next,even=ehead;
        while(even!=null&&even.next!=null){
            odd.next=even.next;
            odd=odd.next;
            even.next=odd.next;
            even=even.next;
        }
        odd.next=ehead;
        return head;
    }
}
'''