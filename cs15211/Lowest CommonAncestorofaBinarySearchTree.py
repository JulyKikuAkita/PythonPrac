__source__ = 'https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/#/solutions'
# https://github.com/kamyu104/LeetCode/blob/master/Python/lowest-common-ancestor-of-a-binary-search-tree.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 235. Lowest Common Ancestor of a Binary Search Tree
#
# Given a binary search tree (BST), find the lowest common ancestor (LCA)
# of two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: "The lowest common ancestor
# is defined between two nodes v and w as the lowest node in T that has both v
# and w as descendants (where we allow a node to be a descendant of itself).
#
#         _______6______
#       /              \
#     ___2__          ___8__
#   /      \        /      \
#   0      _4       7       9
#          /  \
#          3   5
# For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6.
# Another example is LCA of nodes 2 and 4 is 2, since a node can be a
# descendant of itself according to the LCA definition.
#
# Companies
# Amazon Microsoft Facebook Twitter
# Related Topics
# Tree
# Similar Questions
# Lowest Common Ancestor of a Binary Tree
#
import unittest
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        s, b = sorted([p.val, q.val])
        while not s <= root.val <= b:
            # Keep searching since root is outside of [s, b].
            root = root.left if s <= root.val else root.right
        # s <= root.val <= b.
        return root

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
#10.07% 10ms
public class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root.val > p.val && root.val > q.val) {
            return lowestCommonAncestor(root.left, p, q);
        } else if (root.val < p.val && root.val < q.val) {
            return lowestCommonAncestor(root.right, p, q);
        } else {
            return root;
        }
    }
}

#52.64% 8ms
public class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null) return null;
        if ((p.val - root.val) * (q.val - root.val) <= 0) return root;
        else if (p.val > root.val) return lowestCommonAncestor(root.right, p, q);
        else return lowestCommonAncestor(root.left, p, q);
    }
}
'''

