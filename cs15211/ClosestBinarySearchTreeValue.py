__source__ = 'https://leetcode.com/problems/closest-binary-search-tree-value/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/closest-binary-search-tree-value.py
# Time:  O(h)
# Space: O(1)
#
# Description: Leetcode # 270. Closest Binary Search Tree Value
#
# Given a non-empty binary search tree and a target value,
# find the value in the BST that is closest to the target.
# Note:
# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest to the target.
#
# Companies
# Microsoft Google Snapchat
# Related Topics
# Tree Binary Search
# Similar Questions
# Count Complete Tree Nodes Closest Binary Search Tree Value II
#
import unittest
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

# 32ms 99.29%
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return 0

        gap = float("inf")
        candidate = root

        while root:
            if abs(root.val - target) < gap:
                gap = abs(root.val - target)
                candidate = root

            if target == root.val:
                break
            elif target > root.val:
                root = root.right
            else:
                root = root.left
        return candidate.val

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# 0 ms 100%
class Solution {
    public int closestValue(TreeNode root, double target) {
        TreeNode kid = target < root.val? root.left : root.right;

        if( kid == null) return root.val;

        int closet = closestValue(kid, target);

        return Math.abs(root.val - target) < Math.abs(closet - target) ? root.val : closet;
    }
}

# 0 ms 100%
public class Solution {
    public int closestValue(TreeNode root, double target) {
        int closet = root.val;

        while (root != null){
            closet = Math.abs(root.val - target) < Math.abs(closet - target) ? root.val : closet;
            root = target < root.val? root.left:root.right;
        }
        return closet;
    }
}

# 0 ms 100%
class Solution {
    public int closestValue(TreeNode root, double target) {
        if (root == null) {
            return 0;
        }
        int result = root.val;
        while (root != null) {
            if (Math.abs(target - root.val) < Math.abs(target - result)) {
                result = root.val;
            }
            if (root.val > target) {
                root = root.left;
            } else if (root.val < target) {
                root = root.right;
            } else {
                return root.val;
            }
        }
        return result;
    }
}

# 0 ms 100%
class Solution {
    public int closestValue(TreeNode root, double target) {
        int result = root.val;
        if (root.left != null) {
            int left = closestValue(root.left, target);
            if (Math.abs(left - target) < Math.abs(result - target)) {
                result = left;
            }
        }
        if (root.right != null) {
            int right = closestValue(root.right, target);
            if (Math.abs(right - target) < Math.abs(result - target)) {
                result = right;
            }
        }
        return result;
    }
}
'''