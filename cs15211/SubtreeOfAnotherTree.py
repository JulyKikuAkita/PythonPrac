__source__ = 'https://leetcode.com/problems/subtree-of-another-tree/'
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 572. Subtree of Another Tree
#
# Given two non-empty binary trees s and t,
# check whether tree t has exactly the same structure and node values with a subtree of s.
# A subtree of s is a tree consists of a node in s and all of this node's descendants.
# The tree s could also be considered as a subtree of itself.
#
# Example 1:
# Given tree s:
# example = '''
#       3
#     / \
#    4   5
#   / \
#  1   2
# Given tree t:
#    4
#   / \
#  1   2
# Return true, because t has the same structure and node values with a subtree of s.
# Example 2:
# Given tree s:
#
#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
# Given tree t:
#    4
#   / \
#  1   2
# Return false.
# Hide Company Tags Facebook eBay
# Hide Tags Tree
# Hide Similar Problems (M) Count Univalue Subtrees (M) Most Frequent Subtree Sum

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import unittest
# 96ms 88.74%
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def convert(p):
            return "^" + str(p.val) + "#" + convert(p.left) + convert(p.right) if p else "$"
        return convert(t) in convert(s)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/subtree-of-another-tree/solution/

# 24ms 20.16%
class Solution {
    public boolean isSubtree(TreeNode s, TreeNode t) {
        String sPre = getPreorderString(s);
        String tPre = getPreorderString(t);
        return sPre.contains(tPre);
    }
    
    public String getPreorderString(TreeNode s) {
        StringBuilder sb = new StringBuilder();
        Stack<TreeNode> stacktree = new Stack();
        stacktree.push(s);
        while(!stacktree.isEmpty()) {
            TreeNode elem = stacktree.pop();
            if(elem == null) {
                sb.append(",#");
            }else {
                sb.append("," + elem.val);
                stacktree.push(elem.right);
                stacktree.push(elem.left);
            }
        }
        return sb.toString();
    }
}


# 12ms 91.09%
class Solution {
    public boolean isSubtree(TreeNode s, TreeNode t) {
        if (s == null) return false;
        if (isSame(s, t)) return true;
        return isSubtree(s.left, t) || isSubtree(s.right, t);
    }

    private boolean isSame(TreeNode s, TreeNode t) {
        if (s == null && t == null) return true;
        if (s == null || t == null) return false;

        if (s.val != t.val) return false;
        return isSame(s.left, t.left) && isSame(s.right, t.right);
    }
}
'''
