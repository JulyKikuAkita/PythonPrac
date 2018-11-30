__source__ = 'https://leetcode.com/problems/n-ary-tree-preorder-traversal/description/'
# Time:  O(N)
# Space: O(N)
#
# Description: Leetcode # 589. N-ary Tree Preorder Traversal
# Given an n-ary tree, return the preorder traversal of its nodes' values.
#
# For example, given a 3-ary tree:
#
# Return its preorder traversal as: [1,3,5,6,2,4].
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

#116ms 95.15%
class Iteration(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []

        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])

        return output

#59.49% 124ms
class Recursion(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        ans = [root.val]
        if root.children:
            for child in root.children:
                if child:
                    ans.extend(self.preorder(child))
        return ans



class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/n-ary-tree-preorder-traversal/solution/
Complexity Analysis

Time complexity : we visit each node exactly once, and for each visit,
the complexity of the operation
(i.e. appending the child nodes) is proportional to the number of child nodes n
(n-ary tree). Therefore the overall time complexity is O(N),
where N is the number of nodes, i.e. the size of tree.

Space complexity : depending on the tree structure,
we could keep up to the entire tree, therefore,
the space complexity is )O(N).

# Recursion
# 2ms 100%
class Solution {
    public List<Integer> preorder(Node root) {
        List<Integer> result = new ArrayList<>();
        return preorder(root, result);
    }

    List<Integer> preorder(Node root, List<Integer> res){
        if (root == null) return res;
        res.add(root.val);
        for (Node child: root.children) {
            preorder(child, res);
        }
        return res;
    }
}

# iteration
# 8.48% 10ms
class Solution {
    public List<Integer> preorder(Node root) {
        LinkedList<Integer> res = new LinkedList<>();
        if (root == null) return res;
        Stack<Node> stack = new Stack();
        stack.push(root);
        while ( !stack.isEmpty()) {
            Node node = stack.pop();
            res.addLast(node.val);
            for (int i = node.children.size() - 1; i >= 0; i--) {
                stack.push(node.children.get(i));
            }
        }
        return res;
    }
}

class Solution {
  public List<Integer> preorder(Node root) {
    LinkedList<Node> stack = new LinkedList<>();
    LinkedList<Integer> output = new LinkedList<>();
    if (root == null) {
      return output;
    }

    stack.add(root);
    while (!stack.isEmpty()) {
      Node node = stack.pollLast();
      output.add(node.val);
      Collections.reverse(node.children);
      for (Node item : node.children) {
        stack.add(item);
      }
    }
    return output;
  }
}
'''