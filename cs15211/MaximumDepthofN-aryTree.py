__source__ = ' https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description/'
# Time:  O(N)
# Space: O(N)
#
# Description: Leetcode # 559. Maximum Depth of N-ary Tree
#
# Given a n-ary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path
# from the root node down to the farthest leaf node.
#
# For example, given a 3-ary tree:
#
# We should return its max depth, which is 3.
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

class Solution(object):
    def maxDepth(self, root): #DFS
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        elif root.children == []:
            return 1
        else:
            height = [self.maxDepth(c) for c in root.children]
            return max(height) + 1

    def maxDepthBFS(self, root):
        """
        :type root: Node
        :rtype: int
        """
        stack = []
        if root is not None:
            stack.append((1, root))

        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                for c in root.children:
                    stack.append((current_depth + 1, c))
        return depth

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/maximum-depth-of-n-ary-tree/solution/
Complexity analysis

Time complexity : we visit each node exactly once,
thus the time complexity is O(N), where NN is the number of nodes.

Space complexity : in the worst case, the tree is completely unbalanced,
e.g. each node has only one child node,
the recursion call would occur N times (the height of the tree),
therefore the storage to keep the call stack would be O(N).
But in the best case (the tree is completely balanced),
the height of the tree would be log(N).
Therefore, the space complexity in this case would be O(log(N)).

# DFS
# 2ms 100%
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
class Solution {
    public int maxDepth(Node root) {
        if (root == null) return 0;
        else if (root.children.isEmpty()) return 1;
        else {
            List<Integer> heights = new LinkedList();
            for (Node child : root.children) {
                heights.add(maxDepth(child));
            }
            return Collections.max(heights) + 1;
        }
    }
}

#BFS
class Solution {
    public int maxDepth(Node root) {
        if (root == null) return 0;
        else if (root.children.isEmpty()) return 1;
        Queue<Node> queue = new LinkedList();
        queue.offer(root);
        int count = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                Node item = queue.poll();
                if (item.children != null) {
                    for (Node each: item.children) queue.offer(each);
                }
            }
            count++;
        }
        return count;
    }
}

BFS + Pair
import javafx.util.Pair;
import java.lang.Math;

class Solution {
  public int maxDepth(Node root) {
    Queue<Pair<Node, Integer>> stack = new LinkedList<>();
    if (root != null) {
      stack.add(new Pair(root, 1));
    }

    int depth = 0;
    while (!stack.isEmpty()) {
      Pair<Node, Integer> current = stack.poll();
      root = current.getKey();
      int current_depth = current.getValue();
      if (root != null) {
        depth = Math.max(depth, current_depth);
        for (Node c : root.children) {
          stack.add(new Pair(c, current_depth + 1));
        }
      }
    }
    return depth;
  }
};

'''