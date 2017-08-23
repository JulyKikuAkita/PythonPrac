__source__ = 'https://leetcode.com/problems/maximum-width-of-binary-tree/description/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 662. Maximum Width of Binary Tree
#
# Given a binary tree, write a function to get the maximum width of the given tree.
# The width of a tree is the maximum width among all levels.
# The binary tree has the same structure as a full binary tree, but some nodes are null.
#
# The width of one level is defined as the length between the end-nodes
# (the leftmost and right most non-null nodes in the level,
# where the null nodes between the end-nodes are also counted into the length calculation.
#
# Example 1:
# Input:
#
#            1
#          /   \
#         3     2
#        / \     \
#       5   3     9
#
# Output: 4
# Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
# Example 2:
# Input:
#
#           1
#          /
#         3
#        / \
#       5   3
#
# Output: 2
# Explanation: The maximum width existing in the third level with the length 2 (5,3).
# Example 3:
# Input:
#
#           1
#          / \
#         3   2
#        /
#       5
#
# Output: 2
# Explanation: The maximum width existing in the second level with the length 2 (3,2).
# Example 4:
# Input:
#
#           1
#          / \
#         3   2
#        /     \
#       5       9
#      /         \
#     6           7
# Output: 8
# Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).
#
#
# Note: Answer will in the range of 32-bit signed integer.
# Companies
# Amazon
# Related Topics
# Tree

import unittest

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Thought:
# The main idea with this question is we will give each node a position value.
# If we go down the left neighbor, then position -> position * 2;
# and if we go down the right neighbor, then position -> position * 2 + 1.
# This makes it so that when we look at the position values L and R of two nodes with the same depth,
# the width will be R - L + 1.
#
# From there, we have two choices for traversals: BFS or DFS. In a BFS,
# all the nodes with the same depth are searched adjacent to each other,
# so we only need to remember the first and last positions seen for each depth.
#
#49ms
class SolutionBFS(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [(root, 0, 0)]
        cur_depth = left = ans = 0
        for node, depth, pos in queue:
            if node:
                queue.append((node.left, depth+1, pos*2))
                queue.append((node.right, depth+1, pos*2 + 1))
                if cur_depth != depth:
                    cur_depth = depth
                    left = pos
                ans = max(pos - left + 1, ans)

        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
Regardless whether these nodes exist:

Always make the id of left child as parent_id * 2;
Always make the id of right child as parent_id * 2 + 1;
So we can just:

Record the id of left most node at each level of the tree
(you can tell be check the size of the container to hold the first nodes);

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

#DFS
#35.39% 13ms
class Solution {
    public int widthOfBinaryTree(TreeNode root) {
        return dfs(root, 0, 1, new ArrayList<Integer>(), new ArrayList<Integer>());
    }
    public int dfs(TreeNode root, int level, int order, List<Integer> start, List<Integer> end){
        if(root == null)return 0;
        if(start.size() == level){
            start.add(order); end.add(order);
        }
        else end.set(level, order);
        int cur = end.get(level) - start.get(level) + 1;
        int left = dfs(root.left, level + 1, 2*order, start, end);
        int right = dfs(root.right, level + 1, 2*order + 1, start, end);
        return Math.max(cur, Math.max(left, right));
    }
}

#BFS:
#22.76% 15ms
import java.util.AbstractMap;
class Solution {
    public int widthOfBinaryTree(TreeNode root) {
        if (root == null) return 0;
        int max = 0;
        Queue<Map.Entry<TreeNode, Integer>> q = new LinkedList<Map.Entry<TreeNode, Integer>>();
        q.offer(new AbstractMap.SimpleEntry(root, 1));

        while (!q.isEmpty()) {
            int l = q.peek().getValue(), r = l; // right started same as left
            for (int i = 0, n = q.size(); i < n; i++) {
                TreeNode node = q.peek().getKey();
                r = q.poll().getValue();
                if (node.left != null) q.offer(new AbstractMap.SimpleEntry(node.left, r * 2));
                if (node.right != null) q.offer(new AbstractMap.SimpleEntry(node.right, r * 2 + 1));
            }
            max = Math.max(max, r + 1 - l);
        }
        return max;
    }
}

# Level order
#64.30% 11ms
class Solution {
    public int widthOfBinaryTree(TreeNode root) {
        if(root == null) return 0;
        ArrayDeque<TreeNode> queue = new ArrayDeque<>();
        ArrayDeque<Integer>  count = new ArrayDeque<>();
        queue.offer(root);
        count.offer(0);
        int max = 1;

        while(!queue.isEmpty()) {
            int size = queue.size();
            int left = 0;
            int right = 0;
            for(int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                int index = count.poll();
                if(i == 0)  left = index;
                if(i == size-1)  right = index;
                if(node.left != null) {
                    queue.offer(node.left);
                    count.offer(index*2);
                }
                if(node.right != null) {
                    queue.offer(node.right);
                    count.offer(index*2 + 1);
                }
            }
            max = Math.max(max,right - left + 1);
        }
        return max;
    }
}
'''