__source__ = 'https://leetcode.com/problems/populating-next-right-pointers-in-each-node/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/populating-next-right-pointers-in-each-node.py
# Time:  O(n)
# Space: O(1)
# Divide and conquer
#
# Description: Leetcode # 116. Populating Next Right Pointers in Each Node
#
# Given a binary tree
#
#     struct TreeLinkNode {
#       TreeLinkNode *left;
#       TreeLinkNode *right;
#       TreeLinkNode *next;
#     }
#
# Populate each next pointer to point to its next right node.
# If there is no next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
# Note:
#
# You may only use constant extra space.
# You may assume that it is a perfect binary tree
# (ie, all leaves are at the same level, and every parent has two children).
# For example,
# Given the following perfect binary tree,
#          1
#        /  \
#       2    3
#      / \  / \
#     4  5  6  7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \  / \
#     4->5->6->7 -> NULL
# Topics:
# Tree Depth-first Search
# You might like:
# (M) Populating Next Right Pointers in Each Node II (M) Binary Tree Right Side View
# Company:
# Microsoft
#
import unittest
#Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

    def __repr__(self):
        if self == None:
            return "Nil"
        else:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        head = root
        while head:
            cur = head
            while cur and cur.left:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            head = head.left

# Time:  O(n)
# Space: O(logn)
# recusion
class Solution2:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        if root.left:
            root.left.next = root.right
        if root.right and root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)


class SolutionOther:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root == None:
            return
        self.connect(root.left)
        self.connect(root.right)

        nl = root.left
        nr = root.right
        while (nl != None):
            #print nl.val, self.preorderTraversal1(nl)
            nl.next = nr
            nl = nl.right
            nr = nr.left

    def preorderTraversal1(self, root):
        ans = []
        p = root

        def preorder(p, ans):
            if p is None:
                return
            ans += [p.val]
            if p.left != None:
                preorder(p.left, ans)

            if p.right != None:
                preorder(p.right, ans)

        preorder(p, ans)
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        #############test
        #creating BST tree ####
        root0 = TreeNode(0)
        tree1 = TreeNode(1)
        tree2 = TreeNode(2)
        tree3 = TreeNode(3)
        tree4 = TreeNode(4)
        tree5 = TreeNode(5)
        tree6 = TreeNode(6)
        root0.left = tree1
        root0.right = tree2
        tree1.left = tree3
        tree1.right = tree4
        tree2.left = tree5
        tree2.right = tree6
        #end of creating BST tree ####

        root, root.left, root.right = TreeNode(1), TreeNode(2), TreeNode(3)
        root.left.left, root.left.right, root.right.left, root.right.right = TreeNode(4), TreeNode(5), TreeNode(
            6), TreeNode(7)
        Solution().connect(root)
        print root
        print root.left
        print root.left.left

        test = SolutionOther()
        test.connect(root0)
        #print test.preorderTraversal1(root0)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# DFS:
# 0ms 100%
class Solution {
    public void connect(TreeLinkNode root) {
        if (root == null) return;
        if (root.left != null) {
            root.left.next = root.right;
            if (root.next != null) {
                root.right.next = root.next.left;
            }
        }
        connect(root.left);
        connect(root.right);
    }
}

# BFS
# 0ms 100%
class Solution {
    public void connect(TreeLinkNode root) {
        if (root == null || root.left == null) {
            return;
        }
        TreeLinkNode leftMost = root.left;
        while (leftMost != null) {
            root.left.next = root.right;
            if (root.next != null) {
                root.right.next = root.next.left;
                root = root.next;
            } else {
                root = leftMost;
                leftMost = leftMost.left;
            }
        }
    }
}
'''