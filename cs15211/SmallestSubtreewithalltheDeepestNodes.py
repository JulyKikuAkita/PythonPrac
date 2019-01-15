__source__ = 'https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/'
# Time:  O(N)
# Space: O(N)
#
# Description: Leetcode # 865. Smallest Subtree with all the Deepest Nodes
#
# Given a binary tree rooted at root, the depth of each node is the shortest distance to the root.
#
# A node is deepest if it has the largest depth possible among any node in the entire tree.
#
# The subtree of a node is that node, plus the set of all descendants of that node.
#
# Return the node with the largest depth such that it contains all the deepest nodes in its subtree.
#
# Example 1:
#
# Input: [3,5,1,6,2,0,8,null,null,7,4]
# Output: [2,7,4]
# Explanation:
#
# We return the node with value 2, colored in yellow in the diagram.
# The nodes colored in blue are the deepest nodes of the tree.
# The input "[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]" is a serialization of the given tree.
# The output "[2, 7, 4]" is a serialization of the subtree rooted at the node with value 2.
# Both the input and output have TreeNode type.
#
# Note:
#
# The number of nodes in the tree will be between 1 and 500.
# The values of each node are unique.
#
import unittest

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 24ms 99.69%
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def r(root):
            if not root.left and not root.right:
                return 0, root
            if root.left and root.right:
                l_depth, l_res = r(root.left)
                r_depth, r_res = r(root.right)
                if l_depth == r_depth: return l_depth+1, root
                elif l_depth > r_depth: return l_depth+1, l_res
                else: return r_depth+1, r_res
            if root.left:
                l_depth, l_res = r(root.left)
                return l_depth+1, l_res
            if root.right:
                r_depth, r_res = r(root.right)
                return r_depth+1, r_res
        if not root: return None
        depth, res = r(root)
        return res

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/solution/
#
# Time Complexity: O(N), where N is the number of nodes in the tree.
# Space Complexity: O(N).

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
# Two pass DFS: 1. get max_depth, 2. get subtree
# 4ms 48.78%
class Solution {
    Map<TreeNode, Integer> depth;
    int max_depth;

    public TreeNode subtreeWithAllDeepest(TreeNode root) {
        depth = new HashMap();
        depth.put(null, -1);
        dfs(root, null);
        max_depth = -1;
        for (Integer d: depth.values()) {
            max_depth = Math.max(max_depth, d);
        }
        return getSubtree(root);
    }

    public void dfs(TreeNode node, TreeNode parent) {
        if (node != null) {
            depth.put(node, depth.get(parent) + 1);
            dfs(node.left, node);
            dfs(node.right, node);
        }
    }

    public TreeNode getSubtree(TreeNode node) {
        if (node == null || depth.get(node) == max_depth) return node;
        TreeNode left = getSubtree(node.left),
                 right = getSubtree(node.right);
        if (left != null && right != null) return node;
        if (left != null) return left;
        if (right != null) return right;
        return null;
    }
}

/**
 * The TreeDepth of a subtree is:
 *       Result.node: the largest depth node that is equal to or
 *                    an ancestor of all the deepest nodes of this subtree.
 *       Result.dist: the number of nodes in the path from the root
 *                    of this subtree, to the deepest node in this subtree.
 */
# One pass DFS
# 3ms 87.24%
class TreeDepth {
    TreeNode node;
    int depth;
    TreeDepth(TreeNode n, int d) {
        node = n;
        depth = d;
    }
}

class Solution {
    public TreeNode subtreeWithAllDeepest(TreeNode root) {
        return dfs(root).node;
    }

    public TreeDepth dfs(TreeNode node) {
        if (node == null) return new TreeDepth(null, 0);
        TreeDepth left = dfs(node.left),
                  right = dfs(node.right);
        if (left.depth > right.depth) return new TreeDepth(left.node, left.depth + 1);
        if (left.depth < right.depth) return new TreeDepth(right.node, right.depth + 1);
        return new TreeDepth(node, left.depth + 1);
    }
}
'''
