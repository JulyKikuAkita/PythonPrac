__source__ = 'https://leetcode.com/problems/zigzag-conversion/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/binary-tree-zigzag-level-order-traversal.py
# Time:  O(n)
# Space: O(n)
# BFS
#
# Description: Leetcode # 103. Binary Tree Zigzag Level Order Traversal
#
# Given a binary tree, return the zigzag level order traversal of its nodes' values.
# (ie, from left to right, then right to left for the next level and alternate between).
#
# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]
#
# Companies
# LinkedIn Bloomberg Microsoft
# Related Topics
# Tree Breadth-first Search Stack
# Similar Questions
# Binary Tree Level Order Traversal
#
import unittest
# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if root == None:
            return []
        result, cur, level = [], [root],1

        while cur:
            next_level, vals = [], []
            for node in cur:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if level % 2 == 0:
                result.append(vals[::-1])  # syntax: [ <first element to include> : <first element to exclude> : <step> ]
                #print level, vals
            else:
                result.append(vals)
            level += 1
            cur = next_level
        return result

#don't like this
class SolutionOther:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        res = []
        if root == None:
            return res
        SolutionOther.L = {}
        self.dfs(root, 0)

        for i in sorted(SolutionOther.L.keys()):
            if i % 2 == 0:
                res.append(SolutionOther.L[i])
            else:
                res.append(SolutionOther.L[i][::-1])
        return res

    def dfs(self, root, level):
        if level not in SolutionOther.L:
            SolutionOther.L[level] = [root.val]
        else:
            SolutionOther.L[level].append(root.val)

        if root.left:
            self.dfs(root.left, level+1)
        if root.right:
            self.dfs(root.right, level +1)

#test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        root = TreeNode(3)
        root.left = TreeNode(4)
        root.right = TreeNode(5)
        root.right.left = TreeNode(-7)
        root.right.right = TreeNode(-6)
        root.right.left.left = TreeNode(-7)
        root.right.right.left = TreeNode(-5)
        root.right.left.left.left = TreeNode(-4)
        result = Solution().zigzagLevelOrder(root)
        #result2 = SolutionFail().zigzagLevelOrder(root)
        print result
        #print result2

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/contains-duplicate/solution/
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
 #BFS 31.75% 2ms
public class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
         List<List<Integer>> res = new ArrayList<>();
         if ( root == null) return res;
         Queue<TreeNode> q = new LinkedList<>();
         q.offer(root);
         boolean fromRight = false;
         while (!q.isEmpty()) {
             int len = q.size();
             List<Integer> tmp = new LinkedList<>();
             for (int i = 0; i < len; i++) {
                TreeNode cur = q.poll();
                if (cur.left != null) q.offer(cur.left);
                if (cur.right != null) q.offer(cur.right);
                if (fromRight) {
                    tmp.add(0, cur.val);
                } else {
                    tmp.add(cur.val);
                }
             }
             res.add(tmp);
             fromRight = !fromRight;
         }
         return res;
    }
}

#31.75% 2ms
#DFS:
public class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        dfs(root, res, 0);
        return res;
    }

    private void dfs(TreeNode root, List<List<Integer>> res, int level) {
        if (root == null) return;

        //== when level == 0
        //res.get(level) == null got java.lang.IndexOutOfBoundsException: Index: 0, Size: 0
        if (res.size() <= level) {
            List<Integer> tmp = new LinkedList<>();
            res.add(level, tmp);
        }

        if ( (level & 1) == 0) { // even ( 1 & 1 = 1, otherwise all 0)
            res.get(level).add(root.val);
        } else {
            res.get(level).add(0, root.val);
        }

        dfs(root.left, res, level+1);
        dfs(root.right, res, level+1);
    }
}

'''