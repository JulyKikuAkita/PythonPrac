# coding=utf-8
__source__ = 'https://leetcode.com/problems/delete-node-in-a-bst/#/description'
# Time:  O()
# Space: O()
#
# Description: 450. Delete Node in a BST
#
# Given a root node reference of a BST and a key,
# delete the node with the given key in the BST.
# Return the root node reference (possibly updated) of the BST.
#
# Basically, the deletion can be divided into two stages:
#
# Search for a node to remove.
# If the node is found, delete the node.
# Note: Time complexity should be O(height of tree).
#
# Example:
#
# root = [5,3,6,2,4,null,7]
# key = 3
#
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Given key to delete is 3. So we find the node with value 3 and delete it.
#
# One valid answer is [5,4,6,2,null,null,7], shown in the following BST.
#
#     5
#    / \
#   4   6
#  /     \
# 2       7
#
# Another valid answer is [5,2,6,null,4,null,7].
#
#     5
#    / \
#   2   6
#    \   \
#     4   7
# Hide Company Tags Uber
# Hide Tags Tree

import unittest

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        pass
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

Steps:

Recursively find the node that has the same value as the key,
while setting the left/right nodes equal to the returned subtree
Once the node is found, have to handle the below 4 cases
node doesn't have left or right - return null
node only has left subtree- return the left subtree
node only has right subtree- return the right subtree
node has both left and right - find the minimum value in the right subtree,
set that value to the currently found node,
then recursively delete the minimum value in the right subtree

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

# 3ms 100%
class Solution {
    public TreeNode deleteNode(TreeNode root, int key) {
        TreeNode target = root, parent = null;
        while (target != null && target.val != key) {
            parent = target;
            if (key > target.val) target = target.right;
            else target = target.left;
        }
        if (target == null) return root;  // not found
        if (target.right == null) {  // no right subtree
            if (parent == null) return target.left;
            if (target == parent.left) parent.left = target.left;
            else parent.right = target.left;
            return root;
        }
        // with right subtree
        TreeNode prev = target, p = target.right;
        while (p.left != null) {
            prev = p;
            p = p.left;
        }
        target.val = p.val;
        if (p == prev.left) prev.left = p.right;
        else prev.right = p.right;
        return root;
    }
}


# 4ms 66.98%
class Solution {
    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) return null;

        if (key < root.val) {
            root.left = deleteNode(root.left, key);
        }else if ( key > root.val) {
            root.right = deleteNode(root.right, key);
        } else {
            if (root.left == null) {
                return root.right;
            } else if (root.right == null) {
                return root.left;
            }
            TreeNode minNode = findMin(root.right);
            root.val = minNode.val;
            root.right = deleteNode(root.right, root.val);
        }
        return root;
    }

    private TreeNode findMin(TreeNode node) {
        while( node.left != null) {
            node = node.left;
        }
        return node;
    }
}

# 5ms 26.58%
class Solution {
    public TreeNode deleteNode(TreeNode root, int key) {
        if(root==null) return null;
        if(root.val > key){
            root.left = deleteNode(root.left, key);
        }else if(root.val < key){
            root.right = deleteNode(root.right, key);
        }else{
            if(root.left==null) return root.right;
            if(root.right==null) return root.left;
            //如果左右都不是null,要从右边的subtree里面找最小的
            //要不就从左边的subtree里面找最大的
           /* int min = findMin(root.right);
            root.val = min;
            root.right = deleteNode(root.right, min);*/
            int max = findMax(root.left);
            root.val = max;
            root.left = deleteNode(root.left, max);
        }
        return root;
    }

    public int findMax(TreeNode root){
        TreeNode temp = root;
        while(temp.right!=null){
            temp = temp.right;
        }

        return temp.val;
    }

    public int findMin(TreeNode root){
        TreeNode temp = root;
        while(temp.left!=null){
            temp = temp.left;
        }

        return temp.val;
    }
}


'''