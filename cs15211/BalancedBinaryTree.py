__source__ = 'https://leetcode.com/problems/balanced-binary-tree/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/balanced-binary-tree.py
# Time:  O(n)
# Space: O(h), h is height of binary tree
# divide and conquer
#
# Description: Leetcode # 110. Balanced Binary Tree
#
# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more than 1.
#
# Companies
# Bloomberg
# Related Topics
# Tree Depth-first Search
# Similar Questions
# Maximum Depth of Binary Tree
#
import unittest
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

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        root = TreeNode(0)
        root.left = TreeNode(1)
        result = Solution().isBalanced(root)
        print result

        root.left.left = TreeNode(2)
        result = javaSolution().isBalanced(root)
        print result

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/contains-duplicate/solution/


Thought:  This problem is generally believed to have two solutions:
the top down approach and the bottom up way.

DFS 1) The first method checks whether the tree is balanced strictly according to the definition
of balanced binary tree: the difference between the heights of the two sub trees are not bigger than 1,
and both the left sub tree and right sub tree are also balanced. With the helper function depth(),
we could easily write the code;
For the current node root, calling depth() for its left and right children actually has to access all of its children,
thus the complexity is O(N). We do this for each node in the tree,
so the overall complexity of isBalanced will be O(N^2). This is a top down approach.

DFS 2)The second method is based on DFS. Instead of calling depth() explicitly for each child node,
we return the height of the current node in DFS recursion.
When the sub tree of the current node (inclusive) is balanced, the function dfsHeight()
returns a non-negative value as the height.
Otherwise -1 is returned. According to the leftHeight and rightHeight of the two children,
the parent node could check if the sub tree is balanced, and decides its return value.

# DFS
# 87.89% 1ms
class Solution {
    public boolean isBalanced(TreeNode root) {
        return dfsHeight(root) != -1;
    }
    
    public int dfsHeight(TreeNode root) {
        if (root == null) return 0;
        int left = dfsHeight(root.left);
        int right = dfsHeight(root.right);
        if (left == -1 || right == -1 || Math.abs(left - right) > 1) return -1;
        return Math.max(left, right) + 1;
    }
}

# DFS
# 87.89% 1ms
class Solution {
    public boolean isBalanced(TreeNode root) {
        if (root == null) return true;
        int left = getDpeth(root.left);
        int right = getDpeth(root.right);
        return Math.abs(left - right) <= 1 && isBalanced(root.left) && isBalanced(root.right);
    }

    public int getDpeth(TreeNode root) {
        if (root == null) return 0;
        return Math.max(getDpeth(root.left), getDpeth(root.right)) + 1;
    }
}
'''
