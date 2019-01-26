__source__ = 'https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 971. Flip Binary Tree To Match Preorder Traversal
#
# Given a binary tree with N nodes, each node has a different value from {1, ..., N}.
#
# A node in this binary tree can be flipped by swapping the left child and the right child of that node.
#
# Consider the sequence of N values reported by a preorder traversal starting from the root.
# Call such a sequence of N values the voyage of the tree.
#
# (Recall that a preorder traversal of a node means we report the current node's value,
# then preorder-traverse the left child, then preorder-traverse the right child.)
#
# Our goal is to flip the least number of nodes in the tree
# so that the voyage of the tree matches the voyage we are given.
#
# If we can do so, then return a list of the values of all nodes flipped.
# You may return the answer in any order.
#
# If we cannot do so, then return the list [-1].
#
# Example 1:
#
# Input: root = [1,2], voyage = [2,1]
# Output: [-1]
# Example 2:
#
# Input: root = [1,2,3], voyage = [1,3,2]
# Output: [1]
# Example 3:
#
# Input: root = [1,2,3], voyage = [1,2,3]
# Output: []
# Note:
#
# 1 <= N <= 100
#
import unittest

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        self.flipped = []
        self.i = 0

        def dfs(node):
            if node:
                if node.val != voyage[self.i]:
                    self.flipped = [-1]
                    return
                self.i += 1

                if (self.i < len(voyage) and
                        node.left and node.left.val != voyage[self.i]):
                    self.flipped.append(node.val)
                    dfs(node.right)
                    dfs(node.left)
                else:
                    dfs(node.left)
                    dfs(node.right)

        dfs(root)
        if self.flipped and self.flipped[0] == -1:
            self.flipped = [-1]
        return self.flipped

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/solution/
# Approach 1: Depth-First Search
# Complexity Analysis
# Time Complexity: O(N), where N is the number of nodes in the given tree.
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
# 6ms 93.52% 
class Solution {
    List<Integer> flipped;
    int index;
    int[] voyage;
    
    public List<Integer> flipMatchVoyage(TreeNode root, int[] voyage) {
        flipped = new ArrayList();
        index = 0;
        this.voyage = voyage;
        dfs(root);
        if (!flipped.isEmpty() && flipped.get(0) == -1) {
            flipped.clear();
            flipped.add(-1);
        }
        return flipped;
    }
    
    private void dfs(TreeNode node) {
        if (node != null) {
            if (node.val != voyage[index++]) {
                flipped.clear();
                flipped.add(-1);
                return;
            }
            
            if (index < voyage.length && node.left != null &&
                    node.left.val != voyage[index]) {
                flipped.add(node.val);
                dfs(node.right);
                dfs(node.left);
            } else {
                dfs(node.left);
                dfs(node.right);
            }
        }       
    }
}
'''
