__source__ = 'https://leetcode.com/problems/split-bst/'
# Time:  O(N)
# Space: O(N)
#
# Description: Leetcode # 776. Split BST
#
# Given a Binary Search Tree (BST) with root node root,
# and a target value V, split the tree into two subtrees
# where one subtree has nodes that are all smaller or equal to the target value,
# while the other subtree has all nodes that are greater than the target value.
# It's not necessarily the case that the tree contains a node with value V.
#
# Additionally, most of the structure of the original tree should remain.
# Formally, for any child C with parent P in the original tree,
# if they are both in the same subtree after the split,
# then node C should still have the parent P.
#
# You should output the root TreeNode of both subtrees after splitting, in any order.
#
# Example 1:
#
# Input: root = [4,2,6,1,3,5,7], V = 2
# Output: [[2,1],[4,3,6,null,null,5,7]]
# Explanation:
# Note that root, output[0], and output[1] are TreeNode objects, not arrays.
#
# The given tree [4,2,6,1,3,5,7] is represented by the following diagram:
#
#           4
#         /   \
#       2      6
#      / \    / \
#     1   3  5   7
#
# while the diagrams for the outputs are:
#
#           4
#         /   \
#       3      6      and    2
#             / \           /
#            5   7         1
# Note:
#
# The size of the BST will not exceed 50.
# The BST is always valid and each node's value is different.
#
import unittest

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#20ms 100%
class Solution(object):
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        if not root:
            return None, None
        elif root.val <= V:
            bns = self.splitBST(root.right, V)
            root.right = bns[0]
            return root, bns[1]
        else:
            bns = self.splitBST(root.left, V)
            root.left = bns[1]
            return bns[0], root

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/split-bst/solution/
Complexity Analysis
Time Complexity: O(N), where N is the number of nodes in the input tree, as each node is checked once.
Space Complexity: O(N).

#99.36% 2ms
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
    public TreeNode[] splitBST(TreeNode root, int V) {
        if (root == null) return new TreeNode[]{null, null};
        else if (root.val <= V) {
            TreeNode[] subtree = splitBST(root.right, V);
            root.right = subtree[0];
            subtree[0] = root;
            return subtree;
        } else {
            TreeNode[] subtree = splitBST(root.left, V);
            root.left = subtree[1];
            subtree[1] = root;
            return subtree;
        }
    }
}

#99.36% 2ms
class Solution {
    public TreeNode[] splitBST(TreeNode root, int V) {
        TreeNode[] res = new TreeNode[2];
        if (root == null) return res;
        if (root.val <= V) {
            res[0] = root;
            TreeNode[] rightChild = splitBST(root.right, V);
            res[1] = rightChild[1];
            root.right = rightChild[0];
        } else {
            res[1] = root;
            TreeNode[] leftChild = splitBST(root.left, V);
            res[0] = leftChild[0];
            root.left = leftChild[1];
        }
        return res;
    }
}
'''