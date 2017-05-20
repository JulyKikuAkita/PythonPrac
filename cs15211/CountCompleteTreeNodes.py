__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/count-complete-tree-nodes.py
# Time:  O(h * logn) = O((logn)^2)
# Space: O(1)

# Given a complete binary tree, count the number of nodes.
#
# In a complete binary tree every level, except possibly the last,
# is completely filled, and all nodes in the last level are as far
# left as possible. It can have between 1 and 2h nodes inclusive at
# the last level h.
#

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
java = '''
public class Solution {
    public int countNodes(TreeNode root) {
        if(root == null) return 0;
        int leftlevel = 0;
        int rightlevel = 0;

        TreeNode leftnode = root;
        TreeNode rightnode = root;

        while(leftnode != null){
            leftnode = leftnode.left;
            leftlevel++;
        }

        while(rightnode != null){
            rightnode = rightnode.right;
            rightlevel++;
        }

        if(leftlevel == rightlevel){
            return (1 << leftlevel) - 1;
        }else{
            return 1 + countNodes(root.left) + countNodes(root.right);
        }

    }
}
'''