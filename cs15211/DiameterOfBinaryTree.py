__source__ = 'https://leetcode.com/problems/diameter-of-binary-tree/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/contains-duplicate.py
# Time:  O(n)
# Space: O(n)
#
# Description: Leetcode # 543. Diameter of Binary Tree
#
# Given a binary tree, you need to compute the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
# This path may or may not pass through the root.
#
# Example:
# Given a binary tree
#           1
#          / \
#         2   3
#        / \
#       4   5
#
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
#
# Note: The length of path between two nodes is represented by the number of edges between them.
#
# Companies
# Google Facebook
# Related Topics
# Tree
#
import unittest
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
#72ms
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def depth(root):
            if not root:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            self.ans = max(self.ans, left + right)
            return 1 + max(left, right)
        depth(root)
        return self.ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
#58.85% 9ms

public class Solution {
    int max = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        maxDepth(root);
        return max;
    }

    private int maxDepth(TreeNode root) {
        if (root == null) return 0;

        int left = maxDepth(root.left);
        int right = maxDepth(root.right);

        max = Math.max(max, left + right);

        return Math.max(left, right) + 1;
    }
}
'''