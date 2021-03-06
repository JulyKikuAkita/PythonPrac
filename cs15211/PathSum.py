__source__ = 'https://leetcode.com/problems/path-sum/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/path-sum.py
# Time:  O(n)
# Space: O(h), h is height of binary tree
# DFS
#
# Description: Leetcode # 112. Path Sum
#
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.
#
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
#
# Companies
# Microsoft
# Related Topics
# Tree Depth-first Search
# Similar Questions
# Path Sum II Binary Tree Maximum Path Sum Sum Root to Leaf Numbers Path Sum III
#
import unittest
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root is None:
            return False

        if root.left is None and root.right is None and root.val == sum:
            return True

        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

# http://www.programcreek.com/2013/01/leetcode-path-sum/
# breadth first search(BFS) problem with queue
class javaSolution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if not root:
            return False
        nodes = [(root, root.val)]
        while nodes:
            (cur, sumValue) = nodes.pop()

            if cur.left == None and cur.right == None and sumValue == sum:
                return True
            if cur.left != None:
                nodes.insert(0, (cur.left, cur.left.val + sumValue))
            if cur.right != None:
                nodes.insert(0, (cur.right, cur.right.val + sumValue))
        return False

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)
        root.left.left = TreeNode(11)
        root.left.left.right = TreeNode(2)
        print Solution().hasPathSum(root, 22)
        print javaSolution().hasPathSum(root, 22)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/path-sum/solution/
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

# 0ms 100%
class Solution {
    public boolean hasPathSum(TreeNode root, int sum) {
        if ( root == null) return false;
        if (root.left == null && root.right == null){
            return root.val == sum;
        }
           return hasPathSum(root.left, sum - root.val) || hasPathSum(root.right, sum - root.val);
    }
}

# 0ms 100%
class Solution {
    public boolean hasPathSum(TreeNode root, int sum) {
        if (root == null) {
            return false;
        }
        sum -= root.val;
        if (root.left == null && root.right == null) {
            return sum == 0;
        } else {
            return hasPathSum(root.left, sum) || hasPathSum(root.right, sum);
        }
    }
}
'''