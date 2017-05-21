__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/kth-smallest-element-in-a-bst.py
# Time:  O(max(h, k))
# Space: O(h)

# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
#
# Note:
# You may assume k is always valid, 1 <= k <= BST's total elements.
#
# Follow up:
# What if the BST is modified (insert/delete operations) often and
# you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
# Bloomberg Uber Google
# Hide Tags Binary Search Tree
# Hide Similar Problems (M) Binary Tree Inorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        s, cur, rank = [], root, 0

        while s or cur:
            if cur:
                s.append(cur)
                cur = cur.left
            else:
                cur = s.pop()
                rank += 1
                if rank == k:
                    return cur.val
                cur = cur.right
        return float("-inf")

    def kthSmallest2(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        while root:
            left = self.count(root.left)
            if left == k - 1:
                return root.val
            elif left < k -1:
                root= root.right
                k = k - left - 1
            else:
                root = root.left


    def count(self, root):
        if not root:
            return 0
        return 1 + self.count(root.left) + self.count(root.right)

    def kthSmallest3(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        count = []
        self.helper(root, count)
        return count[k-1]

    def helper(self, node, count):
        if not node:
            return

        self.helper(node.left, count)
        count.append(node.val)
        self.helper(node.right, count)

#java
js = '''
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
    public int kthSmallest(TreeNode root, int k) {
        while (root != null) {
            int leftCount = countNodes(root.left);
            if (leftCount == k - 1) {
                return root.val;
            } else if (leftCount < k - 1) {
                root = root.right;
                k -= leftCount + 1;
            } else {
                root = root.left;
            }
        }
        return 0;
    }

    private int countNodes(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return countNodes(root.left) + countNodes(root.right) + 1;
    }
}

 # Binary Search (dfs): most preferable
    public int kthSmallest(TreeNode root, int k) {
        int count = countNodes(root.left);
        if (k <= count) {
            return kthSmallest(root.left, k);
        } else if (k > count + 1) {
            return kthSmallest(root.right, k-1-count); // 1 is counted as current node
        }
        return root.val;
    }

    public int countNodes(TreeNode n) {
        if (n == null) return 0;
        return 1 + countNodes(n.left) + countNodes(n.right);
    }



# Inorder traverse for BST gives the natural order of numbers.
No need to use array.
Recursive:
public class Solution {
    int count = 0;
    int result = Integer.MIN_VALUE;

    public int kthSmallest(TreeNode root, int k) {
        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode p = root;
        int cnt = 0;
        while(!stack.isEmpty() || p != null) {
            if (p != null) {
                stack.push(p);
                p = p.left;
            } else {
                TreeNode node = stack.pop();
                cnt++;
                if (cnt == k) return node.val;
                p = node.right;
            }
        }
        return -1;
    }

    public int kthSmallestDFS(TreeNode root, int k) {
        dfs(root, k);
        return result;
    }

    public void dfs(TreeNode root, int k) {
        if (root == null) return;
        dfs(root.left, k);
        count++;
        if (count == k) result = root.val;
        dfs(root.right, k);
    }
}
'''