__source__ = 'https://leetcode.com/problems/count-complete-tree-nodes/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/count-complete-tree-nodes.py
# Time:  O(h * logn) = O((logn)^2)
# Space: O(1)
#
# Description: Leetcode # 222. Count Complete Tree Nodes
#
# Given a complete binary tree, count the number of nodes.
#
# In a complete binary tree every level, except possibly the last,
# is completely filled, and all nodes in the last level are as far
# left as possible. It can have between 1 and 2h nodes inclusive at
# the last level h.
#
# Related Topics
# Tree Binary Search
# Similar Questions
# Closest Binary Search Tree Value
#
import unittest
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        if root is None:
            return 0

        node, level = root, 0
        while node.left is not None:
            node = node.left
            level += 1

        # Binary search.
        left, right = 2 ** level, 2 ** (level + 1)
        while left < right:
            mid = (left + right) / 2
            if not self.exist(root, mid):
                right = mid
            else:
                left = mid + 1
        return left - 1

        # Check if the nth node exist.
    def exist(self, root, n):
        k = 1
        while k <= n:
            k <<= 1
        k >>= 2

        node = root
        while k > 0:
            if (n & k) == 0:
                node = node.left
            else:
                node = node.right
            k >>= 1
        return node is not None

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().containsDuplicate([12344555,12344555])

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: http://bookshadow.com/weblog/2015/06/06/leetcode-count-complete-tree-nodes/
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

#DFS #27.17% 108ms
public class Solution {
    public int countNodes(TreeNode root) {
        int h = height(root);
        return h < 0 ? 0 :
               height(root.right) == h-1 ? (1 << h) + countNodes(root.right)
                                         : (1 << h-1) + countNodes(root.left);
    }

    public int height(TreeNode root) {
        return root == null ? -1 : 1 + height(root.left);
    }
}

# BFS # 97.86% 47ms
public class Solution {
    private int depth(TreeNode root) {
        int ans = 0;
        while (root != null) {
            ans++;
            root = root.left;
        }
        return ans;
    }
    public int countNodes(TreeNode root) {
        int depth = depth(root), count = (1 << depth)-1;
        TreeNode cur = root;
        while (cur != null) {
            depth--;
            int rightdepth = depth(cur.right);
            if (depth == rightdepth) {
                cur = cur.right;
            } else {
                count -= 1 << (depth-1);
                cur = cur.left;
            }
        }
        return count;
    }
}

# 87.48%
# 64 ms
public class Solution {
    public int countNodes(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int index = 1;
        while (root.left != null || root.right != null) {
            int left = countLeftDepth(root.left);
            int right = countLeftDepth(root.right);
            if (left == right) {
                index = index * 2 + 1;
                root = root.right;
            } else {
                index = index * 2;
                root = root.left;
            }
        }
        return index;
    }

    private int countLeftDepth(TreeNode root) {
        int count = 0;
        while (root != null) {
            root = root.left;
            count++;
        }
        return count;
    }
}

#DFS
#39.87% 103ms
public class Solution {
    public int countNodes(TreeNode root) {

        int leftDepth = leftDepth(root);
        int rightDepth = rightDepth(root);

        if (leftDepth == rightDepth)
            return (1 << leftDepth) - 1;
        else
            return 1+countNodes(root.left) + countNodes(root.right);

    }

    private int rightDepth(TreeNode root) {
        // TODO Auto-generated method stub
        int dep = 0;
        while (root != null) {
            root = root.right;
            dep++;
        }
        return dep;
    }

    private int leftDepth(TreeNode root) {
        // TODO Auto-generated method stub
        int dep = 0;
        while (root != null) {
            root = root.left;
            dep++;
        }
        return dep;
    }
}
'''