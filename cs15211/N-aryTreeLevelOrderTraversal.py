__source__ = 'https://leetcode.com/problems/n-ary-tree-level-order-traversal/'
# Time:  O(N)
# Space: O(N)
#
# Description: Leetcode # 429. N-ary Tree Level Order Traversal
#
# Given an n-ary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
# For example, given a 3-ary tree:
#
# We should return its level order traversal:
#
# [
#      [1],
#      [3,2,4],
#      [5,6]
# ]
#
#
# Note:
#
# The depth of the tree is at most 1000.
# The total number of nodes is at most 5000.
#

import unittest

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

# 124ms 73.61%
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        q, ret = [root], []
        while any(q):
            ret.append([node.val for node in q])
            q = [child for node in q for child in node.children if child]
        return ret

# 204ms 13.27%
class Solution2(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res, cur_level = [], [root]
        while cur_level:
            next_level, tmp_res = [], []
            for node in cur_level:
                tmp_res.append(node.val)
                for child in node.children:
                    next_level.append(child)
            res.append(tmp_res)
            cur_level = next_level
        return res

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:

/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val,List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/
# Iteration
# 2ms 100%
class Solution {
    public List<List<Integer>> levelOrder(Node root) {
        List<List<Integer>> res = new ArrayList();
        if (root == null) return res;
        Queue<Node> queue = new LinkedList();
        queue.add(root);
        while (!queue.isEmpty()) {
            int size = queue.size();
            List<Integer> tmp = new ArrayList();
            for (int i = 0; i < size; i++) {
                tmp.add(queue.peek().val);
                queue.addAll(queue.poll().children);
            }
            res.add(tmp);
        }
        return res;
    }
}

# Recursion
# 2ms 100%
class Solution {
    public List<List<Integer>> levelOrder(Node root) {
        List<List<Integer>> ans = new ArrayList<>();
        dfs(root, 0, ans);
        return ans;
    }

    public void dfs(Node node, int depth, List<List<Integer>> levels) {
        if (node == null) return;
        if (depth == levels.size()) levels.add(new ArrayList());
        levels.get(depth).add(node.val);
        for (int i = 0; i < node.children.size(); i++) {
            dfs(node.children.get(i), depth + 1, levels);
        }
    }
}
'''
