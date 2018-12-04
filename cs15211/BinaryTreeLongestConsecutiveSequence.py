__source__ = 'https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/binary-tree-longest-consecutive-sequence.py
# Time:  O(n)
# Space: O(h)
#
# Description: 298. Binary Tree Longest Consecutive Sequence
#
# Given a binary tree, find the length of the longest consecutive sequence path.
#
# The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections.
# The longest consecutive path need to be from parent to child (cannot be the reverse).
#
# For example,
#    1
#     \
#      3
#     / \
#    2   4
#         \
#          5
# Longest consecutive sequence path is 3-4-5, so return 3.
#    2
#     \
#      3
#     /
#    2
#   /
#  1
# Longest consecutive sequence path is 2-3,not3-2-1, so return 2.
#
# Companies
# Google
# Related Topics
# Tree
# Similar Questions
# Longe'st Consecutive Sequence Binary Tree Longest Consecutive Sequence II
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
#Python Iterative Breadth-First Search
from collections import deque
import unittest
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = 0
        dq = deque([[root,1]]) # [[]] otherwise tree obj not iterable err

        while dq:
            node, length = dq.popleft()
            res = max( res, length)
            for child in [node.left, node.right]:
                if child:
                    l = length + 1 if child.val == node.val + 1 else 1
                    dq.append([child,l])
        return res

# Python Iterative Depth-First Search
class Solution2(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = 0
        stack = [[root, 1]]

        while stack:
            node, length = stack.pop()
            res = max(res, length)
            for child in [node.left, node.right]:
                if child:
                    l = length +1 if child.val == node.val + 1 else 1
                    stack.append([child,l])
        return res

class Solution3(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_len = 0

        def longestConsecutiveHelper(root):
            if not root:
                return 0

            left_len = longestConsecutiveHelper(root.left)
            right_len = longestConsecutiveHelper(root.right)

            cur_len = 1
            if root.left and root.left.val == root.val + 1:
                cur_len = max(cur_len, left_len + 1);
            if root.right and root.right.val == root.val + 1:
                cur_len = max(cur_len, right_len + 1)

            self.max_len = max(self.max_len, cur_len, left_len, right_len)

            return cur_len

        longestConsecutiveHelper(root)
        return self.max_len

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought : https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/solution/

# 1ms 92.79%
class Solution {
    private int result;

    public int longestConsecutive(TreeNode root) {
        helper(root);
        return result;
    }

    private int helper(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int cur = 0;
        if (root.left != null) {
            int leftLen = helper(root.left);
            if (root.val + 1 == root.left.val) {
                cur = leftLen;
            }
        }
        if (root.right != null) {
            int rightLen = helper(root.right);
            if (root.val + 1 == root.right.val) {
                cur = Math.max(cur, rightLen);
            }
        }
        cur++;
        result = Math.max(result, cur);
        return cur;
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

Approach #1 (Top Down Depth-first Search) [Accepted]

# 0ms 100%
class Solution {
    public int longestConsecutive(TreeNode root) {
        return dfs(root, null, 0);
    }

    private int dfs(TreeNode p, TreeNode parent, int length) {
        if (p == null) return length;
        length = (parent != null && p.val == parent.val + 1) ? length + 1 : 1;
        return Math.max(length, Math.max(dfs(p.left, p, length),dfs(p.right, p, length)));
    }
}

# 1ms 92.79%
class Solution {
    private int max = 0;

    public int longestConsecutive(TreeNode root) {
        if(root == null) return 0;
        helper(root, 0, root.val);
        return max;
    }

    public void helper(TreeNode root, int cur, int target){
        if (root == null) return;
        if (root.val == target) cur++;
        else cur = 1;
        max = Math.max(max, cur);
        helper(root.left, cur, root.val + 1);
        helper(root.right, cur, root.val + 1);
    }
}

Approach #2 (Bottom Up Depth-first Search) [Accepted]
# 1ms 92.79%
class Solution {
    private int maxLength = 0;
    public int longestConsecutive(TreeNode root) {
        dfs(root);
        return maxLength;
    }

    private int dfs(TreeNode p) {
        if (p == null) return 0;
        int L = dfs(p.left) + 1;
        int R = dfs(p.right) + 1;
        if (p.left != null && p.val + 1 != p.left.val) {
            L = 1;
        }
        if (p.right != null && p.val + 1 != p.right.val) {
            R = 1;
        }
        int length = Math.max(L, R);
        maxLength = Math.max(maxLength, length);
        return length;
    }
}

# 1ms 92.79%
class Solution {
    public int longestConsecutive(TreeNode root) {
        int[] result = new int[1];
        longestConsecutive(root, result);
        return result[0];
    }

    private int longestConsecutive(TreeNode root, int[] result) {
        if (root == null) {
            return 0;
        }
        int leftLen = longestConsecutive(root.left, result);
        int rightLen = longestConsecutive(root.right, result);
        int curLen = 0;
        if (root.left != null && root.left.val == root.val + 1) {
            curLen = Math.max(curLen, leftLen);
        }
        if (root.right != null && root.right.val == root.val + 1) {
            curLen = Math.max(curLen, rightLen);
        }
        curLen++;
        result[0] = Math.max(result[0], curLen);
        return curLen;
    }
}

'''