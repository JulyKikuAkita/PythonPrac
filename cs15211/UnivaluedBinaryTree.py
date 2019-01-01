__source__ = 'https://leetcode.com/problems/univalued-binary-tree/'
# Time:  O(N)
# Space: O(H)
#
# Description: Leetcode # 965. Univalued Binary Tree
#
# A binary tree is univalued if every node in the tree has the same value.
#
# Return true if and only if the given tree is univalued.
# Example 1:
#
# Input: [1,1,1,1,1,null,1]
# Output: true
#
# Example 2:
#
# Input: [2,2,2,5,2]
# Output: false
#
# Note:
#     The number of nodes in the given tree will be in the range [1, 100].
#     Each node's value will be an integer in the range [0, 99].
#
import unittest

# 44ms 100%
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        left_correct = (not root.left or root.val == root.left.val
                and self.isUnivalTree(root.left))
        right_correct = (not root.right or root.val == root.right.val
                and self.isUnivalTree(root.right))
        return left_correct and right_correct

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/univalued-binary-tree/solution/
#
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

Approach 1: Depth-First Search
Complexity Analysis
Time Complexity: O(N), where N is the number of nodes in the given tree.
Space Complexity: O(N)


Approach 2: Recursion
Complexity Analysis
Time Complexity: O(N), where N is the number of nodes in the given tree.
Space Complexity: O(H), where H is the height of the given tree.

# 4ms 100%
class Solution {
    public boolean isUnivalTree(TreeNode root) {
        boolean left_correct = (root.left == null ||
                (root.val == root.left.val && isUnivalTree(root.left)));
        boolean right_correct = (root.right == null ||
                (root.val == root.right.val && isUnivalTree(root.right)));
        return left_correct && right_correct;
    }
}

# 5ms 100%
class Solution {
    public boolean isUnivalTree(TreeNode root) {
        if (root == null || root.left == null && root.right == null) return true;
        
        if ((root.left != null && root.val != root.left.val) || 
        (root.right != null && root.val != root.right.val)) return false;
        return isUnivalTree(root.left) && isUnivalTree(root.right);
    }
}
'''
