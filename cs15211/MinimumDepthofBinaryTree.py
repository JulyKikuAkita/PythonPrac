__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/minimum-depth-of-binary-tree.py
# Time:  O(n)
# Space: O(h), h is height of binary tree
# divide and conquer
#
# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
#

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root == None:
            return 0
        if root.left == None:
            return self.minDepth(root.right) + 1
        if root.right == None:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


class Solution2:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root == None:
            return 0
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1

# http://www.programcreek.com/2013/02/leetcode-minimum-depth-of-binary-tree-java/
class javaSolution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if not root:
            return 0
        nodes = [(root, 1)]
        while nodes:
            (cur, count) = nodes.pop()
            if cur.left != None:
                nodes.insert(0, (cur.left, count + 1))
            if cur.right != None:
                nodes.insert(0, (cur.right, count + 1))
            if cur.left == None and cur.right == None:
                return count
        return 0

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    print Solution().minDepth(root)  # answer = 2
    print Solution2().minDepth(root)  # answer = 2
    print javaSolution().minDepth(root)

class SolutionOther:
    # @param root, a tree node
    # @return an integer

    def minDepth(self, root):
        if root is None:
            return 0
        elif (not root.left) and not (root.right):
            return 1
        elif not root.left:
            return 1 + self.minDepth(root.right)
        elif not root.right:
            return 1 + self.minDepth(root.left)
        else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

#test
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
root0.right=tree2
tree1.left=tree3
tree1.right=tree4
tree2.left=tree5
tree2.right=tree6
#end of creating BST tree ####
test = SolutionOther()
#print test.minDepth(root0)