__source__ = 'https://leetcode.com/problems/insert-into-a-cyclic-sorted-list/description/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 708. Insert into a Cyclic Sorted List
#
# Given a node from a cyclic linked list which is sorted in ascending order,
# write a function to insert a value into the list such that it remains a cyclic sorted list.
# The given node can be a reference to any single node in the list,
# and may not be necessarily the smallest value in the cyclic list.
#
# If there are multiple suitable places for insertion, you may choose any place to insert the new value.
# After the insertion, the cyclic list should remain sorted.
#
# If the list is empty (i.e., given node is null),
# you should create a new single cyclic list and return the reference to that single node.
# Otherwise, you should return the original given node.
#
# The following example may help you understand the problem better:
#
# In the figure above, there is a cyclic sorted list of three elements.
# You are given a reference to the node with value 3, and we need to insert 2 into the list.
# The new node should insert between node 1 and node 3. After the insertion,
# the list should look like this, and we should still return node 3
#
import unittest
# Thought
# There are only 2 situations :
#
# insertVal is between 2 nodes
# insertVal is the smallest or biggest. And both of them are same.
#
# 480 ms, 37.87%
# Definition for a Node.
class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next

class Solution(object):
	def insert(self, head, insertVal):
		"""
		:type head: Node
		:type insertVal: int
		:rtype: Node
		"""

		new_node = Node(insertVal, None)
		if not head:
			new_node.next = new_node
			return new_node

		cur = head

		while not (cur.val < insertVal <= cur.next.val):

			if cur.next.val <= cur.val:
				if cur.val < insertVal or cur.next.val >= insertVal:
					break

			cur = cur.next

		cur.next, new_node.next = new_node, cur.next
		return head

class Solution2(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        if head  is None:
            return Node(insertVal, None)

        cur_ptr = head
        next_ptr = cur_ptr.next

        # insert when the cur_ptr is <= insertval and insertval <= next_ptr
        # and then we break

        start = True
        add = False

        while start or cur_ptr != head:
            if start:
                start = False
            if cur_ptr.val > next_ptr.val:
                # there was a reverse in the list
                if insertVal <= next_ptr.val or insertVal >= cur_ptr.val:
                    cur_ptr.next = Node(insertVal, next_ptr)
                    add = True
                    break
            if cur_ptr.val <= insertVal and insertVal <= next_ptr.val:
                cur_ptr.next = Node(insertVal, next_ptr)
                add = True
                break
            else:
                cur_ptr = next_ptr
                next_ptr = next_ptr.next
        if not add:
            cur_ptr.next = Node(insertVal, next_ptr)
        return head

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: 4 ms 100%

/*
// Definition for a Node.
class Node {
    public int val;
    public Node next;

    public Node() {}

    public Node(int _val,Node _next) {
        val = _val;
        next = _next;
    }
};
*/
class Solution {
    public Node insert(Node head, int insertVal) {
        Node node = new Node(insertVal);
        if (head == null) {
            node.next = node;
            return node;
        }

        Node pre = head;
        Node cur = head.next;

        while (pre.next != head) {
            // insertVal is between pre and cur
            if (pre.val <= insertVal && cur.val > insertVal) break;

            // insertVal is smallest or biggest
            if (pre.val > cur.val && ( cur.val > insertVal || pre.val <= insertVal)) break;
            pre = cur;
            cur = cur.next;
        }
        pre.next = node;
        node.next = cur;
        return head;
    }
}
'''