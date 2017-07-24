__source__ = 'https://leetcode.com/problems/find-duplicate-subtrees/description/'
# Time:  O()
# Space: O()
#
# Description: Leetcode #
#
# Given a binary tree, return all duplicate subtrees.
# For each kind of duplicate subtrees,
# you only need to return the root node of any one of them.
#
# Two trees are duplicate if they have the same structure with same node values.
#
# Example 1:
#         1
#        / \
#       2   3
#      /   / \
#     4   2   4
#        /
#       4
# The following are two duplicate subtrees:
#       2
#      /
#     4
#
# and
#     4
#
# Therefore, you need to return above trees' root in the form of a list. [2,4]
# Companies
# Google
# Related Topics
# Tree
# Similar Questions
# Serialize and Deserialize Binary Tree Serialize and Deserialize BST
# Construct String from Binary Tree
#
import unittest
import collections
# Thought:
# We'll assign every subtree a unique merkle hash. ' \
# You can find more information about Merkle tree hashing here:
# https://discuss.leetcode.com/topic/88520/python-straightforward-with-explanation-o-st-and-o-s-t-approaches

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 112ms
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        from hashlib import sha256
        def hash_(x):
            S = sha256()
            S.update(x)
            return S.hexdigest()

        def merkle(node):
            if not node:
                return '#'
            m_left = merkle(node.left)
            m_right = merkle(node.right)
            node.merkle = hash_(m_left + str(node.val) + m_right)
            count[node.merkle].append(node)
            return node.merkle

        count = collections.defaultdict(list)
        merkle(root)
        return [nodes.pop() for nodes in count.values() if len(nodes) >= 2]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

# 69.95% 40ms
class Solution {
    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        List<TreeNode> res = new LinkedList<>();
        postorder(root, new HashMap<>(), res);
        return res;
    }

    public String postorder(TreeNode cur, Map<String, Integer> map, List<TreeNode> res) {
        if (cur == null) return "#";
        String serial = cur.val + "," + postorder(cur.left, map, res) + "," + postorder(cur.right, map, res);
        if (map.getOrDefault(serial, 0) == 1) res.add(cur);
        map.put(serial, map.getOrDefault(serial, 0) + 1);
        return serial;
    }
}

# 98.43% 28ms
public class Solution {
    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        List<TreeNode> res = new ArrayList<>();
        if (root == null) return res;
        Map <String, Integer> map = new HashMap<>();
        tree2str(root, map, res);
        return res;
    }

    private String tree2str(TreeNode root, Map<String, Integer> map, List<TreeNode> res)
    {
        if (root == null)
            return "#";
        String str = root.val + tree2str(root.left, map, res) + tree2str(root.right, map, res);
        if (map.getOrDefault(str, 0) == 1)
            res.add(root);
        map.put(str, map.getOrDefault(str, 0) + 1);
        return str;
    }
}

# DFS with isSameTree
# TLE
public class Solution {
    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        List<TreeNode> res = new ArrayList<>();
        if (root == null) return res;
        HashSet<TreeNode> set = new HashSet<>();
        set.add(root);
        findDuplicateSubtrees(root.left, set, res);
        findDuplicateSubtrees(root.right, set, res);

        return res;
    }

    private void findDuplicateSubtrees(TreeNode root, HashSet<TreeNode> set, List<TreeNode> res)
    {
        if (root == null)
            return;
        for (TreeNode r: set)
        {
            if (isSameTree(r, root))
            {
                boolean nodeContianedInRes = false;
                for (TreeNode nodeInRes: res)
                {
                    if (isSameTree(nodeInRes, root))
                        nodeContianedInRes = true;
                }
                if (!nodeContianedInRes)
                    res.add(root);
            }
        }
        set.add(root);
        findDuplicateSubtrees(root.left, set, res);
        findDuplicateSubtrees(root.right, set, res);
    }

    private boolean isSameTree(TreeNode p, TreeNode q)
    {
        if (p == null && q == null)
            return true;
        if (p == null ^ q == null)
            return false;
        if (p.val != q.val)
            return false;
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}
'''