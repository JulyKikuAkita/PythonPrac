__source__ = 'https://leetcode.com/problems/minimum-absolute-difference-in-bst/'
# Time:  O()
# Space: O()
#
# Description: 530. Minimum Absolute Difference in BST
#
# Given a binary search tree with non-negative values,
# find the minimum absolute difference between values of any two nodes.
#
# Example:
#
# Input:
#
#    1
#     \
#      3
#     /
#    2
#
# Output:
# 1
#
# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
# Note: There are at least two nodes in this BST.
#
# Hide Company Tags Google
# Hide Tags Binary Search Tree
# Hide Similar Problems (E) K-diff Pairs in an Array
#
import unittest
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 48ms 97.41%
class Solution(object):
    def getMinimumDifference(self, root):
        if not root:
            return 0
        res=[]
        def innerOrder(node):
            if node:
                innerOrder(node.left)
                res.append(node.val)
                innerOrder(node.right)
        innerOrder(root)

        minnum=min([res[i]-res[i-1] for i in range(1,len(res))])
        return minnum

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: 
https://discuss.leetcode.com/topic/80823/two-solutions-in-order-traversal-and-a-more-general-way-using-treeset
The most common idea is to first inOrder traverse the tree and compare the delta between each of the adjacent values.
It's guaranteed to have the correct answer because it is a BST thus inOrder traversal values are sorted.

Solution 1 - In-Order traverse, time complexity O(N), space complexity O(1).
# 10ms 53.03%
class Solution {
    int min = Integer.MAX_VALUE;
    Integer prev = null;

    public int getMinimumDifference(TreeNode root) {
        if (root == null) return min;
        getMinimumDifference(root.left);
        if (prev != null) {
            min = Math.min(min, root.val - prev);
        }
        prev = root.val;
        getMinimumDifference(root.right);
        return min;
    }
}

What if it is not a BST? (Follow up of the problem) The idea is to put values in a TreeSet
and then every time we can use O(lgN) time to lookup for the nearest values.

Solution 2 - Pre-Order traverse, time complexity O(NlgN), space complexity O(N).
# 27ms 6.37%
class Solution {
    TreeSet<Integer> set = new TreeSet<>();
    int min = Integer.MAX_VALUE;

    public int getMinimumDifference(TreeNode root) {
        if (root == null) return min;

        if (!set.isEmpty()) {
            if (set.floor(root.val) != null) {
                min = Math.min(min, root.val - set.floor(root.val));
            }
            if (set.ceiling(root.val) != null) {
                min = Math.min(min, set.ceiling(root.val) - root.val);
            }
        }

        set.add(root.val);
        getMinimumDifference(root.left);
        getMinimumDifference(root.right);
        return min;
    }
}

'''
