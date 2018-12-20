__source__ = 'https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 671. Second Minimum Node In a Binary Tree
#
# Given a non-empty special binary tree consisting of nodes with the non-negative value,
# where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes,
# then this node's value is the smaller value among its two sub-nodes.
#
# Given such a binary tree, you need to output the second minimum value in the set
# made of all the nodes' value in the whole tree.
#
# If no such second minimum value exists, output -1 instead.
#
# Example 1:
# Input:
#     2
#    / \
#   2   5
#      / \
#     5   7
#
# Output: 5
# Explanation: The smallest value is 2, the second smallest value is 5.
# Example 2:
# Input:
#     2
#    / \
#   2   2
#
# Output: -1
# Explanation: The smallest value is 2, but there isn't any second smallest value.
#
# Companies
# LinkedIn
# Related Topics
# Tree
# Similar Questions
# Kth Smallest Element in a BST
#
import unittest
#32ms
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 20ms 100%
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = float('inf')
        min1 = root.val

        def dfs(node):
            if node:
                if min1 < node.val < self.ans:
                    self.ans = node.val
                elif node.val == min1:
                    dfs(node.left)
                    dfs(node.right)

        dfs(root)
        return self.ans if self.ans < float('inf') else -1

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''

# Thought: https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/solution/
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

# BFS
# 1ms 100%
class Solution {
    public int findSecondMinimumValue(TreeNode root) {
        if (root == null) return -1;
        int rootVal = root.val;
        int res = Integer.MAX_VALUE;
        boolean diffFound = false;

        Queue<TreeNode> q= new LinkedList<TreeNode>();
        q.add(root);

        while (!q.isEmpty()) {
            TreeNode cur = q.poll();
            if (cur.val != rootVal && cur.val < res) {
                res = cur.val;
                diffFound = true;
            }
            if (cur.left != null) {
                q.add(cur.left);
                q.add(cur.right);
            }
        }
        return (res == Integer.MAX_VALUE && !diffFound) ? -1 : res;
    }
}


# 1ms 100%
class Solution {
    public int findSecondMinimumValue(TreeNode root) {
        if (root == null || root.left == null) return -1;
        if (root.left.val > root.val && root.right.val > root.val)
            return Math.min(root.left.val, root.right.val);
        int left = root.left.val == root.val ? findSecondMinimumValue(root.left) : root.left.val;
        int right = root.right.val == root.val ? findSecondMinimumValue(root.right) :root.right.val;
        if (left != -1 && right != -1) return Math.min(left, right);
        return left == -1 ? right : left;
    }
}

'''
