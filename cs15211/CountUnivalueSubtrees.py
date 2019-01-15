__source__ = 'https://leetcode.com/problems/count-univalue-subtrees/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/count-univalue-subtrees.py
# Time:  O(n)
# Space: O(h)
#
# Description: Leetcode # 250. Count Univalue Subtrees
#
# Given a binary tree, count the number of uni-value subtrees.
#
# A Uni-value subtree means all nodes of the subtree have the same value.
#
# For example:
# Given binary tree,
#
#               5
#              / \
#             1   5
#            / \   \
#           5   5   5
#
# return 4.
#
# Related Topics
# Tree
# Similar Questions
# Subtree of Another Tree
#
import unittest
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def __init__(self):
        self.cnt = 0
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.dfs(root, 0)
        return self.cnt

    def dfs(self, root, count):
        if not root:
            return [True, 0]
        if not root.left and not root.right:
            self.cnt += 1
            return [True, count]
        is_left, left_cnt = self.dfs(root.left, count)
        is_right, right_cnt = self.dfs(root.right, count)
        if( is_left and is_right and (not root.left or root.val == root.left.val) and (not root.right or root.val == root.right.val)):
                self.cnt += 1
                return [True, count]
        return [False, count]

class Solution2:
    # @param {TreeNode} root
    # @return {integer}
    def countUnivalSubtrees(self, root):
        [is_uni, count] = self.isUnivalSubtrees(root, 0);
        return count;

    def isUnivalSubtrees(self, root, count):
        if not root:
            return [True, count]

        [left, count] = self.isUnivalSubtrees(root.left, count)
        [right, count] = self.isUnivalSubtrees(root.right, count)
        if self.isSame(root, root.left, left) and \
           self.isSame(root, root.right, right):
                count += 1
                return [True, count]

        return [False, count]

    def isSame(self, root, child, is_uni):
        return not child or (is_uni and root.val == child.val)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: Helper all tells whether all nodes in the given tree have the given value.
And while doing that, it also counts the uni-value subtrees.
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

1)
# 0ms 100%
class Solution {
    public int countUnivalSubtrees(TreeNode root) {
        if (root == null) return 0;
        int[] res = new int[1];
        all(root, 0, res);
        return res[0];
    }
    
    private boolean all(TreeNode root, int val, int[] count) {
        if (root == null) return true;
        //use '|' so it needs to judge both side
        if (!all(root.left, root.val, count) | !all(root.right, root.val, count)) return false;
        count[0]++;
        return root.val == val;
    }
}

2) Postorder
# 0ms 100%
class Solution {
    public int countUnivalSubtrees(TreeNode root) {
        if (root == null) return 0;
        int[] res = new int[1];
        postOrder(root, res);
        return res[0];
    }
    
    private boolean postOrder(TreeNode root, int[] arr) {
        if (root == null) return true;
        boolean left = postOrder(root.left, arr);
        boolean right = postOrder(root.right, arr);
        if (left && right) {
            if (root.left != null && root.left.val != root.val) return false;
            if (root.right != null && root.right.val != root.val) return false;
            arr[0]++;
            return true;
        }
        return false;
    }
}

# 1ms 17.51%
class Solution {
    public int countUnivalSubtrees(TreeNode root) {
        if (root == null) return 0;
        int[] res = new int[1];
        postOrder(root, 0, res);
        return res[0];
    }

    private boolean postOrder(TreeNode root, int val, int[] count) {
        if (root == null) return true;
        if (!postOrder(root.left, root.val, count) | !postOrder(root.right, root.val, count)) return false;
        count[0]++;
        return root.val == val;
    }
}

# count
# 0ms 100%
class Solution {
    private int result;

    public int countUnivalSubtrees(TreeNode root) {
        if (root == null) {
            return 0;
        }
        count(root);
        return result;
    }

    private Integer count(TreeNode root) {
        boolean isLeftValid = root.left == null || isUnival(root.val, count(root.left));
        boolean isRightValid = root.right == null || isUnival(root.val, count(root.right));
        if (isLeftValid && isRightValid) {
            result++;
            return root.val;
        } else {
            return null;
        }
    }

    private boolean isUnival(int val, Integer childVal) {
        return childVal != null && childVal == val;
    }
}
'''