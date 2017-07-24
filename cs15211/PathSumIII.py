__source__ = 'https://github.com/kamyu104/LeetCode/blob/master/Python/path-sum-iii.py'
# Time:  O(n^2)
# Space: O(h)
#
# Description:
# You are given a binary tree in which each node contains an integer value.
#
# Find the number of paths that sum to a given value.
#
# The path does not need to start or end at the root or a leaf,
# but it must go downwards (traveling only from parent nodes to child nodes).
#
# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
#
# Example:
#
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#
#       10
#      /  \
#     5   -3
#   / \    \
#   3   2   11
#  / \   \
# 3  -2   1
#
# Return 3. The paths that sum to 8 are:
#
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11
# Related Topics
# Tree
# Similar Questions
# Path Sum Path Sum II

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import unittest

# https://leetcode.com/problems/path-sum-iii/#/solutions
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def pathSumHelper(root, prev, sum):
            if not root:
                return 0

            curr = prev + root.val;
            return int(curr == sum) + \
                   pathSumHelper(root.left, curr, sum) + \
                   pathSumHelper(root.right, curr, sum)

        if not root:
            return 0

        return pathSumHelper(root, 0, sum) + \
               self.pathSum(root.left, sum) + \
               self.pathSum(root.right, sum)

# Brute Force Solution
#
# The simplest solution is to traverse each node (preorder traversal) and
# then find all paths which sum to the target using this node as root.
# The worst case complexity for this method is N^2.
# If we have a balanced tree, we have the recurrence: T(N) = N + 2T(N/2). T
# his is the merge sort recurrence and suggests NlgN.

class SolutionBruteForce(object):
    def find_paths(self, root, target):
        if root:
            return int(root.val == target) + self.find_paths(root.left, target-root.val) + self.find_paths(root.right, target-root.val)
        return 0

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root:
            return self.find_paths(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        return 0


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
Typical recursive DFS.
Space: O(n) due to recursion.
Time: O(n^2) in worst case (no branching); O(nlogn) in best case (balanced tree).

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
    public int pathSum(TreeNode root, int sum) {
        if (root == null) return 0;
        return dfs(root, sum) //path sum from root
        + pathSum(root.left, sum)
        + pathSum(root.right, sum);
    }

    private int dfs(TreeNode node, int sum) {
        if (node == null) return 0;
        return (node.val == sum ? 1 : 0)
        + dfs(node.left, sum - node.val)
        + dfs(node.right, sum - node.val);
    }
}
O(n)
#Thought: So the idea is similar as Two sum, using HashMap to store
( key : the prefix sum, value : how many ways get to this prefix sum) ,
and whenever reach a node, we check if prefix sum - target exists in hashmap or not,
if it does, we added up the ways of prefix sum - target into res.
For instance : in one path we have 1,2,-1,-1,2, then the prefix sum will be: 1, 3, 2, 1, 3,
let's say we want to find target sum is 2, then we will have{2}, {1,2,-1}, {2,-1,-1,2} and {2}ways.

public class Solution {
    public int pathSum(TreeNode root, int sum) {
        HashMap<Integer, Integer> preSum = new HashMap<>();
        preSum.put(0, 1);
        return dfs(root, 0, sum, preSum);
    }

    private int dfs(TreeNode root, int curSum, int target, HashMap<Integer, Integer> preSum) {
        if (root == null) return 0;

        curSum += root.val;
        int res = preSum.getOrDefault(curSum - target , 0);
        preSum.put(curSum, preSum.getOrDefault(curSum, 0) + 1);

        res += dfs(root.left, curSum, target, preSum) + dfs(root.right, curSum, target, preSum);
        preSum.put(curSum, preSum.get(curSum) - 1);
        return res;
    }
}

'''