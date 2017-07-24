__source__ = 'https://leetcode.com/problems/merge-two-sorted-lists/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/merge-two-sorted-lists.py
# Time:  O(n)
# Space: O(1)
# Sort
#
# Description: Leetcode # 21. Merge Two Sorted Lists
#
# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.
#
# Companies
# Amazon LinkedIn Apple Microsoft
# Related Topics
# Linked List
# Similar Questions
# Merge k Sorted Lists Merge Sorted Array Sort List Shortest Word Distance II
#
import unittest
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

     def __repr__(self):
         if self:
             return "{} -> {}".format(self.val, self.next)

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        dummyhead = ListNode(0)
        ptr = dummyhead

        while l1 and l2:
            if l1.val < l2.val:
                ptr.next = l1
                l1 = l1.next
            else:
                ptr.next = l2
                l2 = l2.next
            ptr = ptr.next

        if l1:
            ptr.next = l1
        else:
            ptr.next = l2

        return dummyhead.next

class SolutionOther:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        node = ListNode(0)
        lnode1, lnode2, noden = l1 ,l2, node

        while lnode1 != None or lnode2 != None:
            if lnode1 is None:
                node.next = lnode2
                lnode2 = lnode2.next
            elif lnode2 is None:
                node.next = lnode1
                lnode1 = lnode1.next
            elif lnode1.val < lnode2.val:
                node.next = lnode1
                lnode1 = lnode1.next
            else:
                node.next = lnode2
                lnode2 = lnode2.next
            node = node.next
        return noden.next

#test
q0 = ListNode(2)
w0 = ListNode(1)
test = SolutionOther()
mergel = test.mergeTwoLists(q0,w0)
i = 0
while mergel:
    print i, mergel.val
    mergel = mergel.next
    i += 1

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        l1 = ListNode(0)
        l1.next = ListNode(1)
        l2 = ListNode (2)
        l2.next = ListNode(3)
        print Solution().mergeTwoLists(l1, l2)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:

# 80.24% 14ms
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode fakeHead = new ListNode(0);
        ListNode cur = fakeHead;
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                cur.next = l1;
                l1 = l1.next;
            } else {
                cur.next = l2;
                l2 = l2.next;
            }
            cur = cur.next;
        }
        while (l1 != null) {
            cur.next = l1;
            l1 = l1.next;
            cur = cur.next;
        }
        while (l2 != null) {
            cur.next = l2;
            l2 = l2.next;
            cur = cur.next;
        }
        return fakeHead.next;
    }
}

#Recursion:
# 80.24% 14ms
public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2){
		if(l1 == null) return l2;
		if(l2 == null) return l1;
		if(l1.val < l2.val){
			l1.next = mergeTwoLists(l1.next, l2);
			return l1;
		} else{
			l2.next = mergeTwoLists(l1, l2.next);
			return l2;
		}
    }
}
'''