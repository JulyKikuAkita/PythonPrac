__source__ = 'https://leetcode.com/problems/find-bottom-left-tree-value/'
# Time:  O(n)
# Space: O(n)
#
# Description: 513. Find Bottom Left Tree Value
#
# Given a binary tree, find the leftmost value in the last row of the tree.
#
# Example 1:
# Input:
#
#     2
#    / \
#   1   3
#
# Output:
# 1
# Example 2:
# Input:
#
#         1
#        / \
#       2   3
#      /   / \
#     4   5   6
#        /
#       7
#
# Output:
# 7
# Note: You may assume the tree (i.e., the given root node) is not NULL.
#
# Hide Company Tags Microsoft
# Hide Tags Tree Depth-first Search Breadth-first Search
#

import unittest

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 56ms 20.16%
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        for node in queue:
            queue += filter(None, (node.right, node.left))
        return node.val

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
Doing BFS right-to-left means we can simply return the last node's value
and don't have to keep track of the first node in the current row or
even care about rows at all.
Inspired by @fallcreek's solution (not published) which uses two nested loops
to go row by row but already had the right-to-left idea making it easier. 
I just took that further.


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

# BFS:
# 7ms 31.01%
class Solution {
    public int findBottomLeftValue(TreeNode root) {
        if (root == null) return -1;
        LinkedList<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while(!queue.isEmpty()) {
            root = queue.poll();
            if (root.right != null) {
                queue.offer(root.right);
            }
            if (root.left != null) {
                queue.offer(root.left);
            }
        }
        return root.val;
    }
}

# DFS:
# 3ms 99.93%
class Solution {
    public int findBottomLeftValue(TreeNode root) {
         if (root == null) return -1;
         int[] res = new int[]{0, root.val}; //res[0] = depth, res[1] = leftNode.val
         dfs(root, 0, res);
         return res[1];
    }

    public void dfs(TreeNode root, int depth, int[] res) {
        if (depth > res[0]) {
            res[1] = root.val;
            res[0] = depth;
        }
        if (root.left != null) dfs(root.left, depth + 1, res);
        if (root.right != null) dfs(root.right, depth + 1, res);
    }
}

# BFS with idea of depth:
# 4ms 90.66%
class Solution {
    public int findLeftMostNode(TreeNode root) {
        if (root == null) return 0;

        int result = 0;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);

        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                if (i == 0) result = node.val;
                if (node.left != null) queue.add(node.left);
                if (node.right != null) queue.add(node.right);
            }
        }

        return result;
    }
}
'''