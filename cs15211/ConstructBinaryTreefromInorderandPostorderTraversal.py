__source__ = 'https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/#/solutions'
# Time:  O(n)
# Space: O(n)
# divide and conquer
#
# Description: Leetcode # 106. Construct Binary Tree from Inorder and Postorder Traversal
#
# Given preorder and inorder traversal of a tree, construct the binary tree.
# root = preorder[0]
# root = inorder[mid]
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# Companies
# Microsoft
# Related Topics
# Tree Array Depth-first Search
# Similar Questions
# Construct Binary Tree from Inorder and Postorder Traversal
#
import unittest
# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        lookup = {}
        for i, num in enumerate(inorder):
            lookup[num] = i
        return self.buildTreeRecu(lookup, postorder, inorder, len(postorder), 0, len(inorder))

    def buildTreeRecu(self, lookup, postorder, inorder, post_end, in_start, in_end):
        #base case
        if in_start == in_end:
            return None
        node = TreeNode(postorder[post_end - 1])
        i = lookup[postorder[post_end - 1]]
        node.left = self.buildTreeRecu(lookup, postorder, inorder, post_end - 1 - (in_end - i - 1), in_start, i)
        node.right = self.buildTreeRecu(lookup, postorder, inorder, post_end  - 1, i  + 1, in_end )
        return node

#OT
class SolutionOther:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if len(inorder) == 0 :
            return None
        root = TreeNode(postorder[-1])
        rootPos = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[: rootPos], postorder[:rootPos])
        root.right = self.buildTree(inorder[rootPos+1:], postorder[rootPos:-1])
        return root

    def inorderTraversal1(self, root):
        ans = []
        p =root

        def inorder(p, ans):
            if p is None:
                return
            if p.left != None:
                inorder(p.left, ans)
            ans += [p.val]
            if p.right != None:
                inorder(p.right, ans)

        inorder(p,ans)
        return ans
#test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        preorder = [1, 2, 3]
        inorder = [2, 1, 3]
        result = Solution().buildTree(preorder, inorder)
        print result.val
        print result.left.val
        print result.right.val

        test = SolutionOther()
        newRoot = test.buildTree([-1], [-1])
        print test.inorderTraversal1(newRoot)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
1. DFS:
# 3ms 89.61%
public class Solution {
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        if (inorder == null || inorder.length != postorder.length) {
            return null;
        }
        Map<Integer, Integer> inorderMap = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) {
            inorderMap.put(inorder[i], i);
        }
        return dfs(inorder, postorder, 0, inorder.length - 1, 0, postorder.length - 1, inorderMap);
    }
    
    private TreeNode dfs(int[] inorder, int[] postorder, int inStart, int inEnd, int postStart, int postEnd, Map<Integer, Integer> inorderMap) {
        if (inStart > inEnd) return null;
        TreeNode root = new TreeNode(postorder[postEnd]);
        int inIdx = inorderMap.get(root.val);
        int leftNodeCount = inIdx - inStart; // same as inIdx of root
        root.left = dfs(inorder, postorder, inStart, inIdx - 1, postStart, postStart + leftNodeCount - 1, inorderMap);
        root.right = dfs(inorder, postorder, inIdx + 1, inEnd, postStart + leftNodeCount, postEnd - 1, inorderMap);
        return root;
    }
}


This is my iterative solution, think about "Constructing Binary Tree from inorder and preorder array", 
the idea is quite similar. Instead of scanning the preorder array from beginning to end and using 
inorder array as a kind of mark, in this question, the key point is to scanning the postorder array 
from end to beginning and also use inorder array from end to beginning as a mark because 
the logic is more clear in this way. 

The core idea is: Starting from the last element of the postorder and inorder array, 
we put elements from postorder array to a stack and each one is the right child of the last one until 
an element in postorder array is equal to the element on the inorder array. 
Then, we pop as many as elements we can from the stack and decrease the mark in inorder array 
until the peek() element is not equal to the mark value or the stack is empty. 
Then, the new element that we are gonna scan from postorder array is the left child of the last element 
we have popped out from the stack.

2. BFS:
# 3ms 89.16%
class Solution {
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        return bfs(inorder, postorder);
    }

    public TreeNode bfs(int[] inorder, int[] postorder) {
        if (inorder == null || inorder.length ==0 || inorder.length != postorder.length) {
            return null;
        }
        int inEndIdx = inorder.length - 1;
        int postEndIdx = postorder.length - 1;
        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode root = new TreeNode(postorder[postEndIdx]);
        TreeNode tmp = null;

        stack.push(root);
        postEndIdx--;
        while(postEndIdx >= 0) {
            while(!stack.isEmpty() && stack.peek().val == inorder[inEndIdx]) {
                tmp = stack.pop();
                inEndIdx --;
            }
            TreeNode node = new TreeNode(postorder[postEndIdx--]);
            if (tmp != null) {
                tmp.left = node;
            } else if (!stack.isEmpty()){
                stack.peek().right = node;
            }
            stack.push(node);
            tmp = null;
        }
        return root;
    }
}
'''