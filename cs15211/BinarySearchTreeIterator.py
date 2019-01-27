__source__ = 'https://leetcode.com/problems/binary-search-tree-iterator/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/binary-search-tree-iterator.py
# Time:  O(1)
# Space: O(h), h is height of binary tree
#
# Description: Leetcode # 173. Binary Search Tree Iterator
#
# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
#
# Calling next() will return the next smallest number in the BST.
#
# Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
#
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.
#
# Companies
# LinkedIn Google Facebook Microsoft
# Related Topics
# Tree Stack Design
# Similar Questions
# Binary Tree Inorder Traversal Flatten 2D Vector Zigzag Iterator
# Peeking Iterator
# Inorder Successor in BST
#
# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
import unittest
# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.cur = root
        self.stack = []


    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.stack or self.cur
            #   return len(self.stack) == 0 will print the first element only


    # @return an integer, the next smallest number
    def next(self):
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left
        self.cur = self.stack.pop()
        node = self.cur
        self.cur = self.cur.right

        return node.val

#test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        root.left.left = TreeNode(0)

        # Your BSTIterator will be called like this:
        i, v = BSTIterator(root), []
        while i.hasNext(): v.append(i.next())

        print v

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

# 3ms 87.42%
public class BSTIterator {
    private Stack<TreeNode> stack;

    public BSTIterator(TreeNode root) {
        stack = new Stack<>();
        while (root != null) {
            stack.push(root);
            root = root.left;
        }
    }

    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return !stack.isEmpty();
    }

    /** @return the next smallest number */
    public int next() {
        TreeNode cur = stack.pop();
        int result = cur.val;
        cur = cur.right;
        while (cur != null) {
            stack.push(cur);
            cur = cur.left;
        }
        return result;
    }
}

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = new BSTIterator(root);
 * while (i.hasNext()) v[f()] = i.next();
 */

I use Stack to store directed left children from root.
When next() be called, I just pop one element and process its right child as new root.
The code is pretty straightforward.

So this can satisfy O(h) memory, hasNext() in O(1) time,
But next() is O(h) time.

I can't find a solution that can satisfy both next() in O(1) time, space in O(h).

# 3ms 87.42%
public class BSTIterator {
    private Stack<TreeNode> stack = new Stack<TreeNode>();

    public BSTIterator(TreeNode root) {
        pushAll(root);
    }

    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return !stack.isEmpty();
    }

    /** @return the next smallest number */
    public int next() {
        TreeNode tmpNode = stack.pop();
        pushAll(tmpNode.right);
        return tmpNode.val;
    }

    private void pushAll(TreeNode node) {
        for (; node != null; stack.push(node), node = node.left);
    }
}

'''
