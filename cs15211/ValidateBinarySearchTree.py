__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/validate-binary-search-tree.py
# Time:  O(n)
# Space: O(1)
# divide and conquer
#
# Given a binary tree, determine if it is a valid binary search tree (BST).
# Ex: {1, ,1}  ->False
# {1, #, 1} -> False
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
#
# Amazon Microsoft Bloomberg


# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

# Morris Traversal Solution
class Solution:
    # @param root, a tree node
    # @return a list of integers

    def isValidBST(self, root):
        cur, prev  = root, None
        while cur:
            if cur.left == None:
                if prev and cur and cur.val <= prev.val:
                    return False
                prev = cur
                cur = cur.right

            else:
                node = cur.left
                while node.right and node.right != cur:
                    node = node.right

                if node.right == None:
                    node.right = cur
                    cur = cur.left
                else:
                    if prev and cur and cur.val <= prev.val:
                        return False
                    node.right = None
                    prev = cur
                    cur = cur.right

        return True

# Time:  O(n)
# Space: O(logn)
class Solution2:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        return self.isValidBSTRecu(root, float("-inf"), float("inf"))

    def isValidBSTRecu(self, root, low, high):
        if root == None:
            return True
        if root.val <= low or root.val >= high:
            return False
        return  self.isValidBSTRecu(root.left, low, root.val) and self.isValidBSTRecu(root.right, root.val, high)

        #return low < root.val and root.val < high and \
        #       self.isValidBSTRecu(root.left, low, root.val) and self.isValidBSTRecu(root.right, root.val, high)



if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(20)
    root2 = TreeNode(1)
    root2.left = TreeNode(1)
    print Solution().isValidBST(root)
    print Solution2().isValidBST(root2)


class SolutionOther:
    # @param root, a tree node
    # @return a boolean
    val = None
    def isValidBST(self, root):
        if root is None:
            return True
        ans = self.isValidBST(root.left)
        print self.val, root.val, "ans left= ", ans
        if self.val is None:
            self.val = root.val
        else:
            ans = ans and (root.val > self.val)
            self.val = root.val

        ans = ans and self.isValidBST(root.right)
        #print self.val, root.val, "ans right= ", ans
        return ans
#test
#############test
#creating BST tree ####
root0=TreeNode(3)
tree1=TreeNode(1)
tree2=TreeNode(5)
tree3=TreeNode(0)
tree4=TreeNode(2)
tree5=TreeNode(4)
tree6=TreeNode(6)
root0.left=tree1
root0.right=tree2
tree1.left=tree3
tree1.right=tree4
tree2.left=tree5
tree2.right=tree6
#end of creating BST tree ####
test = SolutionOther()
#print test.isValidBST(root0)

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
    public boolean isValidBST(TreeNode root) {
        return isValidBST(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
    }

    private boolean isValidBST(TreeNode root, long min, long max) {
        return root == null ||
            (root.val >= min && root.val <= max &&
                isValidBST(root.left, min, (long) root.val - 1) && isValidBST(root.right, (long) root.val + 1, max));
    }
}
'''