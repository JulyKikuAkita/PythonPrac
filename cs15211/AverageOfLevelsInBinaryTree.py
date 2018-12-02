__source__ = 'https://leetcode.com/problems/average-of-levels-in-binary-tree/description/'
# Time:  O(N)
# Space: O(M) M refers to the maximum mumber of nodes at any level in the input tree.
#
# Description: Leetcode # 637. Average of Levels in Binary Tree
#
# Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
#
# Example 1:
# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
# Note:
# The range of node's value is in the range of 32-bit signed integer.
# Companies
# Facebook
# Related Topics
# Tree
# Similar Questions
# Binary Tree Level Order Traversal Binary Tree Level Order Traversal II
#
import unittest
# 89ms
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        info = []
        def dfs(node, depth = 0):
            if node:
                if len(info) <= depth:
                    info.append([0, 0])
                info[depth][0] += node.val
                info[depth][1] += 1
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)
        dfs(root)

        return [s/float(c) for s, c in info]
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/average-of-levels-in-binary-tree/solution/
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

#BFS
# 92.06%  9ms
class Solution {
    public List<Double> averageOfLevels(TreeNode root) {
        List<Double> res = new ArrayList<>();
        if (root == null) return res;
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);

        while(!q.isEmpty()) {
            int size = q.size();
            double sum = 0.0;
            for (int i = 0; i < size; i++) {
                TreeNode cur = q.poll();
                sum += cur.val;
                if (cur.left != null) q.add(cur.left);
                if (cur.right != null) q.add(cur.right);
            }
            res.add(sum / size);
        }
        return res;
    }
}

# DFS
# 15.17% 14ms
class Solution {
    public List<Double> averageOfLevels(TreeNode root) {
        List<Double> res = new ArrayList<>();
        if (root == null) return res;
        List<Node> levels = new LinkedList<>();
        dfs(root, levels, 0);
        for (Node level : levels) {
            res.add( level.mSum / level.mCount);
        }
        return res;
    }

    public void dfs(TreeNode root, List<Node> sum, int depth) { //note unable to save (sum .count) to  List<int[]>
        if (root == null ) return;
        if (sum.size() == depth) {
            sum.add(new Node());
        }
        sum.get(depth).mSum += root.val * 1.0;
        sum.get(depth).mCount ++;

        dfs(root.left, sum, depth+1);
        dfs(root.right, sum, depth+1);
    }

    class Node{
        double mSum;
        int mCount;
        public Node() {
            mSum = 0;
            mCount = 0;
        }
    }
}

# 69.79% 10ms
class Solution {
    public List < Double > averageOfLevels(TreeNode root) {
        List < Integer > count = new ArrayList < > ();
        List < Double > res = new ArrayList < > ();
        average(root, 0, res, count);
        for (int i = 0; i < res.size(); i++)
            res.set(i, res.get(i) / count.get(i));
        return res;
    }
    public void average(TreeNode t, int i, List < Double > sum, List < Integer > count) {
        if (t == null)
            return;
        if (i < sum.size()) {
            sum.set(i, sum.get(i) + t.val);
            count.set(i, count.get(i) + 1);
        } else {
            sum.add(1.0 * t.val);
            count.add(1);
        }
        average(t.left, i + 1, sum, count);
        average(t.right, i + 1, sum, count);
    }
}
'''