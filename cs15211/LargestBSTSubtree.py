__source__ = 'https://github.com/kamyu104/LeetCode/blob/master/Python/largest-bst-subtree.py'
# Time:  O(n)
# Space: O(h)
#
# Description:
# # Given a binary tree, find the largest subtree which is a Binary Search Tree (BST),
# where largest means subtree with largest number of nodes in it.
#
# Note:
# A subtree must include all of its descendants.
# Here's an example:
#     10
#     / \
#    5  15
#   / \   \
#  1   8   7
# The Largest BST Subtree in this case is the highlighted one.
# The return value is the subtree's size, which is 3.
# Follow up:
# Can you figure out ways to solve it with O(n) time complexity?
#
# Hide Company Tags Microsoft
# Hide Tags Tree

import unittest
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        max_size = [1]
        def largestBSTSubtreeHelper(root):
            if root.left is None and root.right is None:
                return 1, root.val, root.val

            left_size, left_min, left_max = 0, root.val, root.val
            if root.left is not None:
                left_size, left_min, left_max = largestBSTSubtreeHelper(root.left)

            right_size, right_min, right_max = 0, root.val, root.val
            if root.right is not None:
                right_size, right_min, right_max = largestBSTSubtreeHelper(root.right)

            size = 0
            if (root.left is None or left_size > 0) and \
               (root.right is None or right_size > 0) and \
               left_max <= root.val <= right_min:
                size = 1 + left_size + right_size
                max_size[0] = max(max_size[0], size)

            return size, left_min, right_max

        largestBSTSubtreeHelper(root)
        return max_size[0]


# N is the size of the largest BST in the tree.
# If the tree is a BST, then n is the number of nodes, otherwise it's -infinity.
# If the tree is a BST, then min and max are the minimum/maximum value in the tree.
    def largestBSTSubtree2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return 0, 0, float('inf'), float('-inf')
            N1, n1, min1, max1 = dfs(root.left)
            N2, n2, min2, max2 = dfs(root.right)
            n = n1 + 1 + n2 if max1 < root.val < min2 else float('-inf')
            return max(N1, N2, n), n, min(min1, root.val), max(max2, root.val)
        return dfs(root)[0]

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

#64%
public class Solution {
    private int maxSize;

    public int largestBSTSubtree(TreeNode root) {
        helper(root);
        return maxSize;
    }

    private Result helper(TreeNode root) {
        if (root == null) {
            return new Result(0);
        }
        Result left = helper(root.left);
        Result right = helper(root.right);
        if (left.size == -1 || right.size == -1 
        || (root.left != null && left.max >= root.val) 
        || (root.right != null && right.min <= root.val)) {
            return new Result(-1);
        }
        int curSize = left.size + right.size + 1;
        maxSize = Math.max(maxSize, curSize);
        return new Result(root.left == null ? root.val : left.min, root.right == null ? root.val : right.max, curSize);
    }

    private class Result {
        private int min;
        private int max;
        private int size;

        Result(int min, int max, int size) {
            this.min = min;
            this.max = max;
            this.size = size;
        }
        Result(int size) {
            this(0, 0, size);
        }
    }
}

#64.79%
public int largestBSTSubtree(TreeNode root) {
    if (root == null) return 0;
    if (root.left == null && root.right == null) return 1;
    if (isValid(root, null, null)) return countNode(root);
    return Math.max(largestBSTSubtree(root.left), largestBSTSubtree(root.right));
    // return largestBSTSubtree(root); //fail
    // stack overflow with [10,5,15,1,8,null,7]
}

public boolean isValid(TreeNode root, Integer min, Integer max) {
    if (root == null) return true;
    if (min != null && min >= root.val) return false;
    if (max != null && max <= root.val) return false;
    return isValid(root.left, min, root.val) && isValid(root.right, root.val, max);
}

public int countNode(TreeNode root) {
    if (root == null) return 0;
    if (root.left == null && root.right == null) return 1;
    return 1 + countNode(root.left) + countNode(root.right);
}
'''