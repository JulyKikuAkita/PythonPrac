__source__ = 'https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/'
# Time:  O(N)
# Space: O(N)
#
# Description: Leetcode # 889. Construct Binary Tree from Preorder and Postorder Traversal
#
# Return any binary tree that matches the given preorder and postorder traversals.
#
# Values in the traversals pre and post are distinct positive integers.
#
# Example 1:
#
# Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
# Output: [1,2,3,4,5,6,7]
#
#
# Note:
#
# 1 <= pre.length == post.length <= 30
# pre[] and post[] are both permutations of 1, 2, ..., pre.length.
# It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.
#
import unittest

from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#32ms 99.06%
class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        ##################### V3 ######################
        st, j = [TreeNode(pre[0])], 0
        for i in xrange(1, len(pre)):
            while st[-1].val == post[j]:
                st.pop()
                j += 1
            root, node = st[-1], TreeNode(pre[i])
            if root.left: root.right = node
            else: root.left = node
            st.append(node)
        return st[0]
        ##################### V2 ######################
        # st, j = [TreeNode(post[-1])], len(pre)-1
        # for i in xrange(len(post)-2, -1, -1):
        #     while st[-1].val == pre[j]:
        #         st.pop()
        #         j -= 1
        #     root, node = st[-1], TreeNode(post[i])
        #     root.left, root.right = node, root.left
        #     st.append(node)
        # return st[0]
        ##################### V1 ######################
        # st = [TreeNode(post.pop())]
        # while post:
        #     while st[-1].val == pre[-1]:
        #         st.pop()
        #         pre.pop()
        #     root, node = st[-1], TreeNode(post.pop())
        #     root.left, root.right = node, root.left
        #     st.append(node)
        # return st[0]
        ##################### V0 ######################
        # def dfs(x):
        #     node = TreeNode(x)
        #     while x != pre[-1]:
        #         node.left, node.right = dfs(post.pop()), node.left
        #     pre.pop()
        #     return node
        # return dfs(post.pop())

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/solution/
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/discuss/161372/Logical-Thinking-with-Code-Beats-99.89
# In post[], the rightmost element is the root of tree (equally, the leftmost element in pre[]).
#
#The element following the root in pre[] must be left child of the root.
# That is, 1 is root and 2 is its left child. Since 2 is the root of the left subtree,
# all elements in front of 2 in post[] must be in the left subtree also.
# Thus, preorder : 1 (2 4 5) (3 6); postorder: (4 5 2) (6 3) 1.
# We recursively follow the above approach.
# The key point is 1: preprocessing. 2: Find the correct index
#
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

#10ms 94.66%
class Solution {
    public TreeNode constructFromPrePost(int[] pre, int[] post) {
        return buildTree(pre, post, 0, post.length - 1, new int[]{0});
    }

    TreeNode buildTree(int[] pre, int[] post, int left, int right, int[] index) {

        if(left > right) return null;

        index[0]++;
        TreeNode root = new TreeNode(post[right]);
        if(left == right) return root;

        int i = left;
        while(i <= right && post[i] != pre[index[0]])
            i++;

        root.left = buildTree(pre, post, left, i, index);
        root.right = buildTree(pre, post, i + 1, right - 1, index);
        return root;
    }
}
'''