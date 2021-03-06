__source__ = 'https://leetcode.com/problems/trim-a-binary-search-tree/description/'
# Time:  O(N)
# Space: O(N)
#
# Description: Leetcode # 669. Trim a Binary Search Tree
#
# Given a binary search tree and the lowest and highest boundaries as L and R,
# trim the tree so that all its elements lies in [L, R] (R >= L).
# You might need to change the root of the tree,
# so the result should return the new root of the trimmed binary search tree.
#
# Example 1:
# Input:
#     1
#    / \
#   0   2
#
#   L = 1
#   R = 2
#
# Output:
#     1
#       \
#        2
# Example 2:
# Input:
#     3
#    / \
#   0   4
#    \
#     2
#    /
#   1
#
#   L = 1
#   R = 3
#
# Output:
#       3
#      /
#    2
#   /
#  1
#
#
# Companies
# Bloomberg
# Related Topics
# Tree
#

import unittest
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 48ms 59.59%
class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if L > root.val:
            return self.trimBST(root.right, L, R)
        elif R < root.val:
            return self.trimBST(root.left, L, R)
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/trim-a-binary-search-tree/solution/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

# 3ms 99.45%
class Solution {
    public TreeNode trimBST(TreeNode root, int L, int R) {
        if(root == null) {
            return root;
        }
        if(root.val < L) {
            return trimBST(root.right, L, R);
        }
        if(root.val > R) {
            return trimBST(root.left, L, R);
        }

        root.left = trimBST(root.left, L, R);
        root.right = trimBST(root.right, L, R);
        return root;
    }
}
'''