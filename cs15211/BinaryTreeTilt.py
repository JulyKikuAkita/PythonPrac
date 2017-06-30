__source__ = ''
# Time:  O(n)
# Space: O(n)
#
# Description:
# Given a binary tree, return the tilt of the whole tree.
#
# The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values
# and the sum of all right subtree node values. Null node has tilt 0.
#
# The tilt of the whole tree is defined as the sum of all nodes' tilt.
#
# Example:
# Input:
#          1
#        /   \
#       2     3
# Output: 1
# Explanation:
# Tilt of node 2 : 0
# Tilt of node 3 : 0
# Tilt of node 1 : |2-3| = 1
# Tilt of binary tree : 0 + 0 + 1 = 1
# Note:
#
# The sum of node values in any subtree won't exceed the range of 32-bit integer.
# All the tilt values won't exceed the range of 32-bit integer.
# Hide Company Tags Indeed
# Hide Tags Tree
# Explanation
# If we had each node's subtree sum,
# our answer would look like this psuedocode:
# for each node: ans += abs(node.left.subtreesum - node.right.subtreesum).
# Let _sum(node) be the node's subtree sum.
# We can find it by adding the subtree sum of the left child,
# plus the subtree sum of the right child, plus the node's value.
# While we are visiting the node (each node is visited exactly once),
# we might as well do the ans += abs(left_sum - right_sum) part.

import unittest
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def _sum(node):
            if not node:
                return 0
            left, right = _sum(node.left), _sum(node.right)
            self.ans += abs(left - right)
            return node.val + left + right
        _sum(root)
        return self.ans
# your function here

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:  https://leetcode.com/articles/binary-tree-tilt/
Time complexity : O(n)O(n). where nn is the number of nodes. Each node is visited once.
Space complexity : O(n)O(n). In worst case when the tree is skewed depth of tree will be nn.
In average case depth will be lognlogn.
post-order traversal

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
    int res = 0;
    public int findTilt(TreeNode root) {
        postOrder(root);
        return res;
    }

    private int postOrder(TreeNode root) {
        if (root == null) return 0;
        int left = postOrder(root.left);
        int right = postOrder(root.right);
        res += Math.abs(left - right);
        return left + right + root.val;
    }
}
'''