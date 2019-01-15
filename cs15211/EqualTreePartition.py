__source__ = 'https://leetcode.com/problems/equal-tree-partition/discuss/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 663. Equal Tree Partition
#
# Given a binary tree with n nodes,
# your task is to check if it's possible to partition the tree to two trees
# which have the equal sum of values after removing exactly one edge on the original tree.
#
# Example 1:
# Input:
#     5
#    / \
#   10 10
#     /  \
#    2   3
#
# Output: True
# Explanation:
#     5
#    /
#   10
#
# Sum: 15
#
#    10
#   /  \
#  2    3
#
# Sum: 15
# Example 2:
# Input:
#     1
#    / \
#   2  10
#     /  \
#    2   20
#
# Output: False
# Explanation: You can't split the tree into two trees with equal sum after removing exactly one edge on the tree.
# Note:
# The range of tree node value is in the range of [-100000, 100000].
# 1 <= n <= 10000
#
# Companies
# Amazon
# Related Topics
# Tree
#
import unittest


class Solution(object):
    pass  # your function here


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/equal-tree-partition/solution/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

# 7ms 98.08%
class class Solution {
    int judge=0;
    public boolean checkEqualTree(TreeNode root) {
        if(root==null)
            return false;
        int s=sum(root);
        if(s%2!=0)
            return false;
        check(root.left,s/2);
        check(root.right,s/2);
        if(judge==1)
            return true;
        return false;
    }
    private int sum(TreeNode root){
        if(root==null)
            return 0;
        return root.val+sum(root.left)+sum(root.right);
    }
    private int check(TreeNode root,int half){
        if(root==null)
            return 0;
        int s=root.val+check(root.left,half)+check(root.right,half);
        if(s==half)
            judge=1;
        return s;
    }
}

# hash map
# 14ms 31.49%
class Solution {
    public boolean checkEqualTree(TreeNode root) {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        int sum = getsum(root, map);
        if(sum == 0)return map.getOrDefault(sum, 0) > 1;
        return sum%2 == 0 && map.containsKey(sum/2);
    }

    public int getsum(TreeNode root, Map<Integer, Integer> map ){
        if(root == null)return 0;
        int cur = root.val + getsum(root.left, map) + getsum(root.right, map);
        map.put(cur, map.getOrDefault(cur,0) + 1);
        return cur;
    }
}
'''