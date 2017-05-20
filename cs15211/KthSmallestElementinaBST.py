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
#  Bloomberg Google



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


class Solution2(object):
    def kthSmallest(self, root, k):
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


public class Solution2 {
    public int kthSmallest(TreeNode root, int k) {
        int rank = 0;
        Stack<TreeNode> stack = new Stack<>();
        TreeNode cur = root;

        while(stack != null || cur != null){
            if (cur != null){
                stack.add(cur);
                cur = cur.left;
            }else{
                cur = stack.pop();
                rank++;
                if(rank == k){
                    return cur.val;
                }
                cur = cur.right;
            }
        }
        return -1;
    }
}
'''