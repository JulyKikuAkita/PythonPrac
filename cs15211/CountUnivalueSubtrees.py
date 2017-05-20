__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/count-univalue-subtrees.py
'''
Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

For example:
Given binary tree,
              5
             / \
            1   5
           / \   \
          5   5   5
return 4.

Show Tags
'''

# Time:  O(n)
# Space: O(h)
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def __init__(self):
        self.cnt = 0
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.dfs(root, 0)
        return self.cnt

    def dfs(self, root, count):
        if not root:
            return [True, 0]
        if not root.left and not root.right:
            self.cnt += 1
            return [True, count]
        is_left, left_cnt = self.dfs(root.left, count)
        is_right, right_cnt = self.dfs(root.right, count)
        if( is_left and is_right and (not root.left or root.val == root.left.val) and (not root.right or root.val == root.right.val)):
                self.cnt += 1
                return [True, count]
        return [False, count]

class Solution2:
    # @param {TreeNode} root
    # @return {integer}
    def countUnivalSubtrees(self, root):
        [is_uni, count] = self.isUnivalSubtrees(root, 0);
        return count;

    def isUnivalSubtrees(self, root, count):
        if not root:
            return [True, count]

        [left, count] = self.isUnivalSubtrees(root.left, count)
        [right, count] = self.isUnivalSubtrees(root.right, count)
        if self.isSame(root, root.left, left) and \
           self.isSame(root, root.right, right):
                count += 1
                return [True, count]

        return [False, count]

    def isSame(self, root, child, is_uni):
        return not child or (is_uni and root.val == child.val)


#java
js = '''
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
    public int countUnivalSubtrees(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int[] result = new int[1];
        countUnivalSubtrees(root, result);
        return result[0];
    }

    private Integer countUnivalSubtrees(TreeNode root, int[] result) {
        boolean flag = true;
        if (root.left != null) {
            Integer left = countUnivalSubtrees(root.left, result);
            if (left == null || left != root.val) {
                flag = false;
            }
        }
        if (root.right != null) {
            Integer right = countUnivalSubtrees(root.right, result);
            if (right == null || right != root.val) {
                flag = false;
            }
        }
        if (flag) {
            result[0]++;
            return root.val;
        } else {
            return null;
        }
    }
}
'''