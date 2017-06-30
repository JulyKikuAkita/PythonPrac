__source__ = 'https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/populating-next-right-pointers-in-each-node-ii.py
# Time:  O(n)
# Space: O(1)
# BFS
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
#
# Topics:
# Tree Depth-first Search
# You might like:
# (M) Populating Next Right Pointers in Each Node
# Company:
# Microsoft Bloomberg Facebook

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

#create Tree
root, root.left, root.right = TreeNode(1), TreeNode(2), TreeNode(3)
root.left.left, root.left.right, root.right.right = TreeNode(4), TreeNode(5), TreeNode(7)

#test
test = SolutionOther()
test.connect(root)

if __name__ == "__main__":
    Solution().connect(root)
    print root
    print root.left
    print root.left.left

#java
java = '''
public class Solution {
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

public class Solution {
    public void connect(TreeLinkNode root) {
        if (root == null) {
            return;
        }
        TreeLinkNode leftMost = null;
        TreeLinkNode prev = null;
        while (root != null) {
            if (leftMost == null) {
                leftMost = root.left != null ? root.left : root.right;
            }
            if (root.left != null) {
                if (prev != null) {
                    prev.next = root.left;
                }
                prev = root.left;
            }
            if (root.right != null) {
                if (prev != null) {
                    prev.next = root.right;
                }
                prev = root.right;
            }
            if (root.next != null) {
                root = root.next;
            } else {
                root = leftMost;
                leftMost = null;
                prev = null;
            }
        }
    }
}
'''