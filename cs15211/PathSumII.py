__source__ = 'https://leetcode.com/problems/path-sum-ii/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/path-sum-ii.py
# Time:  O(n)
# Space: O(h), h is height of binary tree
# DFS
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
# Topics:
# Tree Depth-first Search
# You might like:
# (E) Path Sum (E) Binary Tree Paths (E) Path Sum III
# Company:
# Bloomberg
#

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

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    print Solution().pathSum(root, 22)
    print Solution2().pathSum(root, 77)

#Java
java = '''
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

 #48%
public class Solution {
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) {
            return result;
        }
        dfs(root, sum, result, new ArrayList<>());
        return result;
    }

    public void dfs(TreeNode root, int sum, List<List<Integer>> res, List<Integer> tmp) {
        if ( root == null) return;
        if (root.left == null && root.right == null && root.val == sum){
            tmp.add(root.val);
            res.add(new ArrayList<>(tmp));  //add new list, otherwise only save pointers and thus empty list
            tmp.remove(tmp.size() - 1);
            return;
        }
        tmp.add(root.val);
        dfs(root.left, sum - root.val, res, tmp);
        dfs(root.right, sum - root.val, res, tmp);
        tmp.remove(tmp.size() - 1);
    }
}
'''