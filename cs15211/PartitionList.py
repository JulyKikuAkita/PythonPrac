__source__ = 'https://leetcode.com/problems/partition-list/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/partition-list.py
# Time:  O(n)
# Space: O(1)
# Two Pointers
#
# Description: Leetcode # 86. Partition List
#
# Given a linked list and a value x,
# partition it such that all nodes less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the two partitions.
#
# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.
#
# Related Topics
# Linked List Two Pointers
#
import unittest
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

#384 ms
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
class TestMethods(unittest.TestCase):
    def test_Local(self):
        #1->4->3->2->5->2  ans is 1->2->2->4->3->5
        h1 = ListNode(1); n1 = ListNode(4) ; n2 = ListNode(3); n3 = ListNode(2) ; n4 = ListNode(5); n5 = ListNode(2)
        h1.next = n1 ; n1.next = n2; n2.next =n3 ; n3.next = n4; n4.next =n5
        test = SolutionOther()
        result = test.partition(h1 ,3)
        while result:
            print result.val
            result = result.next

        head = ListNode(1)
        head.next = ListNode(4)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(2)
        head.next.next.next.next = ListNode(5)
        head.next.next.next.next.next = ListNode(2)
        print Solution().partition(head, 3)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

the basic idea is to maintain two queues,
the first one stores all nodes with val less than x ,
and the second queue stores all the rest nodes.
Then concat these two queues. Remember to set the tail of second queue a null next, or u will get TLE.

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

# 0ms 100%
class Solution {
    public ListNode partition(ListNode head, int x) {
        ListNode firstHead = new ListNode(0);
        ListNode firstCur = firstHead;
        ListNode secondHead = new ListNode(0);
        ListNode secondCur = secondHead;
        while (head != null) {
            if (head.val < x) {
                firstCur.next = head;
                firstCur = head;
            } else {
                secondCur.next = head;
                secondCur = head;
            }
            head = head.next;
        }
        firstCur.next = secondHead.next;
        secondCur.next = null;
        return firstHead.next;
    }
}

# 0ms 100%
class Solution {
    public ListNode partition(ListNode head, int x) {
        ListNode dummy1 = new ListNode(0), dummy2 = new ListNode(0);  //dummy heads of the 1st and 2nd queues
        ListNode curr1 = dummy1, curr2 = dummy2;      //current tails of the two queues;
        while (head!=null){
            if (head.val<x) {
                curr1.next = head;
                curr1 = head;
            }else {
                curr2.next = head;
                curr2 = head;
            }
            head = head.next;
        }
        curr2.next = null;          //important! avoid cycle in linked list. otherwise u will get TLE.
        curr1.next = dummy2.next;
        return dummy1.next;
    }
}
'''