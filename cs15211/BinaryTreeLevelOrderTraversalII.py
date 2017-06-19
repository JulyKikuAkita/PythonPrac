__source__ = 'https://leetcode.com/problems/binary-tree-level-order-traversal-ii/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/binary-tree-level-order-traversal-ii.py
# Time:  O(n)
# Space: O(n)
# BFS
#
# Given a binary tree, return the bottom-up level order traversal of its nodes' values.
#  (ie, from left to right, level by level from leaf to root).
#
# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
#
# Topics:
# Tree Breadth-first Search
# You might like:
# (M) Binary Tree Level Order Traversal
#
# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if root == None:
            return []
        result, cur = [], [root]
        while cur:
            next_level, val = [], []
            for node in cur:
                val.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            cur = next_level
            result.insert(0, val) # diff from up -> down
        return result




class SolutionOther:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        res = []
        self.dfs(root, 0 ,res)
        res.reverse()
        return res  #cannot return res.reverse()

    def dfs(self, root, level, res):
        if root:
            if len(res) < level+1:
                res.append([])
            res[level].append(root.val)
            print res
            self.dfs(root.left, level+1, res)
            self.dfs(root.right,level+1, res)


#the same as the Binary Tree Level Order Traversal. We only need to reverse the output.
#not use pre_order
    def levelOrderBottom2(self, root):
        if root == None:
            return []
        # In the first stage, we store hte nodes (not their value).
        ans = []
        nextlayer = [root]
        while len(nextlayer) != 0:
            ans.append(nextlayer)
        # Gather the nodes in the next deeper layer.
            nextlayer = []
            for node in ans[-1]:
                if node.left != None:
                    nextlayer.append(node.left)
                if node.right != None:
                    nextlayer.append(node.right)
        ans = [[node.val for node in layers] for layers in ans]

        return ans[::-1]

#test
#############test
#creating BST tree ####
root0=TreeNode(0)
tree1=TreeNode(1)
tree2=TreeNode(2)
tree3=TreeNode(3)
tree4=TreeNode(4)
tree5=TreeNode(5)
tree6=TreeNode(6)
root0.left=tree1
root0.right=tree2
tree1.left=tree3
tree1.right=tree4
tree2.left=tree5
tree2.right=tree6
#end of creating BST tree ####
test = SolutionOther()
#print test.levelOrderBottom(root0)
#print test.levelOrderBottom2(root0)

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    result = Solution().levelOrderBottom(root)
    SolutionOther().levelOrderBottom(root)
    print result

# Java
java ='''
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
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        //return levelOrderBottomBFS(root);

        //below for DFS
        List<List<Integer>> res = new LinkedList<List<Integer>>();
        if(root == null) return res;

        //User Collections
        //levelOrderBottomDFS(root, res, 0);
        //Collections.reverse(res);

        //no user Collecitons.reverse
        levelOrderBottomDFS2(root, res, 0);
        return res;
    }

    #70%
    public List<List<Integer>> levelOrderBottomBFS(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        List<List<Integer>> res = new LinkedList<List<Integer>>();
        if(root == null) return res;

        q.offer(root);
        while(!q.isEmpty()) {
            int len = q.size();
            List<Integer> tmp = new LinkedList<Integer>();
            for (int i = 0; i < len; i++) {
                TreeNode cur = q.poll();
                if (cur.left != null) q.add(cur.left);
                if (cur.right != null) q.offer(cur.right);
                tmp.add(cur.val);
            }
            res.add(0, tmp);
        }
        return res;
    }

    public void levelOrderBottomDFS(TreeNode root, List<List<Integer>> res, int level) {
        if(root == null) return;

        if (res.size() <= level) {
            res.add(level, new LinkedList<Integer>());
        }
        res.get(level).add(root.val);
        levelOrderBottomDFS(root.left, res, level + 1);
        levelOrderBottomDFS(root.right, res, level + 1);
    }

    #11.25%
    public void levelOrderBottomDFS2(TreeNode root, List<List<Integer>> res, int level) {
        if(root == null) return;

        if (res.size() <= level) {
            res.add(0, new LinkedList<Integer>());
        }
        levelOrderBottomDFS2(root.left, res, level + 1);
        levelOrderBottomDFS2(root.right, res, level + 1);
        res.get(res.size() - level - 1).add(root.val);
    }
}
'''