__source__ = 'https://leetcode.com/problems/binary-tree-cameras/'
# Time:  O(N)
# Space: O(H)
#
# Description: Leetcode # 968. Binary Tree Cameras
#
# Given a binary tree, we install cameras on the nodes of the tree.
#
# Each camera at a node can monitor its parent, itself, and its immediate children.
#
# Calculate the minimum number of cameras needed to monitor all nodes of the tree.
#
# Example 1:
#
# Input: [0,0,null,0,0]
# Output: 1
# Explanation: One camera is enough to monitor all nodes if placed as shown.
#
# Example 2:
#
# Input: [0,0,null,0,null,0,null,null,0]
# Output: 2
# Explanation: At least two cameras are needed to monitor all nodes of the tree.
# The above image shows one of the valid configurations of camera placement.
#
# Note:
#     The number of nodes in the given tree will be in the range [1, 1000].
#     Every node has value 0.
#
import unittest

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 76ms 100%
class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def solve(node):
            # 0: Strict ST; All nodes below this are covered, but not this one
            # 1: Normal ST; All nodes below and incl this are covered - no camera
            # 2: Placed camera; All nodes below this are covered, plus camera here

            if not node: return 0, 0, float('inf')
            L = solve(node.left)
            R = solve(node.right)

            dp0 = L[1] + R[1]
            dp1 = min(L[2] + min(R[1:]), R[2] + min(L[1:]))
            dp2 = 1 + min(L) + min(R)

            return dp0, dp1, dp2

        return min(solve(root)[1:])

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/binary-tree-cameras/solution/
#
Approach 1: Dynamic Programming
Complexity Analysis
Time Complexity: O(N), where N is the number of nodes in the given tree.
Space Complexity: O(H), where H is the height of the given tree.

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

# 10ms 100%
class Solution {
    public int minCameraCover(TreeNode root) {
        int[] ans = solve(root);
        return Math.min(ans[1], ans[2]);
    }
    
    // 0: Strict ST; All nodes below this are covered, but not this one
    // 1: Normal ST; All nodes below and incl this are covered - no camera
    // 2: Placed camera; All nodes below this are covered, plus camera here
    public int[] solve(TreeNode node) {
        if (node == null) return new int[]{ 0, 0, 99999 };
        
        int[] L = solve(node.left);
        int[] R = solve(node.right);
        int mL12 = Math.min(L[1], L[2]);
        int mR12 = Math.min(R[1], R[2]);
        
        int d0 = L[1] + R[1];
        int d1 = Math.min(L[2] + mR12, R[2] + mL12);
        int d2 = 1 + Math.min(L[0], mL12) + Math.min(R[0], mR12);
        return new int[]{d0, d1, d2};
    }
}

# https://leetcode.com/problems/binary-tree-cameras/discuss/211180/JavaC%2B%2BPython-Greedy-DFS
# Explanation:
# Apply a recusion function dfs.
# Return 0 if it's a leaf.
# Return 1 if it's a parent of a leaf, with a camera on this node.
# Return 2 if it's coverd, without a camera on this node.
# 
# For each node,
# if it has a child, which is leaf (node 0), then it needs camera.
# if it has a child, which is the parent of a leaf (node 1), then it's covered.
# 
# If it needs camera, then res++ and we return 1.
# If it's covered, we return 2.
# Otherwise, we return 0.

# 9ms 100%
class Solution {
    int res = 0;
    public int minCameraCover(TreeNode root) {
        return (dfs(root) < 1 ? 1: 0)  +  res;
    }
    
    private int dfs(TreeNode root) {
        int left = root.left == null ? 2 : dfs(root.left), 
        right = root.right == null ? 2 : dfs(root.right);
        if (left == 0 || right == 0) {
            res++;
            return 1;
        }
        return left == 1 || right == 1 ? 2 : 0;
    }
}

'''
