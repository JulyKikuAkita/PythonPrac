__source__ = 'https://leetcode.com/problems/middle-of-the-linked-list/'
# Time:  O(N)
# Space: O(1)
#
# Description: Leetcode # 876. Middle of the Linked List
#
# Given a non-empty, singly linked list with head node head,
# return a middle node of linked list.
#
# If there are two middle nodes, return the second middle node.
#
# Example 1:
#
# Input: [1,2,3,4,5]
# Output: Node 3 from this list (Serialization: [3,4,5])
# The returned node has value 3.
# (The judge's serialization of this node is [3,4,5]).
# Note that we returned a ListNode object ans, such that:
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5,
# and ans.next.next.next = NULL.
# Example 2:
#
# Input: [1,2,3,4,5,6]
# Output: Node 4 from this list (Serialization: [4,5,6])
# Since the list has two middle nodes with values 3 and 4,
# we return the second one.
#
import unittest

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        A = [head]
        while A[-1].next:
            A.append(A[-1].next)
        return A[len(A) / 2]

class Solution2(object):
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/middle-of-the-linked-list/solution/
#
# Approach 1: Output to Array
# Intuition and Algorithm
#
# Put every node into an array A in order.
# Then the middle node is just A[A.length // 2],
# since we can retrieve each node by index.
#
# Give input = [1,2,3,4,5,6], expect [4,5,6], the given result was [3,4,5,6]
class WrongSolution {
    public ListNode middleNode(ListNode head) {
        ListNode[] A = new ListNode[100];
        int t = 0;
        while(head.next != null) {
            A[t++] = head;
            head = head.next;
        }
        return A[t / 2];
    }
}

#Wrong: also not work for a circular linked list
Input:
[1,2,3,4,5,6]
Output:
[3,4,5,6]
Expected:
[4,5,6]

# Approach 2: Fast and Slow Pointer (not work for a circular linked list)

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
# 0ms 100%
class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode fast = head, slow = head;
        while(fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }
        return slow;
    }
}

'''
