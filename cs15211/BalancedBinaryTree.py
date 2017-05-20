__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/balanced-binary-tree.py
# Time:  O(n)
# Space: O(h), h is height of binary tree
# divide and conquer
#
# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more than 1.
#

# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        return (self.getHeight(root) >= 0)

    def getHeight(self, root):
        if root is None:
            return 0
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)

        if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1

#http://www.programcreek.com/2013/02/leetcode-balanced-binary-tree-java/
class javaSolution:
        # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if not root:
            return None
        if self.getHeight(root) == -1:
            return False
        return True

    def getHeight(self, root):
        if not root:
            return 0
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)

        if left == -1 or right == -1:
            return -1

        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1

class SolutionOther:
    # @param root, a tree node
    # @return a boolean
    # http://www.cnblogs.com/zuoyuan/p/3720169.html
    def isBalanced(self, root):
        if root == None:
            return True
        if abs(self.Height(root.left) - self.Height(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False

    def Height(self, root) :
        if root == None:
            return 0
        return max(self.Height(root.left), self.Height(root.right)) +1

#############test
#creating BST tree ####
root0=TreeNode(0)
tree1=TreeNode(1)
tree2=TreeNode(2)
tree3=TreeNode(3)
tree4=TreeNode(4)
tree5=TreeNode(5)
tree6=TreeNode(6)
root0.left=tree1
#root0.right=tree2
tree1.left=tree3
tree1.right=tree4
tree2.left=tree5
#tree2.right=tree6
#end of creating BST tree ####
#test
test = SolutionOther()
print test.isBalanced(root0)
#print test.isBalanced3(root0)
#print test.isBalanced2(root0)


if __name__ == "__main__":
    root = TreeNode(0)
    root.left = TreeNode(1)
    result = Solution().isBalanced(root)
    print result

    root.left.left = TreeNode(2)
    result = javaSolution().isBalanced(root)
    print result