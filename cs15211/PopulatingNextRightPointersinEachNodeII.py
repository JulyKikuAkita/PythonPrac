__source__ = 'https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/populating-next-right-pointers-in-each-node-ii.py
# Time:  O(n)
# Space: O(1)
# BFS
#
# Description: Leetcode # 117. Populating Next Right Pointers in Each Node II
#
# Follow up for problem "Populating Next Right Pointers in Each Node".
#
# What if the given tree could be any binary tree? Would your previous solution still work?
#
# Note:
#
# You may only use constant extra space.
# For example,
# Given the following binary tree,
#          1
#        /  \
#       2    3
#      / \    \
#     4   5    7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \    \
#     4-> 5 -> 7 -> NULL
#
# Companies
# Microsoft Bloomberg Facebook
# Related Topics
# Tree Depth-first Search
# Similar Questions
# Populating Next Right Pointers in Each Node
#
import unittest
# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
         self.next = None

     def __repr__(self):
         if self is None:
             return "Nil"
         else:
             return "{} -> {}".format(self.val, repr(self.next))
# 84ms 18.10%
class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        head = root
        while head:
            prev, cur, next_head = None, head, None
            while cur:
                if next_head is None:
                    if cur.left:
                        next_head= cur.left
                    elif cur.right:
                        next_head = cur.right

                if cur.left:
                    if prev:
                        prev.next = cur.left
                    prev = cur.left
                if cur.right:
                    if prev:
                        prev.next = cur.right
                    prev = cur.right

                cur = cur.next
            head = next_head

class SolutionOther:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        curr = root
        while curr:
            firstNodeInNextLevel = None
            prev = None
            while curr:
                if not firstNodeInNextLevel:
                    firstNodeInNextLevel = curr.left if curr.left else curr.right
                if curr.left:
                    if prev:
                        prev.next = curr.left
                    prev = curr.left
                if curr.right:
                    if prev:
                        prev.next = curr.right
                    prev = curr.right

                curr = curr.next

            curr = firstNodeInNextLevel

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        #create Tree
        root, root.left, root.right = TreeNode(1), TreeNode(2), TreeNode(3)
        root.left.left, root.left.right, root.right.right = TreeNode(4), TreeNode(5), TreeNode(7)
        #test
        test = SolutionOther()
        test.connect(root)
        Solution().connect(root)
        print root
        print root.left
        print root.left.left

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# 1ms 86.28%
class Solution {
    //hint to have pre point at root.left
    public void connect(TreeLinkNode root) {
        TreeLinkNode dummyHead = new TreeLinkNode(0);
        TreeLinkNode pre = dummyHead;
        while (root != null) {
            if (root.left != null) {
                pre.next = root.left;
                pre = pre.next;
            }
            if (root.right != null) {
                pre.next = root.right;
                pre = pre.next;
            }
            root = root.next;
            if (root == null) {
                pre = dummyHead;
                root = dummyHead.next;
                dummyHead.next = null;
            }
        }
    }
}

/**
 * Definition for binary tree with next pointer.
 * public class TreeLinkNode {
 *     int val;
 *     TreeLinkNode left, right, next;
 *     TreeLinkNode(int x) { val = x; }
 * }
 */
# 0ms 100%
class Solution {
    public void connect(TreeLinkNode root) {
        while(root != null){
            TreeLinkNode tempChild = new TreeLinkNode(0);
            TreeLinkNode currentChild = tempChild;
            while(root!=null){
                if(root.left != null) { currentChild.next = root.left; currentChild = currentChild.next;}
                if(root.right != null) { currentChild.next = root.right; currentChild = currentChild.next;}
                root = root.next;
            }
            root = tempChild.next;
        }
    }
}
'''