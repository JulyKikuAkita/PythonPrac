__source__ = 'https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/remove-duplicates-from-sorted-list-ii.py
# Time:  O(n)
# Space: O(1)
# LinkedList
#
# Description: Leetcode # 82. Remove Duplicates from Sorted List II
#
# Given a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.
#
# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.
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
    def deleteDuplicatesif(self, head):
        #below not working for 1->1->1->null
        dummy = ListNode(0)
        dummy.next = head
        prev, cur, next = dummy, head, head

        while cur and cur.next:
            next = cur.next
            if cur.val == next.val:
                while next.next and next.val == next.next.val:
                    next = next.next
                prev.next = next.next
                cur = prev.next
            else:
                prev = prev.next
                cur = cur.next
        return dummy.next

    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current.next:
            next = current.next
            while next.next and next.next.val == next.val:
                next = next.next
            if current.next is not next:
                current.next = next.next
            else:
                current = current.next
        return dummy.next

class SolutionOther:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None:
            return None
        nHead, flag = ListNode(0), False
        nHead.next , head = head, nHead
        while head:
            if (head.next and head.next.next and head.next.next.val == head.next.val):
                head.next =head.next.next
                flag = True

            elif flag == True and head.next:
                head.next = head.next.next
                flag = False
            else:
                head = head.next
        return nHead.next

class TestMethods(unittest.TestCase):
    def test_Local(self):
        #test
        c1 = ListNode(1)
        c2 = ListNode(2)
        c3 = ListNode(2)
        c1.next = c2
        c2.next = c3

        test = SolutionOther()
        ans = test.deleteDuplicates(c1)
        while ans:
            print ans.val
            ans = ans.next

        head, head.next, head.next.next = ListNode(1), ListNode(1), ListNode(1)
        head.next.next.next, head.next.next.next.next = ListNode(1), ListNode(1)
        head.next.next.next.next.next, head.next.next.next.next.next.next = ListNode(1), ListNode(1)
        print Solution().deleteDuplicates(head)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# if current node is not unique, return deleteDuplicates with head.next.
# If current node is unique, link it to the result of next list made by recursive call. Any improvement?
# 14.08% 1ms
# DFS
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
# 1ms 70.96%
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) return null;

        if (head.next != null && head.val == head.next.val) {
            while (head.next != null && head.val == head.next.val) {
                head = head.next;
            }
            return deleteDuplicates(head.next);
        } else {
            head.next = deleteDuplicates(head.next);
        }
        return head;
    }
}

# 1ms 70.96%
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode fakeHead = new ListNode(0);
        fakeHead.next = head;
        ListNode cur = fakeHead;
        while (head != null) {
            boolean isDuplicate = false;
            while (head.next != null && head.next.val == head.val) {
                isDuplicate = true;
                head = head.next;
            }
            if (isDuplicate) {
                cur.next = head.next;
            } else {
                cur.next = head;
                cur = cur.next;
            }
            head = head.next;
        }
        return fakeHead.next;
    }
}

# Use fasr, slow pointer
# 1ms 70.96%
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        //use two pointers, slow - track the node before the dup nodes,
        // fast - to find the last node of dups.
        ListNode dummy = new ListNode(0), fast = head, slow = dummy;
        slow.next = fast;
        while(fast != null) {
            while (fast.next != null && fast.val == fast.next.val) {
                fast = fast.next;    //while loop to find the last node of the dups.
            }
            if (slow.next != fast) { //duplicates detected.
                slow.next = fast.next; //remove the dups.
                fast = slow.next;     //reposition the fast pointer.
            } else { //no dup, move down both pointer.
                slow = slow.next;
                fast = fast.next;
            }

        }
        return dummy.next;
    }
}
'''
