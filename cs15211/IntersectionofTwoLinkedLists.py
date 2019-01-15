__source__ = 'https://leetcode.com/problems/intersection-of-two-linked-lists/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/intersection-of-two-linked-lists.py
# Time:  O(m + n)
# Space: O(1)
# LinkedList
#
# Description: Leetcode # 160. Intersection of Two Linked Lists
#
# Write a program to find the node at which the intersection of two singly linked lists begins.
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
# Companies
# Amazon Microsoft Bloomberg Airbnb
# Related Topics
# Linked List
# Similar Questions
# Minimum Index Sum of Two Lists
#
import unittest
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

# test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        test = SolutionOther()
        headA = ListNode(1)
        headB = ListNode(2)
        h1 = ListNode(3) ; h2 = ListNode(5); h3 = ListNode(7) ; h4 = ListNode(9) ; h5 = ListNode(11) ;
        h7 = ListNode(13) ; h8 = ListNode(15); h9 = ListNode(17) ; h10 = ListNode(19) ; h11 = ListNode(21) ;
        headA.next = h1; h1.next = h2; h2.next = h3; h3.next = h4; h4.next = h5; h5.next = h7; h7.next = h8
        h8.next = h9; h9.next = h10; h10.next = h11;

        ans = test.getIntersectionNode(headA, headB)
        print "None" if ans == None else ans.val

        headA = ListNode(10)
        headB = ListNode(20)
        h1 = ListNode(11) ; h2 = ListNode(12); h3 = ListNode(30) ;h5 = ListNode(31) ;
        h4 = ListNode(21) ;
        headA.next = h1 ; h1.next = h2 ; h2.next = h3 ; h3.next = h5
        headB.next = h4 ; h4.next = h3 ;
        print Solution().getIntersectionNode(headA,headB)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/intersection-of-two-linked-lists/solution/
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */

1, Get the length of the two lists.
2, Align them to the same start point.
3, Move them together until finding the intersection point, or the end null

# 1ms 100%
class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int lenA = getLength(headA);
        int lenB = getLength(headB);
        while (lenA > lenB) {
            headA = headA.next;
            lenA--;
        }
        while (lenB > lenA) {
            headB = headB.next;
            lenB--;
        }
        while (headA != null) {
            if (headA == headB) {
                return headA;
            } else {
                headA = headA.next;
                headB = headB.next;
            }
        }
        return null;
    }

    private int getLength(ListNode head) {
        int count = 0;
        while (head != null) {
            head = head.next;
            count++;
        }
        return count;
    }
}

Thought:
Maintain two pointers pA and pB initialized at the head of A and B, respectively.
Then let them both traverse through the lists, one node at a time.
When pA reaches the end of a list, then redirect it to the head of B (yes, B, that's right.);
similarly when pB reaches the end of a list, redirect it the head of A.
If at any point pA meets pB, then pA/pB is the intersection node.

# 2ms 38.83%
class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        //boundary check
        if(headA == null || headB == null) return null;

        ListNode a = headA;
        ListNode b = headB;

        //if a & b have different len, then we will stop the loop after second iteration
        while( a != b){
            //for the end of first iteration, we just reset the pointer to the head of another linkedlist
            a = a == null? headB : a.next;
            b = b == null? headA : b.next;
        }
        return a;
    }
}
'''