__author__ = 'July'
# Time:  O(n)
# Space: O(h)
# https://github.com/kamyu104/LeetCode/blob/master/Python/house-robber-iii.py

# The thief has found himself a new place for his thievery again.
# There is only one entrance to this area, called the "root."
# Besides the root, each house has one and only one parent house.
# After a tour, the smart thief realized that "all houses in this
# place forms a binary tree". It will automatically contact the
# police if two directly-linked houses were broken into on the
# same night.
#
# Determine the maximum amount of money the thief can rob tonight
# without alerting the police.
#
# Example 1:
#      3
#     / \
#   2   3
#     \   \
#      3   1
# Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
# Example 2:
#      3
#     / \
#   4   5
#   / \   \
#  1   3   1
# Maximum amount of money the thief can rob = 4 + 5 = 9.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#  Uber
# Hide Tags Tree Depth-first Search


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def robHelper(root):
            if not root:
                return (0, 0)
            left, right = robHelper(root.left), robHelper(root.right)
            return (root.val + left[1] + right[1], max(left) + max(right))

        return max(robHelper(root))


# https://www.hrwhisper.me/leetcode-house-robber-iii/
# rob_root = max(rob_L + rob_R , no_rob_L + no_nob_R + root.val)
# no_rob_root = rob_L + rob_R
class Solution2(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root)[0]

    def dfs(self, root):
        if not root:
            return (0, 0)
        rob_L, no_rob_L = self.dfs(root.left)
        rob_R, no_rob_R = self.dfs(root.right)
        return max(rob_L + rob_R,  no_rob_L + no_rob_R + root.val) , rob_L + rob_R

#java
js = '''
Java

public class Solution {
    public int rob(TreeNode root) {
        return dfs(root)[0];
    }

    private int[] dfs(TreeNode root) {
        int dp[]={0,0};
        if(root != null){
            int[] dp_L = dfs(root.left);
            int[] dp_R = dfs(root.right);
            dp[1] = dp_L[0] + dp_R[0];
            dp[0] = Math.max(dp[1] ,dp_L[1] + dp_R[1] + root.val);
        }
        return dp;
    }
}

'''