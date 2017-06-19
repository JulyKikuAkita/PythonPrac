__source__ = 'https://leetcode.com/problems/same-tree/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/same-tree.py
# Time:  O(n)
# Space: O(h), h is height of binary tree
# divide and conquer
#
# Given two binary trees, write a function to check if they are equal or not.
#
# Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
#Topics:
# Tree Depth-first Search
# Company:
# Bloomberg
#

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        if p != None and q != None:
            return ( p.val == q.val ) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False

if __name__ == "__main__":
    root1, root1.left, root1.left.left = TreeNode(1), TreeNode(2), TreeNode(3)
    root2, root2.left, root2.right = TreeNode(1), TreeNode(2), TreeNode(3)
    print Solution().isSameTree(root1, root2)

#Java
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
public class Solution {
    //DFS
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null  && q == null) return true;
        if (p == null || q == null || p.val != q.val) return false;
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}
'''