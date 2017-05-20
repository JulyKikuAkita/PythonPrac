__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/binary-tree-zigzag-level-order-traversal.py
# Time:  O(n)
# Space: O(n)
# BFS
#
# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
#
# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]
#
# LinkedIn Bloomberg Microsoft


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
if __name__ == "__main__":
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


#java
js = '''
public class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) {
            return result;
        }
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        queue.add(null);
        List<Integer> list = new ArrayList<>();
        while (!queue.isEmpty()) {
            TreeNode curr = queue.poll();
            if (curr == null) {
                if (queue.isEmpty()) {
                    result.add(list);
                    break;
                } else {
                    result.add(list);
                    queue.add(null);
                    list = new ArrayList<>();
                }
            } else {
                list.add(curr.val);
                if (curr.left != null) {
                    queue.add(curr.left);
                }
                if (curr.right != null) {
                    queue.add(curr.right);
                }
            }
        }
        for (int i = 1; i < result.size(); i += 2) {
            Collections.reverse(result.get(i));
        }
        return result;
    }
}
'''