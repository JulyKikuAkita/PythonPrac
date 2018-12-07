__source__ = 'https://leetcode.com/problems/convert-bst-to-greater-tree/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 538. Convert BST to Greater Tree
#
# Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is
# changed to the original key plus sum of all keys greater than the original key in BST.
#
# Example:
#
# Input: The root of a Binary Search Tree like this:
#               5
#             /   \
#            2     13
#
# Output: The root of a Greater Tree like this:
#              18
#             /   \
#           20     13
# Hide Company Tags Amazon
# Hide Tags Tree
#
import unittest
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 92ms 22.08%
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def visit1(root):
            if root:
                visit1(root.left)
                vals.append(root.val)
                visit1(root.right)
        vals = []
        visit1(root)

        self.s = 0
        def visit2(root):
            if root:
                visit2(root.right)
                self.s += vals.pop()
                root.val = self.s
                visit2(root.left)
        visit2(root)
        return root

if __name__ == '__main__':
    # run all tests
    unittest.main()

    # run one test
    #unittest.main(defaultTest='FooTest.test_foo', warnings='ignore')

Java = '''
# Thought: https://leetcode.com/problems/convert-bst-to-greater-tree/solution/

Java Recursive O(n) time
Since this is a BST, we can do a reverse inorder traversal to traverse the nodes of the tree in descending order.
In the process, we keep track of the running sum of all nodes which we have traversed thus far.

# 8ms 83.65%
class Solution {
    int sum = 0;
    public TreeNode convertBST(TreeNode root) {
        convert(root);
        return root;
    }

    public void convert(TreeNode cur) {
        if (cur == null) return;
        convert(cur.right);
        cur.val += sum;
        sum = cur.val;
        convert(cur.left);
    }
}

# 10ms 59.92%
class Solution {
    int sum = 0;
    public TreeNode convertBST(TreeNode root) {
        inOrder(root);
        return root;
    }

    public void inOrder(TreeNode cur) {
        if (cur == null) return;
        inOrder(cur.right);
        cur.val += sum;
        sum = cur.val;
        inOrder(cur.left);
    }
}
'''