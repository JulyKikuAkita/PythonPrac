__source__ = 'https://leetcode.com/problems/reverse-linked-list/#/solutions'
# https://github.com/kamyu104/LeetCode/blob/master/Python/reverse-linked-list.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 206. Reverse Linked List
# Reverse a singly linked list.
#
# click to show more hints.
#
# Hint:
# A linked list can be reversed either iteratively or recursively. Could you implement both?
#
# Companies
# Uber Facebook Twitter Zenefits Amazon Microsoft Snapchat Apple Yahoo Bloomberg Yelp Adobe
# Related Topics
# Linked List
# Similar Questions
# Reverse Linked List II Binary Tree Upside Down Palindrome Linked List

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

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        print Solution3().reverseList(head)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/articles/reverse-linked-list/

// recursion
# 28.41% 0ms
public class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode p = reverseList(head.next);
        head.next.next = head;
        head.next = null;
        return p;
    }
}

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
#3.84% 1ms
public class Solution {
    public ListNode reverseList(ListNode head) {
        if ( head == null) return head;
        //return dfs(head);
        return dfs2(head, null);
    }
//#3.84% 1ms
    private ListNode dfs(ListNode head) {
        if (head.next == null) return head;
        ListNode next = head.next;
        head.next = null;
        ListNode newHead = dfs(next);
        next.next = head; //reverse
        return newHead;
    }
//#3.84% 1ms
    private ListNode dfs2(ListNode head, ListNode newHead) {
        if (head == null) return newHead;
        ListNode next = head.next;
        head.next = newHead;
        return dfs2(next, head);
    }
}

//iteration
# 28.41% 0ms
public class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode dummy = null;
        while (head != null) {
            ListNode next = head.next;
            head.next = dummy;
            dummy = head;
            head = next;
        }
        return dummy;
    }
}
'''