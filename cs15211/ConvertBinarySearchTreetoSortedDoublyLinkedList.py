__source__ = 'https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/description/'
# Time:  O(N)
# Space: O(N)
#
# Description: Leetcode # 426. Convert Binary Search Tree to Sorted Doubly Linked List
#
# Convert a BST to a sorted circular doubly-linked list in-place.
# Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.
#
# Let's take the following BST as an example, it may help you understand the problem better:
# We want to transform this BST into a circular doubly linked list.
# Each node in a doubly linked list has a predecessor and successor.
# For a circular doubly linked list, the predecessor of the first element is the last element,
# and the successor of the last element is the first element.
#
# The figure below shows the circular doubly linked list for the BST above.
# The "head" symbol means the node it points to is the smallest element of the linked list.
#
# Specifically, we want to do the transformation in place. After the transformation,
# the left pointer of the tree node should point to its predecessor,
# and the right pointer should point to its successor.
# We should return the pointer to the first element of the linked list.
#
# The figure below shows the transformed BST. The solid line indicates the successor relationship,
# while the dashed line means the predecessor relationship.
#

import unittest
# Inorder Transverse
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return
        dummy = Node(0, None, None)
        prev = dummy
        stack, node = [], root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            node.left, prev.right, prev = prev, node, node
            node = node.right
        dummy.right.left, prev.right = prev, dummy.right
        return dummy.right

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
#
# step1: inorder tranversal by recursion to connect the original BST
# step2: connect the head and tail to make it circular
#
# Tips: Using dummy node to handle corner case

// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;

    public Node() {}

    public Node(int _val,Node _left,Node _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};

class Solution {
    Node prev = null;
    public Node treeToDoublyList(Node root) {
        if (root == null) return null;
        Node dummy = new Node(0, null, null);
        prev = dummy;
        helper(root);
       	//connect head and tail
        prev.right = dummy.right;
        dummy.right.left = prev;
        return dummy.right;
    }

    private void helper(Node cur) {
        if (cur == null) return;
        helper(cur.left);
        prev.right = cur;
        cur.left = prev;
        prev = cur;
        helper(cur.right);
    }
}

#iteration: 91.73% 3ms
class Solution {
    public Node treeToDoublyList(Node root) {
        if (root == null) {
            return null;
        }

        Node first = null;
        Node last = null;

        Deque<Node> stack = new ArrayDeque<>();
        while (root != null || !stack.isEmpty()) {
            while (root != null) {
                stack.push(root);
                root = root.left;
            }
            root = stack.pop();
            if (first == null) {
                first = root;
            }
            if (last != null) {
                last.right = root;
                root.left = last;
            }
            last = root;
            root = root.right;
        }
        first.left = last;
        last.right = first;
        return first;
    }
}

# Divide and Conquer without Dummy Node Java Solution
# 2ms 100%
# Step 1: Divide:
# We divide tree into three parts: left subtree, root node, right subtree.
# Convert left subtree into a circular doubly linked list as well as the right subtree.
# Be careful. You have to make the root node become a circular doubly linked list.
#
# Step 2: Conquer:
# Firstly, connect left circular doubly linked list with the root circular doubly linked list.
# Secondly, connect them with the right circular doubly linked list. Here we go!
#
# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/discuss/154659/Divide-and-Conquer-without-Dummy-Node-Java-Solution
class Solution {
    public Node treeToDoublyList(Node root) {
        if (root == null) return null;
        Node leftHead = treeToDoublyList(root.left);
        Node rightHead = treeToDoublyList(root.right);
        root.left = root;
        root.right = root;
        return connect(connect(leftHead, root), rightHead);
    }

    // Used to connect two circular doubly linked lists. n1 is the head as well as n2.
    private Node connect(Node n1, Node n2) {
        if (n1 == null) return n2;
        if (n2 == null) return n1;
        Node tail1 = n1.left;
        Node tail2 = n2.left;
        tail1.right = n2;
        n2.left = tail1;
        tail2.right = n1;
        n1.left = tail2;
        return n1;
    }
}
'''