__source__ = 'https://leetcode.com/problems/smallest-string-starting-from-leaf/'
# Time:  O(NLogN)
# Space: O(N)
#
# Description: Leetcode # 988. Smallest String Starting From Leaf
#
# Given the root of a binary tree, each node has a value from 0 to 25 representing the letters 'a' to 'z':
# a value of 0 represents 'a', a value of 1 represents 'b', and so on.
#
# Find the lexicographically smallest string that starts at a leaf of this tree and ends at the root.
#
# (As a reminder, any shorter prefix of a string is lexicographically smaller:
# for example, "ab" is lexicographically smaller than "aba".  A leaf of a node is a node that has no children.)
#
# Example 1:
#
# Input: [0,1,2,3,4,3,4]
# Output: "dba"
# Example 2:
#
# Input: [25,1,3,1,3,0,2]
# Output: "adz"
# Example 3:
#
# Input: [2,2,1,null,1,0,null,0]
# Output: "abc"
#
# Note:
#
# The number of nodes in the given tree will be between 1 and 1000.
# Each node in the tree will have a value between 0 and 25.
import unittest

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 28ms 94.22%
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        self.ans = "~"

        def dfs(node, A):
            if node:
                A.append(chr(node.val + ord('a')))
                if not node.left and not node.right:
                    self.ans = min(self.ans, "".join(reversed(A)))

                dfs(node.left, A)
                dfs(node.right, A)
                A.pop()

        dfs(root, [])
        return self.ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/smallest-string-starting-from-leaf/solution/
# https://leetcode.com/problems/smallest-string-starting-from-leaf/discuss/231623/Java-Two-ways-postorder-preorder
# Approach 1: Brute Force
# Complexity Analysis
# Time Complexity: O(NlogN)
# We use O(N) to traverse the array and maintain A [Python] or sb. 
# Then, our reversal and comparison with the previous answer is O(L), 
# where L is the size of the string we have when at the leaf. 
# For example, for a perfectly balanced tree, L=logN and the time complexity would be O(NlogN).
# Space Complexity: O(N). 
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
# 4ms 62.04%
class Solution {
    String ans = "~";
    public String smallestFromLeaf(TreeNode root) {
        dfs(root, new StringBuilder());
        return ans;
    }

    public void dfs(TreeNode node, StringBuilder sb) {
        if (node == null) return;
        sb.append((char)('a' + node.val));

        if (node.left == null && node.right == null) {
            sb.reverse();
            String S = sb.toString();
            sb.reverse();

            if (S.compareTo(ans) < 0)
                ans = S;
        }

        dfs(node.left, sb);
        dfs(node.right, sb);
        sb.deleteCharAt(sb.length() - 1);
    }
}

# Post order
# 3ms 100%
class Solution {
    public String smallestFromLeaf(TreeNode root) {
        return helper(root);
    }

    public String helper(TreeNode root) {
        if (root != null) {
            String left = helper(root.left);
            String right = helper(root.right);
            if (left.length() > 0 && right.length() > 0) {
                return((left.compareTo(right) < 0 ? left: right) + (char)(root.val + 'a'));
            } else if (left.length() > 0) {
                return left + (char)(root.val + 'a');
            } else {
                return right + (char)(root.val + 'a');
            }
        }
        return "";
    }
}
'''
