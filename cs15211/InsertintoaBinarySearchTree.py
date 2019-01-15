__source__ = 'https://leetcode.com/problems/insert-into-a-binary-search-tree/'
# Time:  O(h) h: height of the tree
# Space: O(h)
#
# Description: Leetcode # 701. Insert into a Binary Search Tree
#
# Given the root node of a binary search tree (BST) and a value to be inserted into the tree,
# insert the value into the BST. Return the root node of the BST after the insertion.
# It is guaranteed that the new value does not exist in the original BST.
#
# Note that there may exist multiple valid ways for the insertion,
# as long as the tree remains a BST after insertion.
#  You can return any of them.
#
# For example,
#
# Given the tree:
#         4
#        / \
#       2   7
#      / \
#     1   3
# And the value to insert: 5
# You can return this binary search tree:
#
#          4
#        /   \
#       2     7
#      / \   /
#     1   3 5
# This tree is also valid:
#
#          5
#        /   \
#       2     7
#      / \
#     1   3
#          \
#           4
#
import unittest

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#108ms 55.06%
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            root = TreeNode(val)
            return root
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root

#100ms 98.14%
class Solution2(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        return Solution2.BST_insert(root, val)

    @staticmethod
    def BST_insert(root, val):
        if root == None:
            root = TreeNode(val)
        elif root.val < val:
            root.right = Solution.BST_insert(root.right, val)
        else:
            root.left = Solution.BST_insert(root.left, val)
        return root

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
time complexity of the insertion operation is the same with search operation which is O(h).
Or O(N) in the worst case and O(logN) ideally if the tree is well organized.
The space complexity of the recursion soultion is O(h) as well.
In other word, O(N) in the worst case and O(logN) ideally.
If you implement the algorithm iteratively, the space complexity can be O(1).

# Recursion
# 1ms 100%
class Solution {
    public TreeNode insertIntoBST(TreeNode root, int val) {
        if (root == null) return new TreeNode(val);
        if (val < root.val) {
            root.left = insertIntoBST(root.left, val);
        } else {
            root.right = insertIntoBST(root.right, val);
        }
        return root;
    }
}

Ex: [7,3,9,2,5], insert 4,
the new BST will be : [7,3,9,2,5,null,null,null,null,4]. no need to balance

# Iteration
# 1ms 100%
class Solution {
      public TreeNode insertIntoBST(TreeNode root, int val) {
        if(root == null) return new TreeNode(val);
        TreeNode cur = root;
        while(true) {
            if(cur.val <= val) {
                if(cur.right != null) cur = cur.right;
                else {
                    cur.right = new TreeNode(val);
                    break;
                }
            } else {
                if(cur.left != null) cur = cur.left;
                else {
                    cur.left = new TreeNode(val);
                    break;
                }
            }
        }
        return root;
    }
}
'''