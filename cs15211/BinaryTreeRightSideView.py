__source__ = 'https://leetcode.com/problems/binary-tree-right-side-view/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/binary-tree-right-side-view.py
# Time:  O(n)
# Space: O(h)
# DFS
#
# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
#
# For example:
# Given the following binary tree,
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
# You should return [1, 3, 4].
#
# Companies
# Amazon
# Related Topics
# Tree, Depth-first Search, Breadth-first Search
# Similar Questions
# Populating Next Right Pointers in Each Node Boundary of Binary Tree
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
    # @return a list of integers
    def rightSideView(self, root):
        result = []
        self.rightSideViewDFS(root, 1, result)
        return result

    def rightSideViewDFS(self, node, depth, result):
        if not node:
            return

        if depth > len(result):
            result.append(node.val)

        self.rightSideViewDFS(node.right, depth+1, result)
        self.rightSideViewDFS(node.left, depth+1, result)

# BFS solution
# Time:  O(n)
# Space: O(n)
class Solution2:
    # @param root, a tree node
    # @return a list of integers
    def rightSideView(self, root):
        if not root:
            return []
        result, cur = [], [root]
        while cur:
            next_level = []
            for (i, node) in enumerate(cur):
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                if len(cur) - 1 == i :
                    result.append(node.val)
            cur = next_level
        return result

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(4)
        result = Solution().rightSideView(root)
        print result

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/contains-duplicate/solution/

Thought:
The core idea of this algorithm:
1.Each depth of the tree only select one node.
2. View depth is current size of result list.

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
public class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        rightSideView(root, result, 0);
        return result;
    }
    
    #loop left tree first, need to reset every node val
    #73.64% 1ms
    private void rightSideView(TreeNode root, List<Integer> result, int depth) {
        if (root == null) {
            return;
        }
        if (result.size() == depth) {
            result.add(root.val);
        } else {
            result.set(depth, root.val);
        }
        rightSideView(root.left, result, depth + 1);
        rightSideView(root.right, result, depth + 1);
    }
        
    # loop right tree first  
    # 26.14% 2ms
    private void dfs2(TreeNode root, List<Integer> res, int currDepth){
        if (root == null) return;
        if (res.size() == currDepth) {
            res.add(root.val);
        }
        dfs2(root.right, res, currDepth + 1);
        dfs2(root.left, res, currDepth + 1);
    }
}


# BFS
# 26.14% 2ms
#loop to right child first
public class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        if (root == null) return res;
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);

        while(!q.isEmpty()) {
            int len = q.size();
            for (int i = 0; i < len; i++) {
                TreeNode cur = q.poll();
                if (i == 0) res.add(cur.val);
                if (cur.right != null) q.offer(cur.right);
                if (cur.left != null) q.offer(cur.left);
            }
        }
        return res;
    }
}

# 26.14% 2ms
# loopto left child first
public class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) {
            return result;
        }
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size - 1; i++) {
                traverse(queue, queue.poll());
            }
            TreeNode cur = queue.poll();
            result.add(cur.val);
            traverse(queue, cur);
        }
        return result;
    }
    
    private void traverse(Queue<TreeNode> queue, TreeNode cur) {
        if (cur.left != null) {
            queue.add(cur.left);
        }
        if (cur.right != null) {
            queue.add(cur.right);
        }
    }
}
'''