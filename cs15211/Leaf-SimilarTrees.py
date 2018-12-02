__source__ = 'https://leetcode.com/problems/leaf-similar-trees/'
# Time:  O(N + M)
# Space: O(N + M)
#
# Description: Leetcode # 872. Leaf-Similar Trees
#
# Consider all the leaves of a binary tree.
# From left to right order, the values of those leaves form a leaf value sequence.
#
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
#
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
#
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
#
# Note:
#
# Both of the given trees will have between 1 and 100 nodes.
#
import unittest

#20ms 100%
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def TreeOne(root,r):
            if root is None:
                return None
            if root.left is not None:
                TreeOne(root.left,r)
            if root.right is not None:
                TreeOne(root.right,r)
            if root.left is None and  root.right is None:
                r.append(root.val)
            return r
        r1 = TreeOne(root1,[])
        r2 = TreeOne(root2,[])
        return r1 == r2

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/leaf-similar-trees/solution/
Approach 1: Depth First Search
Complexity Analysis
Time Complexity: O(T_1 + T_2), where T1, T2 are the lengths of the given trees.
Space Complexity: O(T_1 + T_2)O, the space used in storing the leaf values.

#DFS 2ms 99.33%

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        List<Integer> leaves1 = new ArrayList();
        List<Integer> leaves2 = new ArrayList();
        dfs(root1, leaves1);
        dfs(root2, leaves2);
        return leaves1.equals(leaves2);
    }

    private void dfs(TreeNode node, List<Integer> leafValues) {
        if (node == null) return;
        if (node.left == null && node.right == null) leafValues.add(node.val);
        dfs(node.left, leafValues);
        dfs(node.right, leafValues);
    }
}

# Queue:
# 2ms 99.33%
class Solution {
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        Queue<Integer> q = new LinkedList<Integer>();
        buildLeafNodeSeq(root1, q, true);
        buildLeafNodeSeq(root2, q, false);
        if (q.isEmpty()) return true;
        return false;
    }

    private void buildLeafNodeSeq(TreeNode node, Queue<Integer> q, boolean add) {
        if (node == null) {
            return;
        }
        if (node.left == null && node.right == null) {
            if (add) {
                q.add(node.val);
            } else {
                if (q.peek() == node.val) {
                    q.remove(node.val);
                }
            }
        }
        if (node.left != null) {
            buildLeafNodeSeq(node.left, q, add);
        }
        if (node.right != null) {
            buildLeafNodeSeq(node.right, q, add);
        }
    }
}
'''