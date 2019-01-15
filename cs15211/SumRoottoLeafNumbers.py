__source__ = 'https://leetcode.com/problems/sum-root-to-leaf-numbers/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/sum-root-to-leaf-numbers.py
# Time:  O(n)
# Space: O(h), h is height of binary tree
# divide and conquer
#
# Description: Leetcode # 129. Sum Root to Leaf Numbers
#
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
#
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
#
# Find the total sum of all root-to-leaf numbers.
#
# For example,
#
#     1
#    / \
#   2   3
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
#
# Return the sum = 12 + 13 = 25.
# Related Topics
# Tree Depth-first Search
# Similar Questions
# Path Sum Binary Tree Maximum Path Sum
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
    # @return an integer
    def sumNumbers(self, root):
        return self.sumNumbersRecu(root, 0)

    def sumNumbersRecu(self, root, num):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return num * 10 + root.val
        num = root.val + num * 10
        return self.sumNumbersRecu(root.left, num) +  self.sumNumbersRecu(root.right, num )

    def sumNumbersRecu2(self, root, num):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return num * 10 + root.val
        return self.sumNumbersRecu(root.left, num * 10 + root.val) \
               +  self.sumNumbersRecu(root.right, num * 10 + root.val )

class SolutionOther:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        ans = [0]  #if use int = ans, during recursion, ans is local var and the node.value cannot be accumulated
        if not root:
            return 0
        else:
            return self.dfsTree(root, root.val, ans)

    def dfsTree(self, node, nodeVal, ans):
        if not (node.left or node.right):
            ans[0] += nodeVal
            #print ans
        else:
            if node.left:
                self.dfsTree(node.left, nodeVal*10+node.left.val, ans)
            if node.right:
                self.dfsTree(node.right, nodeVal*10+node.right.val, ans)
        #print ans
        return ans[0]

# Test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        #############test
        #creating BST tree ####
        rootSolo=TreeNode(9)
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
        test = SolutionOther()
        #print test.sumNumbers(rootSolo)
        #print test.sumNumbers(root0)
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(1)
        print Solution().sumNumbers(root)

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
# BFS
# 0ms 100%
class Solution {
    int total;

    public int sumNumbers(TreeNode root) {
        total = 0;
        helper(root, 0);
        return total;
    }

    void helper(TreeNode root, int sum) {
        if (root == null) return;

        sum = sum * 10 + root.val;

        if (root.left == null && root.right == null) {
            total += sum;
            return;
        }

        helper(root.left, sum);
        helper(root.right, sum);
    }
}

# DFS
# 0ms 100%
class Solution {
    public int sumNumbers(TreeNode root) {
        return sum(root, 0);
    }

    public int sum(TreeNode n, int s){
        if (n == null) return 0;
        if (n.right == null && n.left == null) return s*10 + n.val;
        return sum(n.left, s*10 + n.val) + sum(n.right, s*10 + n.val);
    }
}
'''
