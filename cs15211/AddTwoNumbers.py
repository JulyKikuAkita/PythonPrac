__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/add-two-numbers.py
# Time:  O(n)
# Space: O(1)
# LinkedList
#
# You are given two linked lists representing two non-negative numbers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
#
# Definition for singly-linked list.
# Bloomberg


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry = val / 10
            current.next  = ListNode (val % 10)
            current = current.next

        if carry > 0:
            current.next = ListNode(carry)

        return dummy.next

if __name__ == '__main__':
    a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
    b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
    result = Solution().addTwoNumbers(a, b)
    print "{0} -> {1} -> {2}".format(result.val, result.next.val, result.next.next.val)

class SolutionOther:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        newHead = ListNode(0)
        carry = 0
        pointer = newHead

        while carry or l1 or l2:
            node = ListNode(carry)
            if l1:
                node.val += l1.val
                l1 = l1.next
            if l2:
                node.val += l2.val
                l2 = l2.next
            carry = node.val // 10
            node.val = node.val % 10
            #move pointer from newHead to next node
            pointer.next = node
            pointer = node

        return newHead.next

#test
l1 = ListNode(2)
#l1.next = ListNode(4)
#l1.next.next = ListNode(3)

l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)

test = Solution()
ans = test.addTwoNumbers(l1, l2)

while ans:
    print (ans.val)
    ans = ans.next

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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode fakeHead = new ListNode(0);
        ListNode cur = fakeHead;
        int carry = 0;
        while (l1 != null || l2 != null) {
            int val1 = 0;
            int val2 = 0;
            if (l1 != null) {
                val1 = l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                val2 = l2.val;
                l2 = l2.next;
            }
            int sum = val1 + val2 + carry;
            cur.next = new ListNode(sum % 10);
            carry = sum / 10;
            cur = cur.next;
        }
        if (carry > 0) {
            cur.next = new ListNode(carry);
        }
        return fakeHead.next;
    }
}
'''