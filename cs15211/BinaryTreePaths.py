__source__ = 'https://leetcode.com/problems/binary-tree-paths/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/binary-tree-paths.py
# Time:  O(n * h)
# Space: O(h)
#
# Description: Leetcode # 257. Binary Tree Paths
#
# Given a binary tree, return all root-to-leaf paths.
#
# For example, given the following binary tree:
#
#   1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:
#
# ["1->2->5", "1->3"]
#
# Companies
# Google Facebook
# Related Topics
# Tree Depth-first Search
# Similar Questions
# Path Sum II
#
import unittest
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        result, path = [], []
        self.binaryTreePathRecu(root, path, result)
        return result

    def binaryTreePathRecu(self, node, path, result):
        if node is None:
            return
        if node.left is node.right is None:
            ans = ""
            for n in path:
                ans += str(n.val) + "->"
            result.append(ans +  str(node.val))

        if node.left:
            path.append(node)
            self.binaryTreePathRecu(node.left, path, result)
            path.pop()

        if node.right:
            path.append(node)
            self.binaryTreePathRecu(node.right, path, result)
            path.pop()

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

DFS 52.75% 17ms elegant:
public class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> result = new ArrayList<>();
        if (root == null) {
            return result;
        }
        getPaths(root, result, new StringBuilder());
        return result;
    }
    
    private void getPaths(TreeNode root, List<String> result, StringBuilder sb) {
        int length = sb.length();
        sb.append(root.val);
        if (root.left == null && root.right == null) {
            result.add(sb.toString());
        } else {
            sb.append("->");
            if (root.left != null) {
                getPaths(root.left, result, sb);
            }
            if (root.right != null) {
                getPaths(root.right, result, sb);
            }
        }
        sb.setLength(length);
    }
}

DFS: 33.76% 18ms need to setLength at each condition
public class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> res = new ArrayList<>();
        if (root == null) return res;
        dfs(root, res, new StringBuilder());
        return res;
    }
    
    public void dfs(TreeNode root, List<String> res, StringBuilder sb) {
        if (root == null) {
           return;
        }
        if( root.left == null && root.right == null) {
            int length = sb.length();
            sb.append(root.val);
            res.add(sb.toString());
            sb.setLength(length);
            return;
        }
        int length = sb.length();
        sb.append(root.val).append("->");
        if (root.left != null) {
            dfs(root.left, res, sb);
        }
        if (root.right != null) {
            dfs(root.right, res, sb);
        }
        sb.setLength(length);
    }
}

#22.26% 19ms
public class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> res = new ArrayList<>();
        helper(root, "", res);
        return res;
    }

    private void helper(TreeNode root, String path, List<String> res) {
        if (root == null)   return;
        path += root.val;

        if (root.left == null && root.right == null) {
            res.add(path);
            return;
        }

        if (root.left != null) {
            helper(root.left, path + "->", res);
        }

        if (root.right != null) {
            helper(root.right, path + "->", res);
        }
    }
}

BFS: 7.62% 22ms
public class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> res = new ArrayList<>();
        if (root == null) return res;
        Queue<NodeSB> q = new LinkedList<>();
        q.offer(new NodeSB(root, new StringBuilder()));
        
        while(!q.isEmpty()) {
            NodeSB curSB = q.poll();
            TreeNode cur = curSB.mNode;
            StringBuilder sb = curSB.mSB;
            if (cur.left == null && cur.right == null) {
                sb.append(cur.val);
                res.add(sb.toString());
            }
            sb.append(cur.val).append("->");
            if (cur.left != null) {
                q.add(new NodeSB(cur.left, new StringBuilder(sb) ));    
            }
            if (cur.right != null) {
                q.add(new NodeSB(cur.right, new StringBuilder(sb)));
            }       
        }
        return res;
    }
    
    class NodeSB{
        TreeNode mNode;
        StringBuilder mSB;
        public NodeSB(TreeNode node, StringBuilder sb) {
            mNode = node;
            mSB= sb;
        }
    }
}
'''
