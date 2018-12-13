__source__ = 'https://leetcode.com/problems/kth-smallest-element-in-a-bst/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/kth-smallest-element-in-a-bst.py
# Time:  O(max(h, k))
# Space: O(h)
#
# Description: Leetcode # 217. Contains Duplicate
#
# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
#
# Note:
# You may assume k is always valid, 1 <= k <= BST's total elements.
#
# Follow up:
# What if the BST is modified (insert/delete operations) often and
# you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
#
# Companies
# Bloomberg Uber Google
# Related Topics
# Binary Search Tree
# Similar Questions
# Binary Tree Inorder Traversal
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import unittest
class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        s, cur, rank = [], root, 0

        while s or cur:
            if cur:
                s.append(cur)
                cur = cur.left
            else:
                cur = s.pop()
                rank += 1
                if rank == k:
                    return cur.val
                cur = cur.right
        return float("-inf")

    def kthSmallest2(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        while root:
            left = self.count(root.left)
            if left == k - 1:
                return root.val
            elif left < k -1:
                root= root.right
                k = k - left - 1
            else:
                root = root.left


    def count(self, root):
        if not root:
            return 0
        return 1 + self.count(root.left) + self.count(root.right)

    # 80ms 12.27%
    def kthSmallest3(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        count = []
        self.helper(root, count)
        return count[k-1]

    def helper(self, node, count):
        if not node:
            return

        self.helper(node.left, count)
        count.append(node.val)
        self.helper(node.right, count)

Java = '''
# Thought:
#
1. InOrder with BFS/DFS, and Binary search (most preferably)
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
    TreeNode res = null;
    int count = 0;
    public int kthSmallest(TreeNode root, int k) {
        count = k;
        find(root);
        return res.val;
    }

    void find(TreeNode root) {
        if (root == null || res != null) return;
        find(root.left);
        count--;
        if (count == 0) res = root;
        find(root.right);
    }
}

# BFS
# 2ms 22.23%
class Solution {
    public int kthSmallest(TreeNode root, int k) {
        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode p = root;
        int count = 0;

        while(!stack.isEmpty() || p != null) {
            if ( p != null) {
                stack.push(p);
                p = p.left;
            } else {
                TreeNode node = stack.pop();
                if (++ count == k) return node.val;
                p = node.right;
            }
        }
        return Integer.MIN_VALUE;
    }
}

# Binary Search
# 1ms 63.43%
class Solution {
    public int kthSmallest(TreeNode root, int k) {
        int cnt = countNodes(root.left);
        if (k == cnt + 1) {
            return root.val;
        } else if (k <= cnt) {
            return kthSmallest(root.left, k);
        } else{ // k > cnt + 1
            return kthSmallest(root.right, k - cnt - 1);
        }
    }

    public int countNodes(TreeNode node) {
        if (node == null) return 0;
        return 1 + countNodes(node.left) + countNodes(node.right);
    }
}

#45.07% 1ms
class Solution {
    int dfsCnt = 0;
    int result = Integer.MIN_VALUE;

    public int kthSmallest(TreeNode root, int k) {
        dfs(root, k);
        return result;
    }
    public void dfs(TreeNode root, int k) {
        if (root == null) return;
        dfs(root.left, k); //cannot use k--
        dfsCnt ++;
        if(dfsCnt == k) result = root.val;
        dfs(root.right, k);
    }
}
'''