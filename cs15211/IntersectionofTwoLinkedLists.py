__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/intersection-of-two-linked-lists.py
# Time:  O(m + n)
# Space: O(1)
# LinkedList
#
# Write a program to find the node at which the intersection of two singly linked lists begins.
#
#
# For example, the following two linked lists:
#
# A:          a1 - a2
#                    \
#                      c1 - c2 - c3
#                    /
# B:     b1 - b2 - b3
# begin to intersect at node c1.
#
#
# Notes:
#
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
#
#  Amazon Microsoft Bloomberg



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        curA, curB = headA, headB
        tailA, tailB = None, None

        #idea: len(A)+len(B) is the same, so traverse A -> B ; B->A
        while curA and curB:
            if curA == curB:
                return curA

            if curA.next:
                curA = curA.next
            elif tailA is None: #reach here when !curA.next
                tailA = curA
                curA = headB
            else:
                break

            if curB.next:
                curB = curB.next #reach here when !curB.next
            elif tailB is None:
                tailB = curB
                curB = headA
            else:
                break

        return None


# http://blog.csdn.net/lilong_dream/article/details/41683563
class SolutionOther:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        curA, curB = headA, headB
        lenA, lenB = 0,0
        # get the length of A, B
        while curA is not None:
            lenA += 1
            curA = curA.next
        while curB is not None:
            lenB += 1
            curB = curB.next

        curA, curB = headA, headB

        # move diff steps for longer list
        if lenA > lenB:
            for i in range(lenA - lenB):
                curA = curA.next
        elif lenB > lenA:
            for i in range(lenB - lenA):
                curB = curB.next

        while curB != curA:
            curB = curB.next
            curA = curA.next

        return curA

#test
test = SolutionOther()
headA = ListNode(1)
headB = ListNode(2)
n = [1,3,5,7,9,11,13,15,17,19,21]
h1 = ListNode(3) ; h2 = ListNode(5); h3 = ListNode(7) ; h4 = ListNode(9) ; h5 = ListNode(11) ;
h7 = ListNode(13) ; h8 = ListNode(15); h9 = ListNode(17) ; h10 = ListNode(19) ; h11 = ListNode(21) ;
headA.next = h1; h1.next = h2; h2.next = h3; h3.next = h4; h4.next = h5; h5.next = h7; h7.next = h8
h8.next = h9; h9.next = h10; h10.next = h11;

ans = test.getIntersectionNode(headA, headB)
print "None" if ans == None else ans.val

if __name__ == "__main__":
    headA = ListNode(10)
    headB = ListNode(20)
    h1 = ListNode(11) ; h2 = ListNode(12); h3 = ListNode(30) ;h5 = ListNode(31) ;
    h4 = ListNode(21) ;
    headA.next = h1 ; h1.next = h2 ; h2.next = h3 ; h3.next = h5
    headB.next = h4 ; h4.next = h3 ;
    print Solution().getIntersectionNode(headA,headB)