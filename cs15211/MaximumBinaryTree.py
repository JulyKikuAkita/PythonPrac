__source__ = 'https://leetcode.com/problems/maximum-binary-tree/'
# Time:  O(n^2)
# Space: O(n)
#
# Description: Leetcode # 654. Maximum Binary Tree
#
# Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:
#
# The root is the maximum number in the array.
# The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
# The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
# Construct the maximum tree by the given array and output the root node of this tree.
#
# Example 1:
# Input: [3,2,1,6,0,5]
# Output: return the tree root node representing the following tree:
#
#       6
#     /   \
#    3     5
#     \    /
#      2  0
#        \
#         1
# Note:
# The size of the given array will be in the range [1,1000].
#
# Companies
# Microsoft
# Related Topics
# Tree
#
import unittest
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 128ms 67.74%
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        dummy = TreeNode(None)
        def d(root, nums):
            if not nums:
                return
            i = nums.index(max(nums))
            root.val = max(nums)
            if nums[:i]:
                root.left = TreeNode(None)
                d(root.left, nums[:i])
            if nums[i+1:]:
                root.right = TreeNode(None)
                d(root.right, nums[i+1:])
        d(dummy, nums)
        return dummy

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/maximum-binary-tree/solution/
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

Complexity Analysis

# Time complexity : O(n^2). T(n) = 2T(n /2)
# The function construct is called nn times. 
# At each level of the recursive tree, we traverse over all the nn elements to find the maximum element. 
# In the average case, there will be a log(n) levels leading to a complexity of O(nlog(n)). 
# In the worst case, the depth of the recursive tree can grow upto n, 
# which happens in the case of a sorted numsnums array, giving a complexity of O(n^2)
#
# Space complexity : O(n). The size of the setset can grow upto nn in the worst case. 
# In the average case, the size will be log(n) for n elements in numsnums, 
# giving an average case complexity of O(log(n))

# 9ms 57.26%
class Solution {
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        if (nums == null) return null;
        return build(nums, 0, nums.length - 1);
    }

    private TreeNode build(int[] nums, int start, int end) {
        if (start > end) return null;

        int idxMax = start;
        for (int i = start + 1; i <= end; i++) {
            if (nums[i] > nums[idxMax]) {
                idxMax = i;
            }
        }

        TreeNode root = new TreeNode(nums[idxMax]);
        root.left = build(nums, start, idxMax - 1);
        root.right = build(nums, idxMax + 1, end);
        return root;
    }
}
'''
