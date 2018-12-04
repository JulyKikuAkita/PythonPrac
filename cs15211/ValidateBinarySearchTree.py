__source__ = 'https://leetcode.com/problems/validate-binary-search-tree/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/validate-binary-search-tree.py
# Time:  O(n)
# Space: O(1)
# divide and conquer
#
# Description: Leetcode # 98. Validate Binary Search Tree
#
# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Example 1:
#     2
#    / \
#   1   3
# Binary tree [2,1,3], return true.
# Example 2:
#     1
#    / \
#   2   3
# Binary tree [1,2,3], return false.
#
# Companies
# Amazon Microsoft Bloomberg Facebook
# Related Topics
# Tree Depth-first Search
# Similar Questions
# Binary Tree Inorder Traversal Find Mode in Binary Search Tree

import unittest
# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

# Morris Traversal Solution
class Solution:
    # @param root, a tree node
    # @return a list of integers

    def isValidBST(self, root):
        cur, prev  = root, None
        while cur:
            if cur.left == None:
                if prev and cur and cur.val <= prev.val:
                    return False
                prev = cur
                cur = cur.right

            else:
                node = cur.left
                while node.right and node.right != cur:
                    node = node.right

                if node.right == None:
                    node.right = cur
                    cur = cur.left
                else:
                    if prev and cur and cur.val <= prev.val:
                        return False
                    node.right = None
                    prev = cur
                    cur = cur.right

        return True

# Time:  O(n)
# Space: O(logn)
class Solution2:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        return self.isValidBSTRecu(root, float("-inf"), float("inf"))

    def isValidBSTRecu(self, root, low, high):
        if root == None:
            return True
        if root.val <= low or root.val >= high:
            return False
        return  self.isValidBSTRecu(root.left, low, root.val) and self.isValidBSTRecu(root.right, root.val, high)

        #return low < root.val and root.val < high and \
        #       self.isValidBSTRecu(root.left, low, root.val) and self.isValidBSTRecu(root.right, root.val, high)

class SolutionOther:
    # @param root, a tree node
    # @return a boolean
    val = None
    def isValidBST(self, root):
        if root is None:
            return True
        ans = self.isValidBST(root.left)
        print self.val, root.val, "ans left= ", ans
        if self.val is None:
            self.val = root.val
        else:
            ans = ans and (root.val > self.val)
            self.val = root.val

        ans = ans and self.isValidBST(root.right)
        #print self.val, root.val, "ans right= ", ans
        return ans
#test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(20)
        root2 = TreeNode(1)
        root2.left = TreeNode(1)
        print Solution().isValidBST(root)
        print Solution2().isValidBST(root2)

        self.assertEqual(1, 1)
        print Solution().containsDuplicate([12344555,12344555])

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
 Note: buggy to rely on Integer.MAX_VALUE, Integer.MIN_VALUE, prefer for inorder traversal

# 0ms 100%
class Solution {
    public boolean isValidBST(TreeNode root) {
        return isValidBST(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
    }

    private boolean isValidBST(TreeNode root, long min, long max) {
        return root == null ||
            (root.val >= min && root.val <= max &&
                isValidBST(root.left, min, (long) root.val - 1) && isValidBST(root.right, (long) root.val + 1, max));
    }
}

# 0ms 100%
class Solution {
    public boolean isValidBST(TreeNode root) {
        return isValidBST(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    public boolean isValidBST(TreeNode root, long minVal, long maxVal) {
        if (root == null) return true;
        if (root.val >= maxVal || root.val <= minVal) return false;
        return isValidBST(root.left, minVal, root.val) && isValidBST(root.right, root.val, maxVal);
    }
}

# inOrder traversal
# BFS :
# https://discuss.leetcode.com/topic/4659/c-in-order-traversal-and-please-do-not-rely-on-buggy-int_max-int_min-solutions-any-more
# 2ms 28.95%
class Solution {
    public boolean isValidBST(TreeNode root) {
        if (root == null) return true;
        Stack<TreeNode> stack = new Stack<>();
        TreeNode pre = null;
        while (root != null || !stack.isEmpty()) {
            while( root != null) {
                stack.push(root);
                root = root.left;
            }
            root = stack.pop();
            if (pre != null && root.val <= pre.val) return false;
            pre = root;
            root = root.right;
        }
        return true;
    }
}

# wrong answer
Note: Not working with min/max
Fail at [3,1,5,0,2,4,6,null,null,null,3]
class Solution {
    public boolean isValidBST(TreeNode root) {
        return validate(root, null);
    }
    
    private boolean validate(TreeNode root, TreeNode prev) {
        if ( root == null ) return true;
        if ( root.left != null && root.val <= root.left.val) return false;
        if (!validate(root.left, prev)) return false;
        if ( prev != null && prev.val >= root.val) return false;
        return validate(root.right, root);
    }
}

'''