__source__ = 'https://leetcode.com/problems/flip-equivalent-binary-trees/'
# Time:  O(N1 + N2) where N1, N2 are the lengths of root1 and root2.
# Space: O(N1 + N2)
#
# Description: Leetcode # 951. Flip Equivalent Binary Trees
#
# For a binary tree T, we can define a flip operation as follows:
# choose any node, and swap the left and right child subtrees.
#
# A binary tree X is flip equivalent to a binary tree Y
# if and only if we can make X equal to Y after some number of flip operations.
#
# Write a function that determines whether two binary trees are flip equivalent.
# The trees are given by root nodes root1 and root2.
#
# Example 1:
#
# Input: root1 = [1,2,3,4,5,6,null,null,null,7,8],
# root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
# Output: true
# Explanation: We flipped at nodes with values 1, 3, and 5.
# Flipped Trees Diagram
#
# Note:
#
# Each tree will have at most 100 nodes.
# Each value in each tree will be a unique integer in the range [0, 99].
#
import unittest

# 36ms 15.91%
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if root1 is root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False

        return (self.flipEquiv(root1.left, root2.left) and
                self.flipEquiv(root1.right, root2.right) or
                self.flipEquiv(root1.left, root2.right) and
                self.flipEquiv(root1.right, root2.left))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/flip-equivalent-binary-trees/solution/
Approach 1: Recursion
Complexity Analysis
Time Complexity: O(min(N_1, N_2)), where N1, N2 are the lengths of root1 and root2.
Space Complexity: O(min(H_1, H_2)), where H_1, H_2 are the heights of the trees of root1 and root2.

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
# 2ms 100%
class Solution {
    public boolean flipEquiv(TreeNode root1, TreeNode root2) {
        if (root1 == root2) return true;
        if (root1 == null || root2 == null || root1.val != root2.val) return false;
        return flipEquiv(root1.left, root2.left) && flipEquiv(root1.right, root2.right) ||
            flipEquiv(root1.left, root2.right) && flipEquiv(root1.right, root2.left);
    }
}

Approach 2: Canonical Traversal
Complexity Analysis
Time Complexity: O(N_1 + N_2), where N1, N2 are the lengths of root1 and root2.
In Python, this is min(N1, N2)
Space Complexity: O(N_1 + N_2). In Python, this is min(H1 ,H2),
where H1, H2 are the heights of the trees of root1 and root2

# 5ms 22.01%
class Solution {
    public boolean flipEquiv(TreeNode root1, TreeNode root2) {
        List<Integer> vals1 = new ArrayList();
        List<Integer> vals2 = new ArrayList();
        dfs(root1, vals1);
        dfs(root2, vals2);
        return vals1.equals(vals2);
    }

    private void dfs(TreeNode node, List<Integer> vals) {
        if (node != null) {
            vals.add(node.val);
            int L = node.left != null ? node.left.val : -1;
            int R = node.right != null ? node.right.val : -1;
            if (L < R) {
                dfs(node.left, vals);
                dfs(node.right, vals);
            } else {
                dfs(node.right, vals);
                dfs(node.left, vals);
            }
            vals.add(null);
        }
    }

}
'''