__source__ = 'https://leetcode.com/problems/remove-duplicates-from-sorted-list/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/remove-duplicates-from-sorted-list.py
# Time:  O(n)
# Space: O(1)
# LinkedList
#
# Description: Leetcode # 83. Remove Duplicates from Sorted List
#
# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.
#
# Related Topics
# Linked List
#
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
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        current = head
        while current and current.next:
            next = current.next
            if current.val == next.val:
                current.next = current.next.next
            else:
                current = next
        return head

class Solutionif:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None or head.next == None:
            return head
        dummy = ListNode(0)
        dummy.next, prev = head, head
        cur = head.next

        while cur:
            if prev.val == cur.val:
                prev.next = cur.next
                cur = cur.next
            else:
                prev = prev.next
                cur = cur.next
        return dummy.next

    def printList(self, head):
        curr = head
        count = 1
        while ( curr != None):
            print count, curr.val
            count += 1
            curr= curr.next

    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):

        curr = head

        # list has only one node
        if curr == None or curr.next == None:
            return head
        else:
            nextnode = head.next

        while ( curr != None and nextnode != None and nextnode.next != None):

            if curr.val == nextnode.val :

                curr.next = nextnode.next
                nextnode.val =None
                nextnode.next=None
                nextnode = curr.next

            else :
                #print curr.val, nextnode.val
                curr = curr.next
                nextnode = curr.next

        # list has only 2 node
        if nextnode != None and nextnode.next == None:
           if curr.val == nextnode.val :
                    curr.next = None
                    nextnode.val =None
                    nextnode.next=None
        return head

# test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        head, head.next, head.next.next = ListNode(1), ListNode(1), ListNode(2)
        head.next.next.next, head.next.next.next.next = ListNode(3), ListNode(3)
        print Solution().deleteDuplicates(head)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/remove-duplicates-from-sorted-list/solution/

 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
# Recursion
# 0ms 100%
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if(head == null || head.next == null)return head;
        head.next = deleteDuplicates(head.next);
        return head.val == head.next.val ? head.next : head;
    }
}

# 0ms 100%
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode cur = head;
        while (cur != null && cur.next != null) {
            if (cur.val == cur.next.val) {
                cur.next = cur.next.next;
            } else {
                cur = cur.next;
            }
        }
        return head;
    }
}

# 0ms 100%
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if ( head == null || head.next == null) return head;
        ListNode cur = head.next;
        ListNode prev = head;

        while( cur != null) {
            if (cur.val == prev.val){
                prev.next = cur.next;
                cur = prev.next;
            }else{
                cur = cur.next;
                prev = prev.next;
            }
        }
        return head;
    }
}
'''
