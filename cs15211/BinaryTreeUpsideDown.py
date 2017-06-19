__source__ = 'https://leetcode.com/problems/binary-tree-upside-down/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/binary-tree-upside-down.py
# Time:  O(n)
# Space: O(1)
#
# Given a binary tree where all the right nodes are either leaf nodes with a sibling
# (a left node that shares the same parent node) or empty, flip it upside down and
# turn it into a tree where the original right nodes turned into left leaf nodes.
# Return the new root.
#
# For example:
# Given a binary tree {1,2,3,4,5},
#
#     1
#    / \
#   2   3
#  / \
# 4   5
#
# return the root of the binary tree [4,5,2,#,#,3,1].
#
#    4
#   / \
#  5   2
#     / \
#    3   1
#
# Definition for a  binary tree node
# LinkedIn
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return root of the upside down tree
    def upsideDownBinaryTree(self, root):
        p, parent, parent_right = root, None, None
        while p:
            left = p.left
            p.left = parent_right
            parent_right = p.right
            p.right = parent
            parent = p
            p = left
        return parent

# Time:  O(n)
# Space: O(n)
class Solution2:
    # @param root, a tree node
    # @return root of the upside down tree
    def upsideDownBinaryTree(self, root):
        return self.upsideDownBinaryTreeRecu(root, None)

    def upsideDownBinaryTreeRecu(self, p, parent):
        if p is None:
            return parent
        root = self.upsideDownBinaryTreeRecu(p.left, p)
        if parent:
            p.left = parent.left
        else:
            p.left = None
        p.right = parent

        return root
    def preorderTraversal1(self, root):
        allnodes = []
        p =root

        def preorder(p, ans):
            if p is None:
                return
            ans.append(p.val)
            if p.left != None:
                preorder(p.left, ans)

            if p.right != None:
                preorder(p.right, ans)

        preorder(p,allnodes)
        return allnodes
#test
#############test
#creating BST tree ####
root0=TreeNode(0)
tree1=TreeNode(1)
tree2=TreeNode(2)
#tree3=TreeNode(3)
#tree4=TreeNode(4)
#tree5=TreeNode(5)
#tree6=TreeNode(6)
root0.left=tree1
root0.right=tree2
#tree1.left=tree3
#tree1.right=tree4
#tree2.left=tree5
#tree2.right=tree6
#end of creating BST tree ####
#test
if __name__ == "__main__":
    print  Solution().upsideDownBinaryTree(root0).val
    #ans = Solution2().upsideDownBinaryTree(root0)
    #print Solution2().preorderTraversal1(ans)

#Java
Java= '''
Thought: https://leetcode.com/problems/binary-tree-upside-down/#/solutions
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
 #BFS:
public class Solution {
    public TreeNode upsideDownBinaryTree(TreeNode root) {
        TreeNode cur = root;
        TreeNode parent = null;
        TreeNode right = null;

        while(cur != null){
            TreeNode left = cur.left;
            cur.left = right;
            right = cur.right;
            cur.right = parent;
            parent = cur;
            cur = left;
        }
        return parent;
    }

    public TreeNode upsideDownBinaryTree(TreeNode root) {
        TreeNode curr = root;
        TreeNode next = null;
        TreeNode temp = null;
        TreeNode prev = null;

        while(curr != null){
            next = curr.left;

            // swapping nodes now, need temp to keep the previous right child
            curr.left = temp;
            temp = curr.right;
            curr.right = prev;

            prev = curr;
            curr = next;
        }
       return prev;
    }
}
# DFS:
public class Solution {
    public TreeNode upsideDownBinaryTree1(TreeNode root) {
        if (root == null || root.left == null) {
            return root;
        }
        TreeNode left = root.left;
        TreeNode parent = upsideDownBinaryTree(root.left);
        left.left = root.right;
        left.right = root;
        root.left = null;
        root.right = null;
        return parent;
    }

    public TreeNode upsideDownBinaryTree2(TreeNode root) {
        if(root == null || root.left == null) {
            return root;
        }
        TreeNode newRoot = upsideDownBinaryTree(root.left);
        root.left.left = root.right; // node 2 left children
        root.left.right = root; // node 2 right children
        root.left = null;
        root.right = null;
        return newRoot;
    }
}
'''

