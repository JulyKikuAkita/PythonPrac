__source__ = 'https://leetcode.com/problems/count-complete-tree-nodes/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/count-complete-tree-nodes.py
# Time:  O(h * logn) = O((logn)^2)
# Space: O(1)

# Given a complete binary tree, count the number of nodes.
#
# In a complete binary tree every level, except possibly the last,
# is completely filled, and all nodes in the last level are as far
# left as possible. It can have between 1 and 2h nodes inclusive at
# the last level h.
#Topics:
# Tree Binary Search
# You might like:
# (E) Closest Binary Search Tree Value


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        if root is None:
            return 0

        node, level = root, 0
        while node.left is not None:
            node = node.left
            level += 1

        # Binary search.
        left, right = 2 ** level, 2 ** (level + 1)
        while left < right:
            mid = (left + right) / 2
            if not self.exist(root, mid):
                right = mid
            else:
                left = mid + 1
        return left - 1

        # Check if the nth node exist.
    def exist(self, root, n):
        k = 1
        while k <= n:
            k <<= 1
        k >>= 2

        node = root
        while k > 0:
            if (n & k) == 0:
                node = node.left
            else:
                node = node.right
            k >>= 1
        return node is not None

#Java
# http://bookshadow.com/weblog/2015/06/06/leetcode-count-complete-tree-nodes/
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

#DFS #47%
public class Solution {
    public int countNodes(TreeNode root) {
        int h = height(root);
        return h < 0 ? 0 :
               height(root.right) == h-1 ? (1 << h) + countNodes(root.right)
                                         : (1 << h-1) + countNodes(root.left);
    }

    public int height(TreeNode root) {
        return root == null ? -1 : 1 + height(root.left);
    }
}

# BFS # 96%
public class Solution {
    private int depth(TreeNode root) {
        int ans = 0;
        while (root != null) {
            ans++;
            root = root.left;
        }
        return ans;
    }
    public int countNodes(TreeNode root) {
        int depth = depth(root), count = (1 << depth)-1;
        TreeNode cur = root;
        while (cur != null) {
            depth--;
            int rightdepth = depth(cur.right);
            if (depth == rightdepth) {
                cur = cur.right;
            } else {
                count -= 1 << (depth-1);
                cur = cur.left;
            }
        }
        return count;
    }
}'''