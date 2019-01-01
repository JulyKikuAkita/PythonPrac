__source__ = 'https://leetcode.com/problems/cousins-in-binary-tree/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 993. Cousins in Binary Tree
#
# In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
#
# Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
#
# We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
#
# Return true if and only if the nodes corresponding to the values x and y are cousins.
#
# Example 1:
#
# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false
# Example 2:
#
# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true
# Example 3:
#
# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false
#
# Note:
#
# The number of nodes in the tree will be between 2 and 100.
# Each node has a unique integer value from 1 to 100.
#
import unittest

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 24ms 100%
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        parent = {}
        depth = {}
        def dfs(node, par = None):
            if node:
                depth[node.val] = 1 + depth[par.val] if par else 0
                parent[node.val] = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        return depth[x] == depth[y] and parent[x] != parent[y]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/cousins-in-binary-tree/solution/
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
# Complexity Analysis
# Time Complexity: O(N), where N is the number of nodes in the tree.
# Space Complexity: O(N) 
# 5ms 100%
class Solution {
    Map<Integer, Integer> depth;
    Map<Integer, TreeNode> parent;
    
    public boolean isCousins(TreeNode root, int x, int y) {
        depth = new HashMap();
        parent = new HashMap();
        dfs(root, null);
        return depth.get(x) == depth.get(y) && parent.get(x) != parent.get(y);
    }
    
    void dfs(TreeNode cur, TreeNode par) {
        if (cur != null) {
            depth.put(cur.val, par != null ? depth.get(par.val) + 1 : 0);
            parent.put(cur.val, par);
            dfs(cur.left, cur);
            dfs(cur.right, cur);
        }
    }
}

# DFS
# 23mas 100%
class Solution {
    private int depthX;
    private int depthY;
    private TreeNode parentX;
    private TreeNode parentY;
    
    public boolean isCousins(TreeNode root, int x, int y) {
        getCousin(root, x, y, 0, null);
        return depthX == depthY && parentX != parentY;
    }
    
    private void getCousin(TreeNode node, int x, int y, int depth, TreeNode parent) {
        if (node == null) return;
        if (node.val == x) {
            depthX = depth;
            parentX = parent;
        }
        if (node.val == y) {
            depthY = depth;
            parentY = parent;
        }
        getCousin(node.left, x, y, depth + 1, node);
        getCousin(node.right, x, y, depth + 1, node);
    }
}

# BFS
# 6ms 100%
class Solution {
    public boolean isCousins(TreeNode root, int x, int y) {
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        while (!q.isEmpty()) {
            int sz = q.size(), depth = 0, dX = -1, dY = -1;
            for (int i = 0; i < sz; i++) {
                TreeNode cur = q.poll();
                if (cur.val == x) dX = i;
                else if (cur.val == y) dY = i;
                if (cur.left != null && cur.right != null) {
                    if (cur.left.val == x && cur.right.val == y) return false;
                    if (cur.left.val == y && cur.right.val == x) return false;
                }
                if (cur.left != null) q.offer(cur.left);
                if (cur.right != null) q.offer(cur.right);
            }
            if (dX != -1 && dY != -1) return true;
        }
        return false;
    }
}
'''
