__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/merge-two-sorted-lists.py
# Time:  O(n)
# Space: O(1)
# Sort
#
# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.
#

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

if __name__ == "__main__":
    l1 = ListNode(0)
    l1.next = ListNode(1)
    l2 = ListNode (2)
    l2.next = ListNode(3)
    print Solution().mergeTwoLists(l1, l2)