__source__ = 'https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/binary-tree-vertical-order-traversal.py
# Time:  O(n)
# Space: O(n)
#
# Given a binary tree, return the vertical order traversal of its nodes' values.
# (ie, from top to bottom, column by column).
#
# If two nodes are in the same row and column, the order should be from left to right.
#
# Examples:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its vertical order traversal as:
# [
#   [9],
#   [3,15],
#   [20],
#   [7]
# ]
# Given binary tree [3,9,20,4,5,2,7],
#     _3_
#    /   \
#   9    20
#  / \   / \
# 4   5 2   7
# return its vertical order traversal as:
# [
#   [4],
#   [9],
#   [3,5,2],
#   [20],
#   [7]
# ]
#
# Companies
# Google Facebook Snapchat
# Related Topics
# Hash Table
# Similar Questions
# Binary Tree Level Order Traversal
#

import unittest
import collections
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# BFS + hash solution.
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        cols = collections.defaultdict(list)
        queue = [(root, 0)]
        for node, i in queue:
            if node:
                cols[i].append(node.val)
                queue += (node.left, i - 1), (node.right, i + 1)
        return [cols[i] for i in xrange(min(cols.keys()), max(cols.keys()) + 1)] \
                   if cols else []

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
#94.35% 3ms
public class Solution {
    public List<List<Integer>> verticalOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) {
            return result;
        }
        Queue<TreeNode> nodeQueue = new LinkedList<>();
        Queue<Integer> indexQueue = new LinkedList<>();
        nodeQueue.add(root);
        indexQueue.add(0);
        int zeroIndex = 0;
        while (!nodeQueue.isEmpty()) {
            TreeNode curNode = nodeQueue.poll();
            int curIndex = indexQueue.poll();
            if (curIndex >= 0) {
                int offsetIndex = curIndex + zeroIndex;
                if (offsetIndex == result.size()) {
                    result.add(new ArrayList<>());
                }
                result.get(offsetIndex).add(curNode.val);
            } else {
                int offsetIndex = curIndex + zeroIndex;
                if (offsetIndex < 0) {
                    result.add(0, new ArrayList<>());
                    zeroIndex++;
                    offsetIndex++;
                }
                result.get(offsetIndex).add(curNode.val);
            }
            if (curNode.left != null) {
                nodeQueue.add(curNode.left);
                indexQueue.add(curIndex - 1);
            }
            if (curNode.right != null) {
                nodeQueue.add(curNode.right);
                indexQueue.add(curIndex + 1);
            }
        }
        return result;
    }
}

#84.47% 4ms
public class Solution {
    public List<List<Integer>> verticalOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        List<List<Integer>> leftList = new ArrayList<>();
        List<List<Integer>> rightList = new ArrayList<>();
        Queue<TreeNode> nodeQueue = new LinkedList<>();
        Queue<Integer> indexQueue = new LinkedList<>();

        if (root == null) {
            return result;
        }
        nodeQueue.add(root);
        indexQueue.add(0);
        while (!nodeQueue.isEmpty()) {
            TreeNode curNode = nodeQueue.poll();
            int curIndex = indexQueue.poll();
            if (curIndex >= 0) {
                if (rightList.size() == curIndex) {
                    rightList.add(new ArrayList<>());
                }
                rightList.get(curIndex).add(curNode.val);
            } else {
                if (leftList.size() == -curIndex - 1) {
                    leftList.add(new ArrayList<>());
                }
                leftList.get(-curIndex - 1).add(curNode.val);
            }
            if (curNode.left != null) {
                nodeQueue.add(curNode.left);
                indexQueue.add(curIndex - 1);
            }
            if (curNode.right != null) {
                nodeQueue.add(curNode.right);
                indexQueue.add(curIndex + 1);
            }
        }
        Collections.reverse(leftList);
        result.addAll(leftList);
        result.addAll(rightList);
        return result;
    }
}
'''