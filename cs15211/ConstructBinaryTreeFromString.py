__source__ = 'https://leetcode.com/problems/construct-binary-tree-from-string/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 536. Construct Binary Tree from String
#
# You need to construct a binary tree from a string consisting of parenthesis and integers.
#
# The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis.
# The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.
#
# You always start to construct the left child node of the parent first if it exists.
#
# Example:
# Input: "4(2(3)(1))(6(5))"
# Output: return the tree root node representing the following tree:
#
#       4
#     /   \
#    2     6
#   / \   /
#  3   1 5
# Note:
# There will only be '(', ')', '-' and '0' ~ '9' in the input string.
# An empty tree is represented by "" instead of "()".
# Hide Company Tags Amazon
# Hide Tags Tree String
#
import unittest
#
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

# 120ms 72%
class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        def t(val, left=None, right=None):
            node, node.left, node.right = TreeNode(val), left, right
            return node
        return eval('t(' + s.replace('(', ',t(') + ')') if s else None

class FooTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setupDown(self):
        pass

    def tearDown(self):
        pass

    def test_foo(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    # run all tests
    unittest.main()

    # run one test
    #unittest.main(defaultTest='FooTest.test_foo', warnings='ignore')

Java = '''
# Thought:

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

Java stack solution
# 17ms 61.77%
class Solution {
    public TreeNode str2tree(String s) {
        Stack<TreeNode> stack = new Stack<>();
        for(int i = 0, j = i; i < s.length(); i++, j = i){
            char c = s.charAt(i);
            if(c == ')')    stack.pop();
            else if(c >= '0' && c <= '9' || c == '-'){
                while(i + 1 < s.length() && s.charAt(i + 1) >= '0' && s.charAt(i + 1) <= '9') i++;
                TreeNode currentNode = new TreeNode(Integer.valueOf(s.substring(j, i + 1)));
                if(!stack.isEmpty()){
                    TreeNode parent = stack.peek();
                    if(parent.left != null)    parent.right = currentNode;
                    else parent.left = currentNode;
                }
                stack.push(currentNode);
            }
        }
        return stack.isEmpty() ? null : stack.peek();
    }
}

# 24ms 41.52%
class Solution {
    public TreeNode str2tree(String s) {
        // Base case
        if (s.length() == 0) return null;

        // Create root
        int i = 0, j = 0;
        while (j < s.length() && (Character.isDigit(s.charAt(j)) || s.charAt(j) == '-')) j++;
        TreeNode root = new TreeNode(Integer.parseInt(s.substring(i, j)));

        // Left child
        if (j < s.length()) {
            i = j;
            int count = 1;
            while (j + 1 < s.length() && count != 0) {
                j++;
                if (s.charAt(j) == ')') count--;
                if (s.charAt(j) == '(') count++;
            }
            root.left = str2tree(s.substring(i + 1, j));
        }

        j++;
        // Right child
        if (j < s.length()) {
            root.right = str2tree(s.substring(j + 1, s.length() - 1));
        }

        return root;
    }
}
'''