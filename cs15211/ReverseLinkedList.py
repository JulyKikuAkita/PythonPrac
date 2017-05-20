__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/reverse-linked-list.py
# Time:  O(n)
# Space: O(1)
#
# Reverse a singly linked list.
#
# click to show more hints.
#
# Hint:
# A linked list can be reversed either iteratively or recursively. Could you implement both?
#

# Definition for singly-linked list.
import unittest
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

# Iterative solution.
class Solution(unittest.TestCase):
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        dummy = ListNode(float("-inf"))
        while head:
            dummy.next, head.next, head = head, dummy.next, head.next
        return dummy.next

    def test(self):
        self.assertEqual()
# Time:  O(n)
# Space: O(n)
# Recursive solution.
class Solution2:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        [begin, end] = self.reverseListRecu(head)
        return begin
    def reverseListRecu(self, head):
        if not head:
            return [None, None]
        [begin, end] = self.reverseListRecu(head.next)

        if end:
            end.next = head
            head.next = None
            return [begin, head]
        else:
            return [head, head]
# java solution
# iterative and recursion
# http://www.programcreek.com/2014/05/leetcode-reverse-linked-list-java/
class Solution3:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if not head or not head.next:
            return head
        #get 2nd Node
        second = head.next
        # set the first's next to null
        head.next = None

        rest = self.reverseList(second)
        second.next = head

        return rest


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print Solution3().reverseList(head)

#java
js = '''
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode reverseList(ListNode head) {
        if(head == null || head.next == null) return head;

        ListNode p2 = head.next;
        head.next = null;

        ListNode rest = reverseList(p2);
        p2.next = head;

        return rest;

    }
}

public class Solution {
    public ListNode reverseList(ListNode head) {
        if(head == null || head.next == null) return head;
        ListNode prev = head;
        ListNode cur = head.next;
        prev.next = null;

        while(prev != null && cur != null){
            ListNode last = cur.next;
            cur.next = prev;
            prev = cur;
            cur = last;
        }
        return prev;
    }

}

// import org.junit.*;
// StringBuilder sb = new StringBuilder();
/*
ListNode head = new ListNode()[1,2,3];
*/
// ListNode testhead = sol.reverseList(head);
// While( testhead != null){
//    sb.append(testhead.val);
//    testhead = testhead.next;
// }
//
//Assert.assertequals("[3,2,1]", sb.toString());
'''