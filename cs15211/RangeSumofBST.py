__source__ = 'https://leetcode.com/problems/range-sum-of-bst/'
# Time:  O(N)
# Space: O(H) height of the tree
#
# Description: Leetcode # 938. Range Sum of BST
#
# Given the root node of a binary search tree,
# return the sum of values of all nodes with value between L and R (inclusive).
#
# The binary search tree is guaranteed to have unique values.
#
# Example 1:
#
# Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
# Output: 32
# Example 2:
#
# Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
# Output: 23
#
# Note:
#
# The number of nodes in the tree is at most 10000.
# The final answer is guaranteed to be less than 2^31.
#
import unittest

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 252ms 89.32%
class SolutionRecursion(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                if L < node.val:
                    dfs(node.left)
                if node.val < R:
                    dfs(node.right)
        self.ans = 0
        dfs(root)
        return self.ans

# 260ms 84.38%
class SolutionIteration(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if L <= node.val <= R:
                    ans += node.val
                if L < node.val:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/range-sum-of-bst/solution/

# Recursion:
# 2ms 100%
class Solution {
    public int rangeSumBST(TreeNode root, int L, int R) {
        if (root == null) return 0; // base case.
        if (root.val < L) return rangeSumBST(root.right, L, R); // left branch excluded.
        if (root.val > R) return rangeSumBST(root.left, L, R); // right branch excluded.
        return root.val + rangeSumBST(root.right, L, R) + rangeSumBST(root.left, L, R); // count in both children.
    }
}

# 3ms 83.72%
class Solution {
    public int rangeSumBST(TreeNode root, int L, int R) {
       if (root == null) return 0; // base case.
       return (L <= root.val && root.val <= R ? root.val : 0) 
       + rangeSumBST(root.right, L, R) + rangeSumBST(root.left, L, R);
    }
}

# 2ms 100%
class Solution {
    public int rangeSumBST(TreeNode root, int L, int R) {
        if (root == null) return 0;
        int sum = 0;
        if (root.val > L) sum += rangeSumBST(root.left, L, R);
        if (root.val < R) sum += rangeSumBST(root.right, L, R);
        if (root.val >= L && root.val <= R) sum += root.val;
        return sum;
    }
}

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
# Iteration:
# 12ms 9.11%
class Solution {
    public int rangeSumBST(TreeNode root, int L, int R) {
        int ans = 0;
        Stack<TreeNode> stack = new Stack();
        stack.push(root);
        while (!stack.isEmpty()) {
            TreeNode node = stack.pop();
            if (node != null) {
                if (node.val >= L && node.val <= R) ans += node.val;
                if (node.val > L ) stack.push(node.left);
                if (node.val < R ) stack.push(node.right);
            }
        }
        return ans;
    }
}

'''
