__source__ = 'https://leetcode.com/problems/distribute-coins-in-binary-tree/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 979. Distribute Coins in Binary Tree
#
# Given the root of a binary tree with N nodes,
# each node in the tree has node.val coins,
# and there are N coins total.
#
# In one move, we may choose two adjacent nodes and move one coin from one node to another.
# (The move may be from parent to child, or from child to parent.)
#
# Return the number of moves required to make every node have exactly one coin.
#
# Example 1:
#
# Input: [3,0,0]
# Output: 2
# Example 2:
#
# Input: [0,3,0]
# Output: 3
# Example 3:
#
# Input: [1,0,2]
# Output: 2
# Example 4:
#
# Input: [1,0,0,null,3]
# Output: 4
#
# Note:
#
# 1<= N <= 100
# 0 <= node.val <= N
import unittest


class Solution(object):
    pass  # your function here


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/distribute-coins-in-binary-tree/solution/
Approach 1: Depth First Search 
Complexity Analysis
Time Complexity: O(N), where N is the number of nodes in the tree.
Space Complexity: O(H), where H is the height of the tree. 

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
# 5ms 100%
class Solution {
    int ans;
    public int distributeCoins(TreeNode root) {
        ans = 0;
        dfs(root);
        return ans;
    }
    
    public int dfs(TreeNode node) {
        if (node == null) return 0;
        int left = dfs(node.left);
        int right = dfs(node.right);
        ans += Math.abs(left) + Math.abs(right);
        return node.val + left + right - 1;
    }
}

# 5ms 100%
class Solution {
    public int distributeCoins(TreeNode root) {
        int[] result = helper(root);
        return result[1];
    }
    
    private int[] helper(TreeNode root) {
        int[] res = new int[2];
        if (root == null) return res;
        int[] left = helper(root.left);
        int[] right = helper(root.right);
        
        res[0] = (root.val - 1) + left[0] + right[0];
        res[1] = Math.abs(res[0]) + left[1] + right[1];
        return res;
    }
}
'''
