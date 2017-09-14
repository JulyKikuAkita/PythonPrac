__source__ = 'https://leetcode.com/problems/longest-univalue-path/description/'
# Time:  O(n) where NN is the number of nodes in the tree. We process every node once.
# Space: O(h) where HH is the height of the tree. Our recursive call stack could be up to HH layers deep.
#
# Description: Leetcode # 687. Longest Univalue Path
#
# Given a binary tree, find the length of the longest path where each node in the path has the same value.
# This path may or may not pass through the root.
#
# Note: The length of path between two nodes is represented by the number of edges between them.
#
# Example 1:
#
# Input:
#
#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
# Output:
#
# 2
# Example 2:
#
# Input:
#
#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
# Output:
#
# 2
# Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
#
# Companies
# Google
# Related Topics
# Tree Recursion
# Similar Questions
# Binary Tree Maximum Path Sum Count Univalue Subtrees Path Sum III
#
import unittest
# The approach is similar to the Diameter of Binary Tree question except that we
# reset the left/right to 0 whenever the current node does not match the children node value.
#
# In the Diameter of Binary Tree question, the path can either go through the root or it doesn't.
#
# Imgur
#
# Hence at the end of each recursive loop, return the longest length using that node as the root
# so that the node's parent can potentially use it in its longest path computation.
#
# We also use an external variable longest that keeps track of the longest path seen so far.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#612ms
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Time: O(n)
        # Space: O(n)
        longest = [0]
        def traverse(node):
            if not node:
                return 0
            left_len, right_len = traverse(node.left), traverse(node.right)
            left = (left_len + 1) if node.left and node.left.val == node.val else 0
            right = (right_len + 1) if node.right and node.right.val == node.val else 0
            longest[0] = max(longest[0], left + right)
            return max(left, right)
        traverse(root)
        return longest[0]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/articles/longest-univalue-path/

Longest-Univalue-Path of a tree is among those Longest-Univalue-Path-Across at each node;
Longest-Univalue-Path-Across a node is sum of { Longest-Univalue-Path-Start-At each child with same value, + 1}

#76.50% 14ms
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    int max = 0;
    public int longestUnivaluePath(TreeNode root) {
        if (root == null) return 0;
        dfs(root, root.val);
        return max;
    }

    public int dfs(TreeNode root, int val) {
        if (root == null) return 0;
        int left = dfs(root.left, root.val);
        int right = dfs(root.right, root.val);
        max = Math.max(max, left + right);
        if (root.val == val) return 1 + Math.max(left, right);
        else return 0;
    }
}


class Solution {
    public int longestUnivaluePath(TreeNode root) {
        int[] res = new int[1];
        if (root != null) dfs(root, res);
        return res[0];
    }

    private int dfs(TreeNode node, int[] res) {
        int l = node.left != null ? dfs(node.left, res) : 0;
        int r = node.right != null ? dfs(node.right, res) : 0;
        int resl = node.left != null && node.left.val == node.val ? l + 1 : 0;
        int resr = node.right != null && node.right.val == node.val ? r + 1 : 0;
        res[0] = Math.max(res[0], resl + resr);
        return Math.max(resl, resr);
    }
}

'''