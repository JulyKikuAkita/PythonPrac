__source__ = 'https://leetcode.com/problems/binary-tree-pruning/'
# Time:  O(N)
# Space: O(H)
#
# Description: Leetcode # 814. Binary Tree Pruning
#
# We are given the head node root of a binary tree,
# where additionally every node's value is either a 0 or a 1.
#
# Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.
#
# (Recall that the subtree of a node X is X, plus every node that is a descendant of X.)
#
# Example 1:
# Input: [1,null,0,0,1]
# Output: [1,null,0,null,1]
#
# Explanation:
# Only the red nodes satisfy the property "every subtree not containing a 1".
# The diagram on the right represents the answer.
#
# Example 2:
# Input: [1,0,1,0,0,0,1]
# Output: [1,null,1,null,1]
#
# Example 3:
# Input: [1,1,0,1,1,0,1,0]
# Output: [1,1,0,1,1,null,1]
#
# Note:
#
# The binary tree will have at most 100 nodes.
# The value of each node will only be 0 or 1.
#
import unittest

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#20ms 100%
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def containsOne(node):
            if not node: return False
            a1 = containsOne(node.left)
            a2 = containsOne(node.right)
            if not a1: node.left = None
            if not a2: node.right = None
            return node.val == 1 or a1 or a2
        return root if containsOne(root) else None

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/binary-tree-pruning/solution/
Approach #1: Recursion [Accepted]
Complexity Analysis
Time Complexity: O(N), where N is the number of nodes in the tree. We process each node once.
Space Complexity: O(H), whereHH is the height of the tree.
This represents the size of the implicit call stack in our recursion.

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

# 1ms 100%
class Solution {
    public TreeNode pruneTree(TreeNode root) {
        return containsOne(root) ? root : null;
    }

    private boolean containsOne(TreeNode node) {
        if (node == null) return false;
        boolean a1 = containsOne(node.left);
        boolean a2 = containsOne(node.right);
        if (!a1) node.left = null;
        if (!a2) node.right = null;
        return node.val == 1 || a1 || a2;
    }
}
'''
