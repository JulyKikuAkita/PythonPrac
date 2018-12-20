__source__ = 'https://leetcode.com/problems/minimum-distance-between-bst-nodes/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 783. Minimum Distance Between BST Nodes
#
# Given a Binary Search Tree (BST) with the root node root,
# return the minimum difference between the values of any two different nodes in the tree.
#
# Example :
#
# Input: root = [4,2,6,1,3,null,null]
# Output: 1
# Explanation:
# Note that root is a TreeNode object, not an array.
#
# The given tree [4,2,6,1,3,null,null] is represented by the following diagram:
#
#           4
#         /   \
#       2      6
#      / \
#     1   3
#
# while the minimum difference in this tree is 1, it occurs between node 1 and node 2,
# also between node 3 and node 2.
# Note:
#
# The size of the BST will be between 2 and 100.
# The BST is always valid, each node's value is an integer, and each node's value is different.
#
import unittest

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 20ms 100%
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if node:
                dfs(node.left)
                self.ans = min(self.ans, node.val - self.prev)
                self.prev = node.val
                dfs(node.right)

        self.prev = float('-inf')
        self.ans = float('inf')
        dfs(root)
        return self.ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/minimum-distance-between-bst-nodes/solution/
#
Approach #2: In-Order Traversal [Accepted]
Complexity Analysis
Time Complexity: O(N), where N is the number of nodes in the tree. 
We iterate over every node once.
Space Complexity: O(H), where H is the height of the tree. 
This is the space used by the implicit call stack when calling dfs.

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
# 3ms 57.05%
class Solution {
    Integer prev, ans;
    public int minDiffInBST(TreeNode root) {
        prev = null;
        ans = Integer.MAX_VALUE;
        dfs(root);
        return ans;
    }
    
    private void dfs(TreeNode node) {
        if (node == null) return;
        dfs(node.left);
        if (prev != null) ans = Math.min(ans, node.val - prev);
        prev = node.val;
        dfs(node.right);
    }
}

# 2ms 99.92%
class Solution {
    private  int result= Integer.MAX_VALUE;
    private  Integer lastVisited=null;
    public int minDiffInBST(TreeNode root) {
        if (root.left != null) minDiffInBST(root.left);
        if (lastVisited != null) {
            result = Math.min(result, root.val - lastVisited);
        }
        lastVisited = root.val;
        if (root.right != null) minDiffInBST(root.right);
        return result;
    }
}

'''
