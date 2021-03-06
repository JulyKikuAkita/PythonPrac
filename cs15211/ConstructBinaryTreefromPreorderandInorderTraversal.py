__source__ = 'https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/construct-binary-tree-from-inorder-and-postorder-traversal.py
# Time:  O(n)
# Space: O(n)
# divide and conquer
#
# Description: Leetcode # 105. Construct Binary Tree from Preorder and Inorder Traversal
#
# Given inorder and postorder traversal of a tree, construct the binary tree.
# root = postorder[-1]
# root = inorder[mid index]

# Note:
# You may assume that duplicates do not exist in the tree.
#
# Companies
# Bloomberg
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
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        lookup = {}
        for i, num in enumerate(inorder):
            lookup[num] = i
        return self.buildTreeRecu(lookup, preorder, inorder, 0, 0, len(inorder))

    def buildTreeRecu(self, lookup, preorder, inorder, pre_start, in_start, in_end):
        # base case
        if in_start == in_end:
            return None
        node = TreeNode(preorder[pre_start])
        i = lookup[preorder[pre_start]]
        node.left = self.buildTreeRecu(lookup, preorder, inorder, pre_start + 1, in_start, i )
        node.right = self.buildTreeRecu(lookup, preorder, inorder, pre_start + 1 + (i - in_start), i + 1, in_end)
        return node

class SolutionOther:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    #http://jelices.blogspot.com/2014/05/leetcode-python-construct-binary-tree.html  explanation
    def buildTree(self, preorder, inorder):
        if len(inorder) == 0:
            return None
        root = TreeNode(preorder[0])
        rootPos = inorder.index(preorder[0]) # return the corresponding index of array given any value
        print inorder.index(-1)
        root.left = self.buildTree(preorder[1 : 1+rootPos], inorder[ : rootPos])
        root.right = self.buildTree(preorder[rootPos +1:], inorder[rootPos+1:])
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
        inorder = [2, 1, 3]
        postorder = [2, 3, 1]
        result = Solution().buildTree(inorder, postorder)
        print result.val
        print result.left.val
        print result.right.val

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solution/

In this questions, most of people just loop through inorder[] to find the root.
However, by caching positions of inorder[] indices using a HashMap, the run time can drop from 20ms to 5ms.
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

1. DFS
# 3ms 93.49%
class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (preorder.length != inorder.length) return null;
        Map<Integer, Integer> inMap = new HashMap<Integer, Integer>();

        for (int i = 0; i < inorder.length; i++) inMap.put(inorder[i], i);

        return buildTree(preorder, 0, preorder.length - 1, inorder, 0, inorder.length - 1, inMap);
    }

    public TreeNode buildTree(int[] preorder, int preStart, int preEnd, int[] inorder, int inStart, int inEnd, Map<Integer, Integer> inMap) {
        if(preStart > preEnd || inStart > inEnd) return null;
        TreeNode root = new TreeNode(preorder[preStart]);
        int inRoot = inMap.get(root.val);
        int numsLeft = inRoot - inStart;

        root.left = buildTree(preorder, preStart +1, preStart + numsLeft, inorder, inStart, inRoot - 1, inMap);
        root.right = buildTree(preorder, preStart + numsLeft + 1, preEnd, inorder, inRoot + 1, inEnd, inMap);
        return root;
    }
}


2. BFS
# 3ms 93.49%
class Solution {
     public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (preorder.length == 0 || inorder.length == 0) return null;
        Stack<TreeNode> s = new Stack<>();
        TreeNode root = new TreeNode(preorder[0]), tmp = root;
        int preStart = 0, inStart = 0;
        s.push(tmp);
        preStart++;
        int flag = 0;
        while (preStart < preorder.length) {
            if (!s.isEmpty() && s.peek().val == inorder[inStart]) { //reach left end
                tmp = s.pop();
                inStart++;
                flag = 1;
            } else {
                if (flag == 0) { //left subtree
                    tmp.left = new TreeNode(preorder[preStart]);
                    tmp = tmp.left;
                    s.push(tmp);
                    preStart++;
                } else { //right subtree
                    flag = 0;
                    tmp.right = new TreeNode(preorder[preStart]);
                    tmp = tmp.right;
                    s.push(tmp);
                    preStart++;
                }
            }
        }
        return root;
    }
}
'''
