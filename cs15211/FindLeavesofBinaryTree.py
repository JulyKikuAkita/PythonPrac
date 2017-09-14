__source__ = 'https://leetcode.com/problems/find-leaves-of-binary-tree/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/find-leaves-of-binary-tree.py
# Time:  O(n)
# Space: O(h)
#
# Description: Leetcode # 366. Find Leaves of Binary Tree
#
# Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves,
# repeat until the tree is empty.
#
# Example:
# Given binary tree
#           1
#          / \
#         2   3
#        / \
#       4   5
# Returns [4, 5, 3], [2], [1].
#
# Explanation:
# 1. Removing the leaves [4, 5, 3] would result in this tree:
#
#           1
#          /
#         2
# 2. Now removing the leaf [2] would result in this tree:
#
#           1
# 3. Now removing the leaf [1] would result in the empty tree:
#
#           []
# Returns [4, 5, 3], [2], [1].
#
#
# Companies
# LinkedIn
# Related Topics
# Tree Depth-first Search
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import unittest
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def findLeavesHelper(node, result):
            if not node:
                return -1
            level = 1 + max(findLeavesHelper(node.left, result), \
                            findLeavesHelper(node.right, result))
            if len(result) < level + 1:
                result.append([])
            result[level].append(node.val)
            return level

        result = []
        findLeavesHelper(root, result)
        return result

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:

Thought: For this question we need to take bottom-up approach. 
The key is to find the height of each node. Here the definition of height is:
The height of a node is the number of edges from the node to the deepest leaf. 
--CMU 15-121 Binary Trees
https://www.cs.cmu.edu/~adamchik/15-121/lectures/Trees/trees.html

I used a helper function to return the height of current node. 
According to the definition, 
the height of leaf is 0. h(node) = 1 + max(h(node.left), h(node.right)).
The height of a node is also the its index in the result list (res). 
For example, leaves, whose heights are 0, are stored in res[0]. 
Once we find the height of a node, we can put it directly into the result.


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public List<List<Integer>> findLeaves(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        findLeaves(result, root);
        return result;
    }

    private int findLeaves(List<List<Integer>> result, TreeNode root) {
        if (root == null) {
            return 0;
        }
        int index = Math.max(findLeaves(result, root.left), findLeaves(result, root.right));
        if (result.size() == index) {
            result.add(new ArrayList<>());
        }
        result.get(index).add(root.val);
        return index + 1;
    }
}

'''