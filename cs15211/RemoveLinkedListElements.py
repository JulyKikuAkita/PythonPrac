__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/remove-linked-list-elements.py
# Time:  O(n)
# Space: O(1)
#
# Remove all elements from a linked list of integers that have value val.
#
# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5
#
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
     def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))
        else:
            return "Nil"

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        cur, prev = head, dummy

        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return dummy.next


if __name__ == "__main__":
    head = ListNode(3)
    head.next = ListNode(1)
    head.next.next = ListNode(1)
    print Solution().removeElements(head, 1)

#java
js = '''
public class Solution {
    public ListNode removeElements(ListNode head, int val) {
        ListNode fakeHead = new ListNode(0);
        fakeHead.next = head;
        ListNode prev = fakeHead;
        while (head != null) {
            if (head.val == val) {
                prev.next = head.next;
            } else {
                prev = head;
            }
            head = head.next;
        }
        return fakeHead.next;
    }
}

public class Solution {
    public ListNode removeElements(ListNode head, int val) {
        if(head == null) return head;

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode cur = dummy;

        while(cur.next != null){
            if(cur.next.val == val)
                cur.next = cur.next.next;
            else{
                cur = cur.next;
            }
        }

        return dummy.next;
    }
}
'''
