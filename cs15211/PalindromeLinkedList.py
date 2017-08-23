__source__ = 'https://leetcode.com/problems/palindrome-linked-list/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/palindrome-linked-list.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 234. Palindrome Linked List
# Given a singly linked list, determine if it is a palindrome.
#
# Follow up:
# Could you do it in O(n) time and O(1) space?
# Companies
# Amazon Facebook
# Related Topics
# Linked List Two Pointers
# Similar Questions
# Palindrome Number Valid Palindrome Reverse Linked List
#
import unittest
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        reverse, fast = None, head
        # Reverse the first half part of the list.
        while fast and fast.next:
            fast = fast.next.next
            head.next, reverse, head = reverse, head, head.next

         # If the number of the nodes is odd,
        # set the head of the tail list to the next of the median node.
        tail = head.next if fast else head


        # Compare the reversed first half list with the second half list.
        # And restore the reversed first half list.
        is_palinrome = True
        while reverse:
            is_palinrome = is_palinrome and reverse.val == tail.val
            reverse.next, head, reverse = head, reverse, reverse.next
            tail = tail.next

        return is_palinrome

class Solution2(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True

        fast = head
        mid = head

        while fast and fast.next:
            fast = fast.next.next
            mid = mid.next

        #odd count
        if fast:
            mid = mid.next

        halfhead = mid
        halfhead = self.reverseList(halfhead)

        while head and halfhead:
            print head.val, halfhead.val
            if head.val != halfhead.val:
                return False
            head, halfhead = head.next, halfhead.next
        return True

    def reverseList(self, head):
        prev = None

        while head:
            tmp = head.next
            head.next = prev
            prev, head = head, tmp

        return prev

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

        #test
        head = ListNode(0)
        sec = ListNode(0)
        third = ListNode(0)
        head.next, sec.next = sec, third
        print Solution2().isPalindrome(head)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
1. find mid node and reverse the 2nd half of the list
2. compare value for first one and reversed 2nd half

#35.24% 2ms
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
#34.88% 2ms
public class Solution {
    public boolean isPalindrome(ListNode head) {
        if(head == null) return true;
        ListNode mid = getMidNode(head);
        mid = reverseList(mid);
        while(head != null && mid != null){
            if(head.val != mid.val) return false;
            head = head.next;
            mid = mid.next;
        }
        return true;
    }

    private ListNode getMidNode(ListNode head) {
        ListNode mid = head;
        ListNode fast = head;
        while(fast != null && fast.next != null){
            fast = fast.next.next;
            mid = mid.next;
        }

        mid = fast == null ? mid : mid.next;

        return mid;
    }


    private ListNode reverseList(ListNode head) {
        ListNode prev = null;
        while(head != null){
            ListNode tmp = head.next;
            head.next = prev;
            prev = head;
            head = tmp;
        }
        return prev;
    }
}

#34.88% 2ms
public class Solution {
    public boolean isPalindrome(ListNode head) {
        if(head == null){
            return true;
        }

        ListNode fast = head, slow = head;
        while (fast.next != null && fast.next.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }

        slow = reverseList(slow);
        fast = head;

        while(fast != null && slow != null){    // need to use slow in this while loop cause right half is smaller
            if(fast.val != slow.val){
                return false;
            }
            fast = fast.next;
            slow = slow.next;
        }

        return true;
    }

    private ListNode reverseList(ListNode node){
        ListNode fakeHead = null;
        while(node != null){
            ListNode next = node.next;
            node.next = fakeHead;
            fakeHead = node;
            node = next;
        }

        return fakeHead;
    }
}
'''