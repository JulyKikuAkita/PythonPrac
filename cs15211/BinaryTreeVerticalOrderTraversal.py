__source__ = 'https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/binary-tree-vertical-order-traversal.py
# Time:  O(n)
# Space: O(n)
#
# Description: Leetcode # 314. Binary Tree Vertical Order Traversal
#
# Note: When two nodes have the same position (i.e. same X and same Y value),
# 314 asks us to sort them in the result based on X ("from left to right"),
# while 987 asks us to sort them in the result based on the nodes' values.
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
# Thought:
# https://leetcode.com/problems/binary-tree-vertical-order-traversal/discuss/76401/5ms-Java-Clean-Solution

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
# 2ms 96.49%
class Solution {
    public List<List<Integer>> verticalOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) return res;

        Map<Integer, ArrayList<Integer>> map = new HashMap<>();
        Queue<TreeNode> q = new LinkedList<>();
        Queue<Integer> cols = new LinkedList<>();

        q.add(root); 
        cols.add(0);

        int min = 0;
        int max = 0;
        
        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode cur = q.poll();
                int col = cols.poll();
                if (!map.containsKey(col)) map.put(col, new ArrayList());
                map.get(col).add(cur.val);
                min = Math.min(min, col);
                max = Math.max(max, col);
                
                if (cur.left != null) {
                    q.add(cur.left);
                    cols.add(col - 1);
                }
                
                if (cur.right != null) {
                    q.add(cur.right);
                    cols.add(col + 1);
                }
            }
        }
        for (int i = min; i <= max; i++) res.add(map.get(i));
        return res;
    }
}


# DFS
# 5ms 23.43%
class Solution {
    public List<List<Integer>> verticalOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList();
        TreeMap<Integer, TreeMap<Integer, List<Integer>>> map = new TreeMap<>();
        dfs(map, 0, 0, root);
        for (TreeMap<Integer, List<Integer>> depMap : map.values()) {
            List<Integer> val = new ArrayList();
            for (List<Integer> q : depMap.values()) {
                val.addAll(0, q);
            }
            res.add(val);
        }
        return res;
    }
    
    public void dfs(TreeMap<Integer, TreeMap<Integer, List<Integer>>> map, int col, int dep, TreeNode root) {
        if (root == null) return;
        if (map.get(col) == null) map.put(col,new TreeMap());
        if (map.get(col).get(dep) == null) {
            map.get(col).put(dep, new LinkedList());
        }
        dfs(map, col - 1, dep - 1, root.left);
        dfs(map, col + 1, dep - 1, root.right);
        map.get(col).get(dep).add(root.val);
    }
}
'''
