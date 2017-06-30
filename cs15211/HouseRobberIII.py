__source__ = 'https://leetcode.com/problems/house-robber-iii/#/description'
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
# Companies
# Uber
# Related Topics
# Tree Depth-first Search
# Similar Questions
# House Robber House Robber II
#
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

#Java
Java = '''
Thought: https://discuss.leetcode.com/topic/39834/step-by-step-tackling-of-the-problem
why we have overlapping subproblems.
If you trace all the way back to the beginning, you'll find the answer lies in the way how we have defined rob(root).
As I mentioned, for each tree root, there are two scenarios: it is robbed or is not. rob(root)
does not distinguish between these two cases, so "information is lost as the recursion goes deeper and deeper",
which results in repeated subproblems.

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
# Naive 4.38%
public class Solution {
    public int rob(TreeNode root) {
        if (root == null) return 0;
        return Math.max(robInclude(root), robExclude(root));
    }

    public int robInclude(TreeNode node) {
        if (node == null) return 0;
        return node.val + robExclude(node.left) + robExclude(node.right);
    }

    public int robExclude(TreeNode node) {
        if (node == null) return 0;
        return rob(node.left) + rob(node.right);
    }
}

#Naive 13.41%
public class Solution {
    public int rob(TreeNode root) {
        return robSub(root);
    }

    private int robSub(TreeNode root) {
        if (root == null) return 0;

        int val = 0;

        if (root.left != null) {
            val += robSub(root.left.left) + robSub(root.left.right);
        }

        if (root.right != null) {
            val += robSub(root.right.left) + robSub(root.right.right);
        }

        val = Math.max(val + root.val, robSub(root.left) + robSub(root.right));
        return val;
    }
}

#DFS + memorization 37.2%
public class Solution {
    public int rob(TreeNode root) {
        return robSub(root, new HashMap<>());
    }

    private int robSub(TreeNode root, Map<TreeNode, Integer> map) {
        if (root == null) return 0;
        if (map.containsKey(root)) return map.get(root);

        int val = 0;

        if (root.left != null) {
            val += robSub(root.left.left, map) + robSub(root.left.right, map);
        }

        if (root.right != null) {
            val += robSub(root.right.left, map) + robSub(root.right.right, map);
        }

        val = Math.max(val + root.val, robSub(root.left, map) + robSub(root.right, map));
        map.put(root, val);

        return val;
    }
}

# 86%
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