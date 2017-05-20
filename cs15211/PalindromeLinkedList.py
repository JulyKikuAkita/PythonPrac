__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/palindrome-linked-list.py
# Time:  O(n)
# Space: O(1)
#
# Given a singly linked list, determine if it is a palindrome.
#
# Follow up:
# Could you do it in O(n) time and O(1) space?
#
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

#test
head = ListNode(0)
sec = ListNode(0)
third = ListNode(0)
head.next, sec.next = sec, third
if __name__ == "__main__":
    print Solution2().isPalindrome(head)


#java
# http://www.jiuzhang.com/solutions/palindrome-linked-list/
js = '''
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
'''