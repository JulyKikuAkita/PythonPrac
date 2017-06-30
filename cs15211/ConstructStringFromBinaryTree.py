__source__ = 'https://leetcode.com/problems/construct-string-from-binary-tree/#/description'
# Time:  O(n)
# Space: O(n)
#
# Description:
# You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.
#
# The null node needs to be represented by empty parenthesis pair "()".
# And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping
# relationship between the string and the original binary tree.
#
# Example 1:
# Input: Binary tree: [1,2,3,4]
#        1
#      /   \
#     2     3
#    /
#   4
#
# Output: "1(2(4))(3)"
#
# Explanation: Originallay it needs to be "1(2(4)())(3()())",
# but you need to omit all the unnecessary empty parenthesis pairs.
# And it will be "1(2(4))(3)".
# Example 2:
# Input: Binary tree: [1,2,3,null,4]
#        1
#      /   \
#     2     3
#      \
#       4
#
# Output: "1(2()(4))(3)"
#
# Explanation: Almost the same as the first example,
# except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
# Hide Company Tags Amazon
# Hide Tags Tree String
# Hide Similar Problems (M) Construct Binary Tree from String

# Explanation:
# We do this recursively.
#
# If the tree is empty, we return an empty string.
# We record each child as '(' + (string of child) + ')'
# If there is a right child but no left child, we still need to record '()' instead of empty string.

import unittest

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ''
        left = '({})'.format(self.tree2str(t.left)) if (t.left or t.right) else ''
        right = '({})'.format(self.tree2str(t.right)) if t.right else ''
        return '{}{}{}'.format(t.val, left, right)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/articles/construct-string-from-binary-tree/
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
    public String tree2str(TreeNode t) {
        StringBuilder sb = new StringBuilder();
        helper(sb,t);
        return sb.toString();
    }
    public void helper(StringBuilder sb,TreeNode t){
        if(t!=null){
            sb.append(t.val);
            if(t.left!=null||t.right!=null){
                sb.append("(");
                helper(sb,t.left);
                sb.append(")");
                if(t.right!=null){
                    sb.append("(");
                helper(sb,t.right);
                sb.append(")");
                }
            }
        }
    }
}

Time complexity : O(n). n nodes are pushed and popped in a stack.
Space complexity : O(n). stack size can grow upto n.

public class Solution {
    public String tree2str(TreeNode t) {
        if ( t == null) return "";
        Stack<TreeNode> stack = new Stack<>();
        stack.push(t);
        Set<TreeNode> visited = new HashSet<>();
        StringBuilder sb = new StringBuilder();
        sb.append("");

        while (!stack.isEmpty()) {
            t = stack.peek();
            if (visited.contains(t)) {
                stack.pop();
                sb.append(")");
            } else {
                visited.add(t);
                sb.append("(").append(t.val);
                if (t.left == null && t.right != null) {
                    sb.append("()");
                }
                if (t.right != null) {
                    stack.push(t.right);
                }
                 if (t.left != null) {
                    stack.push(t.left);
                }
            }
        }
        return sb.toString().substring(1, sb.length() - 1);
    }
}
'''