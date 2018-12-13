__source__ = 'https://leetcode.com/problems/flatten-binary-tree-to-linked-list/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/flatten-binary-tree-to-linked-list.py
# Time:  O(n)
# Space: O(h), h is height of binary tree
#
# Description: Leetcode # 114. Flatten Binary Tree to Linked List
#
# Given a binary tree, flatten it to a linked list in-place.
#
# For example,
# Given
#
#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# The flattened tree should look like:
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6
#
#
# Definition for a  binary tree node
# Related Topics
# Tree, Depth-first Search
# Companies
# Microsoft
#
import unittest
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        return self.flattenRecu(root, None)

    def flattenRecu(self, root, list_head):
        if root != None:
            list_head = self.flattenRecu(root.right, list_head)
            list_head = self.flattenRecu(root.left, list_head)
            root.right = list_head
            root.left = None
            return root
        else:
            return list_head

class Solution2:
    list_head = None
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if root != None:
            self.flatten(root.right)
            self.flatten(root.left)
            root.right = self.list_head
            root.left = None
            self.list_head = root
            return root

# http://www.cnblogs.com/zuoyuan/p/3721157.html
class SolutionOther:
    # @param root, a tree node
    # @return nothing, do it in place

    def flatten(self, root):
        if root == None:
            return root
        self.flatten(root.left)
        self.flatten(root.right)

        if root.left == None:
            return
        else:
            p = root.left
            while p.right != None:
                p = p.right

            p.right = root.right
            root.right =root.left
            root.left = None
        return

#test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        #creating BST tree ####
        root0=TreeNode(0)
        tree1=TreeNode(1)
        tree2=TreeNode(2)
        tree3=TreeNode(3)
        tree4=TreeNode(4)
        tree5=TreeNode(5)
        tree6=TreeNode(6)
        root0.left=tree1
        root0.right=tree2
        tree1.left=tree3
        tree1.right=tree4
        tree2.left=tree5
        tree2.right=tree6
        #end of creating BST tree ####
        #test
        test = SolutionOther()
        #test.flatten(root0)

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right = TreeNode(5)
        root.right.right = TreeNode(6)
        result = Solution().flatten(root)
        print result.val
        print result.right.val
        print result.right.right.val
        print result.right.right.right.val
        print result.right.right.right.right.val
        print result.right.right.right.right.right.val

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

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
    public void flatten(TreeNode root) {
        dfs_flatten(root, null);
    }

    # DFS
    # 10ms 45.14%
    private TreeNode dfs_flatten(TreeNode root, TreeNode prev) {
        if (root == null) {
            return prev;
        }
        prev = dfs_flatten(root.right, prev);
        prev = dfs_flatten(root.left, prev);
        root.right = prev;
        root.left = null;
        return root;
    }
    
    # BFS # morris traverse?
    # 7ms 90.99%
    private void bfs_flatten(TreeNode root) {
        TreeNode cur = root;
        while (cur != null) {
            if (cur.left != null) {
                //Find current node's prenode that links to current node's right subtree
                TreeNode pre = cur.left;
                while (pre.right != null) pre = pre.right;
                pre.right = cur.right;
                //Use current node's left subtree to replace its right subtree(original right 
                //subtree is already linked by current node's prenode
                cur.right = cur.left;
                cur.left = null;
            }
            cur = cur.right;
        }
    }
}

# BFS with stack
# 12ms 22.47%
class Solution {
   public void flatten(TreeNode root) {
        if (root == null) return;
        Stack<TreeNode> stk = new Stack<TreeNode>();
        stk.push(root);
        while (!stk.isEmpty()){
            TreeNode cur = stk.pop();
            if ( cur.right != null) stk.push(cur.right);
            if ( cur.left != null) stk.push(cur.left);
            if (!stk.isEmpty()) cur.right = stk.peek();
            cur.left = null; // dont forget this!!  // create loop
        }
    }
}

# 9ms 64.07%
class Solution {
    public void flatten(TreeNode root) {
        Stack<TreeNode> stack = new Stack<TreeNode>();
        pushStack(stack, root);

        TreeNode curr = null;
        TreeNode last = null;
        while(!stack.empty()) {
            curr = stack.pop();
            curr.left = null;
            curr.right = last;
            last = curr;
        }
    }

    private void pushStack(Stack<TreeNode> stack, TreeNode root) {
        if (root == null) {
            return;
        }
        stack.push(root);
        pushStack(stack, root.left);
        pushStack(stack, root.right);
    }
}
'''