__source__ = 'https://leetcode.com/problems/same-tree/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/same-tree.py
# Time:  O(n)
# Space: O(h), h is height of binary tree
# divide and conquer
#
# Description: Leetcode # 100. Same Tree
#
# Given two binary trees, write a function to check if they are equal or not.
#
# Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
#
# Companies
# Bloomberg
# Related Topics
# Tree Depth-first Search
import unittest
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        if p != None and q != None:
            return ( p.val == q.val ) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        root1, root1.left, root1.left.left = TreeNode(1), TreeNode(2), TreeNode(3)
        root2, root2.left, root2.right = TreeNode(1), TreeNode(2), TreeNode(3)
        print Solution().isSameTree(root1, root2)

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

# DFS
# 3ms 63.11%
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null  && q == null) return true;
        if (p == null || q == null || p.val != q.val) return false;
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}

# BFS
# 3ms 63.11%
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        Stack<TreeNode> stack_p = new Stack<>();
	    Stack<TreeNode> stack_q = new Stack<>();
	    if (p != null) stack_p.push(p);
	    if (q != null) stack_q.push( q ) ;
        while (!stack_p.isEmpty() && !stack_q.isEmpty()) {
            TreeNode pn = stack_p.pop();
            TreeNode qn = stack_q.pop();
            if (pn.val != qn.val) return false ;
            if (pn.right != null) stack_p.push(pn.right);
            if (qn.right != null) stack_q.push(qn.right);
            if (stack_p.size() != stack_q.size()) return false;
            if (pn.left != null) stack_p.push(pn.left);
            if (qn.left != null) stack_q.push(qn.left);
            if (stack_p.size() != stack_q.size()) return false;
        }
        return stack_p.size() == stack_q.size() ;
    }
}

'''
