__source__ = 'https://leetcode.com/problems/path-sum-ii/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/path-sum-ii.py
# Time:  O(n)
# Space: O(h), h is height of binary tree
# DFS
#
# Description: Leetcode # 113. Path Sum II
#
# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
#
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
#
#
# Companies
# Bloomberg
# Related Topics
# Tree Depth-first Search
# Similar Questions
# Path Sum Binary Tree Paths Path Sum III
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
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        return self.pathSumRecu([], [], root, sum)

    def pathSumRecu(self, result, cur, root, sum):
        if root is None:
            return result

        if root.left is None and root.right is None and root.val == sum:
            result.append(cur + [root.val])
            return result

        cur.append(root.val)
        self.pathSumRecu(result, cur, root.left, sum - root.val)
        self.pathSumRecu(result, cur, root.right, sum - root.val)
        cur.pop()
        return result

class Solution2:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        result = []
        self.pathSumRecu(result, [], root, sum)
        return result

    def pathSumRecu(self, result, cur, root, sum):
        if root is None:
            return result # if fo return, it means return null, bad behavior

        if root.left is None and root.right is None and root.val == sum:
            result.append(cur + [root.val])
            return result

        self.pathSumRecu(result, cur + [root.val], root.left, sum - root.val)
        self.pathSumRecu(result, cur + [root.val], root.right, sum - root.val)
        return result

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)
        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        print Solution().pathSum(root, 22)
        print Solution2().pathSum(root, 77)

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
# DFS
# 83.04% 2ms
public class Solution {
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) {
            return result;
        }
        pathSum(root, sum, result, new ArrayList<>());
        return result;
    }

    private void pathSum(TreeNode root, int sum, List<List<Integer>> result, List<Integer> list) {
        sum -= root.val;
        list.add(root.val);
        if (root.left == null && root.right == null) {
            if (sum == 0) {
                result.add(new ArrayList<>(list));
            }
        } else {
            if (root.left != null) {
                pathSum(root.left, sum, result, list);
            }
            if (root.right != null) {
                pathSum(root.right, sum, result, list);
            }
        }
        list.remove(list.size() - 1);
    }
}

# 46.34% 3ms
public class Solution {
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> path = new ArrayList<>();
        dfs(root, sum, res, path);
        return res;
    }

    public void dfs(TreeNode root, int sum, List<List<Integer>> res, List<Integer> path){
        if(root==null) return;
        path.add(root.val);

        if(root.left==null && root.right==null ){
            if(root.val==sum)
                res.add(new ArrayList<Integer>(path));
            return;
        }
        if(root.left!=null) {
            dfs(root.left,sum-root.val,res,path);
            path.remove(path.size()-1);
        }
        if(root.right!=null) {
            dfs(root.right,sum-root.val,res,path);
            path.remove(path.size()-1);
        }

    }
}

# BFS
# 12.42% 7ms
public class Solution {
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> path = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<TreeNode>();
        int SUM = 0;
        TreeNode cur = root;
        TreeNode pre = null;
        while(cur!=null || !stack.isEmpty()){
            while(cur!=null){
                stack.push(cur);
                path.add(cur.val);
                SUM+=cur.val;
                cur=cur.left;
            }
            cur = stack.peek();
            if(cur.right!=null && cur.right!=pre){
                cur = cur.right;
                continue;
            }
            if(cur.left==null && cur.right==null && SUM==sum)
                res.add(new ArrayList<Integer>(path));

            pre = cur;
            stack.pop();
            path.remove(path.size()-1);
            SUM-=cur.val;
            cur = null;
        }
        return res;
    }
}
'''