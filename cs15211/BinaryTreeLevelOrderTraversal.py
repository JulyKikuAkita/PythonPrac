__source__ = 'https://leetcode.com/problems/binary-tree-level-order-traversal/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/binary-tree-level-order-traversal.py
# Time:  O(n)
# Space: O(n)
# BFS
#
# Description: Leetcode # 102. Binary Tree Level Order Traversal
#
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
#
# For example:
# Given binary tree {3,9,20,#,#,15,7},
#    3
#   / \
#  9  20
#    /  \
#   15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
#
# Companies
# LinkedIn Facebook Amazon Microsoft Apple Bloomberg
# Related Topics
# Tree Breadth-first Search
# Similar Questions
# Binary Tree Zigzag Level Order Traversal Binary Tree Level Order Traversal II
# Minimum Depth of Binary Tree Binary Tree Vertical Order Traversal
# Average of Levels in Binary Tree
#

# Definition for a  binary tree node
import unittest
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if root is None:
            return []
        result, current = [], [root]
        while current:
            next_level, vals = [], []
            for node in current:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level
            result.append(vals)
        return result

#preOrder
class Solution2(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        self.dfs(root, 0, res)
        return res

    def dfs(self, root, level, res):
        if not root:
            return
        if level + 1 > len(res):
            res.append([])
        res[level].append(root.val)

        self.dfs(root.left, level + 1, res)
        self.dfs(root.right, level + 1, res)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        #creating BST tree ####
        root0=TreeNode(3)
        tree1=TreeNode(1)
        tree2=TreeNode(5)
        tree3=TreeNode(0)
        tree4=TreeNode(2)
        tree5=TreeNode(4)
        tree6=TreeNode(6)
        root0.left=tree1
        root0.right=tree2
        tree1.left=tree3
        tree1.right=tree4
        tree2.left=tree5
        tree2.right=tree6
        #end of creating BST tree ####
        test = Solution2()
        print test.levelOrder(root0)

        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        result = Solution().levelOrder(root)
        print result

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/contains-duplicate/solution/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

# DFS
# 9.30% 3ms
public class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        dfs(root, 0, res);
        return res;
    }

    public void dfs(TreeNode root, int level, List<List<Integer>> res) {
        if(root == null) return;
        if(level + 1 > res.size()){ //same as if (res.size() <= level) {
            res.add(new ArrayList<Integer>());
        }
        res.get(level).add(root.val);
        dfs(root.left, level+1, res);
        dfs(root.right, level+1, res);

    }
}

#BFS
#32.79% , 2ms
public class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        List<List<Integer>> res = new LinkedList<List<Integer>>();

        if(root == null) return res;

        q.offer(root);
        while(!q.isEmpty()) {
            int size = q.size();
            List<Integer> tmp = new LinkedList<Integer>();
            for (int i = 0 ; i < size; i++) {
                TreeNode cur = q.poll();
                if (cur.left != null) q.offer(cur.left);
                if (cur.right != null) q.offer(cur.right);
                tmp.add(cur.val);
            }
            res.add(tmp);
        }
        return res;
    }
}

'''