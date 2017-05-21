__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/lowest-common-ancestor-of-a-binary-search-tree.py
# Time:  O(n)
# Space: O(1)
#
# Given a binary search tree (BST), find the lowest common ancestor (LCA)
# of two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes v and w as the lowest node in T that has both v
# and w as descendants (where we allow a node to be a descendant of itself).”
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
# Amazon Microsoft Facebook Twitter
# Hide Tags Tree
# Hide Similar Problems (M) Lowest Common Ancestor of a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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


#java
js = '''
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

 public class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(p.val > q.val){
            return lowestCommonAncestor(root, q, p);
        }

        while(!(p.val <= root.val && root.val <= q.val)){
            root = root.val >= p.val ? root.left : root.right;
        }
        return root;
    }
}

public class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(p.val > q.val){
            return lowestCommonAncestor(root, q, p);
        }

        if(root.val >= p.val && root.val <= q.val) return root;

        else if(root.val >= p.val)
            return lowestCommonAncestor(root.left, p, q);
        else
            return lowestCommonAncestor(root.right, p, q);

    }
}
'''

