__source__ = 'https://leetcode.com/problems/search-in-a-binary-search-tree/'
# Time:  O(N)
# Space: O(N)
#
# Description: Leetcode # 700. Search in a Binary Search Tree
#
# Given the root node of a binary search tree (BST) and a value.
# You need to find the node in the BST that the node's value equals the given value.
# Return the subtree rooted with that node.
# If such node doesn't exist, you should return NULL.
#
# For example,
#
# Given the tree:
#         4
#        / \
#       2   7
#      / \
#     1   3
#
# And the value to search: 2
# You should return this subtree:
#
#       2
#      / \
#     1   3
# In the example above, if we want to search the value 5,
# since there is no node with value 5, we should return NULL.
#
# Note that an empty tree is represented by NULL,
# therefore you would see the expected output (serialized tree format) as [], not null.
#

import unittest

class Solution(object):
    pass  # your function here

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
# 2ms 91.91%
class Solution {
    public TreeNode searchBST(TreeNode root, int val) {
        if (root == null || root.val == val) return root;
        if (val < root.val) return searchBST(root.left, val);
        return searchBST(root.right, val);
    }
}
'''
