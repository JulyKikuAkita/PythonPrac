__source__ = 'https://leetcode.com/problems/diameter-of-binary-tree/'
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

# 40ms 46.13%
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
# Thought: https://leetcode.com/problems/diameter-of-binary-tree/solution/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
# 7ms 46.10%
class Solution {
    public int diameterOfBinaryTree(TreeNode root) {
        int[] res = new int[1];
        getHeight(root, res);
        return res[0];
    }
    
    private int getHeight(TreeNode root, int[] res) {
        if (root == null) return 0;
        int left = getHeight(root.left, res);
        int right = getHeight(root.right, res);
        res[0] = Math.max(res[0], left + right);
        return 1 + Math.max(left, right);
    }
}

# 4ms 99.46%
class Solution {
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
