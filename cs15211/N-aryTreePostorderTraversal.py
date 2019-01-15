__source__ = 'https://leetcode.com/problems/n-ary-tree-postorder-traversal/'
# Time:  O(N)
# Space: O(N)
#
# Description: Leetcode #  590. N-ary Tree Postorder Traversal
#
# Given an n-ary tree, return the postorder traversal of its nodes' values.
#
# For example, given a 3-ary tree:
#
# Return its postorder traversal as: [5,6,3,2,4,1].
# Note:
#
# Recursive solution is trivial, could you do it iteratively?
#
import unittest

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

# 196ms 12.49%
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        stack, output = [root,], []
        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
            for c in root.children:
                stack.append(c)
        return output[::-1]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/n-ary-tree-postorder-traversal/solution/

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

# Recursion
# 2ms 100%
class Solution {
    List<Integer> res = new ArrayList();
    public List<Integer> postorder(Node root) {
        if (root == null) return res;
        for (int i = 0; i < root.children.size(); i++) {
            postorder(root.children.get(i));
        }
        res.add(root.val);
        return res;
    }
}

# Iteration
# 6ms 43.59%
class Solution {
    public List<Integer> postorder(Node root) {
        LinkedList<Integer> res = new LinkedList<>();
        if (root == null) return res;
        Stack<Node> stack = new Stack();
        stack.push(root);
        while (!stack.isEmpty()) {
            Node node = stack.pop();
            res.addFirst(node.val);
            for (Node child : node.children) {
                stack.push(child);
            }
        }
        return res;
    }
}
'''
